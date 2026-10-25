"""Offline-only draft request projection and validation. Never sends API requests."""
import argparse
import copy
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'experiments/generation_preservation_v1_20260909'
DOC = ROOT / 'docs/31_generation_preservation_experiment_plan_2026-09-09.md'


def sha(value):
    return hashlib.sha256(value).hexdigest()


def read(path):
    return json.loads(path.read_text())


def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def encode(value, jsonl=False):
    return (''.join(compact(row) + '\n' for row in value) if jsonl else
            json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()


def project(case):
    return {k: copy.deepcopy(case[k]) for k in
            ('case_id', 'source', 'target_text', 'question_ko', 'context_blocks')}


def derive():
    protocol = read(BASE / 'protocol.json')
    assert protocol['status'] == 'DRAFT_READY_FOR_REVIEW'
    old = ROOT / protocol['source_experiment']
    assert sha((old / 'input_freeze_manifest.json').read_bytes()) == protocol['source_input_manifest_sha256']
    for file, expected in read(old / 'input_freeze_manifest.json')['file_sha256'].items():
        assert sha((ROOT / file).read_bytes()) == expected, file
    cases = read(old / 'cases.json')
    schema = read(old / 'response_schema.json')
    template = (old / 'prompt_template.md').read_text()
    modal = (BASE / 'modality_instruction.md').read_text()
    checklist = (BASE / 'checklist_instruction.md').read_text()
    assert [c['case_id'] for c in cases] == protocol['case_ids']
    assert protocol['arms'] == ['A0_BASE', 'A1_MODAL', 'A2_MODAL_CHECK']
    assert protocol['replicates'] == [1, 2] and protocol['planned_calls'] == 18
    assert protocol['parameters'] == read(old / 'protocol.json')['parameters']
    assert protocol['model'] == read(old / 'protocol.json')['model']
    for case in cases:
        assert sha((ROOT / case['pdf']['path']).read_bytes()) == case['pdf']['sha256']
        for block in case['context_blocks']:
            page = ROOT / block['page_text_path']
            assert sha(page.read_bytes()) == block['page_text_sha256']
            assert block['quote'] in page.read_text()

    def schedule(source_cases):
        records = []
        for case in source_cases:
            c = project(case)
            context = '\n\n'.join(f"[PDF page {b['pdf_page']}]\n{b['quote']}" for b in c['context_blocks'])
            values = dict(question_ko=c['question_ko'], target_text=c['target_text'],
                          context_text=context, hint_text='', **c['source'])
            baseline = re.sub(r'{{([a-z_]+)}}', lambda m: values[m[1]], template)
            inputs = {'A0_BASE': baseline, 'A1_MODAL': baseline + '\n' + modal,
                      'A2_MODAL_CHECK': baseline + '\n' + modal + '\n' + checklist}
            for arm in protocol['arms']:
                text = inputs[arm]
                assert '{{' not in text
                request = {'model': protocol['model'], 'input': text,
                           'temperature': protocol['parameters']['temperature'],
                           'reasoning': {'effort': protocol['parameters']['reasoning_effort']},
                           'max_output_tokens': protocol['parameters']['max_output_tokens'],
                           'store': False, 'text': {'format': {'type': 'json_schema',
                           'name': 'normative_explanation', 'strict': True, 'schema': schema}}}
                prices = protocol['pricing_usd_per_million']
                reservation = ((len(text.encode()) + len(compact(schema).encode()) + 2048) * prices['input']
                               + request['max_output_tokens'] * prices['output']) / 1e6
                for replicate in protocol['replicates']:
                    records.append({'slot_id': f"{c['case_id']}-{arm}-R{replicate}",
                                    'case_id': c['case_id'], 'arm': arm, 'replicate': replicate,
                                    'request': request, 'request_sha256': sha(compact(request).encode()),
                                    'estimated_reservation_usd': reservation})
        return sorted(records, key=lambda r: sha((protocol['execution_order_seed'] + r['slot_id']).encode()))

    plan = schedule(cases)
    assert len(plan) == len({r['slot_id'] for r in plan}) == 18
    assert Counter(r['arm'] for r in plan) == {arm: 6 for arm in protocol['arms']}
    contaminated = copy.deepcopy(cases)
    for case in contaminated:
        for field in ('requirements', 'modal_hint', 'development_reference', 'prior_judgment'):
            case[field] = 'EVALUATOR_ONLY_SENTINEL_NOT_FOR_GENERATION'
    assert plan == schedule(contaminated), 'Evaluator data influenced generation'
    assert all('EVALUATOR_ONLY_SENTINEL_NOT_FOR_GENERATION' not in r['request']['input'] for r in plan)
    old_plan = [json.loads(line) for line in (old / 'request_plan.jsonl').read_text().splitlines()]
    for case in cases:
        by_arm = {arm: [r for r in plan if r['case_id'] == case['case_id'] and r['arm'] == arm]
                  for arm in protocol['arms']}
        for arm, rows in by_arm.items():
            assert rows[0]['request'] == rows[1]['request']
        baseline = by_arm['A0_BASE'][0]['request']
        prior = next(r['request'] for r in old_plan if r['case_id'] == case['case_id']
                     and r['context'] == 'FULL' and r['hint'] == 'NONE')
        assert baseline == prior, 'Baseline differs from prior FULL/NONE request'
        for arm in ('A1_MODAL', 'A2_MODAL_CHECK'):
            treatment = by_arm[arm][0]['request']
            assert {k: v for k, v in treatment.items() if k != 'input'} == {k: v for k, v in baseline.items() if k != 'input'}
            suffix = '\n' + modal + ('\n' + checklist if arm == 'A2_MODAL_CHECK' else '')
            assert treatment['input'] == baseline['input'] + suffix
    total = sum(r['estimated_reservation_usd'] for r in plan)
    assert total < protocol['generation_cost_cap_usd']
    old_protocol = read(old / 'protocol.json')
    evaluation = {
        'role': 'EVALUATOR_ONLY_DO_NOT_INCLUDE_IN_REQUESTS',
        'rules': {key: old_protocol[key] for key in ('assessment_surface', 'compound_requirement_rule', 'ambiguity_policy')},
        'cases': [{'case_id': c['case_id'], 'source': c['source'], 'pdf': c['pdf'],
                   'requirements': c['requirements']} for c in cases]
    }
    assert sum(len(c['requirements']) for c in cases) == 9
    report = {
        'status': 'OFFLINE_PLAN_VALIDATED_NOT_FROZEN_NOT_EXECUTED',
        'planned_calls': 18, 'source_cases': 3, 'calls_per_arm': 6,
        'live_api_calls': 0, 'requirements_per_reviewer': 54, 'reviewers_planned': 2,
        'baseline_exact_prior_FULL_NONE': True, 'only_instruction_suffix_changes': True,
        'evaluator_field_perturbation_check': 'PASS', 'source_hash_and_quote_checks': 'PASS',
        'same_parameters_schema_and_replicate_inputs': True,
        'total_planning_reservation_usd': round(total, 9),
        'generation_cost_cap_usd': protocol['generation_cost_cap_usd'],
        'estimated_reservation_by_arm_usd': {arm: round(sum(r['estimated_reservation_usd'] for r in plan if r['arm'] == arm), 9) for arm in protocol['arms']},
        'input_utf8_bytes_by_case_arm': [{'case_id': r['case_id'], 'arm': r['arm'], 'bytes': len(r['request']['input'].encode())} for r in plan if r['replicate'] == 1],
        'limits': ['No model response or semantic effectiveness validated', 'No separate AI design review performed for this draft', 'Hash inventory is a review snapshot, not execution freeze']
    }
    return {'request_plan.preview.jsonl': encode(plan, True), 'generator_inputs.json': encode([project(c) for c in cases]),
            'evaluation_reference.json': encode(evaluation), 'response_schema.json': (old / 'response_schema.json').read_bytes(),
            'validation_report.json': encode(report)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['build', 'verify'])
    mode = parser.parse_args().mode
    assert not (BASE / 'input_freeze_manifest.json').exists(), 'Frozen input cannot be rebuilt'
    artifacts = derive()
    support = [BASE / 'protocol.json', BASE / 'modality_instruction.md', BASE / 'checklist_instruction.md',
               Path(__file__).resolve(), DOC]
    assert all(p.is_file() for p in support)
    hashes = {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in support}
    hashes.update({str((BASE / name).relative_to(ROOT)): sha(data) for name, data in artifacts.items()})
    artifacts['plan_review_manifest.json'] = encode({'status': 'DRAFT_REVIEW_SNAPSHOT_NOT_EXECUTION_FREEZE', 'file_sha256': hashes})
    for name, data in artifacts.items():
        path = BASE / name
        if mode == 'build':
            path.write_bytes(data)
        else:
            assert path.read_bytes() == data, name
    print(compact(read(BASE / 'validation_report.json')))


if __name__ == '__main__':
    main()
