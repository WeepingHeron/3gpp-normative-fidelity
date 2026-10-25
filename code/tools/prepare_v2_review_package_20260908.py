"""Prepare immutable, masked v2 review materials without judging responses or API calls."""
import argparse
import copy
import csv
import hashlib
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FREEZE = ROOT / 'experiments/posthoc_treatment_v1_20260908'
PACKAGE = ROOT / 'outputs/review/v2_20260908'
VERSION = 'posthoc_treatment_v1_20260908'
RUBRIC = ROOT / 'experiments/scoring_v2_frozen_20260908.md'
GOLD_FIELDS = ['modal_class', 'polarity', 'actor', 'condition', 'action', 'exception', 'gold_summary_ko']


def read(p):
    return json.loads(p.read_text(encoding='utf-8'))


def lines(p):
    return [json.loads(s) for s in p.read_text(encoding='utf-8').splitlines() if s.strip()]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def digest(obj):
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def write(p, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def write_lines(p, rows):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')


def write_csv(p, rows):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        for row in rows:
            w.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else v for k, v in row.items()})


def require(test, message):
    if not test:
        raise ValueError(message)


def verify_freeze():
    r = subprocess.run([sys.executable, str(ROOT / 'tools/verify_posthoc_treatment_v1.py')], capture_output=True, text=True)
    require(r.returncode == 0, 'Treatment freeze validation failed: ' + r.stdout + r.stderr)
    return json.loads(r.stdout)


def load_inputs():
    verify_freeze()
    protocol = read(FREEZE / 'protocol.json')
    ids = set(protocol['cohorts']['SENS_GOLD_EXCEPTION_51']['case_ids'])
    with (ROOT / 'data/main_cases.csv').open(encoding='utf-8-sig', newline='') as f:
        cases = {r['case_id']: r for r in csv.DictReader(f) if r['case_id'] in ids}
    audit = {r['case_id']: r for r in read(ROOT / 'outputs/analysis/main72_eligibility_20260908/eligibility_audit.json')['rows']}
    records = {(r['case_id'], r['condition']): r for p in set(protocol['response_files'].values()) for r in lines(ROOT / p)}
    index = {(r['case_id'], r['condition']): r for r in read(FREEZE / 'response_index.json')['rows']}
    for key, row in index.items():
        require(digest(records[key]) == row['record_sha256'], 'Response binding mismatch')
    return protocol, cases, audit, records, index


def delivery(record):
    parsed = record.get('parsed')
    if isinstance(parsed, dict) and isinstance(parsed.get('explanation_ko'), str):
        return ('EXPLANATION' if parsed['explanation_ko'].strip() else 'EMPTY'), parsed['explanation_ko']
    if record.get('status') == 'abstained_extraction_invalid_or_unclear' and parsed is None:
        return 'NOT_GENERATED', None
    # New/unrecognized pipeline states need inspection; never manufacture model failure from missing data.
    raise ValueError('Unrecognized delivery state: ' + repr((record.get('case_id'), record.get('condition'), record.get('status'))))


