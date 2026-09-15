import fs from 'node:fs';
import path from 'node:path';
import {performance} from 'node:perf_hooks';
import {sha256,parseCsv,responseObject,tokenCost,reserveCost} from './c3_lib.mjs';
import {modalProjection,modalTemplate,modalInput} from './c1m_lib.mjs';
const ROOT=path.resolve(import.meta.dirname,'..');
const MODEL='gpt-5.4-mini-2026-03-17',SEED='c1m-main72-v1-20260906',CAP=.5;
const bytes=n=>fs.readFileSync(path.join(ROOT,n));
const json=n=>JSON.parse(bytes(n));
const freeze=json('data/main_freeze_manifest.json');
for(const [n,h] of Object.entries(freeze.file_sha256))if(sha256(bytes(n))!==h)throw new Error(`Changed input ${n}`);
const rows=parseCsv(bytes('data/main_cases.csv').toString());
if(rows.length!==72||new Set(rows.map(r=>r.case_id)).size!==72)throw new Error('Expected 72 cases');
const base=bytes('experiments/prompts/c1_v2.md').toString(),schema=json('experiments/response_schema.json');
const selected=rows.map(r=>({case_id:r.case_id,input:modalProjection(r),prompt:modalInput(base,r)})).sort((a,b)=>sha256(SEED+a.case_id).localeCompare(sha256(SEED+b.case_id)));
const files=['data/main_cases.csv','data/main_freeze_manifest.json','docs/14_modal_hint_extension_protocol.md','experiments/prompts/c1_v2.md','experiments/response_schema.json','experiments/c3_lib.mjs','experiments/c1m_lib.mjs','experiments/test_c1m_contract.mjs','experiments/run_c1m_extension.mjs'];
const plan={experiment:'C1M_MODAL_HINT_MAIN72_V1',condition:'C1M',model:MODEL,cases:72,max_successful_calls:72,
 request_order_seed:SEED,max_estimated_cost_usd:CAP,source_projection_keys:Object.keys(selected[0].input),
 file_sha256:Object.fromEntries(files.map(n=>[n,sha256(bytes(n))])),projection_sha256:sha256(JSON.stringify(selected)),
 parameters:{temperature:0,reasoning_effort:'none',max_output_tokens:600,store:false},
 comparison_run:'main72_v3_2026-09-03T07-35-49-603Z',review_basis:'C3 fresh provisional pass 1; new C1M meanings not yet evaluated'};
