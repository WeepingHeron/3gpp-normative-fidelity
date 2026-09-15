"""Independently verify stored C3 inputs, responses, pair coverage, and costs.

This command is read-only and makes no API calls.
"""
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    directory = Path(sys.argv[1]).resolve()
    load = lambda name: json.loads((directory / name).read_text())
    lines = lambda name: [json.loads(x) for x in (directory / name).read_text().splitlines() if x]
    digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    manifest = load('manifest.json')
    assert manifest['status'] == 'generation_complete_semantics_pending'
    for name, expected in load('input_freeze_manifest.json')['file_sha256'].items():
        assert digest(ROOT / name) == expected, ('input', name)
    for name, expected in load('output_freeze_manifest.json')['file_sha256'].items():
        assert digest(directory / name) == expected, ('output', name)
    with (ROOT / 'data/main_cases.csv').open(encoding='utf-8-sig', newline='') as f:
        gold = {x['case_id']: x for x in csv.DictReader(f)}
    projected = {x['case_id']: x['input'] for x in lines('projected_inputs.jsonl')}
    expected_keys = {'source_text_en', 'question_ko', 'spec_id', 'version', 'clause_id'}
    assert gold.keys() == projected.keys()
    for case, value in projected.items():
        assert set(value) == expected_keys
        assert value == {k: gold[case][k] for k in expected_keys}
    extraction = {x['case_id']: x for x in lines('extractions.jsonl')}
    generation = {x['case_id']: x for x in lines('parsed_responses.jsonl')}
    assert len(extraction) == len(generation) == 72
    assert gold.keys() == extraction.keys() == generation.keys()
    requests = lines('requests.jsonl')
    responses = lines('raw_responses.jsonl')
    assert len(requests) == len(responses) == manifest['attempts']
    et = (ROOT / 'experiments/prompts/c3_extract_v1.md').read_text()
    gt = (ROOT / 'experiments/prompts/c2_v2.md').read_text()
    cost = 0
    elapsed = {'extraction': [], 'generation': []}
    for request, response in zip(requests, responses):
        identity = ('case_id', 'stage', 'attempt')
        assert all(request[k] == response[k] for k in identity)
        case = request['case_id']
        if request['stage'] == 'extraction':
            variables = {'source_text_en': projected[case]['source_text_en']}
            template = et
        else:
            variables = {**projected[case], **extraction[case]['parsed']}
            template = gt
        expected_input = re.sub(r'{{([a-z_]+)}}', lambda m: variables[m[1]], template)
        assert request['request']['input'] == expected_input
        assert request['request']['model'] == manifest['model']
        assert request['request']['store'] is False
        if response.get('http_status') == 200:
            body = response['response']
            assert body['model'] == manifest['model']
            u = body['usage']
            cached = u.get('input_tokens_details', {}).get('cached_tokens', 0)
            cost += ((u['input_tokens'] - cached) * .75 + cached * .075 + u['output_tokens'] * 4.5) / 1e6
            elapsed[request['stage']].append(response['elapsed_ms'])
    assert abs(cost - manifest['estimated_cost_usd']) < 1e-10
    held = [r['case_id'] for r in generation.values() if r['status'].startswith('abstained')]
    for case in held:
        assert not any(r['case_id'] == case and r['stage'] == 'generation' for r in requests)
    assert sum(r['parsed'] is not None for r in generation.values()) == manifest['parsed_generations']
    print(json.dumps({'status': 'PASS', 'cases': 72, 'attempts': len(requests),
                      'actual_request_gold_leakage_check': 'PASS', 'hashes': 'PASS',
                      'parsed_generations': manifest['parsed_generations'], 'held_case_ids': held,
                      'estimated_cost_usd': cost,
                      'mean_api_elapsed_ms': {k: sum(v)/len(v) for k, v in elapsed.items() if v},
                      'meaning_preservation': 'NOT_EVALUATED'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