def materials():
    protocol, cases, audit, records, index = load_inputs()
    refs, refmap = [], {}
    patch = {r['case_id']: r for r in read(FREEZE / 'gold_overlay.json')['patches']}
    for i, cid in enumerate(sorted(cases), 1):
        g, a = cases[cid], audit[cid]
        rid = f'G{i:03d}'
        refmap[cid] = rid
        gold = {k: g[k] for k in GOLD_FIELDS}
        for key, change in patch.get(cid, {}).get('fields', {}).items():
            require(gold[key] == change['before'], 'Gold overlay before mismatch')
            gold[key] = change['after']
        pdf = 'data/source/ts_' + ('123501' if '23.501' in g['spec_id'] else '124501') + 'v181200p.pdf'
        refs.append({'reference_id': rid, 'source': {k: g[k] for k in ['spec_id', 'version', 'clause_id', 'source_text_en', 'source_sha256']},
                     'pdf': {'path': pdf, 'sha256': sha(ROOT / pdf), 'pdf_page': int(g['pdf_page']), 'printed_page': a['printed_page']},
                     'question_ko': g['question_ko'], 'gold_guidance': gold,
                     'adjudication_only_context': {'preceding': a['preceding_context'], 'following': a['following_context'],
                                                  'available_in_original_generation_input_as_context': False},
                     'preflight_status': 'PENDING',
                     'warning': 'Gold fields are guidance pending source preflight; PDF context is not retroactively part of model input.'})
    byref = {r['reference_id']: r for r in refs}
    packet_sets, keys = {}, {}
    for pass_name, prefix in [('pass1', 'V2-P1'), ('pass2', 'V2-P2')]:
        def sortkey(pair):
            cid, cond = pair
            s = f"{protocol['review_procedure']['order_seed']}|{pass_name}|{cid}|{cond}"
            return hashlib.sha256(s.encode()).hexdigest(), cid, cond
        pairs = sorted(((cid, cond) for cid in cases for cond in protocol['conditions']), key=sortkey)
        packets, keyrows = [], []
        for i, pair in enumerate(pairs, 1):
            cid, cond = pair
            record = records[pair]
            state, explanation = delivery(record)
            review_id = f'{prefix}-{i:03d}'
            ref = byref[refmap[cid]]
            packets.append({'review_id': review_id, 'reference_id': ref['reference_id'],
                            'source': ref['source'], 'pdf': ref['pdf'], 'question_ko': ref['question_ko'],
                            'gold_guidance': ref['gold_guidance'], 'adjudication_only_context': ref['adjudication_only_context'],
                            'delivery_status': state, 'explanation_ko': explanation})
            keyrows.append({'review_id': review_id, 'reference_id': ref['reference_id'], 'case_id': cid, 'condition': cond,
                            'response_binding': index[pair], 'packet_sha256': digest(packets[-1]),
                            'cohorts': [name for name, co in protocol['cohorts'].items() if cid in co['case_ids']],
                            'original_delivery_status': record.get('status')})
        packet_sets[pass_name], keys[pass_name] = packets, keyrows
    return refs, refmap, packet_sets, keys, records


def blanks(packets, pass_name):
    return [{'review_id': r['review_id'], 'reference_id': r['reference_id'], 'treatment_version': VERSION,
             'rubric_sha256': sha(RUBRIC), 'review_pass': pass_name, 'delivery_status': r['delivery_status'],
             'reviewer': '', 'reviewed_at': '', 'semantic_judgment': '', 'complete_preservation': None,
             'gold_status': '', 'reason_codes': [], 'rationale': '', 'source_provenance': [],
             'propositions_and_relations': []} for r in packets]


def preflight_blanks(refs):
    return [{'reference_id': r['reference_id'], 'reference_sha256': digest(r), 'reviewer': '', 'reviewed_at': '',
             'gold_status': '', 'propositions_and_relations': [], 'source_provenance': [],
             'input_context_gap': '', 'proposed_errata': [], 'rationale': ''} for r in refs]


