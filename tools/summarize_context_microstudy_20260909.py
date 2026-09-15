"""Verify paired manual reviews and report each reviewer without voting or rescoring."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sqlite3
import subprocess
import sys

import prepare_context_microstudy_review_20260909 as gen
import compare_independent_ai15_20260909 as old_review

ROOT, OUT = gen.ROOT, gen.OUT
ANALYSIS = OUT / 'analysis'
DOC = ROOT / 'docs/30_separate_ai_review_and_context_microstudy_2026-09-09.md'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(p):
    return json.loads(p.read_text())


def rows(p):
    return [json.loads(x) for x in p.read_text().splitlines() if x]


def write(p, data):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in data) if p.suffix == '.jsonl' else json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def validate_review(items, packets):
    assert len(items) == 24 and {r['review_id'] for r in items} == set(packets)
    for r in items:
        p = packets[r['review_id']]
        assert r['reviewer'] and r['reviewed_at'] and r['overall_rationale']
        assert [x['requirement_id'] for x in r['requirement_coverage']] == [x['id'] for x in p['requirements']]
        values = []
        for item in r['requirement_coverage']:
            v = item['value']; assert type(v) is int and v in (0,1) or v is None
            assert item['rationale'] and all(q in p['explanation_ko'] for q in item['response_quotes'])
            if v == 1:
                assert item['response_quotes']
            values.append(v)
        claim = r['unsupported_or_distorted_claim']
        assert type(claim) is bool or claim is None
        assert r['claim_rationale'] and all(q in p['explanation_ko'] for q in r['claim_evidence_quotes'])
        if claim is True:
            assert r['claim_evidence_quotes']
        assert type(r['metadata_inconsistency']) is bool or r['metadata_inconsistency'] is None
        assert r['metadata_rationale']
        expected = 0 if 0 in values or claim is True else None if None in values or claim is None else 1
        assert type(r['full_context_target_completeness']) is int or r['full_context_target_completeness'] is None
        assert r['full_context_target_completeness'] == expected


def derived():
    generation = gen.verify_generation()
    old = old_review.compare()
    assert len(old) == 15 and all(x['same'] for x in old)
    packet_manifest = read(OUT/'packet_manifest.json')
    for p,h in packet_manifest['file_sha256'].items(): assert sha(OUT/p) == h
    for p,h in packet_manifest['input_file_sha256'].items(): assert sha(ROOT/p) == h
    root_manifest = read(OUT/'root_review/reviewer_manifest.json')
    for p,h in root_manifest['file_sha256'].items(): assert sha(OUT/'root_review'/p) == h
    for p,h in root_manifest['input_file_sha256'].items(): assert sha(ROOT/p) == h
    assert sha(ROOT/root_manifest['authored_decision_source']) == root_manifest['authored_decision_source_sha256']
    # The separate reviewer manifest is required before any conditions are joined.
    fresh_manifest = read(OUT/'fresh_review/reviewer_manifest.json')
    assert sha(OUT/'fresh_review/reviewer_manifest.json') == '8a1d5705e7b7580e9a8092e3f6b07942cdadaeb6c274a7aadfcf5f820e40e96a'
    for p,h in {**fresh_manifest['input_sha256'],**fresh_manifest['output_sha256']}.items():assert sha(ROOT/p)==h
    assert fresh_manifest['validation']['records']==24 and fresh_manifest['read_boundary']['other_judgments_read'] is False
    assert fresh_manifest['read_boundary']['coordinator_condition_key_read'] is False
    packets = {p['review_id']:p for p in rows(OUT/'reviewer/packets_24.jsonl')}
    key = {p['review_id']:p for p in rows(OUT/'coordinator/keys_24.jsonl')}
    all_reviews = {'root': rows(OUT/'root_review/judgments_24.jsonl'), 'fresh': rows(OUT/'fresh_review/judgments_24.jsonl')}
    for items in all_reviews.values(): validate_review(items, packets)
    for r in all_reviews['fresh']:
        assert datetime.fromisoformat(r['reviewed_at']) <= datetime.fromisoformat(fresh_manifest['recorded_at_utc'])
    joined, comparisons, groups, coverage_groups, paired = [], [], [], [], []
    for reviewer, items in all_reviews.items():
        for r in items:
            joined.append({'reviewer': reviewer, **key[r['review_id']],
                           'complete': r['full_context_target_completeness'],
                           'unsupported_or_distorted_claim': r['unsupported_or_distorted_claim'],
                           'metadata_inconsistency': r['metadata_inconsistency'],
                           'requirement_coverage': r['requirement_coverage']})
    for a,b in zip(all_reviews['root'],all_reviews['fresh']):
        # Do not rely on physical order in either reviewer output.
        b = next(x for x in all_reviews['fresh'] if x['review_id'] == a['review_id'])
        diffs = []
        for field in ['full_context_target_completeness','unsupported_or_distorted_claim','metadata_inconsistency']:
            if a[field] != b[field]: diffs.append(field)
        for x,y in zip(a['requirement_coverage'], b['requirement_coverage']):
            if x['value'] != y['value']: diffs.append('coverage:'+x['requirement_id'])
        comparisons.append({'review_id': a['review_id'], 'same_all_scored_fields': not diffs,
                            'different_fields': diffs, 'root': a, 'fresh': b,
                            'adjudication_applied': False})
    for reviewer in all_reviews:
        for context in ['SHORT','FULL']:
            for hint in ['NONE','MODAL']:
                selected = [r for r in joined if (r['reviewer'],r['context'],r['hint']) == (reviewer,context,hint)]
                assert len(selected) == 6 and len({r['case_id'] for r in selected}) == 3
                counts = Counter('UNRESOLVED' if r['complete'] is None else 'COMPLETE' if r['complete'] == 1 else 'INCOMPLETE' for r in selected)
                claims = Counter('UNRESOLVED' if r['unsupported_or_distorted_claim'] is None else 'PRESENT' if r['unsupported_or_distorted_claim'] else 'ABSENT' for r in selected)
                groups.append({'reviewer':reviewer,'context':context,'hint':hint,'n_slots':6,'distinct_cases':3,
                               **{k:counts[k] for k in ['COMPLETE','INCOMPLETE','UNRESOLVED']},
                               'completion_lower':counts['COMPLETE']/6,'completion_upper':(counts['COMPLETE']+counts['UNRESOLVED'])/6,
                               'claim_present':claims['PRESENT'],'claim_absent':claims['ABSENT'],'claim_unresolved':claims['UNRESOLVED'],
                               'metadata_inconsistency_count':sum(r['metadata_inconsistency'] is True for r in selected)})
        for case_id in ['CTX-001','CTX-002','CTX-003']:
            for context in ['SHORT','FULL']:
                selected = [r for r in joined if (r['reviewer'],r['case_id'],r['context']) == (reviewer,case_id,context)]
                assert len(selected) == 4
                for i in range(len(selected[0]['requirement_coverage'])):
                    cells = [r['requirement_coverage'][i] for r in selected]
                    coverage_groups.append({'reviewer':reviewer,'case_id':case_id,'context':context,
                                            'requirement_id':cells[0]['requirement_id'],'n_slots':4,
                                            'covered':sum(c['value']==1 for c in cells),'missing_or_incorrect':sum(c['value']==0 for c in cells),
                                            'unresolved':sum(c['value'] is None for c in cells)})
        for case_id in ['CTX-001','CTX-002','CTX-003']:
            for hint in ['NONE','MODAL']:
                for rep in [1,2]:
                    a = next(r for r in joined if (r['reviewer'],r['case_id'],r['hint'],r['replicate'],r['context']) == (reviewer,case_id,hint,rep,'SHORT'))
                    b = next(r for r in joined if (r['reviewer'],r['case_id'],r['hint'],r['replicate'],r['context']) == (reviewer,case_id,hint,rep,'FULL'))
                    paired.append({'reviewer':reviewer,'case_id':case_id,'hint':hint,'replicate':rep,'short_review_id':a['review_id'],'full_review_id':b['review_id'],
                                   'short_complete':a['complete'],'full_complete':b['complete'],
                                   'complete_change': None if a['complete'] is None or b['complete'] is None else b['complete']-a['complete']})
    # Independently check group counts using SQLite, at the reviewer/slot grain.
    db = sqlite3.connect(':memory:')
    db.execute('create table ratings(reviewer text, context text, hint text, case_id text, complete integer, claim integer)')
    db.executemany('insert into ratings values(?,?,?,?,?,?)', [(r['reviewer'],r['context'],r['hint'],r['case_id'],r['complete'],r['unsupported_or_distorted_claim']) for r in joined])
    sql = 'select reviewer,context,hint,count(*),count(distinct case_id),sum(complete=1),sum(complete=0),sum(complete is null),sum(claim=1),sum(claim=0),sum(claim is null) from ratings group by reviewer,context,hint'
    for reviewer,context,hint,n,k,p,f,u,ct,cf,cu in db.execute(sql):
        g=next(r for r in groups if (r['reviewer'],r['context'],r['hint'])==(reviewer,context,hint))
        assert [n,k,p,f,u,ct,cf,cu] == [g[x] for x in ['n_slots','distinct_cases','COMPLETE','INCOMPLETE','UNRESOLVED','claim_present','claim_absent','claim_unresolved']]
    validation = {**generation,'assessment':'Share with caveats','reviewer_slot_rows':48,'unique_generation_slots':24,
                  'source_cases':3,'reviewers':2,'reviewer_condition_groups':8,'sqlite_group_count_check':True,
                  'paired_comparisons':24,'inferential_tests_performed':False,'old_v2_results_changed':False,
                  'same_scored_fields':sum(c['same_all_scored_fields'] for c in comparisons),
                  'different_scored_fields_rows':sum(not c['same_all_scored_fields'] for c in comparisons),
                  'same_overall_completeness':sum(c['root']['full_context_target_completeness']==c['fresh']['full_context_target_completeness'] for c in comparisons),
                  'same_claim_status':sum(c['root']['unsupported_or_distorted_claim']==c['fresh']['unsupported_or_distorted_claim'] for c in comparisons),
                  'same_requirement_coverage_items':sum(a['value']==b['value'] for c in comparisons for a,b in zip(c['root']['requirement_coverage'],c['fresh']['requirement_coverage'])),
                  'human_expert_validation':False,'automatic_adjudication_applied':False}
    return {'joined_reviews_48.jsonl':joined,'review_comparison_24.jsonl':comparisons,
            'condition_results_8.jsonl':groups,'requirement_results_36.jsonl':coverage_groups,
            'paired_results_24.jsonl':paired,'validation_report.json':validation}


def build():
    assert not (OUT/'completion_manifest.json').exists()
    data=derived()
    for name,content in data.items():write(ANALYSIS/name,content)
    print(json.dumps(data['validation_report.json'],ensure_ascii=False))


def finish():
    assert not (OUT/'completion_manifest.json').exists()
    data=derived()
    for name,content in data.items():assert (rows(ANALYSIS/name) if name.endswith('jsonl') else read(ANALYSIS/name))==content
    assert 'RESULTS_PENDING' not in DOC.read_text()
    support=[DOC,Path(__file__).resolve(),Path(gen.__file__).resolve(),Path(old_review.__file__).resolve(),
             ROOT/'tools/record_context_microstudy_root_review_20260909.py',
             ROOT/'outputs/review/v2_independent_ai_20260909/summary.json',
             ROOT/'outputs/review/v2_independent_ai_20260909/comparison_15.jsonl',
             ROOT/'outputs/review/v2_independent_ai_20260909/reviewer_a/reviewer_manifest.json']
    write(OUT/'completion_manifest.json',{'status':'SEPARATE_AI_REVIEW_AND_MICROSTUDY_COMPLETE','completed_at':datetime.now(timezone.utc).isoformat(),
                                         'file_sha256':{str(p.relative_to(OUT)):sha(p) for p in sorted(OUT.rglob('*')) if p.is_file()},
                                         'support_file_sha256':{str(p.relative_to(ROOT)):sha(p) for p in support}})
    for p in OUT.rglob('*'):
        if p.is_file():p.chmod(0o444)


def verify():
    m=read(OUT/'completion_manifest.json')
    for p,h in m['file_sha256'].items():assert sha(OUT/p)==h
    for p,h in m['support_file_sha256'].items():assert sha(ROOT/p)==h
    data=derived()
    for name,content in data.items():assert (rows(ANALYSIS/name) if name.endswith('jsonl') else read(ANALYSIS/name))==content
    subprocess.run([sys.executable,str(ROOT/'tools/prepare_v2_followup_20260909.py'),'verify'],cwd=ROOT,check=True,capture_output=True,text=True)
    print(json.dumps(data['validation_report.json'],ensure_ascii=False))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['build','finish','verify'])
    {'build':build,'finish':finish,'verify':verify}[parser.parse_args().command]()
