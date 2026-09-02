import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

const ROOT = path.resolve(import.meta.dirname, "..");
const MODAL_TO_TYPE = { shall: "obligation", shall_not: "prohibition", should: "recommendation", should_not: "discouragement", may: "permission", can: "capability" };

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
if (!runArg) throw new Error("Usage: node experiments/score_run.mjs <run_directory>");
const runDir = path.resolve(runArg);
const dataset = parseCsv(fs.readFileSync(path.join(ROOT, "data", "pilot_cases.csv"), "utf8"));
const gold = new Map(dataset.map(r => [r.case_id, r]));
const parsed = fs.readFileSync(path.join(runDir, "parsed_responses.jsonl"), "utf8").trim().split("\n").filter(Boolean).map(JSON.parse);
const auto = parsed.map(item => {
  const g = gold.get(item.case_id); const p = item.parsed;
  const citationApplicable = item.condition !== "C0";
  return {
    request_index: item.request_index, case_id: item.case_id, condition: item.condition, response_status: p ? "parsed" : "failed",
    expected_normative_type: MODAL_TO_TYPE[g.modal_class], predicted_normative_type: p?.normative_type || "",
    modal_correct: p ? Number(p.normative_type === MODAL_TO_TYPE[g.modal_class]) : 0,
    citation_applicable: Number(citationApplicable),
    citation_exact: !citationApplicable ? "" : Number(Boolean(p) && p.citation_spec === g.spec_id && p.citation_version === g.version && p.citation_clause === g.clause_id),
    actor_preserved: "", polarity_preserved: "", condition_preserved: "", action_preserved: "", exception_preserved: "",
    complete_preservation: "", unsupported_addition: "", error_codes: "", reviewer_note: "",
  };
});
const autoHeaders = Object.keys(auto[0]);
writeCsv(path.join(runDir, "scores.csv"), auto, autoHeaders);

const shuffled = parsed.map(item => ({
  item,
  order: crypto.createHash("sha256").update(`${path.basename(runDir)}:${item.case_id}:${item.condition}`).digest("hex"),
})).sort((a, b) => a.order.localeCompare(b.order));
const blindKey = {};
const blind = shuffled.map(({ item }, i) => {
  const reviewId = `R${String(i + 1).padStart(3, "0")}`;
  const g = gold.get(item.case_id); const p = item.parsed;
  blindKey[reviewId] = { case_id: item.case_id, condition: item.condition };
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
writeCsv(path.join(runDir, "blind_review.csv"), blind, Object.keys(blind[0]));
fs.writeFileSync(path.join(runDir, "blind_key.json"), JSON.stringify(blindKey, null, 2) + "\n");

const conditions = ["C0", "C1", "C2"];
const summary = { note: "Only schema, modal class, and exact citation are deterministic. Semantic component fields require blind human review." };
for (const c of conditions) {
  const rows = auto.filter(r => r.condition === c);
  summary[c] = {
    n: rows.length,
    parsed: rows.filter(r => r.response_status === "parsed").length,
    modal_accuracy_provisional: rows.reduce((s, r) => s + r.modal_correct, 0) / rows.length,
    citation_exactness_provisional: c === "C0" ? null : rows.reduce((s, r) => s + Number(r.citation_exact), 0) / rows.length,
  };
}
fs.writeFileSync(path.join(runDir, "summary.json"), JSON.stringify(summary, null, 2) + "\n");
console.log(JSON.stringify(summary, null, 2));