def build(output):
    require(not output.exists(), 'Output already exists; immutable package will not be overwritten')
    refs, refmap, packets, keys, records = materials()
    write_lines(output / 'preflight/references.jsonl', refs)
    blank = preflight_blanks(refs)
    write_lines(output / 'preflight/judgments_blank.jsonl', blank)
    write_csv(output / 'preflight/judgments_blank.csv', blank)
    write_lines(output / 'reviewer/pass1/packets.jsonl', packets['pass1'])
    write_lines(output / 'reviewer/pass1/judgments_blank.jsonl', blanks(packets['pass1'], 'pass1'))
    write_csv(output / 'reviewer/pass1/judgments_blank.csv', blanks(packets['pass1'], 'pass1'))
    write(output / 'coordinator/keys.json', keys)
    write(output / 'coordinator/reference_key.json', {v: k for k, v in refmap.items()})
    write_lines(output / 'coordinator/response_records.jsonl', [records[(r['case_id'], r['condition'])] for r in keys['pass1']])
    write(output / 'coordinator/cohorts.json', read(FREEZE / 'protocol.json')['cohorts'])
    write(output / 'coordinator/input_availability.json', {
        'basis': 'Frozen runner/prompt routing; source availability does not mean the response preserved it.',
        'C0': {'source': False, 'question': True, 'structured_gold': False},
        'C1': {'source': True, 'question': True, 'structured_gold': False},
        'C2': {'source': True, 'question': True, 'structured_gold': 'original unchanged fields; not corrected overlay'},
        'C1M': {'source': True, 'question': True, 'structured_gold': 'modal and polarity only'},
        'C3': {'extractor': {'source': True, 'question': False, 'gold': False},
               'generator_if_extraction_usable': {'source': True, 'question': True, 'structure': 'automatically extracted'}},
        'extra_pdf_context': 'adjudication_only_context; not supplied to original model',
        'warning': 'Keep coordinator materials out of masked semantic review. Resolve case-specific provenance after blind judgments.'})
    write(output / 'package_state.json', {'status': 'PREPARED_PREFLIGHT_PENDING', 'treatment_version': VERSION,
        'freeze_manifest_sha256': sha(FREEZE / 'freeze_manifest.json'), 'rubric_sha256': sha(RUBRIC),
        'case_count': 51, 'review_slots_per_pass': 255, 'delivery_counts': dict(Counter(r['delivery_status'] for r in packets['pass1'])),
        'gold_preflight_completed': 0, 'semantic_reviews_completed': 0, 'new_model_calls': 0,
        'pass2': 'ORDER_STAGED_NOT_RELEASED', 'masking': 'Condition/old-score/key masked; not independent or fully blind.'})
    return refs, packets


def check_preflight(rows, refs):
    expected = {r['reference_id']: r for r in refs}
    require(len(rows) == 51 and {r['reference_id'] for r in rows} == set(expected), 'Preflight requires 51 unique references')
    for row in rows:
        require(row['reference_sha256'] == digest(expected[row['reference_id']]), 'Preflight reference changed')
        require(row['gold_status'] in {'SOURCE_SUPPORTED', 'UNRESOLVED'}, 'New correction must remain UNRESOLVED; frozen overlay already applied')
        require(bool(row['reviewer'].strip()) and bool(row['rationale'].strip()), 'Preflight reviewer/rationale required')
        require(row['input_context_gap'] in {'NONE_IDENTIFIED', 'IDENTIFIED', 'UNRESOLVED'}, 'Context-gap disposition required')
        require(bool(row['propositions_and_relations']) and bool(row['source_provenance']), 'Propositions and source provenance required')
        require(isinstance(row['propositions_and_relations'], list), 'Propositions must be a list')
        for proposition in row['propositions_and_relations']:
            require(isinstance(proposition, dict) and all(isinstance(proposition.get(k), str) and proposition[k].strip()
                    for k in ['actor', 'modal_surface', 'modal_scope', 'action_or_state', 'condition', 'quantifier', 'relation', 'evidence_quote']),
                    'Each proposition needs scope, relation, and quoted evidence; use explicit none where absent')
        check_provenance(row['source_provenance'])
        timestamp(row['reviewed_at'])


def check_provenance(evidence):
    require(isinstance(evidence, list) and bool(evidence), 'Provenance must be a nonempty list')
    for item in evidence:
        require(isinstance(item, dict) and item.get('evidence_location') in
                {'reference_source', 'reference_question', 'adjudication_only_context'}, 'Evidence location required')
        require(all(isinstance(item.get(k), str) and item[k].strip()
                    for k in ['quote', 'spec_id', 'version', 'clause_id']), 'Quoted source locator required')
        require(type(item.get('pdf_page')) is int and item['pdf_page'] > 0, 'Positive PDF page required')


def timestamp(value):
    t = datetime.fromisoformat(value.replace('Z', '+00:00'))
    require(t.tzinfo is not None and t <= datetime.now(timezone.utc), 'Timestamp requires timezone and cannot be future')
    return t


