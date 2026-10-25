"""Build and verify a pre-generation, gold-free dynamic request recipe. No API calls."""
import json,hashlib,sys,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'experiments/proposition_pipeline_v1_20260913'
OLD=ROOT/'experiments/generation_preservation_v1_20260909'
SELF=Path(__file__).resolve()
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return json.loads(p.read_text())
def compact(o):return json.dumps(o,ensure_ascii=False,separators=(',',':'))
def write(p,o):p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def source(c):
 return '\n'.join(['## 질문',c['question_ko'],'## 대상 영문 문장',c['target_text'],'## 추가 원문 문맥','\n\n'.join(b['quote'] for b in c['context_blocks']),'## 출처 식별자',c['source']['spec_id'],c['source']['version'],c['source']['clause_id']])
def derive():
 old_manifest=read(OLD/'input_freeze_manifest.json')
 for p,h in old_manifest['file_sha256'].items():assert sha((ROOT/p).read_bytes())==h,p
 cases=read(OLD/'generator_inputs.json');prior=[json.loads(l) for l in (OLD/'request_plan.jsonl').read_text().splitlines()]
 fields=['id','actor','modal','action_or_capability','scope','condition','negation_or_exception','consequent']
 props={f:{'type':'string'} for f in fields};props['source_quotes']={'type':'array','items':{'type':'string'}}
 item={'type':'object','properties':props,'required':list(props),'additionalProperties':False}
 schema={'type':'object','properties':{'propositions':{'type':'array','items':item}},'required':['propositions'],'additionalProperties':False}
 instruction=(BASE/'extraction_instruction.md').read_text();suffix=(BASE/'composition_suffix.md').read_text()
 def build(cs):
  result=[]
  for c in cs:
   baseline=next(r['request'] for r in prior if r['case_id']==c['case_id'] and r['arm']=='A2_MODAL_CHECK')
   ext={**baseline,'input':instruction+'\n'+source(c),'max_output_tokens':2500,'text':{'format':{'type':'json_schema','name':'source_propositions','strict':True,'schema':schema}}}
   for arm in ['A2_FRESH','P1_EXTRACT_COMPOSE']:
    for rep in [1,2]:
     result.append({'slot_id':f"{c['case_id']}-{arm}-R{rep}",'case_id':c['case_id'],'arm':arm,'replicate':rep,'baseline_request':baseline,**({'extraction_request':ext} if arm!='A2_FRESH' else {})})
  return sorted(result,key=lambda r:sha(('proposition-pipeline-v1-20260913'+r['slot_id']).encode()))
 plan=build(cases)
 contaminated=[{**c,'requirements':'EVALUATOR_SENTINEL','prior_judgment':'EVALUATOR_SENTINEL'} for c in cases]
 assert plan==build(contaminated)
 prices={'input':.75,'cached_input':.075,'output':4.5}
 def reserve(r,extra=0):return ((len(r['input'].encode())+extra+len(compact(r['text']['format']['schema']).encode())+2048)*.75+r['max_output_tokens']*4.5)/1e6
 total=0
 for r in plan:
  budget=reserve(r['baseline_request']) if r['arm']=='A2_FRESH' else reserve(r['extraction_request'])+reserve(r['baseline_request'],len(suffix.encode())+24000+1)
  r['planning_reservation_usd']=budget;total+=budget
 assert len(plan)==12 and total<.5
 return cases,schema,plan,total
