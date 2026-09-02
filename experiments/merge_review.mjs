import fs from "node:fs";
import path from "node:path";

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

const runDir = path.resolve(process.argv[2] || "");
if (!process.argv[2]) throw new Error("Usage: node experiments/merge_review.mjs <run_directory>");
const auto = parseCsv(fs.readFileSync(path.join(runDir, "scores.csv"), "utf8"));
const pass1 = parseCsv(fs.readFileSync(path.join(runDir, "blind_review_pass1.csv"), "utf8"));
const blindKey = JSON.parse(fs.readFileSync(path.join(runDir, "blind_key.json"), "utf8"));
const annotationByCaseCondition = new Map(pass1.map(r => {
  const key = blindKey[r.review_id];
  if (!key) throw new Error(`Unknown review_id ${r.review_id}`);
  return [`${key.case_id}:${key.condition}`, r];
}));
const merged = auto.map(r => {
  const a = annotationByCaseCondition.get(`${r.case_id}:${r.condition}`);
  if (!a) throw new Error(`Missing annotation for ${r.case_id}:${r.condition}`);
  return { ...r, ...Object.fromEntries(Object.entries(a).filter(([k]) => k !== "review_id")) };
});
writeCsv(path.join(runDir, "human_scores_pass1.csv"), merged, Object.keys(merged[0]));

const summary = {
  status: "single_annotator_pass1_only",
  warning: "Not final. A delayed second pass or independent reviewer is required before reporting research results.",
  conditions: {},
};
for (const condition of ["C0", "C1", "C2"]) {
  const rows = merged.filter(r => r.condition === condition);
  summary.conditions[condition] = {
    n: rows.length,
    modal_accuracy: rows.reduce((s, r) => s + Number(r.modal_correct), 0) / rows.length,
    complete_preservation_rate_pass1: rows.reduce((s, r) => s + Number(r.complete_preservation), 0) / rows.length,
    unsupported_addition_rate_pass1: rows.reduce((s, r) => s + Number(r.unsupported_addition), 0) / rows.length,
    citation_exactness: condition === "C0" ? null : rows.reduce((s, r) => s + Number(r.citation_exact), 0) / rows.length,
  };
}
fs.writeFileSync(path.join(runDir, "summary_pass1.json"), JSON.stringify(summary, null, 2) + "\n");
console.log(JSON.stringify(summary, null, 2));
