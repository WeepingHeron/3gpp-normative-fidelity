"""Bind sealed generation to masked review packets; never infer semantic scores."""
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'experiments/context_microstudy_v1_20260909'
RUN = ROOT / 'experiments/runs/context_microstudy_v1_20260909'
OUT = ROOT / 'outputs/review/context_microstudy_v1_20260909'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def rows(p):
    return [json.loads(s) for s in p.read_text().splitlines() if s]


def dump(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in value) if p.suffix == '.jsonl' else json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def verify_generation():
    f = json.loads((BASE / 'input_freeze_manifest.json').read_text())
    for p, h in f['file_sha256'].items():
        assert sha(ROOT / p) == h
    o = json.loads((RUN / 'output_freeze_manifest.json').read_text())
    for p, h in o['file_sha256'].items():
        assert sha(RUN / p) == h
    manifest = json.loads((RUN / 'manifest.json').read_text())
    assert manifest['status'] == 'GENERATION_COMPLETE_SEMANTICS_PENDING' and manifest['completed_slots'] == 24
    assert manifest['input_freeze_sha256'] == sha(BASE / 'input_freeze_manifest.json')
    assert datetime.fromisoformat(f['frozen_at']) < datetime.fromisoformat(manifest['started_at'])
    plan = {r['slot_id']: r for r in rows(BASE / 'request_plan.jsonl')}
    requests, raw, parsed = (rows(RUN / n) for n in ['requests.jsonl', 'raw_responses.jsonl', 'parsed_responses.jsonl'])
    assert len(requests) == len(raw) == len(parsed) == len(plan) == 24
    assert len({r['slot_id'] for r in parsed}) == 24
    spent = 0
    for req, response, result in zip(requests, raw, parsed):
        assert req['slot_id'] == response['slot_id'] == result['slot_id']
        p = plan[req['slot_id']]
        assert req['request'] == p['request'] and req['request_sha256'] == result['request_sha256'] == p['request_sha256']
        assert response['http_status'] == 200 and response['response']['model'] == manifest['model']
        body = response['response']
        assert body['id'] == result['response_id'] and body['usage'] == result['usage']
        if result['parsed'] is not None:
            text = ''.join(c['text'] for msg in body['output'] if msg['type'] == 'message' for c in msg.get('content', []) if c['type'] == 'output_text')
            assert json.loads(text) == result['parsed']
        u = result['usage']; cached = u.get('input_tokens_details', {}).get('cached_tokens', 0)
        spent += ((u['input_tokens'] - cached) * .75 + cached * .075 + u['output_tokens'] * 4.5) / 1e6
    assert abs(spent - manifest['estimated_cost_usd']) < 1e-12
    return {'ok': True, 'slots': 24, 'exact_model_and_payloads': True, 'estimated_cost_usd': spent,
            'input_frozen_before_generation': True, 'semantic_truth_automatically_verified': False}


def build():
    assert not (OUT / 'packet_manifest.json').exists()
    receipt = verify_generation()
    cases = {c['case_id']: c for c in json.loads((BASE / 'cases.json').read_text())}
    parsed = rows(RUN / 'parsed_responses.jsonl')
    parsed.sort(key=lambda r: hashlib.sha256(('context-review-v1:' + r['slot_id']).encode()).hexdigest())
    packets, keys, blanks = [], [], []
    for i, r in enumerate(parsed, 1):
        c = cases[r['case_id']]
        rid = f'MCR-{i:03d}'
        packets.append({'review_id': rid, 'target_text': c['target_text'], 'question_ko': c['question_ko'],
                        'source': c['source'], 'pdf': c['pdf'], 'reference_context_blocks': c['context_blocks'],
                        'additional_context_supplied_to_generator': r['context'] == 'FULL',
                        'requirements': c['requirements'], 'delivery_status': r['delivery_status'],
                        'explanation_ko': (r['parsed'] or {}).get('explanation_ko', ''),
                        'output_metadata_for_separate_audit': {k:v for k,v in (r['parsed'] or {}).items() if k != 'explanation_ko'}})
        keys.append({'review_id': rid, **{k:r[k] for k in ['slot_id', 'case_id', 'context', 'hint', 'replicate', 'response_id', 'request_sha256']},
                     'response_record_sha256': hashlib.sha256(json.dumps(r, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()})
        blanks.append({'review_id': rid, 'reviewer': '', 'reviewed_at': '',
                       'requirement_coverage': [{'requirement_id': x['id'], 'value': None, 'response_quotes': [], 'rationale': ''} for x in c['requirements']],
                       'full_context_target_completeness': None, 'unsupported_or_distorted_claim': None,
                       'claim_evidence_quotes': [], 'claim_rationale': '', 'metadata_inconsistency': None,
                       'metadata_rationale': '', 'overall_rationale': ''})
    dump(OUT / 'reviewer/packets_24.jsonl', packets)
    dump(OUT / 'reviewer/judgments_blank_24.jsonl', blanks)
    dump(OUT / 'coordinator/keys_24.jsonl', keys)
    dump(OUT / 'generation_verification.json', receipt)
    dump(OUT / 'packet_manifest.json', {'prepared_at': datetime.now(timezone.utc).isoformat(),
                                      'file_sha256': {str(p.relative_to(OUT)): sha(p) for p in sorted(OUT.rglob('*')) if p.is_file()},
                                      'input_file_sha256': {str(p.relative_to(ROOT)): sha(p) for p in [BASE/'input_freeze_manifest.json', RUN/'output_freeze_manifest.json', RUN/'parsed_responses.jsonl', BASE/'cases.json', BASE/'protocol.json']}})
    for p in OUT.rglob('*'):
        if p.is_file():
            p.chmod(0o444)
    print(json.dumps(receipt, ensure_ascii=False))


if __name__ == '__main__':
    build()
