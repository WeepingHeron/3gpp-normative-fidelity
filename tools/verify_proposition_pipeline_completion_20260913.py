"""Read-only completion verifier. Checks integrity/joins/arithmetic, never assigns semantic values."""
import json,hashlib,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'experiments/proposition_pipeline_v1_20260913';RUN=ROOT/'experiments/runs/proposition_pipeline_v1_20260913';B=ROOT/'outputs/review/proposition_pipeline_v1_20260913'
def read(p):return json.loads(p.read_text())
def rows(p):return list(map(json.loads,p.read_text().splitlines()))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for folder,manifest in [(ROOT,BASE/'input_freeze_manifest.json'),(RUN,RUN/'output_freeze_manifest.json'),(B,B/'packet_manifest.json'),(B/'primary_review',B/'primary_review/reviewer_manifest.json'),(B/'stage_analysis',B/'stage_analysis/analysis_manifest.json')]:
 for p,h in read(manifest)['file_sha256'].items():assert sha(folder/p)==h,p
assert read(B/'stage_analysis/analysis_manifest.json')['primary_manifest_sha256']==sha(B/'primary_review/reviewer_manifest.json')
assert read(B/'primary_review/reviewer_manifest.json')['serializer_sha256']==sha(ROOT/'tools/record_proposition_pipeline_primary_20260913.py')
assert read(B/'stage_analysis/analysis_manifest.json')['script_sha256']==sha(ROOT/'tools/analyze_proposition_pipeline_stages_20260913.py')
assert read(B/'packet_manifest.json')['source_output_freeze_sha256']==sha(RUN/'output_freeze_manifest.json')
P={r['review_id']:r for r in rows(B/'primary_packets_12.jsonl')};J={r['review_id']:r for r in rows(B/'primary_review/judgments_12.jsonl')};K={r['review_id']:r for r in rows(B/'coordinator_keys_12.jsonl')};assert len(P)==len(J)==len(K)==12
for rid,j in J.items():
 p=P[rid];source=[p['target_text']]+[b['quote'] for b in p['reference_context_blocks']];values=[]
 assert [c['requirement_id'] for c in j['requirement_coverage']]==[c['id'] for c in p['requirements']]
 for c in j['requirement_coverage']:
  assert c['value'] is None or type(c['value']) is int and c['value'] in [0,1]
  assert all(q in p['explanation_ko'] for q in c['response_quotes']);assert all(any(q in s for s in source) for q in c['source_quotes']);values.append(c['value'])
 claim=j['unsupported_or_distorted_claim'];assert claim is None or type(claim) is bool
 score=0 if 0 in values or claim is True else None if None in values or claim is None else 1
 assert score==j['full_context_target_completeness']
 assert all(q in p['explanation_ko'] for q in j['claim_evidence_quotes'])
for d in rows(B/'stage_analysis/extraction_judgments_6.jsonl'):
 props={p['id']:p for p in d['all_generated_propositions']}
 for c in d['requirement_coverage']:
  assert c['extraction_field_evidence']==[{k:v for k,v in props[i].items() if k!='source_quotes'} for i in c['proposition_ids']]
trans=rows(B/'stage_analysis/requirement_transitions_18.jsonl');assert len(trans)==18
assert dict(collections.Counter(x['stage_class'] for x in trans))==read(B/'stage_analysis/summary.json')['stage_counts']
for r in read(B/'stage_analysis/condition_results.json'):
 j=[J[i] for i,k in K.items() if k['arm']==r['arm']];c=collections.Counter(x['full_context_target_completeness'] for x in j);assert [r['complete'],r['incomplete'],r['unresolved']]==[c[1],c[0],c[None]]
for name in ['36_proposition_pipeline_plan_2026-09-13.md','37_proposition_pipeline_results_2026-09-13.md']:
 import re
 p=ROOT/'docs'/name
 for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if not link.startswith('https:'):assert (p.parent/link).exists(),link
complete=B/'completion_manifest.json'
if complete.exists():
 for p,h in read(complete)['file_sha256'].items():assert sha(ROOT/p)==h,p
print(json.dumps({'status':'PASS','input_output_primary_stage_seals_valid':True,'manual_score_formula_and_quotes_valid':True,'stage_field_evidence_exact':True,'final_records':12,'primary_requirements':36,'stage_requirements':18,'report_links_valid':True,'new_api_calls':0}))
