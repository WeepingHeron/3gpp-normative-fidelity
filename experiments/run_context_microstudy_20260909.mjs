import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {performance} from 'node:perf_hooks';
import {render, responseObject, tokenCost, reserveCost} from './c3_lib.mjs';

const ROOT=path.resolve(import.meta.dirname,'..');
const BASE=path.join(ROOT,'experiments/context_microstudy_v1_20260909');
const RUN=path.join(ROOT,'experiments/runs/context_microstudy_v1_20260909');
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const bytes=p=>fs.readFileSync(p), read=p=>JSON.parse(bytes(p));
const relative=p=>path.relative(ROOT,p);
const write=(p,o)=>fs.writeFileSync(p,JSON.stringify(o,null,2)+'\n');
const append=(p,o)=>fs.appendFileSync(p,JSON.stringify(o)+'\n');
const clock=()=>new Date().toISOString();
const protocol=read(path.join(BASE,'protocol.json'));
const cases=read(path.join(BASE,'cases.json'));
const template=bytes(path.join(BASE,'prompt_template.md')).toString();
const schema=read(path.join(BASE,'response_schema.json'));

function schedule(){
  const out=[];
  for(const c of cases)for(const context of protocol.context_levels)for(const hint of protocol.hint_levels)for(const replicate of protocol.replicates){
    const contextText=context==='FULL'?c.context_blocks.map(b=>`[PDF page ${b.pdf_page}]\n${b.quote}`).join('\n\n'):'추가 원문 문맥이 제공되지 않았다.';
    const hintText=hint==='MODAL'?`## 대상 문장의 규범 힌트\nnormative_type: ${c.modal_hint.normative_type}\npolarity: ${c.modal_hint.polarity}`:'';
    const input=render(template,{question_ko:c.question_ko,target_text:c.target_text,context_text:contextText,hint_text:hintText,...c.source});
    if(input.includes('{{')||input.includes('development_reference'))throw new Error('INPUT_PROJECTION_FAILED');
    const request={model:protocol.model,input,temperature:protocol.parameters.temperature,
      reasoning:{effort:protocol.parameters.reasoning_effort},max_output_tokens:protocol.parameters.max_output_tokens,
      store:false,text:{format:{type:'json_schema',name:'normative_explanation',strict:true,schema}}};
    out.push({slot_id:`${c.case_id}-${context}-${hint}-R${replicate}`,case_id:c.case_id,context,hint,replicate,
      request,request_sha256:sha(JSON.stringify(request)),estimated_reservation_usd:reserveCost(input,schema,request.max_output_tokens)});
  }
  return out.sort((a,b)=>sha(protocol.execution_order_seed+a.slot_id).localeCompare(sha(protocol.execution_order_seed+b.slot_id)));
}

function preflight(){
  const s=schedule();
  if(cases.length!==3||s.length!==24||new Set(s.map(x=>x.slot_id)).size!==24)throw new Error('SCHEDULE_CARDINALITY');
  for(const c of cases){
    if(sha(bytes(path.join(ROOT,c.pdf.path)))!==c.pdf.sha256)throw new Error('PDF_HASH');
    for(const b of c.context_blocks){
      const page=bytes(path.join(ROOT,b.page_text_path));
      if(sha(page)!==b.page_text_sha256||!page.toString().includes(b.quote))throw new Error('CONTEXT_QUOTE_BINDING');
    }
    for(const context of protocol.context_levels)for(const hint of protocol.hint_levels){
      const r=s.filter(x=>x.case_id===c.case_id&&x.context===context&&x.hint===hint);
      if(r.length!==2||r[0].request_sha256!==r[1].request_sha256)throw new Error('REPLICATE_INPUT_MISMATCH');
    }
  }
  // Metadata outside the intended projections must not influence any prompt.
  const baseline=s.map(x=>x.request_sha256);
  for(const c of cases){c.requirements.push({sentinel:'DO_NOT_LEAK'});c.development_reference='DO_NOT_LEAK';}
  if(JSON.stringify(baseline)!==JSON.stringify(schedule().map(x=>x.request_sha256)))throw new Error('GOLD_LEAK');
  const reserve=s.reduce((n,x)=>n+x.estimated_reservation_usd,0);
  if(reserve>protocol.max_estimated_cost_usd)throw new Error('WHOLE_PLAN_COST_GUARD');
  return {ok:true,planned_calls:s.length,total_conservative_reservation_usd:reserve,max_estimated_cost_usd:protocol.max_estimated_cost_usd,live_api_calls:0};
}

function freeze(){
  if(fs.existsSync(path.join(BASE,'input_freeze_manifest.json'))||fs.existsSync(RUN))throw new Error('ALREADY_FROZEN_OR_EXECUTED');
  const check=preflight();
  const review=read(path.join(ROOT,'outputs/review/context_microstudy_preflight_20260909/review.json'));
  if(review.execution_approved!==true)throw new Error('SOURCE_PREFLIGHT_NOT_APPROVED');
  for(const input of review.input_hashes)if(sha(bytes(path.join(ROOT,input.path)))!==input.sha256)throw new Error('SOURCE_PREFLIGHT_INPUT_CHANGED');
  if(protocol.status!=='READY_TO_FREEZE')throw new Error('PROTOCOL_NOT_READY');
  const s=schedule();
  write(path.join(BASE,'preflight.json'),check);
  fs.writeFileSync(path.join(BASE,'request_plan.jsonl'),s.map(x=>JSON.stringify(x)).join('\n')+'\n');
  const inputs=[...fs.readdirSync(BASE).map(x=>path.join(BASE,x)),
    path.join(ROOT,'experiments/run_context_microstudy_20260909.mjs'),
    path.join(ROOT,'experiments/c3_lib.mjs'),
    path.join(ROOT,'tools/prepare_context_microstudy_20260909.py'),
    path.join(ROOT,'outputs/review/context_microstudy_preflight_20260909/review.json'),
    path.join(ROOT,'outputs/review/context_microstudy_preflight_20260909/review.md')];
  write(path.join(BASE,'input_freeze_manifest.json'),{experiment_id:protocol.experiment_id,frozen_at:clock(),
    source_review_received:true,planned_calls:24,file_sha256:Object.fromEntries(inputs.map(p=>[relative(p),sha(bytes(p))]))});
  for(const p of fs.readdirSync(BASE))fs.chmodSync(path.join(BASE,p),0o444);
  console.log(JSON.stringify({status:'FROZEN_BEFORE_GENERATION',...check}));
}

