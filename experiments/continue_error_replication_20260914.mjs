import fs from 'node:fs';import path from 'node:path';import {ROOT,sha,runSlots} from './run_atomic_audit_20260914.mjs';
const base=path.join(ROOT,'experiments/error_replication_v1_20260914'),runDir=path.join(ROOT,'experiments/runs/error_replication_remaining8_20260914');
const read=p=>JSON.parse(fs.readFileSync(p,'utf8'));const f=read(path.join(base,'input_freeze_manifest.json'));
for(const [p,h]of Object.entries(f.file_sha256))if(sha(fs.readFileSync(path.join(ROOT,p)))!==h)throw Error('HASH');
const ledger=fs.readFileSync(path.join(ROOT,'experiments/runs/error_replication_v1_20260914/slot_ledger.jsonl'),'utf8').trim().split('\n').map(JSON.parse);
const unattempted=new Set(ledger.filter(x=>x.delivery_status==='NOT_ATTEMPTED').map(x=>x.slot_id));
const plan=read(path.join(base,'plan.json')).filter(x=>unattempted.has(x.slot_id));if(plan.length!==8)throw Error('REMAINDER_COUNT');
const protocol=read(path.join(base,'protocol.json'));
const checkpoint=path.join(base,'remaining8_authorization.json');
if(process.argv[2]==='prepare'){if(fs.existsSync(checkpoint))throw Error('EXISTS');fs.writeFileSync(checkpoint,JSON.stringify({frozen_at:new Date().toISOString(),reason:'DNS ENOTFOUND in sandbox; preserve attempted first slot unknown without replay. New authorization to execute only eight NOT_ATTEMPTED slots through network-enabled execution.',slot_ids:plan.map(x=>x.slot_id),runner_sha256:sha(fs.readFileSync(new URL(import.meta.url))),original_freeze_sha256:sha(fs.readFileSync(path.join(base,'input_freeze_manifest.json')))},null,2));console.log('REMAINING8_FROZEN');}else{
const checkpointValue=read(checkpoint);if(checkpointValue.runner_sha256!==sha(fs.readFileSync(new URL(import.meta.url))))throw Error('RUNNER_CHANGED');
let key=process.env.OPENAI_API_KEY;if(!key){const line=fs.readFileSync(path.join(ROOT,'.env.local'),'utf8').split(/\r?\n/).find(x=>/^\s*OPENAI_API_KEY\s*=/.test(x));key=line?.slice(line.indexOf('=')+1).trim().replace(/^['"]|['"]$/g,'');}if(!key)throw Error('KEY_ABSENT');
const result=await runSlots({plan,protocol,runDir,inputFreezeHash:sha(fs.readFileSync(checkpoint)),inputFrozenAt:checkpointValue.frozen_at,transport:async request=>{const r=await fetch('https://api.openai.com/v1/responses',{method:'POST',headers:{Authorization:`Bearer ${key}`,'Content-Type':'application/json'},body:JSON.stringify(request),signal:AbortSignal.timeout(60000)});return {http_status:r.status,body:await r.json()};}});console.log(JSON.stringify(result));}
