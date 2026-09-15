import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {ROOT,sha,usageCost,delivery} from './run_generation_preservation_20260909.mjs';
const BASE=path.join(ROOT,'experiments/preservation_repair_v1_20260914');
export const RUN=path.join(ROOT,'experiments/runs/preservation_repair_v1_20260914');
const read=p=>JSON.parse(fs.readFileSync(p,'utf8'));
const rows=p=>fs.readFileSync(p,'utf8').trim().split('\n').map(JSON.parse);
const write=(p,o)=>fs.writeFileSync(p,JSON.stringify(o,null,2)+'\n');
const append=(p,o)=>fs.appendFileSync(p,JSON.stringify(o)+'\n');
const stamp=()=>new Date().toISOString();
const need=(ok,msg)=>{if(!ok)throw new Error(msg);};
export function validate(value,s){
 if(s.type==='string')return typeof value==='string'&&(!s.enum||s.enum.includes(value));
 if(s.type==='array')return Array.isArray(value)&&value.every(v=>validate(v,s.items));
 if(s.type==='object')return value!==null&&typeof value==='object'&&!Array.isArray(value)&&Object.keys(value).length===s.required.length&&s.required.every(k=>Object.hasOwn(value,k)&&validate(value[k],s.properties[k]));
 return false;
}
export function auditDelivery(body,schema){
 if(body?.status!=='completed')return {status:'AUDIT_NOT_COMPLETED',parsed:null};
 const parts=(body.output??[]).filter(o=>o.type==='message').flatMap(o=>o.content??[]);
 if(parts.some(p=>p.type==='refusal'))return {status:'REFUSAL',parsed:null};
 let parsed;try{parsed=JSON.parse(parts.filter(p=>p.type==='output_text').map(p=>p.text).join(''));}catch{return {status:'INVALID_JSON',parsed:null};}
 // Empty lists are structurally valid and retained; semantic quality never controls retries.
 return validate(parsed,schema)?{status:'AUDIT',parsed}:{status:'SCHEMA_INVALID',parsed:null};
}
export function repair(row,audit,suffix,limit){
 const compact=JSON.stringify(audit);need(Buffer.byteLength(compact)<=limit,'AUDIT_SIZE_LIMIT');
 return {...row.baseline_request,input:row.baseline_request.input+suffix+'\n'+compact};
}
function reservation(r,p){return ((Buffer.byteLength(r.input)+Buffer.byteLength(JSON.stringify(r.text.format.schema))+2048)*p.pricing_usd_per_million.input+r.max_output_tokens*p.pricing_usd_per_million.output)/1e6;}
export function verify(){
 const f=read(path.join(BASE,'input_freeze_manifest.json'));
 need(f.status==='FROZEN_BEFORE_GENERATION','NOT_FROZEN');
 for(const [p,h]of Object.entries(f.file_sha256))need(sha(fs.readFileSync(path.join(ROOT,p)))===h,'FROZEN_HASH_MISMATCH');
 const p=read(path.join(BASE,'protocol.json')),plan=rows(path.join(BASE,'request_recipe_12.jsonl'));
 need(plan.length===12&&new Set(plan.map(r=>r.slot_id)).size===12,'SLOT_COUNT');
 need(plan.reduce((n,r)=>n+(r.audit_request?2:1),0)===18,'CALL_COUNT');
 need(p.planning_reservation_usd<=p.generation_cost_cap_usd,'PLAN_BUDGET');
 return {protocol:p,plan,suffix:fs.readFileSync(path.join(BASE,'repair_suffix.md'),'utf8'),freeze:f,freezeHash:sha(fs.readFileSync(path.join(BASE,'input_freeze_manifest.json')))};
}
export async function run({protocol:p,plan,suffix,freezeHash,freeze,runDir=RUN,transport,provenance='LIVE_API'}){
 need(!fs.existsSync(runDir),'RUN_EXISTS_NO_REPLAY');fs.mkdirSync(runDir);
 const ledger=plan.map(r=>({slot_id:r.slot_id,case_id:r.case_id,arm:r.arm,replicate:r.replicate,status:'NOT_ATTEMPTED',semantic_status:'NOT_OBSERVED',stages:[]}));
 const m={experiment_id:p.experiment_id,provenance,status:'RUNNING',started_at:stamp(),input_freeze_sha256:freezeHash,input_frozen_at:freeze.frozen_at,planned_calls:18,planned_explanations:12,attempts:0,returned:0,explanations:0,known_cost_usd:0,cost_complete:true};
 const save=()=>{write(path.join(runDir,'manifest.json'),m);fs.writeFileSync(path.join(runDir,'slot_ledger.jsonl'),ledger.map(x=>JSON.stringify(x)).join('\n')+'\n');};
 save();
 try{
  for(const [i,row]of plan.entries()){
   const slot=ledger[i];slot.status='RUNNING';save();
   async function call(stage,request,dependency=null){
    need(request.model===p.model&&request.temperature===0&&request.reasoning.effort==='none'&&request.store===false,'REQUEST_PARAMETERS');
    need(m.known_cost_usd+reservation(request,p)<=p.generation_cost_cap_usd,'COST_GUARD');
    const event={slot_id:row.slot_id,stage,started_at:stamp(),request_sha256:sha(JSON.stringify(request)),dependency};
    const state={stage,status:'ATTEMPTED_OUTCOME_UNKNOWN',request_sha256:event.request_sha256};slot.stages.push(state);m.attempts++;
    append(path.join(runDir,'requests.jsonl'),{...event,request});save();
    let result;try{result=await transport(request);}catch{m.cost_complete=false;state.status='TRANSPORT_UNCERTAIN';append(path.join(runDir,'raw_responses.jsonl'),{...event,completed_at:stamp(),transport_error:'OUTCOME_UNKNOWN_NO_RETRY'});throw new Error('TRANSPORT_UNCERTAIN_NO_RETRY');}
    m.returned++;append(path.join(runDir,'raw_responses.jsonl'),{...event,completed_at:stamp(),http_status:result.http_status,response:result.body});
    const body=result.body;state.status='EXECUTION_ERROR';
    const cost=body?.model===p.model?usageCost(body.usage,p.pricing_usd_per_million):null;
    if(cost===null)m.cost_complete=false;else m.known_cost_usd+=cost;
    need(result.http_status>=200&&result.http_status<300,'HTTP_ERROR_NO_RETRY');need(body.model===p.model,'MODEL_MISMATCH');need(cost!==null,'INVALID_USAGE');
    const parsed=stage==='audit'?auditDelivery(body,request.text.format.schema):delivery(body,request.text.format.schema);
    state.status=parsed.status;state.response_id=body.id??null;state.cost_usd=cost;state.usage=body.usage;
    append(path.join(runDir,'parsed_stages.jsonl'),{...event,response_id:state.response_id,...parsed});save();
    need(parsed.parsed!==null,'DELIVERY_FAILURE_NO_RETRY');need(m.known_cost_usd<=p.generation_cost_cap_usd,'ACTUAL_COST_EXCEEDED');
    return {parsed:parsed.parsed,response_id:state.response_id};
   }
   let final;
   if(row.arm==='R0_REWRITE')final=await call('explain',row.baseline_request);
   else{
    const extracted=await call('audit',row.audit_request);
    const request=repair(row,extracted.parsed,suffix,p.max_audit_json_utf8_bytes);
    final=await call('repair',request,{response_id:extracted.response_id,audit_json_sha256:sha(JSON.stringify(extracted.parsed))});
   }
   slot.status='EXPLANATION';slot.semantic_status='PENDING_REVIEW';m.explanations++;
   append(path.join(runDir,'final_explanations.jsonl'),{slot_id:row.slot_id,case_id:row.case_id,arm:row.arm,replicate:row.replicate,parsed:final.parsed});save();
  }
  m.status='GENERATION_COMPLETE_SEMANTICS_PENDING';
 }catch(e){m.status='STOPPED';m.stop_reason=e.message;for(const s of ledger)if(s.status==='RUNNING'){s.status='STOPPED';s.semantic_status='NOT_ASSESSABLE';}}
 m.finished_at=stamp();save();
 write(path.join(runDir,'output_freeze_manifest.json'),{frozen_at:stamp(),provenance,file_sha256:Object.fromEntries(fs.readdirSync(runDir).sort().map(n=>[n,sha(fs.readFileSync(path.join(runDir,n)))]))});
 for(const n of fs.readdirSync(runDir))fs.chmodSync(path.join(runDir,n),0o444);
 return m;
}
async function main(){
 const cmd=process.argv[2]??'verify';need(['verify','execute'].includes(cmd),'UNKNOWN_COMMAND');const checked=verify();
 if(cmd==='verify'){console.log(JSON.stringify({status:'FREEZE_VALID',planned_calls:18,live_calls:0}));return;}
 let key=process.env.OPENAI_API_KEY;
 if(!key){const line=fs.readFileSync(path.join(ROOT,'.env.local'),'utf8').split(/\r?\n/).find(x=>/^\s*OPENAI_API_KEY\s*=/.test(x));key=line?.slice(line.indexOf('=')+1).trim().replace(/^['"]|['"]$/g,'');}
 need(!!key,'API_KEY_UNAVAILABLE');
 const m=await run({...checked,transport:async request=>{
  const http=await fetch('https://api.openai.com/v1/responses',{method:'POST',headers:{Authorization:`Bearer ${key}`,'Content-Type':'application/json'},body:JSON.stringify(request),signal:AbortSignal.timeout(checked.protocol.timeout_ms)});
  let body;try{body=await http.json();}catch{body={non_json_response:true};}return {http_status:http.status,body};
 }});console.log(JSON.stringify(m));if(m.status==='STOPPED')process.exitCode=2;
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))await main().catch(e=>{console.error(e.message);process.exitCode=2;});
