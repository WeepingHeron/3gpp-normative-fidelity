"""Construct masked packets after sealed generation; never assign semantic scores."""
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'experiments/generation_preservation_v1_20260909'
RUN = ROOT / 'experiments/runs/generation_preservation_v1_20260909'
OUT = ROOT / 'outputs/review/generation_preservation_v1_20260909'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def rows(path):
    return [json.loads(x) for x in path.read_text().splitlines()]


def packet(review_id, source, reference, result):
    # Explicit allowlist: no arm, slot ID, timing, model request or prior judgment.
    parsed = result.get('parsed') or {}
    return {'review_id': review_id, 'target_text': source['target_text'],
            'question_ko': source['question_ko'], 'source': source['source'], 'pdf': reference['pdf'],
            'reference_context_blocks': source['context_blocks'], 'requirements': reference['requirements'],
            'delivery_status': result['delivery_status'], 'semantic_status': result['semantic_status'],
            'explanation_ko': parsed.get('explanation_ko', ''),
            'output_metadata_for_separate_audit': {k: v for k, v in parsed.items() if k != 'explanation_ko'}}


def validate_bindings(plan, requests, raw, ledger, manifest, prices):
    assert manifest['status'] == 'GENERATION_COMPLETE_SEMANTICS_PENDING'
    assert manifest['provenance'] == 'LIVE_API', 'Synthetic fault tests cannot become experiment data'
    assert len(plan) == len(requests) == len(raw) == len(ledger) == 18
    assert manifest['attempts'] == manifest['returned_responses'] == 18
    assert manifest['cost_complete'] is True
    assert len({x['slot_id'] for x in ledger}) == 18
    spent = 0
    usable = 0
    for p, request, response, result in zip(plan, requests, raw, ledger):
        assert p['slot_id'] == request['slot_id'] == response['slot_id'] == result['slot_id']
        assert p['request'] == request['request']
        assert p['request_sha256'] == request['request_sha256'] == result['request_sha256']
        assert response['http_status'] >= 200 and response['http_status'] < 300
        body = response['response']
        assert body['model'] == manifest['model'] == p['request']['model']
        assert body.get('id') == result['response_id'] and body['usage'] == result['usage']
        assert all(p[k] == result[k] for k in ('case_id', 'arm', 'replicate'))
        u = body['usage']; cached = u.get('input_tokens_details', {}).get('cached_tokens', 0)
        assert all(type(v) is int and v >= 0 for v in (u['input_tokens'], u['output_tokens'], cached))
        assert cached <= u['input_tokens']
        if 'total_tokens' in u: assert u['total_tokens'] == u['input_tokens'] + u['output_tokens']
        spent += ((u['input_tokens'] - cached) * prices['input'] + cached * prices['cached_input'] + u['output_tokens'] * prices['output']) / 1e6
        if result['delivery_status'] == 'EXPLANATION':
            assert body['status'] == 'completed' and result['semantic_status'] == 'PENDING_REVIEW'
            content = [c for msg in body['output'] if msg['type'] == 'message' for c in msg.get('content', [])]
            assert not any(c['type'] == 'refusal' for c in content)
            text = ''.join(c['text'] for c in content if c['type'] == 'output_text')
            assert json.loads(text) == result['parsed']
            assert result['parsed']['explanation_ko'].strip()
            schema = p['request']['text']['format']['schema']; value = result['parsed']
            assert set(value) == set(schema['required'])
            assert all(isinstance(value[k], str) and ('enum' not in schema['properties'][k] or value[k] in schema['properties'][k]['enum']) for k in value)
            usable += 1
        else:
            assert result['semantic_status'] == 'NOT_ASSESSABLE' and result['parsed'] is None
            assert result['pipeline_completeness'] == 0
    assert usable == manifest['usable_explanations']
    assert abs(spent - manifest['known_cost_usd']) < 1e-12


def main():
    assert not OUT.exists(), 'Review outputs already exist; no overwrite'
    frozen = read(BASE / 'input_freeze_manifest.json')
    for p, h in frozen['file_sha256'].items():
        assert digest(ROOT / p) == h, p
    sealed = read(RUN / 'output_freeze_manifest.json')
    for p, h in sealed['file_sha256'].items():
        assert digest(RUN / p) == h, p
    manifest = read(RUN / 'manifest.json')
    assert manifest['input_freeze_sha256'] == digest(BASE / 'input_freeze_manifest.json')
    assert datetime.fromisoformat(frozen['frozen_at']) < datetime.fromisoformat(manifest['started_at'])
    plan, requests, raw, ledger = (rows(p) for p in [BASE / 'request_plan.jsonl', RUN / 'requests.jsonl',
                                                   RUN / 'raw_responses.jsonl', RUN / 'slot_ledger.jsonl'])
    protocol = read(BASE / 'protocol.json')
    validate_bindings(plan, requests, raw, ledger, manifest, protocol['pricing_usd_per_million'])
    inputs = {x['case_id']: x for x in read(BASE / 'generator_inputs.json')}
    refs = {x['case_id']: x for x in read(BASE / 'evaluation_reference.json')['cases']}
    ordered = sorted(ledger, key=lambda r: hashlib.sha256((protocol['review_packet_seed'] + r['slot_id']).encode()).hexdigest())
    packets, keys = [], []
    for index, result in enumerate(ordered, 1):
        rid = f'GPR-{index:03d}'
        packets.append(packet(rid, inputs[result['case_id']], refs[result['case_id']], result))
        keys.append({'review_id': rid, **{k: result[k] for k in ('slot_id', 'case_id', 'arm', 'replicate', 'request_sha256', 'response_id')}})
    OUT.mkdir(parents=True)
    for relative, data in [('reviewer/packets_18.jsonl', packets), ('coordinator/keys_18.jsonl', keys)]:
        p = OUT / relative; p.parent.mkdir(exist_ok=True)
        p.write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in data))
    evidence = {'prepared_at': datetime.now(timezone.utc).isoformat(), 'records': 18,
                'source_cases': 3, 'semantic_scores_created': 0,
                'input_freeze_sha256': digest(BASE / 'input_freeze_manifest.json'),
                'run_output_freeze_sha256': digest(RUN / 'output_freeze_manifest.json'),
                'file_sha256': {str(p.relative_to(OUT)): digest(p) for p in OUT.rglob('*') if p.is_file()}}
    (OUT / 'packet_manifest.json').write_text(json.dumps(evidence, indent=2) + '\n')
    for p in OUT.rglob('*'):
        if p.is_file(): p.chmod(0o444)
    print(json.dumps({'ok': True, 'packets': 18, 'semantic_scores_created': 0}))


if __name__ == '__main__':
    main()