cmd=sys.argv[1] if len(sys.argv)>1 else 'verify'
if cmd=='prepare':
 assert not (BASE/'protocol.json').exists()
 cases,schema,plan,total=derive()
 for name,obj in [('generator_inputs.json',cases),('extraction_schema.json',schema),('response_schema.json',read(OLD/'response_schema.json')),('evaluation_reference.json',read(OLD/'evaluation_reference.json'))]:write(BASE/name,obj)
 (BASE/'request_recipe_12.jsonl').write_text(''.join(compact(r)+'\n' for r in plan))
 write(BASE/'protocol.json',{'experiment_id':'PROPOSITION_PIPELINE_V1_20260913','status':'READY_TO_FREEZE','source_freeze_sha256':sha((OLD/'input_freeze_manifest.json').read_bytes()),'arms':['A2_FRESH','P1_EXTRACT_COMPOSE'],'cases':3,'replicates':2,'planned_final_explanations':12,'planned_api_calls':18,'model':'gpt-5.4-mini-2026-03-17','pricing_usd_per_million':{'input':.75,'cached_input':.075,'output':4.5},'pricing_checked_date':'2026-09-13','pricing_source':'https://developers.openai.com/api/docs/models/gpt-5.4-mini','generation_cost_cap_usd':.5,'planning_reservation_usd':total,'max_extraction_json_utf8_bytes':24000,'timeout_ms':60000,'no_retry_or_resume':True,'method':'One automatically generated proposition list per treatment replicate; pass complete compact JSON without human editing to an otherwise identical A2 request plus frozen generic suffix. No gold, no case-specific hints. Raw source retained. Extract 2500 output tokens; compose/baseline 900; explanation 2-4 sentences unchanged. Extra call, tokens and generic guidance are a bundled intervention, not an isolated structural-format effect.','runtime':'Fixed hash order of 12 pipeline slots; treatment extraction immediately precedes composition; sequential requests. Freeze recipe before generation, bind actual dynamic request to exact extraction response. Stop on delivery/schema/transport/usage/model/size/budget error; preserve all slots, no rerun. Quote matching is diagnostic only, never semantic grading or response selection.','evaluation':'Same nine requirements and completeness/ambiguity rules; primary surface explanation only. Coordinator manual review first, sealed before intermediate-stage inspection. No independent or two-reviewer success claim in this bounded run. Further independent review remains required before advancement.','diagnosis':'After final review, manually score extraction fields (quotes alone do not count) against same requirements; classify extraction omission, lost in composition, recovery, preserved or unresolved. This localizes observed losses, not internal causal mechanisms.','decision':'No automatic unseen-clause promotion. Report fresh A2 vs P1 counts, unresolved bounds, paired regressions, distortion and stage-localized omissions. Improvement candidate only if P1 confirmed completeness exceeds A2 upper bound with no paired complete regression and no distortion-upper-bound increase; single-review evidence never replaces prior two-review gate.','limitations':'3 previously observed development sources, not 6 independent sources; no p-values/CI/generalization; no post-output tuning or selection.'})
 write(BASE/'validation_report.json',{'status':'OFFLINE_VALIDATED','planned_api_calls':18,'final_explanations':12,'gold_perturbation_check':True,'prior_freeze_verified':True,'baseline_exact_A2':True,'reservation_usd':total})
 print(json.dumps({'status':'PREPARED','reservation_usd':total,'live_calls':0}))
elif cmd in ['verify','freeze']:
 cases,schema,plan,total=derive()
 assert (BASE/'request_recipe_12.jsonl').read_text()==''.join(compact(r)+'\n' for r in plan)
 assert read(BASE/'extraction_schema.json')==schema
 assert read(BASE/'generator_inputs.json')==cases
 assert read(BASE/'evaluation_reference.json')==read(OLD/'evaluation_reference.json')
 assert read(BASE/'response_schema.json')==read(OLD/'response_schema.json')
 assert abs(read(BASE/'protocol.json')['planning_reservation_usd']-total)<1e-12
 if cmd=='freeze':
  assert not (BASE/'input_freeze_manifest.json').exists()
  paths=list(BASE.iterdir())+[SELF,ROOT/'experiments/run_proposition_pipeline_20260913.mjs',ROOT/'experiments/test_proposition_pipeline_20260913.mjs',ROOT/'docs/36_proposition_pipeline_plan_2026-09-13.md',ROOT/'experiments/run_generation_preservation_20260909.mjs']
  write(BASE/'input_freeze_manifest.json',{'status':'FROZEN_BEFORE_GENERATION','frozen_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'file_sha256':{str(p.relative_to(ROOT)):sha(p.read_bytes()) for p in paths}})
  for p in paths+[BASE/'input_freeze_manifest.json']:p.chmod(0o444)
 else:
  if (BASE/'input_freeze_manifest.json').exists():
   for p,h in read(BASE/'input_freeze_manifest.json')['file_sha256'].items():assert sha((ROOT/p).read_bytes())==h,p
 print(json.dumps({'status':cmd.upper()+'_PASS','live_calls':0}))
else:raise ValueError('Unknown command')