function verifyFreeze(){
  const f=read(path.join(BASE,'input_freeze_manifest.json'));
  for(const [p,h] of Object.entries(f.file_sha256))if(sha(bytes(path.join(ROOT,p)))!==h)throw new Error(`FROZEN_INPUT_CHANGED:${p}`);
  return f;
}

async function execute(){
  const freeze=verifyFreeze();
  if(fs.existsSync(RUN))throw new Error('RUN_ALREADY_EXISTS_NO_REPLAY');
  let key=process.env.OPENAI_API_KEY;
  if(!key){const line=bytes(path.join(ROOT,'.env.local')).toString().split(/\r?\n/).find(x=>/^\s*OPENAI_API_KEY\s*=/.test(x));key=line?.slice(line.indexOf('=')+1).trim().replace(/^['"]|['"]$/g,'');}
  if(!key)throw new Error('API_KEY_UNAVAILABLE');
  const plan=bytes(path.join(BASE,'request_plan.jsonl')).toString().trim().split('\n').map(JSON.parse);
  fs.mkdirSync(RUN);
  const manifest={experiment_id:protocol.experiment_id,started_at:clock(),status:'running',model:protocol.model,
    input_freeze_sha256:sha(bytes(path.join(BASE,'input_freeze_manifest.json'))),input_frozen_at:freeze.frozen_at,
    planned_slots:24,attempts:0,completed_slots:0,estimated_cost_usd:0,evaluator_status:'NOT_EVALUATED'};
  write(path.join(RUN,'manifest.json'),manifest);
  try{
    for(const item of plan){
      if(manifest.estimated_cost_usd+item.estimated_reservation_usd>protocol.max_estimated_cost_usd)throw new Error('COST_GUARD');
      const started=clock(),tick=performance.now();
      manifest.attempts++;
      append(path.join(RUN,'requests.jsonl'),{slot_id:item.slot_id,started_at:started,request:item.request,request_sha256:item.request_sha256});
      let http,body;
      try{http=await fetch('https://api.openai.com/v1/responses',{method:'POST',headers:{Authorization:`Bearer ${key}`,'Content-Type':'application/json'},body:JSON.stringify(item.request),signal:AbortSignal.timeout(60000)});body=await http.json();}
      catch(error){append(path.join(RUN,'raw_responses.jsonl'),{slot_id:item.slot_id,completed_at:clock(),transport_error:'REQUEST_OUTCOME_UNCERTAIN',cause_code:error.cause?.code||null});throw new Error('TRANSPORT_UNCERTAIN_NO_RETRY');}
      const elapsed=performance.now()-tick;
      append(path.join(RUN,'raw_responses.jsonl'),{slot_id:item.slot_id,started_at:started,completed_at:clock(),elapsed_ms:elapsed,http_status:http.status,response:body});
      const cost=tokenCost(body.usage);
      if(cost!==null)manifest.estimated_cost_usd+=cost;
      if(!http.ok)throw new Error(`HTTP_${http.status}_NO_RETRY`);
      if(cost===null)throw new Error('USAGE_MISSING');
      if(body.model!==protocol.model)throw new Error('MODEL_SNAPSHOT_MISMATCH');
      const parsed=responseObject(body,schema);
      append(path.join(RUN,'parsed_responses.jsonl'),{slot_id:item.slot_id,case_id:item.case_id,context:item.context,hint:item.hint,replicate:item.replicate,
        response_id:body.id,response_status:body.status,delivery_status:parsed?'EXPLANATION':'NOT_GENERATED',parsed,usage:body.usage,elapsed_ms:elapsed,
        request_sha256:item.request_sha256});
      manifest.completed_slots++;write(path.join(RUN,'manifest.json'),manifest);
      console.log(JSON.stringify({completed:manifest.completed_slots,total:24,slot_id:item.slot_id,parsed:!!parsed,estimated_cost_usd:manifest.estimated_cost_usd}));
    }
    manifest.status='GENERATION_COMPLETE_SEMANTICS_PENDING';
  }catch(error){manifest.status='STOPPED';manifest.stop_reason=error.message;}
  manifest.completed_at=clock();write(path.join(RUN,'manifest.json'),manifest);
  write(path.join(RUN,'output_freeze_manifest.json'),{frozen_at:clock(),file_sha256:Object.fromEntries(fs.readdirSync(RUN).sort().map(n=>[n,sha(bytes(path.join(RUN,n)))]))});
  for(const p of fs.readdirSync(RUN))fs.chmodSync(path.join(RUN,p),0o444);
  console.log(JSON.stringify(manifest));
  if(manifest.status==='STOPPED')process.exitCode=2;
}

const command=process.argv[2]||'preflight';
if(command==='preflight')console.log(JSON.stringify(preflight()));
else if(command==='freeze')freeze();
else if(command==='execute')await execute();
else if(command==='verify-freeze'){verifyFreeze();console.log(JSON.stringify({ok:true}));}
else throw new Error('UNKNOWN_COMMAND');
