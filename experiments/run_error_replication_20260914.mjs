import fs from 'node:fs';import path from 'node:path';
import {ROOT,sha,runSlots} from './run_atomic_audit_20260914.mjs';
const base=path.join(ROOT,'experiments/error_replication_v1_20260914'),runDir=path.join(ROOT,'experiments/runs/error_replication_v1_20260914');
const read=p=>JSON.parse(fs.readFileSync(p,'utf8')),write=(p,v)=>fs.writeFileSync(p,JSON.stringify(v,null,2)+'\n');
const old=path.join(ROOT,'experiments/runs/proposition_pipeline_v1_20260913');
const cmd=process.argv[2];
if(cmd==='prepare'){
 if(fs.existsSync(base))throw Error('BASE_EXISTS');
 for(const [n,h]of Object.entries(read(path.join(old,'output_freeze_manifest.json')).file_sha256))if(sha(fs.readFileSync(path.join(old,n)))!==h)throw Error('OLD_HASH');
 const requests=fs.readFileSync(path.join(old,'requests.jsonl'),'utf8').trim().split('\n').map(JSON.parse);
 const plan=[];for(let rep=1;rep<=3;rep++)for(const id of ['CTX-001','CTX-002','CTX-003']){
 const rows=requests.filter(r=>r.slot_id.startsWith(id+'-A2_FRESH-'));
 if(rows.length!==2||JSON.stringify(rows[0].request)!==JSON.stringify(rows[1].request))throw Error('INPUT_NOT_IDENTICAL');
 const request=rows[0].request;
 const estimated_reservation_usd=((Buffer.byteLength(request.input)+Buffer.byteLength(JSON.stringify(request.text.format.schema))+2048)*.75+request.max_output_tokens*4.5)/1e6;
 plan.push({slot_id:`ERR-${id}-R${rep}`,case_id:id,arm:'FIXED_CONTEXT_DIRECT',replicate:rep,request,request_sha256:sha(JSON.stringify(request)),estimated_reservation_usd});}
 if(plan.reduce((n,r)=>n+r.estimated_reservation_usd,0)>.5)throw Error('BUDGET');
 fs.mkdirSync(base);
 write(path.join(base,'protocol.json'),{experiment_id:'ERROR_REPLICATION_V1_20260914',model:plan[0].request.model,pricing_usd_per_million:{input:.75,cached_input:.075,output:4.5},generation_cost_cap_usd:.5,planned_calls:9,design:'Three known developmental sources, three fixed-input repetitions each. Exact earlier A2 direct-context requests; no tuning, filtering, additional source selection, or retries. All outputs assessed by current same AI against frozen requirements, ambiguity retained. Not independent expert validation, novel-source evidence, or a method comparison. Keep primary49 unchanged. Stop after nine calls regardless of outcome.',selection:'All three existing developmental source cases; not sampled from population. Repetition at temperature0 measures observed recurrence, not independent sample size.',pricing_source:'https://developers.openai.com/api/docs/models/gpt-5.4-mini',evaluation:'explanation_ko only; all frozen required conjuncts, claims assessed 1/0/null. Errors selected for paper only after all nine assessed; first occurrence of each clear error family with full trace. No p-values or confidence intervals.',parameters:{temperature:0,reasoning_effort:'none',max_output_tokens:plan[0].request.max_output_tokens},reservation_usd:plan.reduce((n,r)=>n+r.estimated_reservation_usd,0)});
 write(path.join(base,'plan.json'),plan);
 fs.copyFileSync(path.join(ROOT,'experiments/proposition_pipeline_v1_20260913/evaluation_reference.json'),path.join(base,'evaluation_reference.json'));
 fs.copyFileSync(path.join(ROOT,'experiments/proposition_pipeline_v1_20260913/generator_inputs.json'),path.join(base,'generator_inputs.json'));
 const paths=[...fs.readdirSync(base).map(n=>path.join(base,n)),path.join(ROOT,'experiments/run_error_replication_20260914.mjs'),path.join(ROOT,'experiments/run_atomic_audit_20260914.mjs'),path.join(ROOT,'experiments/run_preservation_repair_20260914.mjs')];
 write(path.join(base,'input_freeze_manifest.json'),{frozen_at:new Date().toISOString(),file_sha256:Object.fromEntries(paths.map(p=>[path.relative(ROOT,p),sha(fs.readFileSync(p))]))});
 console.log(JSON.stringify({prepared:9,reservation_usd:read(path.join(base,'protocol.json')).reservation_usd}));
}else if(cmd==='execute'){
 const f=read(path.join(base,'input_freeze_manifest.json'));for(const [p,h]of Object.entries(f.file_sha256))if(sha(fs.readFileSync(path.join(ROOT,p)))!==h)throw Error('FROZEN_HASH');
 const plan=read(path.join(base,'plan.json')),protocol=read(path.join(base,'protocol.json'));
 let key=process.env.OPENAI_API_KEY;if(!key){const line=fs.readFileSync(path.join(ROOT,'.env.local'),'utf8').split(/\r?\n/).find(x=>/^\s*OPENAI_API_KEY\s*=/.test(x));key=line?.slice(line.indexOf('=')+1).trim().replace(/^['"]|['"]$/g,'');}if(!key)throw Error('KEY_ABSENT');
 const result=await runSlots({plan,protocol,runDir,inputFreezeHash:sha(fs.readFileSync(path.join(base,'input_freeze_manifest.json'))),inputFrozenAt:f.frozen_at,transport:async request=>{const r=await fetch('https://api.openai.com/v1/responses',{method:'POST',headers:{Authorization:`Bearer ${key}`,'Content-Type':'application/json'},body:JSON.stringify(request),signal:AbortSignal.timeout(60000)});return {http_status:r.status,body:await r.json()};}});console.log(JSON.stringify(result));
}else throw Error('COMMAND');
