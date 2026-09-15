import fs from 'node:fs';
import path from 'node:path';
import {performance} from 'node:perf_hooks';
import {sha256,parseCsv,projectCase,extractionInput,generationInput,extractionUsable,responseObject,tokenCost,reserveCost} from './c3_lib.mjs';

const ROOT=path.resolve(import.meta.dirname,'..');
const MODEL='gpt-5.4-mini-2026-03-17';
const SEED='c3-auto72-v1-2026-09-06';
const CAP=1;
const FILES=['data/main_cases.csv','data/main_freeze_manifest.json','docs/10_c3_extension_protocol.md',
  'docs/09_reporting_errata_2026-09-06.md','experiments/prompts/c3_extract_v1.md',
  'experiments/prompts/c2_v2.md','experiments/c3_extraction_schema.json','experiments/response_schema.json',
  'experiments/c3_lib.mjs','experiments/run_c3_extension.mjs','experiments/prepare_c3_review.mjs'];
const bytes=name=>fs.readFileSync(path.join(ROOT,name));
const json=name=>JSON.parse(bytes(name));
const freeze=json('data/main_freeze_manifest.json');
if(sha256(bytes('data/main_cases.csv'))!==freeze.dataset_sha256)throw new Error('Dataset freeze changed');
for(const [name,expected] of Object.entries(freeze.file_sha256))if(sha256(bytes(name))!==expected)throw new Error(`Frozen input changed: ${name}`);
const rows=parseCsv(bytes('data/main_cases.csv').toString('utf8'));
if(rows.length!==72||new Set(rows.map(r=>r.case_id)).size!==72)throw new Error('Expected 72 unique cases');
const selected=rows.map(r=>({case_id:r.case_id,input:projectCase(r)})).sort((a,b)=>sha256(SEED+a.case_id).localeCompare(sha256(SEED+b.case_id)));
const extractor=bytes('experiments/prompts/c3_extract_v1.md').toString('utf8');
const generator=bytes('experiments/prompts/c2_v2.md').toString('utf8');
const extractSchema=json('experiments/c3_extraction_schema.json');
const outputSchema=json('experiments/response_schema.json');
const hashes=Object.fromEntries(FILES.map(name=>[name,sha256(bytes(name))]));
const plan={experiment:'C3_SOURCE_ONLY_EXTRACTION_V1',model:MODEL,cases:72,max_successful_calls:144,
  request_order_seed:SEED,source_projection_keys:Object.keys(selected[0].input),
  extraction_input_keys:['source_text_en'],max_estimated_cost_usd:CAP,file_sha256:hashes,
  projection_sha256:sha256(JSON.stringify(selected)),comparison_run:'main72_v3_2026-09-03T07-35-49-603Z',
  parameters:{temperature:0,reasoning_effort:'none',store:false,extraction_max_output_tokens:1200,generation_max_output_tokens:600}};
