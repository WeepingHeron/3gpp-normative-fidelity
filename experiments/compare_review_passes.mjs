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
  const clean = header.map(h => h.replace(/^\uFEFF/, ""));
  return body.map(r => Object.fromEntries(clean.map((h, i) => [h, r[i] ?? ""])));
}
function csvCell(v) { const s = String(v ?? ""); return /[",\n]/.test(s) ? `"${s.replaceAll('"', '""')}"` : s; }
function normalizeCodes(value) { return String(value || "").split(";").filter(Boolean).sort().join(";"); }
function kappa(pairs) {
  if (!pairs.length) return null;
  const labels = [...new Set(pairs.flat())];
  const observed = pairs.filter(([a, b]) => a === b).length / pairs.length;
  let expected = 0;
  for (const label of labels) {
    expected += (pairs.filter(([a]) => a === label).length / pairs.length) *
      (pairs.filter(([, b]) => b === label).length / pairs.length);
  }
  return expected === 1 ? null : (observed - expected) / (1 - expected);
}

const runDir = path.resolve(process.argv[2] || "");
if (!runDir || !fs.existsSync(runDir)) throw new Error("Usage: node experiments/compare_review_passes.mjs <run_directory>");
const pass1 = parseCsv(fs.readFileSync(path.join(runDir, "blind_review_pass1.csv"), "utf8"));
const pass2 = parseCsv(fs.readFileSync(path.join(runDir, "blind_review_pass2.csv"), "utf8"));
const key1 = JSON.parse(fs.readFileSync(path.join(runDir, "blind_key.json"), "utf8"));
const key2 = JSON.parse(fs.readFileSync(path.join(runDir, "blind_key_pass2.json"), "utf8"));
const identity = x => `${x.case_id}:${x.condition}`;
const index = (rows, key) => new Map(rows.map(r => [identity(key[r.review_id]), r]));
const a = index(pass1, key1); const b = index(pass2, key2);
const scoreFields = ["actor_preserved", "polarity_preserved", "condition_preserved", "action_preserved", "exception_preserved", "complete_preservation", "unsupported_addition"];
const compareFields = [...scoreFields, "error_codes"];
const cases = [...a.keys()].sort();
const disagreements = [];
const fieldStats = {};
for (const field of compareFields) {
  const pairs = cases.map(id => {
    const av = field === "error_codes" ? normalizeCodes(a.get(id)[field]) : a.get(id)[field];
    const bv = field === "error_codes" ? normalizeCodes(b.get(id)[field]) : b.get(id)[field];
    return [av, bv];
  });
  fieldStats[field] = {
    agreements: pairs.filter(([x, y]) => x === y).length,
    total: pairs.length,
    agreement_rate: pairs.filter(([x, y]) => x === y).length / pairs.length,
    cohen_kappa: field === "error_codes" ? null : kappa(pairs.filter(([x, y]) => x !== "NA" && y !== "NA")),
  };
}
for (const id of cases) {
  const [case_id, condition] = id.split(":");
  for (const field of compareFields) {
    const av = field === "error_codes" ? normalizeCodes(a.get(id)[field]) : a.get(id)[field];
    const bv = field === "error_codes" ? normalizeCodes(b.get(id)[field]) : b.get(id)[field];
    if (av !== bv) disagreements.push({ case_id, condition, field, pass1: av, pass2: bv, adjudicated: "", rationale: "" });
  }
}
const responseExact = cases.filter(id => compareFields.every(field => {
  const av = field === "error_codes" ? normalizeCodes(a.get(id)[field]) : a.get(id)[field];
  const bv = field === "error_codes" ? normalizeCodes(b.get(id)[field]) : b.get(id)[field];
  return av === bv;
})).length;
const binaryPairs = cases.flatMap(id => scoreFields.map(field => [a.get(id)[field], b.get(id)[field]])).filter(([x, y]) => x !== "NA" && y !== "NA");
const report = {
  comparison_type: "delayed_intra_rater_agreement",
  pass1_file: "blind_review_pass1.csv",
  pass2_file: "blind_review_pass2.csv",
  responses: cases.length,
  response_level_exact_agreement: { agreements: responseExact, total: cases.length, rate: responseExact / cases.length },
  field_level: fieldStats,
  aggregate_applicable_binary_decisions: {
    agreements: binaryPairs.filter(([x, y]) => x === y).length,
    total: binaryPairs.length,
    rate: binaryPairs.filter(([x, y]) => x === y).length / binaryPairs.length,
    cohen_kappa: kappa(binaryPairs),
  },
  disagreement_count: disagreements.length,
  interpretation_note: "This is same-reviewer delayed agreement, not independent inter-rater reliability.",
};
fs.writeFileSync(path.join(runDir, "review_agreement.json"), JSON.stringify(report, null, 2) + "\n");
const headers = ["case_id", "condition", "field", "pass1", "pass2", "adjudicated", "rationale"];
fs.writeFileSync(path.join(runDir, "adjudication.csv"), "\uFEFF" + [headers.join(","), ...disagreements.map(r => headers.map(h => csvCell(r[h])).join(","))].join("\n") + "\n");
console.log(JSON.stringify(report, null, 2));