if(!process.argv.includes('--execute')){console.log(JSON.stringify({status:'PREFLIGHT_PASS_NO_API',...plan},null,2));}
else{
 const runs=path.join(ROOT,'experiments/runs');
 if(fs.readdirSync(runs).some(n=>n.startsWith('c1m_main72_v1_')))throw new Error('C1M run already exists; do not replay');
 let key=process.env.OPENAI_API_KEY;
 if(!key){const line=fs.readFileSync(path.join(ROOT,'.env.local'),'utf8').split(/\r?\n/).find(l=>/^\s*OPENAI_API_KEY\s*=/.test(l));key=line?.slice(line.indexOf('=')+1).trim().replace(/^['"]|['"]$/g,'');}
 if(!key)throw new Error('API key unavailable');
 const runId='c1m_main72_v1_'+new Date().toISOString().replace(/[:.]/g,'-');const dir=path.join(runs,runId);fs.mkdirSync(dir);
 const write=(n,o)=>fs.writeFileSync(path.join(dir,n),JSON.stringify(o,null,2)+'\n');
 const append=(n,o)=>fs.appendFileSync(path.join(dir,n),JSON.stringify(o)+'\n');
 const manifest={...plan,run_id:runId,created_at:new Date().toISOString(),status:'running',evaluator_status:'NOT_EVALUATED',
  retry_policy:'429/5xx only; maximum 2 retries; no transport or semantic retries',pricing_usd_per_million:{input:.75,cached_input:.075,output:4.5}};
 write('input_freeze_manifest.json',{...plan,frozen_at:new Date().toISOString()});write('manifest.json',manifest);
 fs.writeFileSync(path.join(dir,'projected_inputs.jsonl'),selected.map(x=>JSON.stringify(x)).join('\n')+'\n');
 fs.writeFileSync(path.join(dir,'prompt_template.md'),modalTemplate(base));
 let spent=0,attempts=0;const results=[];
 async function call(item){
  const request={model:MODEL,input:item.prompt,temperature:0,reasoning:{effort:'none'},max_output_tokens:600,store:false,
   text:{format:{type:'json_schema',name:'normative_explanation',strict:true,schema}}};
  for(let attempt=1;attempt<=3;attempt++){
   if(spent+reserveCost(item.prompt,schema,600)>CAP)throw new Error('ESTIMATED_COST_GUARD');
   const started=new Date().toISOString(),tick=performance.now();attempts++;
   append('requests.jsonl',{case_id:item.case_id,condition:'C1M',attempt,started_at:started,request,request_sha256:sha256(JSON.stringify(request))});
   let http,body;
   try{http=await fetch('https://api.openai.com/v1/responses',{method:'POST',headers:{Authorization:`Bearer ${key}`,'Content-Type':'application/json'},body:JSON.stringify(request),signal:AbortSignal.timeout(60000)});body=await http.json();}
   catch(error){append('raw_responses.jsonl',{case_id:item.case_id,attempt,transport_error:'REQUEST_OUTCOME_UNCERTAIN',cause_code:error.cause?.code||null,completed_at:new Date().toISOString()});throw new Error('TRANSPORT_ERROR_NO_AUTOMATIC_RETRY');}
   const elapsed=performance.now()-tick;
   append('raw_responses.jsonl',{case_id:item.case_id,condition:'C1M',attempt,started_at:started,completed_at:new Date().toISOString(),elapsed_ms:elapsed,http_status:http.status,response:body});
   const cost=tokenCost(body.usage);if(cost!==null)spent+=cost;
   manifest.attempts=attempts;manifest.estimated_cost_usd=spent;write('manifest.json',manifest);
   if(http.ok){if(cost===null)throw new Error('USAGE_MISSING');if(body.model!==MODEL)throw new Error('MODEL_SNAPSHOT_MISMATCH');return {case_id:item.case_id,condition:'C1M',parsed:responseObject(body,schema),response_id:body.id,status:body.status,usage:body.usage,elapsed_ms:elapsed};}
   if(body.error?.type==='insufficient_quota'||body.error?.code==='credit_balance_exhausted')throw new Error('API_QUOTA_BLOCKED');
   if(http.status!==429&&http.status<500)throw new Error(`HTTP_${http.status}`);
   if(attempt===3)throw new Error(`TRANSIENT_HTTP_${http.status}_EXHAUSTED`);
   await new Promise(resolve=>setTimeout(resolve,500*2**(attempt-1)));
  }
 }
 try{for(const item of selected){const r=await call(item);results.push(r);append('parsed_responses.jsonl',r);console.log(`${results.length}/72 ${item.case_id} parsed=${Boolean(r.parsed)} cost_usd=${spent.toFixed(5)}`);}manifest.status='generation_complete_semantics_pending';}
 catch(error){manifest.status='stopped';manifest.stop_reason=error.message;}
 manifest.completed_at=new Date().toISOString();manifest.processed_cases=results.length;manifest.parsed_generations=results.filter(r=>r.parsed).length;manifest.attempts=attempts;manifest.estimated_cost_usd=spent;write('manifest.json',manifest);
 write('output_freeze_manifest.json',{frozen_at:new Date().toISOString(),file_sha256:Object.fromEntries(fs.readdirSync(dir).filter(n=>n!=='output_freeze_manifest.json').sort().map(n=>[n,sha256(fs.readFileSync(path.join(dir,n)))]))});
 console.log(JSON.stringify({run_dir:path.relative(ROOT,dir),...manifest},null,2));if(manifest.status==='stopped')process.exitCode=2;
}
