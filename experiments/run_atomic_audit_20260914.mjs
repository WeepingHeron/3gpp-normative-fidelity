import fs from 'node:fs';
import {auditDelivery} from './run_preservation_repair_20260914.mjs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {performance} from 'node:perf_hooks';

export const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
export const BASE_REL = 'experiments/atomic_audit_v1_20260914';
export const RUN_REL = 'experiments/runs/atomic_audit_v1_20260914';
export const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const read = p => JSON.parse(fs.readFileSync(p, 'utf8'));
const rows = p => fs.readFileSync(p, 'utf8').trim().split('\n').map(JSON.parse);
const stamp = () => new Date().toISOString();
const write = (p, o) => fs.writeFileSync(p, JSON.stringify(o, null, 2) + '\n');
const append = (p, o) => fs.appendFileSync(p, JSON.stringify(o) + '\n');
const requireThat = (ok, code) => { if (!ok) throw new Error(code); };

export function usageCost(usage, prices) {
  if (!usage || typeof usage !== 'object') return null;
  const input = usage.input_tokens, output = usage.output_tokens;
  const details = usage.input_tokens_details;
  if (details !== undefined && (details === null || typeof details !== 'object' || Array.isArray(details))) return null;
  const cached = details && Object.hasOwn(details, 'cached_tokens') ? details.cached_tokens : 0;
  if (![input, output, cached].every(x => Number.isSafeInteger(x) && x >= 0) || cached > input) return null;
  if (usage.total_tokens !== undefined && usage.total_tokens !== input + output) return null;
  return ((input - cached) * prices.input + cached * prices.cached_input + output * prices.output) / 1e6;
}

export function delivery(body,schema) { return auditDelivery(body,schema); }

export function checkPlan(root = ROOT, frozen = true) {
  const base = path.join(root, BASE_REL);
  const protocol = read(path.join(base, 'protocol.json'));
  requireThat(protocol.status === 'READY_TO_FREEZE', 'PROTOCOL_STATUS');
  if (frozen) {
    const manifest = read(path.join(base, 'input_freeze_manifest.json'));
    requireThat(manifest.status === 'FROZEN_BEFORE_GENERATION' && manifest.planned_calls === 12, 'FREEZE_STATUS');
    for (const [p, h] of Object.entries(manifest.file_sha256))
      requireThat(sha(fs.readFileSync(path.join(root, p))) === h, `FROZEN_FILE_CHANGED:${p}`);
  }
  const plan = rows(path.join(base, frozen ? 'request_plan.jsonl' : 'request_plan.preview.jsonl'));
  requireThat(plan.length === 12 && new Set(plan.map(x => x.slot_id)).size === 12, 'PLAN_CARDINALITY');
  let reserved = 0;
  for (const row of plan) {
    const r = row.request;
    requireThat(sha(JSON.stringify(r)) === row.request_sha256, 'REQUEST_HASH');
    requireThat(r.model === protocol.model && r.temperature === protocol.parameters.temperature
      && r.max_output_tokens === protocol.parameters.max_output_tokens && r.store === false
      && r.reasoning.effort === protocol.parameters.reasoning_effort, 'REQUEST_PARAMETERS');
    const expected = ((Buffer.byteLength(r.input) + Buffer.byteLength(JSON.stringify(r.text.format.schema)) + 2048)
      * protocol.pricing_usd_per_million.input + r.max_output_tokens * protocol.pricing_usd_per_million.output) / 1e6;
    requireThat(Number.isFinite(row.estimated_reservation_usd) && Math.abs(expected - row.estimated_reservation_usd) < 1e-12, 'RESERVATION_MISMATCH');
    reserved += expected;
  }
  requireThat(reserved <= protocol.generation_cost_cap_usd, 'WHOLE_PLAN_COST_GUARD');
  return {protocol, plan, reserved};
}