def check_pass1(rows, packets, preflight):
    expected = {r['review_id']: r for r in packets}
    gold = {r['reference_id']: r for r in preflight}
    require(len(rows) == 255 and {r['review_id'] for r in rows} == set(expected), 'Pass 1 requires 255 unique slots')
    latest_preflight = max(timestamp(g['reviewed_at']) for g in preflight)
    for row in rows:
        p = expected[row['review_id']]
        require(row['reference_id'] == p['reference_id'] and row['review_pass'] == 'pass1', 'Pass/reference mismatch')
        require(row['treatment_version'] == VERSION and row['rubric_sha256'] == sha(RUBRIC), 'Treatment/rubric mismatch')
        require(row['delivery_status'] == p['delivery_status'], 'Delivery mutation')
        require(row['gold_status'] == gold[p['reference_id']]['gold_status'], 'Gold status differs from preflight')
        require(bool(row['reviewer'].strip()) and bool(row['rationale'].strip()) and bool(row['source_provenance']), 'Judgment evidence required')
        check_provenance(row['source_provenance'])
        reviewed = timestamp(row['reviewed_at'])
        require(reviewed >= latest_preflight, 'Pass 1 predates full preflight completion')
        state, val = row['semantic_judgment'], row['complete_preservation']
        if p['delivery_status'] != 'EXPLANATION':
            require(state == 'NOT_SCORED' and type(val) is int and val == 0, 'Pipeline outcome contract violated')
        elif state == 'UNRESOLVED':
            require(val is None, 'UNRESOLVED must be null')
        else:
            require(type(val) is int and ((state == 'PASS' and val == 1) or (state == 'FAIL' and val == 0)), 'Semantic outcome contract violated')
            if row['gold_status'] == 'UNRESOLVED':
                require(state == 'FAIL' and 'INDEPENDENT_CLEAR_ERROR' in row['reason_codes'], 'Unresolved gold cannot imply PASS; FAIL needs independent error')


def seal_pass1(preflight_path, judgments_path, destination):
    verify_package(PACKAGE)
    refs, _, packets, _, _ = materials()
    pf, rows = lines(preflight_path), lines(judgments_path)
    check_preflight(pf, refs)
    check_pass1(rows, packets['pass1'], pf)
    require(not destination.exists(), 'Seal directory exists; will not overwrite')
    write_lines(destination / 'preflight_completed.jsonl', pf)
    write_lines(destination / 'pass1_completed.jsonl', rows)
    write(destination / 'completion_manifest.json', {'status': 'PASS1_SEALED', 'completed_at': datetime.now(timezone.utc).isoformat(),
        'package_manifest_sha256': sha(PACKAGE / 'package_manifest.json'),
        'file_sha256': {p.name: sha(p) for p in sorted(destination.glob('*.jsonl'))}})


def delay_gate(completed_at, now):
    completed = datetime.fromisoformat(completed_at.replace('Z', '+00:00'))
    require(completed.tzinfo is not None, 'Completion timestamp needs timezone')
    require(now >= completed + timedelta(hours=24), 'Pass 2 requires 24 hours after sealed pass 1 completion')


def release_pass2(seal_dir, destination):
    verify_package(PACKAGE)
    manifest = read(seal_dir / 'completion_manifest.json')
    require(manifest['status'] == 'PASS1_SEALED' and manifest['package_manifest_sha256'] == sha(PACKAGE / 'package_manifest.json'), 'Seal/package mismatch')
    require(set(manifest['file_sha256']) == {'preflight_completed.jsonl', 'pass1_completed.jsonl'}, 'Seal file set mismatch')
    for name, expected in manifest['file_sha256'].items():
        require(sha(seal_dir / name) == expected, 'Completed review changed')
    refs, _, packets, _, _ = materials()
    pf = lines(seal_dir / 'preflight_completed.jsonl')
    rows = lines(seal_dir / 'pass1_completed.jsonl')
    check_preflight(pf, refs)
    check_pass1(rows, packets['pass1'], pf)
    require(timestamp(manifest['completed_at']) >= max(timestamp(r['reviewed_at']) for r in rows), 'Seal predates reviews')
    delay_gate(manifest['completed_at'], datetime.now(timezone.utc))
    require(not destination.exists(), 'Pass 2 destination exists')
    write_lines(destination / 'packets.jsonl', packets['pass2'])
    write_lines(destination / 'judgments_blank.jsonl', blanks(packets['pass2'], 'pass2'))
    write_csv(destination / 'judgments_blank.csv', blanks(packets['pass2'], 'pass2'))
    write(destination / 'release_manifest.json', {'status': 'PASS2_READY_NOT_REVIEWED', 'released_at': datetime.now(timezone.utc).isoformat(),
        'pass1_completion_manifest_sha256': sha(seal_dir / 'completion_manifest.json'),
        'package_manifest_sha256': sha(PACKAGE / 'package_manifest.json'),
        'file_sha256': {p.name: sha(p) for p in sorted(destination.iterdir()) if p.is_file()}})


