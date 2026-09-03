import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

function parseCsv(text) {
  const rows = []; let row = [], field = "", quoted = false;
  for (let i = 0; i < text.length; i++) { const c = text[i];
    if (quoted) { if (c === '"' && text[i + 1] === '"') { field += '"'; i++; } else if (c === '"') quoted = false; else field += c; }
    else if (c === '"') quoted = true; else if (c === ',') { row.push(field); field = ""; } else if (c === '\n') { row.push(field.replace(/\r$/, "")); rows.push(row); row = []; field = ""; } else field += c;
  }
  if (field.length || row.length) { row.push(field.replace(/\r$/, "")); rows.push(row); }
  const [header, ...body] = rows.filter(r => r.some(v => v !== ""));
  return body.map(r => Object.fromEntries(header.map((h, i) => [h.replace(/^\uFEFF/, ""), r[i] ?? ""])));
}
function csvCell(v) { const s = v == null ? "" : String(v); return /[",\n]/.test(s) ? `"${s.replaceAll('"', '""')}"` : s; }
function writeCsv(file, rows, headers) { fs.writeFileSync(file, "\uFEFF" + [headers.join(","), ...rows.map(r => headers.map(h => csvCell(r[h])).join(","))].join("\n") + "\n"); }

const runArg = process.argv[2];
const passArg = process.argv[3];
if (!runArg || !/^pass[0-9]+$/.test(passArg || "")) throw new Error("Usage: node experiments/prepare_review_pass.mjs <run_directory> <passN>");
const root = path.resolve(import.meta.dirname, "..");
const runDir = path.resolve(runArg);
const manifest = JSON.parse(fs.readFileSync(path.join(runDir, "manifest.json"), "utf8"));
if (!manifest.dataset_path) throw new Error("Run manifest is missing dataset_path");
const dataset = parseCsv(fs.readFileSync(path.join(root, manifest.dataset_path), "utf8"));
const gold = new Map(dataset.map(r => [r.case_id, r]));
const parsed = fs.readFileSync(path.join(runDir, "parsed_responses.jsonl"), "utf8").trim().split("\n").filter(Boolean).map(JSON.parse);
const seed = `${path.basename(runDir)}:${passArg}:2026-09-02`;
const shuffled = parsed.map(item => ({
  item,
  order: crypto.createHash("sha256").update(`${seed}:${item.case_id}:${item.condition}`).digest("hex"),
})).sort((a, b) => a.order.localeCompare(b.order));
const key = {};
const rows = shuffled.map(({ item }, index) => {
  const reviewId = `S${String(index + 1).padStart(3, "0")}`;
  const g = gold.get(item.case_id); const p = item.parsed;
  if (!g) throw new Error(`No gold row for ${item.case_id} in ${manifest.dataset_path}`);
  key[reviewId] = { case_id: item.case_id, condition: item.condition };
  return {
    review_id: reviewId,
    source_text_en: g.source_text_en,
    gold_modal_class: g.modal_class,
    gold_actor: g.actor,
    gold_condition: g.condition,
    gold_action: g.action,
    gold_exception: g.exception,
    explanation_ko: p?.explanation_ko || "",
    predicted_normative_type: p?.normative_type || "",
    actor_output: p?.actor || "",
    condition_output: p?.condition || "",
    action_output: p?.action || "",
    exception_output: p?.exception || "",
    actor_preserved: "", polarity_preserved: "", condition_preserved: "", action_preserved: "", exception_preserved: "",
    complete_preservation: "", unsupported_addition: "", error_codes: "", reviewer_note: "",
  };
});
writeCsv(path.join(runDir, `blind_review_${passArg}_blank.csv`), rows, Object.keys(rows[0]));
fs.writeFileSync(path.join(runDir, `blind_key_${passArg}.json`), JSON.stringify(key, null, 2) + "\n");
fs.writeFileSync(path.join(runDir, `blind_${passArg}_manifest.json`), JSON.stringify({
  pass: passArg,
  prepared_at: new Date().toISOString(),
  seed_sha256: crypto.createHash("sha256").update(seed).digest("hex"),
  row_count: rows.length,
  condition_hidden: true,
  case_id_hidden: true,
}, null, 2) + "\n");
console.log(`prepared ${rows.length} rows for ${passArg}`);