if(!process.argv.includes('--execute')){
  console.log(JSON.stringify({status:'PREFLIGHT_PASS_NO_API',...plan},null,2));
}else{
  const runsDir=path.join(ROOT,'experiments/runs');
  if(fs.readdirSync(runsDir).some(name=>name.startsWith('c3_auto72_v1_')))throw new Error('C3 v1 run already exists; inspect it before any new execution');
  let key=process.env.OPENAI_API_KEY;
  if(!key){
    const env=fs.readFileSync(path.join(ROOT,'.env.local'),'utf8');
    const line=env.split(/\r?\n/).find(l=>/^\s*OPENAI_API_KEY\s*=/.test(l));
    key=line?.slice(line.indexOf('=')+1).trim().replace(/^['"]|['"]$/g,'');
  }
  if(!key)throw new Error('API key unavailable');
  const runId='c3_auto72_v1_'+new Date().toISOString().replace(/[:.]/g,'-');
  const dir=path.join(runsDir,runId);fs.mkdirSync(dir);
  const write=(name,obj)=>fs.writeFileSync(path.join(dir,name),JSON.stringify(obj,null,2)+'\n');
  const append=(name,obj)=>fs.appendFileSync(path.join(dir,name),JSON.stringify(obj)+'\n');
  const manifest={...plan,run_id:runId,created_at:new Date().toISOString(),status:'running',
    dataset_path:'data/main_cases.csv',dataset_sha256:freeze.dataset_sha256,condition:'C3',
    evaluator_status:'NOT_EVALUATED',retry_policy:'429/5xx only, at most 2 retries; no transport or semantic retries',
    pricing_usd_per_million:{input:.75,cached_input:.075,output:4.5},attempts:0,estimated_cost_usd:0};
  write('input_freeze_manifest.json',{...plan,frozen_at:new Date().toISOString(),execution_order:selected.map(r=>r.case_id)});
  write('manifest.json',manifest);
  fs.writeFileSync(path.join(dir,'projected_inputs.jsonl'),selected.map(x=>JSON.stringify(x)).join('\n')+'\n');
  let spent=0,attempts=0;const results=[];const extractions=[];
  async function call(caseId,stage,input,schema,maxOutput){
    const request={model:MODEL,input,temperature:0,reasoning:{effort:'none'},max_output_tokens:maxOutput,store:false,
      text:{format:{type:'json_schema',name:stage==='extraction'?'normative_structure':'normative_explanation',strict:true,schema}}};
    const reserve=reserveCost(input,schema,maxOutput);
    for(let attempt=1;attempt<=3;attempt++){
      if(spent+reserve>CAP)throw new Error('ESTIMATED_COST_GUARD');
      const started=new Date().toISOString();const tick=performance.now();
      attempts++;
      append('requests.jsonl',{case_id:caseId,stage,attempt,started_at:started,request,request_sha256:sha256(JSON.stringify(request))});
      let http,body;
      try{
        http=await fetch('https://api.openai.com/v1/responses',{method:'POST',headers:{Authorization:`Bearer ${key}`,'Content-Type':'application/json'},body:JSON.stringify(request),signal:AbortSignal.timeout(60000)});
        body=await http.json();
      }catch{
        append('raw_responses.jsonl',{case_id:caseId,stage,attempt,started_at:started,completed_at:new Date().toISOString(),elapsed_ms:performance.now()-tick,transport_error:'REQUEST_OUTCOME_UNCERTAIN'});
        throw new Error('TRANSPORT_ERROR_NO_AUTOMATIC_RETRY');
      }
      const elapsed=performance.now()-tick;
      append('raw_responses.jsonl',{case_id:caseId,stage,attempt,started_at:started,completed_at:new Date().toISOString(),elapsed_ms:elapsed,http_status:http.status,response:body});
      const cost=tokenCost(body.usage);if(cost!==null)spent+=cost;
      manifest.attempts=attempts;manifest.estimated_cost_usd=spent;write('manifest.json',manifest);
      if(http.ok){
        if(cost===null)throw new Error('USAGE_MISSING');
        if(body.model!==MODEL)throw new Error('MODEL_SNAPSHOT_MISMATCH');
        return {parsed:responseObject(body,schema),response_id:body.id,status:body.status,usage:body.usage,elapsed_ms:elapsed};
      }
      if(body.error?.type==='insufficient_quota'||body.error?.code==='credit_balance_exhausted')throw new Error('API_QUOTA_BLOCKED');
      if(http.status!==429&&http.status<500)throw new Error(`HTTP_${http.status}`);
      if(attempt===3)throw new Error(`TRANSIENT_HTTP_${http.status}_EXHAUSTED`);
      await new Promise(resolve=>setTimeout(resolve,500*2**(attempt-1)));
    }
  }
  try{
    for(const item of selected){
      const ex=await call(item.case_id,'extraction',extractionInput(extractor,item.input),extractSchema,1200);
      const extraction={case_id:item.case_id,...ex};extractions.push(extraction);append('extractions.jsonl',extraction);
      let result;
      if(!extractionUsable(ex.parsed,extractSchema)){
        result={case_id:item.case_id,condition:'C3',status:'abstained_extraction_invalid_or_unclear',parsed:null,usage:null,extraction_elapsed_ms:ex.elapsed_ms};
      }else{
        const gen=await call(item.case_id,'generation',generationInput(generator,item.input,ex.parsed),outputSchema,600);
        result={case_id:item.case_id,condition:'C3',...gen,extraction_elapsed_ms:ex.elapsed_ms};
      }
      results.push(result);append('parsed_responses.jsonl',result);
      console.log(`${results.length}/72 ${item.case_id} extraction=${ex.parsed?'parsed':'failed'} generation=${result.parsed?'parsed':result.status} cost_usd=${spent.toFixed(5)}`);
    }
    manifest.status='generation_complete_semantics_pending';
  }catch(error){manifest.status='stopped';manifest.stop_reason=error.message;}
  manifest.completed_at=new Date().toISOString();manifest.processed_cases=results.length;
  manifest.extractions=extractions.length;manifest.parsed_generations=results.filter(x=>x.parsed).length;
  manifest.attempts=attempts;manifest.estimated_cost_usd=spent;write('manifest.json',manifest);
  write('execution_summary.json',{status:manifest.status,processed_cases:results.length,planned_cases:72,
    extracted_json:extractions.filter(x=>x.parsed).length,parsed_generations:manifest.parsed_generations,
    semantic_preservation:'NOT_EVALUATED',estimated_cost_usd:spent,stop_reason:manifest.stop_reason||null});
  write('output_freeze_manifest.json',{frozen_at:new Date().toISOString(),file_sha256:Object.fromEntries(fs.readdirSync(dir).sort().filter(n=>n!=='output_freeze_manifest.json').map(n=>[n,sha256(fs.readFileSync(path.join(dir,n)))]))});
  console.log(JSON.stringify({run_dir:path.relative(ROOT,dir),...manifest},null,2));
  if(manifest.status==='stopped')process.exitCode=2;
}
