"""Bind and seal explicitly authored v2 pass-1 judgments, without inferring scores."""
import csv
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import prepare_v2_review_package_20260908 as v

OUT = v.ROOT / 'outputs/review/v2_pass1_20260908'
PREFLIGHT = v.ROOT / 'outputs/review/v2_preflight_20260908/preflight_completed.jsonl'
PREFLIGHT_MANIFEST = PREFLIGHT.parent / 'completion_manifest.json'


def verify_finished():
    manifest = v.read(OUT / 'completion_manifest.json')
    for rel, expected in manifest['file_sha256'].items():
        assert v.sha(OUT / rel) == expected, rel
    for rel, expected in manifest['support_file_sha256'].items():
        assert v.sha(v.ROOT / rel) == expected, rel
    assert v.sha(PREFLIGHT_MANIFEST) == manifest['preflight_completion_manifest_sha256']
    previous = v.read(PREFLIGHT_MANIFEST)
    for rel, expected in previous['file_sha256'].items():
        assert v.sha(PREFLIGHT.parent / rel) == expected, rel
    for rel, expected in previous['support_file_sha256'].items():
        assert v.sha(v.ROOT / rel) == expected, rel
    package = v.verify_package(v.PACKAGE)
    packets = v.lines(v.PACKAGE / 'reviewer/pass1/packets.jsonl')
    gold = v.lines(PREFLIGHT)
    completed = v.lines(OUT / 'seal/pass1_completed.jsonl')
    v.check_pass1(completed, packets, gold)
    assert completed == v.lines(OUT / 'judgments_completed.jsonl')
    keys = {x['review_id']: x for x in v.read(v.PACKAGE / 'coordinator/keys.json')['pass1']}
    for row, packet in zip(completed, packets):
        assert row['review_id'] == packet['review_id']
        assert row['packet_sha256'] == v.digest(packet)
        assert row['response_record_sha256'] == keys[row['review_id']]['response_binding']['record_sha256']
        if packet['delivery_status'] == 'EXPLANATION':
            assert row['response_evidence'] in packet['explanation_ko']
    summary = v.read(OUT / 'summary.json')
    assert dict(Counter(r['semantic_judgment'] for r in completed)) == summary['judgment_counts']
    seal = v.read(OUT / 'seal/completion_manifest.json')
    assert seal['completed_at'] == summary['sealed_at']
    assert datetime.fromisoformat(summary['pass2_earliest_at']) == datetime.fromisoformat(seal['completed_at']) + timedelta(hours=24)
    print(json.dumps({'ok': True, 'status': summary['status'], 'slots': len(completed),
                      'counts': summary['judgment_counts'], 'new_artifact_hashes_verified': len(manifest['file_sha256']),
                      'new_support_hashes_verified': len(manifest['support_file_sha256']),
                      'preflight_artifact_hashes_verified': len(previous['file_sha256']),
                      'frozen_files_unchanged': package['frozen_files_unchanged'],
                      'pass2_earliest_kst': summary['pass2_earliest_kst'],
                      'semantic_truth_automatically_verified': False}, ensure_ascii=False, indent=2))


