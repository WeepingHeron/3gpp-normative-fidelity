"""Deterministic preparation/freeze for paired, post-hoc repair of all six prior P1 outputs."""
import json,hashlib,datetime,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'experiments/preservation_repair_v1_20260914';OLD=ROOT/'experiments/proposition_pipeline_v1_20260913';RUN=ROOT/'experiments/runs/proposition_pipeline_v1_20260913'
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return json.loads(p.read_text())
def rows(p):return list(map(json.loads,p.read_text().splitlines()))
def compact(o):return json.dumps(o,ensure_ascii=False,separators=(',',':'))
def write(p,o):p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def derive():
 for folder,manifest in [(ROOT,OLD/'input_freeze_manifest.json'),(RUN,RUN/'output_freeze_manifest.json')]:
  for p,h in read(manifest)['file_sha256'].items():assert sha((folder/p).read_bytes())==h,p
 cases={c['case_id']:c for c in read(OLD/'generator_inputs.json')};finals=[r for r in rows(RUN/'final_explanations.jsonl') if r['arm']=='P1_EXTRACT_COMPOSE'];stages={r['slot_id']:r for r in rows(RUN/'parsed_stages.jsonl') if r['stage']=='extract'};requests={r['slot_id']:r for r in rows(RUN/'requests.jsonl') if r['stage']=='compose'}
 fields={'proposition_id':{'type':'string'},'source_support':{'type':'string','enum':['SUPPORTED','CONFLICT','UNRESOLVED']},'explanation_status':{'type':'string','enum':['PRESERVED','OMITTED','DISTORTED','UNRESOLVED']},'source_quote':{'type':'string'},'explanation_quote':{'type':'string'},'required_change':{'type':'string'}}
 item={'type':'object','properties':fields,'required':list(fields),'additionalProperties':False};schema={'type':'object','properties':{k:{'type':'array','items':item} for k in ['checks','additional_source_findings']},'required':['checks','additional_source_findings'],'additionalProperties':False}
 audit=(BASE/'audit_instruction.md').read_text();rewrite=(BASE/'rewrite_instruction.md').read_text();suffix=(BASE/'repair_suffix.md').read_text()
 def project(c):return {'question_ko':c['question_ko'],'target_text':c['target_text'],'context_quotes':[b['quote'] for b in c['context_blocks']],'source':{k:c['source'][k] for k in ['spec_id','version','clause_id']}}
 def build(cs):
  seeds=[];plan=[]
  for f in finals:
   sid=f['slot_id'];c=cs[f['case_id']];ext=stages[sid];prior=requests[sid]['request'];seed={'seed_id':sid,'case_id':f['case_id'],'replicate':f['replicate'],'source_input':project(c),'propositions':ext['parsed'],'draft':f['parsed'],'source_compose_request_sha256':requests[sid]['request_sha256'],'source_extraction_response_id':ext['response_id']};seeds.append(seed)
   baseline={**prior,'input':prior['input']+rewrite+compact(f['parsed'])}
   ar={**prior,'input':compact({'source':project(c),'automatically_extracted_propositions':ext['parsed'],'draft':f['parsed']})+'\n'+audit,'max_output_tokens':3000,'text':{'format':{'type':'json_schema','name':'proposition_preservation_audit','strict':True,'schema':schema}}}
   for arm in ['R0_REWRITE','R1_AUDIT_REPAIR']:
    plan.append({'slot_id':f"{f['case_id']}-{arm}-R{f['replicate']}",'case_id':f['case_id'],'arm':arm,'replicate':f['replicate'],'seed_id':sid,'baseline_request':baseline,**({'audit_request':ar} if arm=='R1_AUDIT_REPAIR' else {})})
  return seeds,sorted(plan,key=lambda r:sha(('preservation-repair-v1-20260914'+r['slot_id']).encode()))
 seeds,plan=build(cases);assert (seeds,plan)==build({k:{**v,'requirements':'GOLD_SENTINEL','prior_judgment':'GOLD_SENTINEL'} for k,v in cases.items()})
 def reserve(r,extra=0):return ((len(r['input'].encode())+extra+len(compact(r['text']['format']['schema']).encode())+2048)*.75+r['max_output_tokens']*4.5)/1e6
 total=0
 for r in plan:
  v=reserve(r['baseline_request']) if r['arm']=='R0_REWRITE' else reserve(r['audit_request'])+reserve(r['baseline_request'],len(suffix.encode())+24001)
  r['planning_reservation_usd']=v;total+=v
 assert len(seeds)==6 and len(plan)==12 and total<=.5,total
 return seeds,plan,schema,total
