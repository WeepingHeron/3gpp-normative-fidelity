"""Verify a separate AI review and compare only after its completion seal."""
import hashlib
import json
from collections import Counter
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'outputs/review/v2_independent_ai_20260909'
SOURCE = ROOT / 'outputs/review/v2_followup_20260909'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def rows(p):
    return [json.loads(line) for line in p.read_text().splitlines() if line]


def compare():
    manifest = json.loads((OUT / 'reviewer_a/reviewer_manifest.json').read_text())
    assert manifest['review_count'] == 15 and manifest['no_prior_judgments_accessed'] is True
    for f in manifest['input_files'] + manifest['output_files']:
        assert sha(ROOT / f['path']) == f['sha256'], f['path']
    key = {r['review_id']: r for r in rows(SOURCE / 'coordinator/keys_15.jsonl')}
    packets = {r['review_id']: r for r in rows(SOURCE / 'reviewer/packets_15.jsonl')}
    prior = {r['review_id']: r for r in rows(ROOT / 'outputs/review/v2_adjudication_20260909/adjudicated_view_255.jsonl')}
    new = rows(OUT / 'reviewer_a/judgments_15.jsonl')
    assert len(new) == len(key) == len(packets) == 15 and {r['review_id'] for r in new} == set(key)
    compared = []
    for r in new:
        k, p = key[r['review_id']], packets[r['review_id']]
        old = prior[k['prior_review_id']]
        assert old['response_record_sha256'] == k['response_record_sha256']
        assert r['complete_preservation'] == {'PASS': 1, 'FAIL': 0, 'UNRESOLVED': None}[r['semantic_judgment']]
        assert r['rationale'] and r['source_provenance_quotes'] and r['response_evidence_quotes']
        assert all(q in p['explanation_ko'] for q in r['response_evidence_quotes'])
        assert datetime.fromisoformat(r['reviewed_at']) <= datetime.fromisoformat(manifest['review_completed_at_utc'])
        compared.append({**k, 'prior_state': old['semantic_judgment'], 'separate_ai_state': r['semantic_judgment'],
                         'prior_value': old['complete_preservation'], 'separate_ai_value': r['complete_preservation'],
                         'same': (old['semantic_judgment'], old['complete_preservation']) == (r['semantic_judgment'], r['complete_preservation']),
                         'new_rationale': r['rationale'], 'old_result_changed': False})
    return compared


if __name__ == '__main__':
    data = compare()
    summary = {'status': 'SEPARATE_AI_REVIEW_COMPLETE_PRIOR_RESULTS_PRESERVED', 'compared_at': datetime.now(timezone.utc).isoformat(),
               'reviewed': 15, 'same': sum(r['same'] for r in data), 'different': sum(not r['same'] for r in data),
               'new_review_counts': dict(Counter(r['separate_ai_state'] for r in data)),
               'scores_changed': 0, 'human_expert_validation': False, 'error_independence_guaranteed': False}
    for name, value in [('comparison_15.jsonl', data), ('summary.json', summary)]:
        p = OUT / name
        if p.exists():
            if name.endswith('jsonl'):
                assert rows(p) == value
            else:
                saved = json.loads(p.read_text())
                assert {k:v for k,v in saved.items() if k != 'compared_at'} == {k:v for k,v in value.items() if k != 'compared_at'}
        else:
            p.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in value) if name.endswith('jsonl') else json.dumps(value, ensure_ascii=False, indent=2) + '\n')
            p.chmod(0o444)
    print(json.dumps(summary, ensure_ascii=False))