// The injected transport supports offline fault tests. The CLI always uses the fixed OpenAI endpoint.
export async function runSlots({plan, protocol, runDir, transport, inputFreezeHash, inputFrozenAt, provenance = 'LIVE_API'}) {
  requireThat(!fs.existsSync(runDir), 'RUN_EXISTS_NO_REPLAY');
  fs.mkdirSync(runDir, {recursive: false});
  const manifest = {experiment_id: protocol.experiment_id, status: 'RUNNING', provenance,
    started_at: stamp(), input_freeze_sha256: inputFreezeHash, input_frozen_at: inputFrozenAt,
    model: protocol.model, planned_slots: plan.length, attempts: 0, returned_responses: 0,
    usable_explanations: 0, known_cost_usd: 0, cost_complete: true, evaluator_status: 'NOT_EVALUATED'};
  const ledger = plan.map(r => ({slot_id: r.slot_id, case_id: r.case_id, arm: r.arm, replicate: r.replicate,
    delivery_status: 'NOT_ATTEMPTED', semantic_status: 'NOT_OBSERVED', request_sha256: r.request_sha256}));
  write(path.join(runDir, 'manifest.json'), manifest);
  try {
    for (const [i, row] of plan.entries()) {
      requireThat(manifest.known_cost_usd + row.estimated_reservation_usd <= protocol.generation_cost_cap_usd, 'COST_GUARD');
      const item = ledger[i], started = stamp(), tick = performance.now();
      item.delivery_status = 'ATTEMPTED_OUTCOME_UNKNOWN';
      manifest.attempts++;
      append(path.join(runDir, 'requests.jsonl'), {slot_id: row.slot_id, started_at: started,
        request: row.request, request_sha256: row.request_sha256});
      write(path.join(runDir, 'manifest.json'), manifest);
      let response;
      try { response = await transport(row.request); }
      catch {
        item.delivery_status = 'TRANSPORT_UNCERTAIN';
        manifest.cost_complete = false;
        append(path.join(runDir, 'raw_responses.jsonl'), {slot_id: row.slot_id, completed_at: stamp(),
          transport_error: 'OUTCOME_UNKNOWN_NO_RETRY'});
        throw new Error('TRANSPORT_UNCERTAIN_NO_RETRY');
      }
      const {http_status, body} = response;
      const elapsed_ms = performance.now() - tick;
      manifest.returned_responses++;
      append(path.join(runDir, 'raw_responses.jsonl'), {slot_id: row.slot_id, started_at: started,
        completed_at: stamp(), elapsed_ms, http_status, response: body});
      item.delivery_status = 'EXECUTION_ERROR';
      const cost = body?.model === protocol.model ? usageCost(body?.usage, protocol.pricing_usd_per_million) : null;
      if (cost === null) manifest.cost_complete = false;
      else manifest.known_cost_usd += cost;
      requireThat(http_status >= 200 && http_status < 300, `HTTP_${http_status}_NO_RETRY`);
      requireThat(body.model === protocol.model, 'MODEL_SNAPSHOT_MISMATCH');
      requireThat(cost !== null, 'USAGE_INVALID_OR_MISSING');
      const result = delivery(body, row.request.text.format.schema);
      item.delivery_status = result.status;
      item.semantic_status = result.parsed ? 'PENDING_REVIEW' : 'NOT_ASSESSABLE';
      item.pipeline_completeness = result.parsed ? null : 0;
      item.parsed = result.parsed;
      item.response_id = body.id ?? null;
      item.usage = body.usage;
      item.elapsed_ms = elapsed_ms;
      if (result.parsed) manifest.usable_explanations++;
      append(path.join(runDir, 'parsed_responses.jsonl'), item);
      write(path.join(runDir, 'manifest.json'), manifest);
      requireThat(result.parsed !== null, 'AUDIT_DELIVERY_FAILURE_NO_RETRY');
      requireThat(manifest.known_cost_usd <= protocol.generation_cost_cap_usd, 'ACTUAL_COST_EXCEEDED');
    }
    manifest.status = 'GENERATION_COMPLETE_SEMANTICS_PENDING';
  } catch (error) {
    manifest.status = 'STOPPED';
    manifest.stop_reason = error.message;
  }
  manifest.finished_at = stamp();
  fs.writeFileSync(path.join(runDir, 'slot_ledger.jsonl'), ledger.map(x => JSON.stringify(x)).join('\n') + '\n');
  write(path.join(runDir, 'manifest.json'), manifest);
  write(path.join(runDir, 'output_freeze_manifest.json'), {frozen_at: stamp(), provenance,
    file_sha256: Object.fromEntries(fs.readdirSync(runDir).sort().map(n => [n, sha(fs.readFileSync(path.join(runDir, n)))]))});
  for (const name of fs.readdirSync(runDir)) fs.chmodSync(path.join(runDir, name), 0o444);
  return manifest;
}

async function main() {
  const command = process.argv[2] || 'verify-freeze';
  requireThat(['check-draft', 'verify-freeze', 'execute'].includes(command), 'UNKNOWN_COMMAND');
  const checked = checkPlan(ROOT, command !== 'check-draft');
  if (command !== 'execute') {
    console.log(JSON.stringify({ok: true, command, planned_calls: checked.plan.length,
      reservation_usd: checked.reserved, live_api_calls: 0}));
    return;
  }
  const runDir = path.join(ROOT, RUN_REL);
  requireThat(!fs.existsSync(runDir), 'RUN_EXISTS_NO_REPLAY');
  let key = process.env.OPENAI_API_KEY;
  if (!key) {
    const line = fs.readFileSync(path.join(ROOT, '.env.local'), 'utf8').split(/\r?\n/).find(x => /^\s*OPENAI_API_KEY\s*=/.test(x));
    key = line?.slice(line.indexOf('=') + 1).trim().replace(/^['"]|['"]$/g, '');
  }
  requireThat(!!key, 'API_KEY_UNAVAILABLE');
  const freezePath = path.join(ROOT, BASE_REL, 'input_freeze_manifest.json');
  const manifest = await runSlots({...checked, runDir, inputFreezeHash: sha(fs.readFileSync(freezePath)),
    inputFrozenAt: read(freezePath).frozen_at, transport: async request => {
      const http = await fetch('https://api.openai.com/v1/responses', {method: 'POST',
        headers: {Authorization: `Bearer ${key}`, 'Content-Type': 'application/json'},
        body: JSON.stringify(request), signal: AbortSignal.timeout(checked.protocol.runtime_policy.request_timeout_ms)});
      const rawText = await http.text();
      let body;
      try { body = JSON.parse(rawText); } catch { body = {non_json_body: rawText}; }
      return {http_status: http.status, body};
    }});
  console.log(JSON.stringify(manifest));
  if (manifest.status === 'STOPPED') process.exitCode = 2;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url))
  await main().catch(error => { console.error(error.message); process.exitCode = 2; });
