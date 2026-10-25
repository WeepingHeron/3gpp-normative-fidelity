"""Read-only seals, arithmetic, recorded evidence and source-boundary checks; no semantic grading."""
from pathlib import Path
import json,hashlib,re
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'experiments/atomic_audit_v1_20260914';RUN=ROOT/'experiments/runs/atomic_audit_v1_20260914';B=ROOT/'outputs/review/atomic_audit_v1_20260914'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def rows(p):return list(map(json.loads,p.read_text().splitlines()))
for folder,m in [(ROOT,BASE/'input_freeze_manifest.json'),(RUN,RUN/'output_freeze_manifest.json'),(B,B/'packet_manifest.json'),(B/'manual_review',B/'manual_review/reviewer_manifest.json')]:
 for f,h in read(m)['file_sha256'].items():assert sha(folder/f)==h,f
assert read(B/'manual_review/reviewer_manifest.json')['input_sha256']==sha(B/'review_packets_12.jsonl')
assert read(B/'manual_review/reviewer_manifest.json')['script_sha256']==sha(ROOT/'tools/record_atomic_audit_review_20260914.py')
assert read(B/'packet_manifest.json')['run_output_manifest_sha256']==sha(RUN/'output_freeze_manifest.json')
P={r['review_id']:r for r in rows(B/'review_packets_12.jsonl')};K={r['review_id']:r for r in rows(B/'coordinator_keys_12.jsonl')};J=rows(B/'manual_review/judgments_12.jsonl');assert len(P)==len(K)==len(J)==12
for r in J:
 p=P[r['review_id']];items={i.get('check_id',i['proposition_id']):i for g in p['audit'].values() for i in g};ref={q['requirement_id']:q['value'] for q in p['sealed_seed_judgment']['requirement_coverage']}
 assert len(r['requirements'])==len(ref)
 for q in r['requirements']:
  assert q['reference_value']==ref[q['requirement_id']]
  assert q['defect_correctly_detected'] in ([0,1] if q['reference_value']==0 else [None])
  assert q['audit_evidence']==[items[i] for i in q['audit_evidence_ids']]
for c in read(B/'analysis/condition_results.json'):
 r=[j for j in J if K[j['review_id']]['arm']==c['arm']];q=[x for j in r for x in j['requirements']]
 assert c['correctly_detected_defects']==sum(x['defect_correctly_detected']==1 for x in q)
 assert c['false_alarms_on_preserved_requirements']==sum(x['false_alarm_on_preserved_requirement'] for x in q)
 assert c['erroneous_repair_advice_cases']==sum(j['erroneous_repair_advice_case'] for j in r)
 assert c['known_requirement_defects']==8 and c['preserved_requirements']==10
# Verify two explicit wrong-field quotations used in the report.
for rid,cid,expected in [('AAR-004','P8-EXCEPTION',['action','exception']),('AAR-005','P1-E1',['condition'])]:
 p=P[rid];q=next(x['explanation_quote'] for x in p['audit']['checks'] if x.get('check_id')==cid)
 assert q not in p['draft']['explanation_ko'];assert [k for k,v in p['draft'].items() if k!='explanation_ko' and q in v]==expected
for name in ['40_atomic_audit_plan_2026-09-14.md','41_atomic_audit_results_2026-09-14.md']:
 p=ROOT/'docs'/name
 for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if not link.startswith('https:'):assert (p.parent/link).exists(),link
if (B/'completion_manifest.json').exists():
 for f,h in read(B/'completion_manifest.json')['file_sha256'].items():assert sha(ROOT/f)==h,f
print(json.dumps({'status':'PASS','audits':12,'requirement_review_records':36,'seals_and_recorded_evidence_valid':True,'counts_valid':True,'wrong_field_quote_examples_verified':True,'new_api_calls':0}))
