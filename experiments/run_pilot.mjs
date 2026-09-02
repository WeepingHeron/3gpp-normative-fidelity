import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

const ROOT = path.resolve(import.meta.dirname, "..");
const MODAL_TO_TYPE = {
  shall: "obligation",
  shall_not: "prohibition",
  should: "recommendation",
  should_not: "discouragement",
  may: "permission",
  can: "capability",
};

function parseEnvFile(filePath) {
  const result = {};
  if (!fs.existsSync(filePath)) return result;
  for (const line of fs.readFileSync(filePath, "utf8").split(/\r?\n/)) {
    if (!line || line.trimStart().startsWith("#")) continue;
    const i = line.indexOf("=");
    if (i < 1) continue;
    const key = line.slice(0, i).trim();
    let value = line.slice(i + 1).trim();
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) value = value.slice(1, -1);
    result[key] = value;
  }
  return result;
}

function parseCsv(text) {
  const rows = [];
  let row = [], field = "", quoted = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (quoted) {
      if (c === '"' && text[i + 1] === '"') { field += '"'; i++; }
      else if (c === '"') quoted = false;
      else field += c;
    } else if (c === '"') quoted = true;
    else if (c === ',') { row.push(field); field = ""; }
    else if (c === '\n') { row.push(field.replace(/\r$/, "")); rows.push(row); row = []; field = ""; }
    else field += c;
  }
  if (field.length || row.length) { row.push(field.replace(/\r$/, "")); rows.push(row); }
  const [header, ...body] = rows.filter(r => r.some(v => v !== ""));
  return body.map(r => Object.fromEntries(header.map((h, i) => [h.replace(/^\uFEFF/, ""), r[i] ?? ""])));
}

function sha256(data) { return crypto.createHash("sha256").update(data).digest("hex"); }
function render(template, values) {
  return template.replace(/{{([a-z_]+)}}/g, (_, key) => values[key] ?? "");
}
function outputText(response) {
  for (const item of response.output || []) {
    if (item.type !== "message") continue;
    for (const content of item.content || []) if (content.type === "output_text") return content.text;
  }
  return "";
}
function writeJsonl(filePath, value) { fs.appendFileSync(filePath, JSON.stringify(value) + "\n"); }

const args = new Set(process.argv.slice(2));
const fullPilot = args.has("--full-pilot");
const promptVersionArg = process.argv.slice(2).find(v => v.startsWith("--prompt-version="));
const promptVersion = promptVersionArg ? promptVersionArg.split("=", 2)[1] : "v1";
if (!/^v[0-9]+$/.test(promptVersion)) throw new Error("Invalid prompt version");
const model = process.env.OPENAI_MODEL || "gpt-5.4-mini-2026-03-17";
const env = { ...parseEnvFile(path.join(ROOT, ".env.local")), ...process.env };
if (!env.OPENAI_API_KEY) throw new Error("OPENAI_API_KEY is not configured");

const datasetPath = path.join(ROOT, "data", "pilot_cases.csv");
const datasetBytes = fs.readFileSync(datasetPath);
const cases = parseCsv(datasetBytes.toString("utf8"));
const selected = fullPilot ? cases : Object.keys(MODAL_TO_TYPE).map(modal => cases.find(r => r.modal_class === modal));
if (selected.some(v => !v)) throw new Error("Dry-run selection is missing a modal class");

const promptDir = path.join(ROOT, "experiments", "prompts");
const promptFileVersions = promptVersion === "v3"
  ? { C0: "v3", C1: "v2", C2: "v2" }
  : { C0: promptVersion, C1: promptVersion, C2: promptVersion };
const promptTemplates = Object.fromEntries(["C0", "C1", "C2"].map(c => [c, fs.readFileSync(path.join(promptDir, `${c.toLowerCase()}_${promptFileVersions[c]}.md`), "utf8")]));
const schema = JSON.parse(fs.readFileSync(path.join(ROOT, "experiments", "response_schema.json"), "utf8"));
const timestamp = new Date().toISOString().replace(/[:.]/g, "-");
const runId = `${fullPilot ? "pilot18" : "dry6"}_${promptVersion}_${timestamp}`;
const runDir = path.join(ROOT, "experiments", "runs", runId);
fs.mkdirSync(runDir, { recursive: true });
const rawPath = path.join(runDir, "raw_responses.jsonl");
const parsedPath = path.join(runDir, "parsed_responses.jsonl");

const executionPlan = [];
selected.forEach((row, index) => {
  const orders = [["C0", "C1", "C2"], ["C1", "C2", "C0"], ["C2", "C0", "C1"]];
  for (const condition of orders[index % orders.length]) executionPlan.push({ row, condition });
});

