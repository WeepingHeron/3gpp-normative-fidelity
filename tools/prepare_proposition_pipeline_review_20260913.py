"""Verify sealed dynamic pipeline and emit primary-only packets before extraction inspection."""
import json,hashlib,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'experiments/proposition_pipeline_v1_20260913';RUN=ROOT/'experiments/runs/proposition_pipeline_v1_20260913';OUT=ROOT/'outputs/review/proposition_pipeline_v1_20260913'
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return json.loads(p.read_text())
def rows(p):return list(map(json.loads,p.read_text().splitlines()))
def compact(o):return json.dumps(o,ensure_ascii=False,separators=(',',':'))
def write(p,o):p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
for root,manifest in [(ROOT,read(BASE/'input_freeze_manifest.json')),(RUN,read(RUN/'output_freeze_manifest.json'))]:
 for p,h in manifest['file_sha256'].items():assert sha((root/p).read_bytes())==h,p
m=read(RUN/'manifest.json');assert m['status']=='GENERATION_COMPLETE_SEMANTICS_PENDING' and m['attempts']==m['returned']==18 and m['explanations']==12
assert m['input_freeze_sha256']==sha((BASE/'input_freeze_manifest.json').read_bytes())
requests=rows(RUN/'requests.jsonl');raw=rows(RUN/'raw_responses.jsonl');stages=rows(RUN/'parsed_stages.jsonl');finals=rows(RUN/'final_explanations.jsonl');recipe={r['slot_id']:r for r in rows(BASE/'request_recipe_12.jsonl')};suffix=(BASE/'composition_suffix.md').read_text()
by_stage={(r['slot_id'],r['stage']):r for r in stages};total=0
for req,res in zip(requests,raw):
 assert (req['slot_id'],req['stage'],req['request_sha256'])==(res['slot_id'],res['stage'],res['request_sha256'])
 assert sha(compact(req['request']).encode())==req['request_sha256']
 slot=recipe[req['slot_id']]
 if req['stage']=='compose':
  x=by_stage[(req['slot_id'],'extract')];expected={**slot['baseline_request'],'input':slot['baseline_request']['input']+suffix+'\n'+compact(x['parsed'])}
  assert req['dependency']=={'response_id':x['response_id'],'extraction_json_sha256':sha(compact(x['parsed']).encode())}
 else:expected=slot['extraction_request'] if req['stage']=='extract' else slot['baseline_request']
 assert req['request']==expected
 body=res['response'];assert body['status']=='completed' and body['model']=='gpt-5.4-mini-2026-03-17'
 parsed=json.loads(''.join(c['text'] for o in body['output'] if o['type']=='message' for c in o['content'] if c['type']=='output_text'));assert parsed==by_stage[(req['slot_id'],req['stage'])]['parsed']
 u=body['usage'];cache=u.get('input_tokens_details',{}).get('cached_tokens',0);total+=((u['input_tokens']-cache)*.75+cache*.075+u['output_tokens']*4.5)/1e6
assert abs(total-m['known_cost_usd'])<1e-10
cases={c['case_id']:c for c in read(BASE/'generator_inputs.json')};ev={c['case_id']:c for c in read(BASE/'evaluation_reference.json')['cases']}
assert not OUT.exists();OUT.mkdir()
pack=[];keys=[]
for i,r in enumerate(sorted(finals,key=lambda x:sha(('pp-review-v1'+x['slot_id']).encode())),1):
 rid=f'PPR-{i:03d}';c=cases[r['case_id']]
 stage='compose' if r['arm']=='P1_EXTRACT_COMPOSE' else 'explain';assert r['parsed']==by_stage[(r['slot_id'],stage)]['parsed']
 pack.append({'review_id':rid,'target_text':c['target_text'],'question_ko':c['question_ko'],'source':c['source'],'reference_context_blocks':c['context_blocks'],'requirements':ev[r['case_id']]['requirements'],'explanation_ko':r['parsed']['explanation_ko'],'output_metadata_for_separate_audit':{k:v for k,v in r['parsed'].items() if k!='explanation_ko'}})
 keys.append({'review_id':rid,**{k:r[k] for k in ['slot_id','case_id','arm','replicate']}})
for name,data in [('primary_packets_12.jsonl',pack),('coordinator_keys_12.jsonl',keys)]:
 (OUT/name).write_text(''.join(compact(r)+'\n' for r in data))
write(OUT/'execution_verification.json',{'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','actual_requests':18,'final_explanations':12,'all_dynamic_bindings_exact':True,'raw_parsed_final_equal':True,'all_seals_valid':True,'cost_recomputed_usd':total,'input_tokens':sum(r['response']['usage']['input_tokens'] for r in raw),'output_tokens':sum(r['response']['usage']['output_tokens'] for r in raw)})
write(OUT/'packet_manifest.json',{'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_output_freeze_sha256':sha((RUN/'output_freeze_manifest.json').read_bytes()),'file_sha256':{p.name:sha(p.read_bytes()) for p in OUT.iterdir()}})
for p in OUT.iterdir():p.chmod(0o444)
print(json.dumps({'status':'VERIFIED_PRIMARY_PACKETS_READY','explanations':12,'cost_usd':total}))
