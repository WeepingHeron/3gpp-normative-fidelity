"""Freeze static audit requests without exposing evaluator reference labels."""
import json,hashlib,sys,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'experiments/atomic_audit_v1_20260914';OLD=ROOT/'experiments/preservation_repair_v1_20260914'
def read(p):return json.loads(p.read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
def compact(o):return json.dumps(o,ensure_ascii=False,separators=(',',':'))
def write(p,o):p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def derive():
 for p,h in read(OLD/'input_freeze_manifest.json')['file_sha256'].items():assert sha((ROOT/p).read_bytes())==h,p
 old=[json.loads(l) for l in (OLD/'request_recipe_12.jsonl').read_text().splitlines() if l];seeds=read(OLD/'seeds_6.json');byseed={s['seed_id']:s for s in seeds}
 fields={'check_id':{'type':'string'},'proposition_id':{'type':'string'},'dimension':{'type':'string','enum':['MODALITY','ACTOR_ACTION','SCOPE_CONDITION','EXCEPTION','FOLLOWUP']},'source_support':{'type':'string','enum':['SUPPORTED','CONFLICT','UNRESOLVED']},'explanation_status':{'type':'string','enum':['PRESERVED','OMITTED','DISTORTED','UNRESOLVED']},'source_quote':{'type':'string'},'explanation_quote':{'type':'string'},'required_change':{'type':'string'}}
 schema={'type':'object','properties':{'checks':{'type':'array','items':{'type':'object','properties':fields,'required':list(fields),'additionalProperties':False}}},'required':['checks'],'additionalProperties':False}
 atom=(BASE/'atomic_instruction.md').read_text();prior=(OLD/'audit_instruction.md').read_text();plan=[]
 for row in old:
  if 'audit_request' not in row:continue
  r=row['audit_request'];assert r['input'].endswith(prior)
  baseline={**r,'max_output_tokens':6000};atomic={**baseline,'input':r['input'][:-len(prior)]+atom,'text':{'format':{'type':'json_schema','name':'atomic_preservation_audit','strict':True,'schema':schema}}}
  for arm,request in [('C0_COARSE',baseline),('C1_ATOMIC',atomic)]:
   cost=((len(request['input'].encode())+len(compact(request['text']['format']['schema']).encode())+2048)*.75+6000*4.5)/1e6
   plan.append({'slot_id':f"{row['case_id']}-{arm}-R{row['replicate']}",'seed_id':row['seed_id'],'case_id':row['case_id'],'arm':arm,'replicate':row['replicate'],'request':request,'request_sha256':sha(compact(request).encode()),'estimated_reservation_usd':cost})
 plan.sort(key=lambda r:sha(('atomic-audit-v1-20260914'+r['slot_id']).encode()));total=sum(r['estimated_reservation_usd'] for r in plan);assert len(plan)==12 and total<.5,total
 # Seeds are already a generator-only projection; the build above reads only prior actual requests.
 assert all('requirement_coverage' not in r['request']['input'] and 'full_context_target_completeness' not in r['request']['input'] for r in plan)
 return plan,schema,total,seeds
cmd=sys.argv[1] if len(sys.argv)>1 else 'verify'
if cmd=='prepare':
 assert not (BASE/'protocol.json').exists();plan,schema,total,seeds=derive()
 (BASE/'request_plan.jsonl').write_text(''.join(compact(r)+'\n' for r in plan));write(BASE/'atomic_schema.json',schema);write(BASE/'seeds_6.json',seeds)
 for n in ['evaluation_reference.json','generator_inputs.json']:write(BASE/n,read(OLD/n))
 write(BASE/'protocol.json',{'experiment_id':'ATOMIC_AUDIT_V1_20260914','status':'READY_TO_FREEZE','model':'gpt-5.4-mini-2026-03-17','parameters':{'temperature':0,'max_output_tokens':6000,'reasoning_effort':'none'},'planned_calls':12,'pricing_usd_per_million':{'input':.75,'cached_input':.075,'output':4.5},'pricing_checked_date':'2026-09-14','pricing_source':'https://developers.openai.com/api/docs/models/gpt-5.4-mini','generation_cost_cap_usd':.5,'reservation_usd':total,'runtime_policy':{'request_timeout_ms':60000},'comparison':'Fresh coarse vs atomic audits on all six fixed prior P1 seeds; no new explanations or repair. Both capped at 6000 output tokens to accommodate atomic rows; coarse input identical to previous audit, cap differs from historical 3000. Same model/temperature/reasoning/source/extraction/draft; changes are audit granularity, evidence and consistency instructions and schema, a bundled intervention.','evaluation':'Coordinator manually maps audits to the same nine requirements over six seed explanations, including partial detection, contradictory diagnosis and erroneous repair advice. Compare to sealed prior primary labels without changing them; these are AI development references, not human gold. No automated semantic grading.','reference_policy':'Full requirement match includes strength, compound components, evidence and unresolved labels; detection of one missing component must not be inflated to perfect diagnosis. Coverage and evidence diagnostics separate.','primary_metric':'Number of seed-requirement defects (reference=0) explicitly and correctly identified with source/draft grounding, per arm. Report missed or contradictory flags separately. Also count false alarms on reference=1 and adjudication errors on unresolved claims. No unseen promotion based on this audit-only test.','candidate_gate':['All 12 responses usable and sealed','Atomic detects more known requirement defects than coarse','Atomic introduces no additional false alarms on preserved requirements','Atomic introduces no additional erroneous repair-advice cases','Report exact quote, per-proposition coverage and contradiction diagnostics without treating them as semantic proof'],'limits':'Post-hoc test on three known sources/six known drafts, one coordinator reviewer; not new clause efficacy, not independent expert audit, no p-values/CI. No iterative tuning or automatic final-generation experiment.'})
 write(BASE/'validation_report.json',{'status':'OFFLINE_PREPARED','prior_freeze_valid':True,'generator_inputs_only':True,'all_six_seeds_both_arms':True,'same_parameters_except_instruction_schema':True,'reservation_usd':total,'live_calls':0});print(json.dumps({'status':'PREPARED','reservation_usd':total}))
elif cmd in ['verify','freeze']:
 plan,schema,total,seeds=derive();assert (BASE/'request_plan.jsonl').read_text()==''.join(compact(r)+'\n' for r in plan);assert read(BASE/'atomic_schema.json')==schema;assert read(BASE/'seeds_6.json')==seeds
 if cmd=='freeze':
  assert not (BASE/'input_freeze_manifest.json').exists();paths=list(BASE.iterdir())+[Path(__file__).resolve(),ROOT/'experiments/run_atomic_audit_20260914.mjs',ROOT/'experiments/run_preservation_repair_20260914.mjs',ROOT/'experiments/run_generation_preservation_20260909.mjs',ROOT/'experiments/test_atomic_audit_20260914.mjs',ROOT/'docs/40_atomic_audit_plan_2026-09-14.md']
  write(BASE/'input_freeze_manifest.json',{'status':'FROZEN_BEFORE_GENERATION','planned_calls':12,'frozen_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'file_sha256':{str(p.relative_to(ROOT)):sha(p.read_bytes()) for p in paths}})
  for p in paths+[BASE/'input_freeze_manifest.json']:p.chmod(0o444)
 elif (BASE/'input_freeze_manifest.json').exists():
  for p,h in read(BASE/'input_freeze_manifest.json')['file_sha256'].items():assert sha((ROOT/p).read_bytes())==h,p
 print(json.dumps({'status':cmd.upper()+'_PASS','live_calls':0}))
else:raise ValueError('Unknown command')