def main():
    assert not (OUT / 'seal').exists(), 'Will not overwrite a completed review'
    package_receipt = v.verify_package(v.PACKAGE)
    packets = v.lines(v.PACKAGE / 'reviewer/pass1/packets.jsonl')
    gold = v.lines(PREFLIGHT)
    references = v.lines(v.PACKAGE / 'preflight/references.jsonl')
    v.check_preflight(gold, references)
    rows = v.lines(OUT / 'judgments_working.jsonl')
    v.check_pass1(rows, packets, gold)
    assert [r['review_id'] for r in rows] == [p['review_id'] for p in packets]
    assert len(Counter(r['reference_id'] for r in rows)) == 51
    assert set(Counter(r['reference_id'] for r in rows).values()) == {5}
    authored = []
    for path in sorted((OUT / 'authored').glob('batch_*.tsv')):
        authored.extend(csv.DictReader(path.open(), delimiter='\t'))
    assert len(authored) == 255
    same_text = defaultdict(set)
    by_gold = {g['reference_id']: g for g in gold}
    keys = {k['review_id']: k for k in v.read(v.PACKAGE / 'coordinator/keys.json')['pass1']}
    provenance_path = PREFLIGHT.parent / 'coordinator/input_provenance.json'
    bindings = []
    for row, packet, manual in zip(rows, packets, authored):
        assert row['review_id'] == manual['review_id']
        for field in ['semantic_judgment', 'rationale', 'response_evidence']:
            assert row[field] == manual[field]
        assert row['reason_codes'] == manual['reason_codes'].split('|')
        assert row['packet_sha256'] == v.digest(packet)
        assert row['source_provenance'] == by_gold[row['reference_id']]['source_provenance']
        assert row['propositions_and_relations'] == by_gold[row['reference_id']]['propositions_and_relations']
        if packet['delivery_status'] == 'EXPLANATION':
            assert row['response_evidence'] in packet['explanation_ko']
        same_text[(packet['reference_id'], packet['explanation_ko'])].add(row['semantic_judgment'])
        key = keys[row['review_id']]
        binding = key['response_binding']
        original = v.lines(v.ROOT / binding['path'])[binding['line_number']-1]
        assert v.digest(original) == binding['record_sha256']
        row['response_record_sha256'] = binding['record_sha256']
        row['preflight_completion_manifest_sha256'] = v.sha(PREFLIGHT_MANIFEST)
        row['input_provenance_binding'] = {
            'path': 'coordinator/response_bindings.json', 'review_id': row['review_id'],
            'availability_claim': 'Original stage-specific availability is linked separately; adjudication-only context was not added to generation inputs.'}
        bindings.append({'review_id': row['review_id'], 'reference_id': row['reference_id'],
                         'response_binding': binding, 'packet_sha256': key['packet_sha256'],
                         'stage_input_provenance': {'path': str(provenance_path.relative_to(v.ROOT)),
                                                   'sha256': v.sha(provenance_path), 'case_id': binding['case_id']}})
    assert all(len(states) == 1 for states in same_text.values()), 'Identical explanations have inconsistent states'
    v.write_lines(OUT / 'judgments_completed.jsonl', rows)
    v.write(OUT / 'coordinator/response_bindings.json', bindings)
    v.seal_pass1(PREFLIGHT, OUT / 'judgments_completed.jsonl', OUT / 'seal')
    seal = v.read(OUT / 'seal/completion_manifest.json')
    complete = datetime.fromisoformat(seal['completed_at'])
    earliest = complete + timedelta(hours=24)
    summary = {'status': 'PASS1_SEALED_PASS2_PENDING', 'reviewer': rows[0]['reviewer'],
               'slots_reviewed': len(rows), 'references': 51, 'conditions_per_reference': 5,
               'judgment_counts': dict(Counter(r['semantic_judgment'] for r in rows)),
               'gold_unresolved_slots': sum(r['gold_status'] == 'UNRESOLVED' for r in rows),
               'independent_clear_failures_on_unresolved_gold': sum('INDEPENDENT_CLEAR_ERROR' in r['reason_codes'] for r in rows),
               'first_review_recorded_at': rows[0]['reviewed_at'], 'last_review_recorded_at': rows[-1]['reviewed_at'],
               'sealed_at': complete.isoformat(), 'pass2_earliest_at': earliest.isoformat(),
               'pass2_earliest_kst': earliest.astimezone(timezone(timedelta(hours=9))).isoformat(),
               'pass2_completed': 0, 'adjudications_completed': 0, 'new_model_api_calls': 0,
               'condition_comparisons_computed': False, 'final_research_results': False,
               'semantic_truth_automatically_verified': False}
    v.write(OUT / 'summary.json', summary)
    flat = [{k: r[k] for k in ['review_id', 'reference_id', 'reviewed_at', 'gold_status', 'semantic_judgment',
                              'complete_preservation', 'reason_codes', 'rationale', 'response_evidence',
                              'packet_sha256', 'response_record_sha256']} for r in rows]
    v.write_csv(OUT / 'judgments_index.csv', flat)
    for i in range(0, len(rows), 43):
        texts = ['# v2 pass 1 원문·응답·판정 기록\n',
                 '1차 기록이며 최종 조정 결과가 아니다. 2차 검토 자료에 이 파일을 포함하지 않는다.\n']
        for row, packet in zip(rows[i:i+43], packets[i:i+43]):
            source = packet['source']
            texts.extend([f"## {row['review_id']} / {row['reference_id']} — {row['semantic_judgment']}\n",
                          f"출처: {source['spec_id']} v{source['version']} §{source['clause_id']}, PDF {packet['pdf']['pdf_page']}쪽\n",
                          f"원문: {source['source_text_en']}\n", f"질문: {packet['question_ko']}\n",
                          f"응답: {packet['explanation_ko'] if packet['explanation_ko'] is not None else '[NOT_GENERATED]'}\n",
                          f"판정 근거: {row['rationale']}\n", f"기준 상태: {row['gold_status']}; 검토 시각: {row['reviewed_at']}\n"])
        target = OUT / f'readable/review_{i+1:03d}_{min(i+43,255):03d}.md'
        target.parent.mkdir(exist_ok=True)
        target.write_text('\n'.join(texts))
    assert v.lines(OUT / 'seal/pass1_completed.jsonl') == rows
    assert all(v.sha(OUT / 'seal' / rel) == digest for rel, digest in seal['file_sha256'].items())
    v.write(OUT / 'verification_receipt.json', {
        'ok': True, 'status': summary['status'], 'checks': {
            'complete_255_unique_in_frozen_order': True, 'exactly_five_slots_for_each_of_51_references': True,
            'manual_tsv_matches_completed_records': True, 'all_254_response_quotes_verbatim': True,
            'all_255_packet_hashes_match': True, 'all_255_original_response_record_hashes_match': True,
            'preflight_provenance_and_propositions_unchanged': True, 'unresolved_gold_contract_passes': True,
            'all_review_times_after_full_preflight': True, 'identical_text_same_reference_same_state': True,
            'sealed_copy_and_hashes_match': True},
        'preserved_package': package_receipt, 'judgment_counts': summary['judgment_counts'],
        'semantic_truth_automatically_verified': False, 'new_model_api_calls': 0,
        'seal_manifest_sha256': v.sha(OUT / 'seal/completion_manifest.json')})
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    if sys.argv[1:] == ['--verify']:
        verify_finished()
    else:
        assert not sys.argv[1:], 'Use --verify to inspect an already completed review'
        main()
