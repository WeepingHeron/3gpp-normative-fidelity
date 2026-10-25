// Read-only verification of frozen requests, sealed generation and masked packets.
import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import {checkPlan, delivery, usageCost, sha, ROOT} from '../experiments/run_generation_preservation_20260909.mjs';

const read = p => JSON.parse(fs.readFileSync(path.join(ROOT,p),'utf8'));
const rows = p => fs.readFileSync(path.join(ROOT,p),'utf8').trim().split('\n').map(JSON.parse);
const hash = p => sha(fs.readFileSync(path.join(ROOT,p)));
const {plan,protocol} = checkPlan();
const run = 'experiments/runs/generation_preservation_v1_20260909';
const review = 'outputs/review/generation_preservation_v1_20260909';
const record = 'outputs/review/generation_preservation_execution_20260913';
const manifest = read(`${run}/manifest.json`), sealed = read(`${run}/output_freeze_manifest.json`);
assert.equal(manifest.status,'GENERATION_COMPLETE_SEMANTICS_PENDING');
assert.equal(manifest.provenance,'LIVE_API');
assert.equal(manifest.input_freeze_sha256,hash('experiments/generation_preservation_v1_20260909/input_freeze_manifest.json'));
assert.ok(Date.parse(manifest.input_frozen_at)<Date.parse(manifest.started_at));
assert.deepEqual(Object.keys(sealed.file_sha256).sort(),fs.readdirSync(path.join(ROOT,run)).filter(n=>n!=='output_freeze_manifest.json').sort());
for(const [p,h] of Object.entries(sealed.file_sha256))assert.equal(hash(`${run}/${p}`),h);
const requests = rows(`${run}/requests.jsonl`), raw = rows(`${run}/raw_responses.jsonl`), ledger = rows(`${run}/slot_ledger.jsonl`);
assert.deepEqual(rows(`${run}/parsed_responses.jsonl`),ledger);
assert.equal(requests.length,18);assert.equal(raw.length,18);assert.equal(ledger.length,18);
let input=0,cached=0,output=0,cost=0;
for(let i=0;i<18;i++){
  const p=plan[i], req=requests[i], result=ledger[i], response=raw[i];
  assert.equal(req.slot_id,p.slot_id);assert.equal(response.slot_id,p.slot_id);assert.equal(result.slot_id,p.slot_id);
  assert.deepEqual(req.request,p.request);assert.equal(req.request_sha256,p.request_sha256);assert.equal(result.request_sha256,p.request_sha256);
  assert.equal(response.http_status,200);assert.equal(response.response.model,protocol.model);
  assert.deepEqual(response.response.usage,result.usage);
  const classified=delivery(response.response,p.request.text.format.schema);
  assert.equal(classified.status,'EXPLANATION');assert.equal(result.delivery_status,classified.status);assert.deepEqual(classified.parsed,result.parsed);
  assert.equal(result.semantic_status,'PENDING_REVIEW');
  const u=response.response.usage, charge=usageCost(u,protocol.pricing_usd_per_million);
  assert.notEqual(charge,null);cost+=charge;input+=u.input_tokens;cached+=u.input_tokens_details?.cached_tokens??0;output+=u.output_tokens;
}
assert.equal(manifest.attempts,18);assert.equal(manifest.returned_responses,18);assert.equal(manifest.usable_explanations,18);
assert.equal(manifest.cost_complete,true);assert.ok(Math.abs(cost-manifest.known_cost_usd)<1e-12);assert.ok(cost<=.5);
const packets=rows(`${review}/reviewer/packets_18.jsonl`), keys=rows(`${review}/coordinator/keys_18.jsonl`), packetManifest=read(`${review}/packet_manifest.json`);
assert.equal(packets.length,18);assert.equal(keys.length,18);assert.equal(new Set(keys.map(x=>x.slot_id)).size,18);
assert.equal(packetManifest.input_freeze_sha256,manifest.input_freeze_sha256);
assert.equal(packetManifest.run_output_freeze_sha256,hash(`${run}/output_freeze_manifest.json`));
for(const [p,h] of Object.entries(packetManifest.file_sha256))assert.equal(hash(`${review}/${p}`),h);
for(const p of packets){
  const key=keys.find(x=>x.review_id===p.review_id), original=ledger.find(x=>x.slot_id===key.slot_id);
  assert.equal(p.explanation_ko,original.parsed.explanation_ko);
  assert.ok(!Object.hasOwn(p,'arm')&&!Object.hasOwn(p,'request')&&!Object.hasOwn(p,'slot_id'));
}
assert.equal(packets.reduce((n,p)=>n+p.requirements.length,0),54);
const prelaunch=read(`${record}/prelaunch.json`);
assert.ok(Date.parse(prelaunch.checked_at)<Date.parse(manifest.started_at));
assert.equal(prelaunch.input_manifest_sha256,manifest.input_freeze_sha256);
assert.deepEqual(prelaunch.pricing_usd_per_million,protocol.pricing_usd_per_million);
const report={ok:true,generated:18,retries:0,delivery_failures:0,input_tokens:input,cached_input_tokens:cached,output_tokens:output,
  generation_cost_usd:Number(cost.toFixed(9)),masked_packets:18,requirements_per_reviewer:54,
  exact_request_response_binding:true,freeze_and_output_hashes_verified:true,semantic_evaluation_performed:false};
console.log(JSON.stringify(report));
