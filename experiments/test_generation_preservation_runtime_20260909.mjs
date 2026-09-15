import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {checkPlan, usageCost, delivery, runSlots, ROOT, sha} from './run_generation_preservation_20260909.mjs';

const {plan, protocol} = checkPlan(ROOT, fs.existsSync(path.join(ROOT, 'experiments/generation_preservation_v1_20260909/input_freeze_manifest.json')));
const schema = plan[0].request.text.format.schema;
const parsed = Object.fromEntries(schema.required.map(k => [k, k === 'normative_type' ? 'permission' : 'SYNTHETIC_TEST_ONLY']));
const body = () => ({id: 'synthetic-test-response', model: protocol.model, status: 'completed',
  usage: {input_tokens: 100, output_tokens: 30, total_tokens: 130, input_tokens_details: {cached_tokens: 0}},
  output: [{type: 'message', content: [{type: 'output_text', text: JSON.stringify(parsed)}]}]});
const prices = protocol.pricing_usd_per_million;
const checks = [];
function test(name, fn) { fn(); checks.push(name); }
test('invalid_usage_rejected', () => {
  for (const usage of [null, {input_tokens: -1, output_tokens: 0}, {input_tokens: 1.5, output_tokens: 2},
    {input_tokens: 1, output_tokens: true}, {input_tokens: 1, output_tokens: 1, total_tokens: 3},
    {input_tokens: 1, output_tokens: 1, input_tokens_details: {cached_tokens: 2}},
    {input_tokens: 1, output_tokens: 1, input_tokens_details: null},
    {input_tokens: 1, output_tokens: 1, input_tokens_details: {cached_tokens: null}}])
    assert.equal(usageCost(usage, prices), null);
  assert.equal(usageCost({input_tokens: 10, output_tokens: 1}, prices), .000012);
});
test('delivery_states_distinct', () => {
  const invalid = body(); invalid.output[0].content[0].text = 'invalid';
  assert.equal(delivery(invalid, schema).status, 'INVALID_JSON');
  const empty = body(); empty.output[0].content[0].text = JSON.stringify({...parsed, explanation_ko: ' '});
  assert.equal(delivery(empty, schema).status, 'EMPTY_EXPLANATION');
  const bad = body(); bad.output[0].content[0].text = JSON.stringify({...parsed, unknown: 'x'});
  assert.equal(delivery(bad, schema).status, 'SCHEMA_INVALID');
  const refusal = body(); refusal.output[0].content = [{type: 'refusal', refusal: 'synthetic'}];
  assert.equal(delivery(refusal, schema).status, 'REFUSAL');
  assert.equal(delivery({...body(), status: 'incomplete'}, schema).status, 'INCOMPLETE');
});
const scratch = fs.mkdtempSync(path.join(os.tmpdir(), 'generation-preservation-faults-'));
try {
  const fakeRoot = path.join(scratch, 'tampered-freeze');
  const fakeBase = path.join(fakeRoot, 'experiments/generation_preservation_v1_20260909');
  fs.mkdirSync(fakeBase, {recursive: true});
  fs.writeFileSync(path.join(fakeBase, 'protocol.json'), JSON.stringify(protocol));
  fs.writeFileSync(path.join(fakeRoot, 'input.txt'), 'changed');
  fs.writeFileSync(path.join(fakeBase, 'input_freeze_manifest.json'), JSON.stringify({status: 'FROZEN_BEFORE_GENERATION',
    planned_calls: 18, file_sha256: {'input.txt': sha('original')}}));
  assert.throws(() => checkPlan(fakeRoot, true), /FROZEN_FILE_CHANGED/);
  checks.push('changed_frozen_input_rejected');
  async function scenario(name, modifier, expected, override = {}) {
    let calls = 0;
    const runDir = path.join(scratch, name);
    const transport = async () => { calls++; return modifier(calls); };
    const args = {plan, protocol: {...protocol, ...override}, runDir, transport,
      inputFreezeHash: 'SYNTHETIC_TEST_ONLY', inputFrozenAt: '2000-01-01T00:00:00Z', provenance: 'SYNTHETIC_TEST_ONLY'};
    const result = await runSlots(args);
    for (const [k, v] of Object.entries(expected)) assert.equal(k === 'calls' ? calls : result[k], v, `${name}:${k}`);
    const ledger = fs.readFileSync(path.join(runDir, 'slot_ledger.jsonl'), 'utf8').trim().split('\n').map(JSON.parse);
    assert.equal(ledger.length, 18);
    assert.equal(new Set(ledger.map(r => r.slot_id)).size, 18);
    const sealed = JSON.parse(fs.readFileSync(path.join(runDir, 'output_freeze_manifest.json')));
    for (const [p, h] of Object.entries(sealed.file_sha256)) assert.equal(sha(fs.readFileSync(path.join(runDir, p))), h);
    const beforeReplay = calls;
    await assert.rejects(runSlots(args), /RUN_EXISTS_NO_REPLAY/);
    assert.equal(calls, beforeReplay);
    checks.push(name);
    return ledger;
  }
  await scenario('complete_18_no_retry', () => ({http_status: 200, body: body()}),
    {calls: 18, attempts: 18, usable_explanations: 18, status: 'GENERATION_COMPLETE_SEMANTICS_PENDING', cost_complete: true});
  const refused = await scenario('refusal_preserves_denominator', n => {
    const b = body(); if (n === 1) b.output[0].content = [{type: 'refusal', refusal: 'synthetic'}];
    return {http_status: 200, body: b};
  }, {calls: 18, usable_explanations: 17, cost_complete: true});
  assert.equal(refused[0].pipeline_completeness, 0);
  assert.equal(refused[0].semantic_status, 'NOT_ASSESSABLE');
  await scenario('transport_unknown_stops', () => { throw new Error('synthetic transport error'); },
    {calls: 1, attempts: 1, status: 'STOPPED', cost_complete: false, stop_reason: 'TRANSPORT_UNCERTAIN_NO_RETRY'});
  await scenario('http_error_stops', () => ({http_status: 429, body: {error: 'synthetic'}}),
    {calls: 1, status: 'STOPPED', cost_complete: false, stop_reason: 'HTTP_429_NO_RETRY'});
  await scenario('missing_usage_stops', () => ({http_status: 200, body: {...body(), usage: null}}),
    {calls: 1, status: 'STOPPED', cost_complete: false, stop_reason: 'USAGE_INVALID_OR_MISSING'});
  await scenario('model_mismatch_stops', () => ({http_status: 200, body: {...body(), model: 'different'}}),
    {calls: 1, status: 'STOPPED', cost_complete: false, stop_reason: 'MODEL_SNAPSHOT_MISMATCH'});
  await scenario('cost_guard_before_request', () => ({http_status: 200, body: body()}),
    {calls: 0, attempts: 0, status: 'STOPPED', stop_reason: 'COST_GUARD'}, {generation_cost_cap_usd: 0});
  await scenario('actual_cost_overshoot_stops', () => ({http_status: 200, body: {...body(), usage: {input_tokens: 1000000, output_tokens: 0}}}),
    {calls: 1, status: 'STOPPED', known_cost_usd: .75, stop_reason: 'ACTUAL_COST_EXCEEDED'});
} finally { fs.rmSync(scratch, {recursive: true, force: true}); }
console.log(JSON.stringify({ok: true, test_provenance: 'SYNTHETIC_TEST_ONLY', live_api_calls: 0,
  checks, checked_at: new Date().toISOString(), runner_sha256: sha(fs.readFileSync(path.join(ROOT, 'experiments/run_generation_preservation_20260909.mjs')))}));
