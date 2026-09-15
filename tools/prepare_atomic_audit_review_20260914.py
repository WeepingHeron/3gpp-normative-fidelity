"""Verify sealed responses and prepare audit-review packets and structural evidence diagnostics."""
from pathlib import Path
import json,hashlib,datetime,collections
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'experiments/atomic_audit_v1_20260914';RUN=ROOT/'experiments/runs/atomic_audit_v1_20260914';OLD=ROOT/'outputs/review/proposition_pipeline_v1_20260913';OUT=ROOT/'outputs/review/atomic_audit_v1_20260914'
def read(p):return json.loads(p.read_text())
def rows(p):return list(map(json.loads,p.read_text().splitlines()))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def compact(o):return json.dumps(o,ensure_ascii=False,separators=(',',':'))
def write(p,o):p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
for folder,m in [(ROOT,BASE/'input_freeze_manifest.json'),(RUN,RUN/'output_freeze_manifest.json'),(OLD/'primary_review',OLD/'primary_review/reviewer_manifest.json')]:
 for f,h in read(m)['file_sha256'].items():assert sha(folder/f)==h,f
m=read(RUN/'manifest.json');assert m['status']=='GENERATION_COMPLETE_SEMANTICS_PENDING' and m['usable_explanations']==m['attempts']==12
assert m['input_freeze_sha256']==sha(BASE/'input_freeze_manifest.json')
plan={r['slot_id']:r for r in rows(BASE/'request_plan.jsonl')};seeds={s['seed_id']:s for s in read(BASE/'seeds_6.json')};requests=rows(RUN/'requests.jsonl');raw=rows(RUN/'raw_responses.jsonl');parsed={r['slot_id']:r for r in rows(RUN/'parsed_responses.jsonl')}
oldj={r['review_id']:r for r in rows(OLD/'primary_review/judgments_12.jsonl')};oldk={r['slot_id']:r for r in rows(OLD/'coordinator_keys_12.jsonl')};oldp={r['review_id']:r for r in rows(OLD/'primary_packets_12.jsonl')};total=0
for req,res in zip(requests,raw):
 assert req['slot_id']==res['slot_id'];assert req['request']==plan[req['slot_id']]['request'];assert hashlib.sha256(compact(req['request']).encode()).hexdigest()==req['request_sha256'];body=res['response'];p=json.loads(''.join(c['text'] for o in body['output'] if o['type']=='message' for c in o['content'] if c['type']=='output_text'));assert p==parsed[req['slot_id']]['parsed']
 u=body['usage'];cached=u.get('input_tokens_details',{}).get('cached_tokens',0);total+=((u['input_tokens']-cached)*.75+cached*.075+u['output_tokens']*4.5)/1e6
assert abs(total-m['known_cost_usd'])<1e-10
assert not OUT.exists();OUT.mkdir();pack=[];keys=[];diags=[]
for i,row in enumerate(sorted(plan.values(),key=lambda r:hashlib.sha256(('atomic-review-v1'+r['slot_id']).encode()).hexdigest()),1):
 rid=f'AAR-{i:03d}';s=seeds[row['seed_id']];oldrid=oldk[s['seed_id']]['review_id'];op=oldp[oldrid];audit=parsed[row['slot_id']]['parsed']
 pack.append({'review_id':rid,'source_input':s['source_input'],'draft':s['draft'],'propositions':s['propositions'],'audit':audit,'reference_requirements':op['requirements'],'sealed_seed_judgment':oldj[oldrid]});keys.append({'review_id':rid,'slot_id':row['slot_id'],'seed_id':row['seed_id'],'arm':row['arm']})
 items=audit['checks']+audit.get('additional_source_findings',[]);sources=[s['source_input']['target_text']]+s['source_input']['context_quotes'];exp=s['draft']['explanation_ko'];qd=[]
 for x in items:
  q=x['source_quote'];e=x['explanation_quote'];qd.append({'id':x.get('check_id',x['proposition_id']),'proposition_id':x['proposition_id'],'status':x['explanation_status'],'source_nonempty':bool(q),'source_exact':bool(q) and any(q in st for st in sources),'source_whitespace_normalized':bool(q) and any(' '.join(q.split()) in ' '.join(st.split()) for st in sources),'explanation_nonempty':bool(e),'explanation_exact':bool(e) and e in exp})
 expected={p['id'] for p in s['propositions']['propositions']};seen={x['proposition_id'] for x in audit['checks']};labels=collections.defaultdict(set)
 for x in items:labels[(x['proposition_id'],x.get('dimension','WHOLE'))].add(x['explanation_status'])
 diags.append({'review_id':rid,'items':qd,'missing_proposition_ids':sorted(expected-seen),'duplicate_check_ids':len([x.get('check_id') for x in items if 'check_id'in x])!=len({x['check_id'] for x in items if 'check_id'in x}),'mixed_status_same_id_dimension':[{'key':list(k),'statuses':sorted(v)} for k,v in labels.items() if len(v)>1],'note':'Mixed status may describe different atomic claims; not an automatic semantic contradiction verdict.'})
for name,data in [('review_packets_12.jsonl',pack),('coordinator_keys_12.jsonl',keys),('structural_diagnostics_12.jsonl',diags)]:
 (OUT/name).write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in data))
write(OUT/'execution_verification.json',{'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','audits':12,'final_explanations_generated':0,'known_cost_usd':total,'input_tokens':sum(r['response']['usage']['input_tokens'] for r in raw),'output_tokens':sum(r['response']['usage']['output_tokens'] for r in raw),'request_and_response_bindings_valid':True})
write(OUT/'packet_manifest.json',{'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'run_output_manifest_sha256':sha(RUN/'output_freeze_manifest.json'),'file_sha256':{p.name:sha(p) for p in OUT.iterdir()}})
for p in OUT.iterdir():p.chmod(0o444)
print(json.dumps({'status':'PACKETS_READY','audits':12,'cost_usd':total}))