def verify_package(output):
    refs, _, packets, keys, records = materials()
    manifest = read(output / 'package_manifest.json')
    require(manifest['freeze_manifest_sha256'] == sha(FREEZE / 'freeze_manifest.json'), 'Freeze changed')
    for rel, expected in manifest['file_sha256'].items():
        require(sha(output / rel) == expected, 'Package file changed: ' + rel)
    for rel, expected in manifest['support_file_sha256'].items():
        require(sha(ROOT / rel) == expected, 'Support file changed: ' + rel)
    require(lines(output / 'preflight/references.jsonl') == refs, 'Source/gold/context changed')
    require(lines(output / 'preflight/judgments_blank.jsonl') == preflight_blanks(refs), 'Preflight is not blank')
    require(lines(output / 'reviewer/pass1/packets.jsonl') == packets['pass1'], 'Response text/masking/order changed')
    require(lines(output / 'reviewer/pass1/judgments_blank.jsonl') == blanks(packets['pass1'], 'pass1'), 'Review is not blank')
    require(read(output / 'coordinator/keys.json') == keys, 'Key/order/binding changed')
    require(lines(output / 'coordinator/response_records.jsonl') == [records[(r['case_id'], r['condition'])] for r in keys['pass1']], 'Original record copy changed')
    require(not (output / 'reviewer/pass2').exists(), 'Pass 2 released inside immutable package')
    for r in packets['pass1']:
        require(set(r) == {'review_id', 'reference_id', 'source', 'pdf', 'question_ko', 'gold_guidance', 'adjudication_only_context', 'delivery_status', 'explanation_ko'}, 'Unexpected reviewer metadata')
        require('MAIN-' not in json.dumps(r, ensure_ascii=False), 'Case identity leaked')
    for rel, expectedrows in [('preflight/judgments_blank.csv', preflight_blanks(refs)), ('reviewer/pass1/judgments_blank.csv', blanks(packets['pass1'], 'pass1'))]:
        with (output / rel).open(encoding='utf-8-sig', newline='') as f:
            actual = list(csv.DictReader(f))
        expectedrows = [{k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else '' if v is None else str(v) for k, v in r.items()} for r in expectedrows]
        require(actual == expectedrows, 'CSV roundtrip mismatch')
    return {'ok': True, 'status': 'PREPARED_PREFLIGHT_PENDING', 'references': len(refs), 'slots': len(packets['pass1']),
            'delivery_counts': dict(Counter(r['delivery_status'] for r in packets['pass1'])),
            'package_files_verified': len(manifest['file_sha256']), 'support_files_verified': len(manifest['support_file_sha256']),
            'frozen_files_unchanged': 119, 'gold_preflight_completed': 0, 'semantic_reviews_completed': 0, 'new_model_calls': 0}