cmd=sys.argv[1] if len(sys.argv)>1 else 'verify'
if cmd=='prepare':
 assert not (BASE/'protocol.json').exists();seeds,plan,schema,total=derive()
 write(BASE/'seeds_6.json',seeds);write(BASE/'audit_schema.json',schema);write(BASE/'evaluation_reference.json',read(OLD/'evaluation_reference.json'));write(BASE/'generator_inputs.json',read(OLD/'generator_inputs.json'));write(BASE/'response_schema.json',read(OLD/'response_schema.json'))
 (BASE/'request_recipe_12.jsonl').write_text(''.join(compact(r)+'\n' for r in plan))
 write(BASE/'protocol.json',{'experiment_id':'PRESERVATION_REPAIR_V1_20260914','status':'READY_TO_FREEZE','model':'gpt-5.4-mini-2026-03-17','arms':['R0_REWRITE','R1_AUDIT_REPAIR'],'planned_calls':18,'planned_explanations':12,'seed_outputs':6,'source_cases':3,'source_output_freeze_sha256':sha((RUN/'output_freeze_manifest.json').read_bytes()),'pricing_usd_per_million':{'input':.75,'cached_input':.075,'output':4.5},'pricing_checked_date':'2026-09-14','pricing_source':'https://developers.openai.com/api/docs/models/gpt-5.4-mini','generation_cost_cap_usd':.5,'planning_reservation_usd':total,'max_audit_json_utf8_bytes':24000,'timeout_ms':60000,'design':'All six sealed prior P1 seeds, including complete and unresolved, each assigned once to direct rewrite and audit+repair. No new extraction or seed selection. Paired post-hoc repair diagnostic, not an end-to-end fresh generation efficacy estimate. Extra audit call and context are bundled; not an isolated formatting effect.','request_policy':'Same original P1 source/extraction input and draft for both final calls; same generic rewrite instruction. Only R1 adds full unedited audit JSON plus frozen suffix. Source authority precedes automatic extraction/audit. No evaluator requirements/scores in requests.','fixed_parameters':'temperature=0, reasoning none, store false; final schema same and 2-4 sentences, max_output_tokens=900; audit max_output_tokens=3000','execution':'Hash-ordered 12 slots, sequential. Audit immediately precedes repair. No retry/resume/filtering/editing of audit. Stop on transport/HTTP/model/usage/schema/incomplete/size/budget errors. Missing/duplicate IDs or unsupported audit labels are diagnostic, not selection. Preserve all slots.','evaluation':'Coordinator manual primary assessment of 12 anonymized final outputs using unchanged nine requirements and 1/0/null, true/false/null rules; seal before reading new audit outputs or keys. Coordinator knows seed outputs and prior scores, so no independent/blinded review claim. Old seed scores remain unchanged.','diagnostic':'After primary seal, inspect audit whether prior missing/distorted elements were flagged and whether final preserved them. Audit self-labels do not determine final success. Quote matching is diagnostic only.','candidate_gate':['All 18 calls completed and 12 final explanations usable with input/output seals valid','R1 confirmed complete > R0 complete+unresolved','R1 confirmed distorted+unresolved <= R0 confirmed distorted','No R0 confirmed complete paired seed regresses in R1','No previously confirmed complete seed regresses in R1'], 'decision':'At most FIRST_REVIEW_CANDIDATE, never unseen-clause authorization; otherwise IMPROVEMENT_NOT_CONFIRMED. Preserve previous HOLD. No automatic new trial, tuning, independent-agent review or unseen-clause run.','scope':'3 known developmental cases, six fixed drafts; descriptive comparisons and unresolved bounds only; no p-values/CI/generalization.'})
 write(BASE/'validation_report.json',{'status':'OFFLINE_PREPARED','source_integrity_valid':True,'all_six_prior_P1_included':True,'evaluator_field_perturbation_check':True,'planned_reservation_usd':total,'live_calls':0});print(json.dumps({'status':'PREPARED','reservation_usd':total}))
elif cmd in ['verify','freeze']:
 seeds,plan,schema,total=derive();assert read(BASE/'seeds_6.json')==seeds;assert read(BASE/'audit_schema.json')==schema;assert (BASE/'request_recipe_12.jsonl').read_text()==''.join(compact(r)+'\n' for r in plan)
 for n in ['generator_inputs.json','response_schema.json','evaluation_reference.json']:assert read(BASE/n)==read(OLD/n)
 assert abs(read(BASE/'protocol.json')['planning_reservation_usd']-total)<1e-12
 if cmd=='freeze':
  assert not (BASE/'input_freeze_manifest.json').exists()
  paths=list(BASE.iterdir())+[Path(__file__).resolve(),ROOT/'experiments/run_preservation_repair_20260914.mjs',ROOT/'experiments/test_preservation_repair_20260914.mjs',ROOT/'experiments/run_generation_preservation_20260909.mjs',ROOT/'docs/38_preservation_repair_plan_2026-09-14.md']
  write(BASE/'input_freeze_manifest.json',{'status':'FROZEN_BEFORE_GENERATION','frozen_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'file_sha256':{str(p.relative_to(ROOT)):sha(p.read_bytes()) for p in paths}})
  for p in paths+[BASE/'input_freeze_manifest.json']:p.chmod(0o444)
 elif (BASE/'input_freeze_manifest.json').exists():
  for p,h in read(BASE/'input_freeze_manifest.json')['file_sha256'].items():assert sha((ROOT/p).read_bytes())==h,p
 print(json.dumps({'status':cmd.upper()+'_PASS','live_calls':0}))
else:raise ValueError('Unknown command')
