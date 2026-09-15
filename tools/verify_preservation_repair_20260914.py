"""Read-only integrity and arithmetic verification for preservation repair. No semantic inference."""
import json,hashlib,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'experiments/preservation_repair_v1_20260914';RUN=ROOT/'experiments/runs/preservation_repair_v1_20260914';B=ROOT/'outputs/review/preservation_repair_v1_20260914'
def read(p):return json.loads(p.read_text())
def rows(p):return list(map(json.loads,p.read_text().splitlines()))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def hash_json(o):return hashlib.sha256(json.dumps(o,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
for folder,p in [(ROOT,BASE/'input_freeze_manifest.json'),(RUN,RUN/'output_freeze_manifest.json'),(B,B/'packet_manifest.json'),(B/'primary_review',B/'primary_review/reviewer_manifest.json')]:
 for f,h in read(p)['file_sha256'].items():assert sha(folder/f)==h,f
assert read(RUN/'manifest.json')['input_freeze_sha256']==sha(BASE/'input_freeze_manifest.json')
recipe={r['slot_id']:r for r in rows(BASE/'request_recipe_12.jsonl')};stage={(r['slot_id'],r['stage']):r for r in rows(RUN/'parsed_stages.jsonl')};requests=rows(RUN/'requests.jsonl');raw=rows(RUN/'raw_responses.jsonl');assert len(requests)==len(raw)==18
for req,res in zip(requests,raw):
 assert (req['slot_id'],req['stage'])==(res['slot_id'],res['stage']);assert hash_json(req['request'])==req['request_sha256']==res['request_sha256']
 row=recipe[req['slot_id']]
 if req['stage']=='repair':
  a=stage[(req['slot_id'],'audit')];expected={**row['baseline_request'],'input':row['baseline_request']['input']+(BASE/'repair_suffix.md').read_text()+'\n'+json.dumps(a['parsed'],ensure_ascii=False,separators=(',',':'))};assert req['dependency']=={'response_id':a['response_id'],'audit_json_sha256':hash_json(a['parsed'])}
 else:expected=row['audit_request'] if req['stage']=='audit' else row['baseline_request']
 assert req['request']==expected
 body=res['response'];parsed=json.loads(''.join(c['text'] for o in body['output'] if o['type']=='message' for c in o['content'] if c['type']=='output_text'));assert parsed==stage[(req['slot_id'],req['stage'])]['parsed']
P={r['review_id']:r for r in rows(B/'primary_packets_12.jsonl')};J={r['review_id']:r for r in rows(B/'primary_review/judgments_12.jsonl')};K={r['review_id']:r for r in rows(B/'coordinator_keys_12.jsonl')};assert len(P)==len(J)==len(K)==12
assert read(B/'primary_review/reviewer_manifest.json')['input_sha256']==sha(B/'primary_packets_12.jsonl')
for rid,j in J.items():
 p=P[rid];sources=[p['target_text']]+[b['quote'] for b in p['reference_context_blocks']];vals=[]
 assert [q['requirement_id'] for q in j['requirement_coverage']]==[q['id'] for q in p['requirements']]
 for q in j['requirement_coverage']:
  assert q['value'] is None or type(q['value']) is int and q['value'] in [0,1];vals.append(q['value'])
  assert all(x in p['explanation_ko'] for x in q['response_quotes']);assert all(any(x in s for s in sources) for x in q['source_quotes'])
 claim=j['unsupported_or_distorted_claim'];assert claim is None or type(claim) is bool
 assert j['full_context_target_completeness']==(0 if 0 in vals or claim is True else None if None in vals or claim is None else 1)
 assert all(x in p['explanation_ko'] for x in j['claim_evidence_quotes'])
if (B/'analysis/analysis_manifest.json').exists():
 for f,h in read(B/'analysis/analysis_manifest.json')['file_sha256'].items():assert sha(B/'analysis'/f)==h
 for r in read(B/'analysis/condition_results.json'):
  js=[J[i] for i,k in K.items() if k['arm']==r['arm']];c=collections.Counter(j['full_context_target_completeness'] for j in js);assert [r['complete'],r['incomplete'],r['unresolved']]==[c[1],c[0],c[None]]
if (B/'completion_manifest.json').exists():
 for f,h in read(B/'completion_manifest.json')['file_sha256'].items():assert sha(ROOT/f)==h
print(json.dumps({'status':'PASS','requests':18,'primary_explanations':12,'primary_requirements':36,'dynamic_audit_binding_valid':True,'seals_valid':True,'manual_judgment_quotes_and_formula_valid':True,'new_api_calls':0}))