def self_test():
    refs, _, packets, _, _ = materials()
    results = []
    def reject(name, fn):
        try:
            fn()
        except (ValueError, KeyError, TypeError):
            results.append({'name': name, 'passed': True})
        else:
            results.append({'name': name, 'passed': False})
    reject('blank_preflight_rejected', lambda: check_preflight(preflight_blanks(refs), refs))
    reject('missing_preflight_rejected', lambda: check_preflight(preflight_blanks(refs)[:-1], refs))
    reject('missing_response_not_model_failure', lambda: delivery({'parsed': None, 'status': 'missing'}))
    reject('early_pass2_rejected', lambda: delay_gate('2026-01-01T00:00:00Z', datetime(2026, 1, 1, 23, 59, 59, tzinfo=timezone.utc)))
    delay_gate('2026-01-01T00:00:00Z', datetime(2026, 1, 2, tzinfo=timezone.utc))
    results.append({'name': 'exact_24h_allowed', 'passed': True})
    # Synthetic in-memory validation fixtures, never saved as research judgments.
    evidence = [{'evidence_location': 'reference_source', 'quote': 'fixture', 'spec_id': 'fixture',
                 'version': 'fixture', 'clause_id': 'fixture', 'pdf_page': 1}]
    proposition = {k: 'fixture' for k in ['actor', 'modal_surface', 'modal_scope', 'action_or_state',
                   'condition', 'quantifier', 'relation', 'evidence_quote']}
    pf = preflight_blanks(refs)
    for r in pf:
        r.update(reviewer='synthetic validator fixture', reviewed_at='2026-01-01T00:00:00Z', gold_status='SOURCE_SUPPORTED',
                 input_context_gap='NONE_IDENTIFIED', propositions_and_relations=[proposition], source_provenance=evidence, rationale='fixture')
    check_preflight(pf, refs)
    rows = blanks(packets['pass1'], 'pass1')
    for r in rows:
        r.update(reviewer='synthetic validator fixture', reviewed_at='2026-01-02T00:00:00Z', gold_status='SOURCE_SUPPORTED',
                 semantic_judgment='UNRESOLVED' if r['delivery_status'] == 'EXPLANATION' else 'NOT_SCORED',
                 complete_preservation=None if r['delivery_status'] == 'EXPLANATION' else 0, source_provenance=evidence, rationale='fixture')
    check_pass1(rows, packets['pass1'], pf)
    results.append({'name': 'valid_unresolved_and_pipeline_contract', 'passed': True})
    for name, mutation in [
        ('duplicate_review', lambda a: a.__setitem__(0, copy.deepcopy(a[1]))),
        ('rubric_change', lambda a: a[0].update(rubric_sha256='changed')),
        ('unknown_to_zero', lambda a: next(r for r in a if r['semantic_judgment'] == 'UNRESOLVED').update(complete_preservation=0)),
        ('delivery_changed', lambda a: a[0].update(delivery_status='REFUSED')),
        ('old_pass_reuse', lambda a: a[0].update(review_pass='v1')),
        ('judgment_before_preflight', lambda a: a[0].update(reviewed_at='2025-12-31T00:00:00Z')),
    ]:
        changed = copy.deepcopy(rows)
        mutation(changed)
        reject(name, lambda: check_pass1(changed, packets['pass1'], pf))
    require(all(r['passed'] for r in results), 'Self-test failure')
    return results


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('command', choices=['build', 'verify', 'check-preflight', 'seal-pass1', 'release-pass2'])
    p.add_argument('--output', type=Path, default=PACKAGE)
    p.add_argument('--preflight', type=Path)
    p.add_argument('--judgments', type=Path)
    p.add_argument('--seal', type=Path)
    p.add_argument('--self-test', action='store_true')
    a = p.parse_args()
    if a.command == 'build':
        build(a.output)
        result = {'status': 'MATERIALS_CREATED_MANIFEST_PENDING'}
    elif a.command == 'verify':
        result = verify_package(a.output)
    elif a.command == 'check-preflight':
        verify_package(PACKAGE)
        check_preflight(lines(a.preflight), materials()[0])
        result = {'status': 'PREFLIGHT_RECORDS_COMPLETE', 'semantic_truth_automatically_verified': False}
    elif a.command == 'seal-pass1':
        require(a.output != PACKAGE, 'Use a separate --output for completed reviews')
        seal_pass1(a.preflight, a.judgments, a.output)
        result = {'status': 'PASS1_SEALED', 'output': str(a.output)}
    else:
        require(a.output != PACKAGE, 'Use a separate --output for pass 2')
        release_pass2(a.seal, a.output)
        result = {'status': 'PASS2_READY_NOT_REVIEWED', 'output': str(a.output)}
    if a.self_test:
        result['self_tests'] = self_test()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
