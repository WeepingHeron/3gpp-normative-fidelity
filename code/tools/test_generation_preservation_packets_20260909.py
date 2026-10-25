"""Offline packet masking and actual-response binding fault checks."""
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import prepare_generation_preservation_review_20260909 as review

base = review.BASE
plan = review.rows(base / 'request_plan.preview.jsonl')
inputs = {c['case_id']: c for c in review.read(base / 'generator_inputs.json')}
refs = {c['case_id']: c for c in review.read(base / 'evaluation_reference.json')['cases']}
checks = []
seen = []
for i, p in enumerate(plan):
    result = {'parsed': {'explanation_ko': 'SYNTHETIC_TEST_ONLY', 'normative_type': 'permission'},
              'delivery_status': 'EXPLANATION', 'semantic_status': 'PENDING_REVIEW',
              'arm': 'SECRET_ARM', 'slot_id': 'SECRET_SLOT', 'prior_judgment': 'SECRET_GOLD'}
    packet = review.packet(f'GPR-{i+1:03d}', inputs[p['case_id']], refs[p['case_id']], result)
    encoded = json.dumps(packet)
    assert not any(x in encoded for x in ('SECRET_ARM', 'SECRET_SLOT', 'SECRET_GOLD'))
    assert packet['requirements'] == refs[p['case_id']]['requirements']
    assert packet['reference_context_blocks'] == inputs[p['case_id']]['context_blocks']
    seen.append(packet)
assert len(seen) == 18 and sum(len(p['requirements']) for p in seen) == 54
checks.append('18_masked_packets_54_requirements_no_arm_or_prior_score')
empty = review.packet('GPR-TEST', inputs['CTX-001'], refs['CTX-001'],
                      {'parsed': None, 'delivery_status': 'REFUSAL', 'semantic_status': 'NOT_ASSESSABLE'})
assert empty['explanation_ko'] == '' and empty['semantic_status'] == 'NOT_ASSESSABLE'
checks.append('delivery_failure_is_not_semantic_null_or_false')
requests, raw, ledger = [], [], []
for p in plan:
    schema = p['request']['text']['format']['schema']
    value = {k: 'SYNTHETIC_TEST_ONLY' for k in schema['required']}; value['normative_type'] = 'permission'
    usage = {'input_tokens': 0, 'output_tokens': 0}
    requests.append({'slot_id': p['slot_id'], 'request': p['request'], 'request_sha256': p['request_sha256']})
    raw.append({'slot_id': p['slot_id'], 'http_status': 200, 'response': {'id': 'test', 'model': p['request']['model'],
        'status': 'completed', 'usage': usage, 'output': [{'type': 'message', 'content': [{'type': 'output_text', 'text': json.dumps(value)}]}]}})
    ledger.append({k: p[k] for k in ('slot_id', 'case_id', 'arm', 'replicate', 'request_sha256')})
    ledger[-1].update({'response_id': 'test', 'usage': usage, 'parsed': value, 'delivery_status': 'EXPLANATION', 'semantic_status': 'PENDING_REVIEW'})
manifest = {'status': 'GENERATION_COMPLETE_SEMANTICS_PENDING', 'provenance': 'LIVE_API',
            'attempts': 18, 'returned_responses': 18, 'cost_complete': True, 'known_cost_usd': 0,
            'usable_explanations': 18, 'model': plan[0]['request']['model']}
prices = review.read(base / 'protocol.json')['pricing_usd_per_million']
review.validate_bindings(plan, requests, raw, ledger, manifest, prices)
checks.append('request_raw_output_ledger_binding')
for name in ['synthetic_run', 'swapped_slots', 'changed_output', 'changed_cost']:
    req, responses, out, m = copy.deepcopy((requests, raw, ledger, manifest))
    if name == 'synthetic_run': m['provenance'] = 'SYNTHETIC_TEST_ONLY'
    if name == 'swapped_slots': out[0], out[1] = out[1], out[0]
    if name == 'changed_output': out[0]['parsed']['explanation_ko'] = 'tampered'
    if name == 'changed_cost': m['known_cost_usd'] = 1
    try: review.validate_bindings(plan, req, responses, out, m, prices)
    except AssertionError: pass
    else: raise AssertionError(name + ' accepted')
    checks.append(name + '_rejected')
print(json.dumps({'ok': True, 'provenance': 'SYNTHETIC_TEST_ONLY', 'live_api_calls': 0, 'checks': checks,
                  'checked_at': datetime.now(timezone.utc).isoformat(),
                  'adapter_sha256': hashlib.sha256(Path(review.__file__).read_bytes()).hexdigest()}))