const manifest = {
  run_id: runId,
  purpose: fullPilot ? "pilot_all_cases" : "dry_run_one_case_per_modal_class",
  research_use: "prompt/schema/scoring validation only; excluded from main results",
  created_at: new Date().toISOString(),
  provider: "OpenAI",
  api: "Responses API",
  model_requested: model,
  model_snapshot_returned: null,
  parameters: { temperature: 0, reasoning_effort: "none", max_output_tokens: 600, store: false },
  dataset_path: "data/pilot_cases.csv",
  dataset_sha256: sha256(datasetBytes),
  selected_case_ids: selected.map(r => r.case_id),
  prompt_version: promptVersion,
  prompt_file_versions: promptFileVersions,
  conditions: ["C0", "C1", "C2"],
  prompt_sha256: Object.fromEntries(Object.entries(promptTemplates).map(([k, v]) => [k, sha256(v)])),
  response_schema_sha256: sha256(JSON.stringify(schema)),
  execution_order: executionPlan.map((v, i) => ({ request_index: i + 1, case_id: v.row.case_id, condition: v.condition })),
  retry_policy: "At most 2 retries for transient HTTP 429 or 5xx and transport errors, with attempt metadata retained. No retry for insufficient_quota, parse, or semantic failure.",
  status: "running",
};
fs.writeFileSync(path.join(runDir, "manifest.json"), JSON.stringify(manifest, null, 2) + "\n");

let blockedReason = null;
executionLoop: for (let index = 0; index < executionPlan.length; index++) {
  const { row, condition } = executionPlan[index];
  const values = { ...row, normative_type: MODAL_TO_TYPE[row.modal_class] };
  const input = render(promptTemplates[condition], values);
  const request = {
    model,
    input,
    temperature: 0,
    reasoning: { effort: "none" },
    max_output_tokens: 600,
    store: false,
    text: { format: { type: "json_schema", name: "normative_explanation", strict: true, schema } },
  };
  let response = null, status = null, error = null;
  for (let attempt = 1; attempt <= 3; attempt++) {
    const startedAt = new Date().toISOString();
    try {
      const http = await fetch("https://api.openai.com/v1/responses", {
        method: "POST",
        headers: { Authorization: `Bearer ${env.OPENAI_API_KEY}`, "Content-Type": "application/json" },
        body: JSON.stringify(request),
      });
      status = http.status;
      response = await http.json();
      writeJsonl(rawPath, { request_index: index + 1, case_id: row.case_id, condition, attempt, started_at: startedAt, http_status: status, response });
      if (http.ok) { error = null; break; }
      error = response?.error?.message || `HTTP ${status}`;
      if (response?.error?.code === "credit_balance_exhausted" || response?.error?.type === "insufficient_quota") break;
      if (status !== 429 && status < 500) break;
    } catch (e) {
      error = e instanceof Error ? e.message : String(e);
      writeJsonl(rawPath, { request_index: index + 1, case_id: row.case_id, condition, attempt, started_at: startedAt, transport_error: error });
    }
    if (attempt < 3) await new Promise(resolve => setTimeout(resolve, 500 * 2 ** (attempt - 1)));
  }
  let parsed = null, parseError = null;
  if (response && status >= 200 && status < 300) {
    const text = outputText(response);
    try { parsed = JSON.parse(text); } catch (e) { parseError = e instanceof Error ? e.message : String(e); }
    manifest.model_snapshot_returned ||= response.model || null;
  }
  writeJsonl(parsedPath, {
    request_index: index + 1,
    case_id: row.case_id,
    modal_class: row.modal_class,
    condition,
    response_id: response?.id || null,
    status: response?.status || (error ? "failed" : null),
    http_status: status,
    error,
    parse_error: parseError,
    usage: response?.usage || null,
    parsed,
  });
  console.log(`${index + 1}/${executionPlan.length} ${row.case_id} ${condition} ${parsed ? "OK" : "FAILED"}`);
  if (response?.error?.code === "credit_balance_exhausted" || response?.error?.type === "insufficient_quota") {
    blockedReason = "OPENAI_API_CREDIT_BALANCE_EXHAUSTED";
    break executionLoop;
  }
}

manifest.completed_at = new Date().toISOString();
manifest.status = blockedReason ? "blocked" : "completed";
manifest.block_reason = blockedReason;
fs.writeFileSync(path.join(runDir, "manifest.json"), JSON.stringify(manifest, null, 2) + "\n");
console.log(`RUN_DIR=${runDir}`);
