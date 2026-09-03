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

function wilson(successes, n, z = 1.959963984540054) {
  if (!n) return null;
  const p = successes / n, z2 = z * z, d = 1 + z2 / n;
  const center = (p + z2 / (2 * n)) / d;
  const half = z * Math.sqrt((p * (1 - p) + z2 / (4 * n)) / n) / d;
  return [Math.max(0, center - half), Math.min(1, center + half)];
}

function choose(n, k) {
  k = Math.min(k, n - k); let value = 1;
  for (let i = 1; i <= k; i++) value = value * (n - k + i) / i;
  return value;
}

function exactMcNemar(b, c) {
  const n = b + c;
  if (!n) return 1;
  const low = Math.min(b, c);
  let tail = 0;
  for (let k = 0; k <= low; k++) tail += choose(n, k) * 0.5 ** n;
  return Math.min(1, 2 * tail);
}

function lcg(seed) {
  let state = seed >>> 0;
  return () => ((state = (1664525 * state + 1013904223) >>> 0) / 2 ** 32);
}

function pairedBootstrap(a, b, iterations = 20000, seed = 20260903) {
  const random = lcg(seed), n = a.length, values = [];
  for (let r = 0; r < iterations; r++) {
    let delta = 0;
    for (let i = 0; i < n; i++) { const j = Math.floor(random() * n); delta += b[j] - a[j]; }
    values.push(delta / n);
  }
  values.sort((x, y) => x - y);
  return [values[Math.floor(0.025 * iterations)], values[Math.floor(0.975 * iterations)]];
}

const runDir = path.resolve(process.argv[2] || "");
if (!process.argv[2]) throw new Error("Usage: node experiments/analyze_main_pass1.mjs <run_directory>");
const rows = parseCsv(fs.readFileSync(path.join(runDir, "human_scores_pass1.csv"), "utf8"));
if (rows.length !== 216) throw new Error(`Expected 216 rows, got ${rows.length}`);

const byCase = new Map();
for (const row of rows) {
  if (!byCase.has(row.case_id)) byCase.set(row.case_id, {});
  byCase.get(row.case_id)[row.condition] = row;
}
if (byCase.size !== 72 || [...byCase.values()].some(v => !v.C0 || !v.C1 || !v.C2)) throw new Error("Incomplete paired case-condition matrix");

const conditionSummary = {};
for (const condition of ["C0", "C1", "C2"]) {
  const selected = rows.filter(r => r.condition === condition);
  conditionSummary[condition] = {};
  for (const metric of ["modal_correct", "complete_preservation", "unsupported_addition"]) {
    const successes = selected.filter(r => r[metric] === "1").length;
    conditionSummary[condition][metric] = { successes, n: selected.length, rate: successes / selected.length, wilson_95: wilson(successes, selected.length) };
  }
  const citations = selected.filter(r => r.citation_applicable === "1");
  conditionSummary[condition].citation_exact = citations.length ? {
    successes: citations.filter(r => r.citation_exact === "1").length,
    n: citations.length,
    rate: citations.filter(r => r.citation_exact === "1").length / citations.length,
    wilson_95: wilson(citations.filter(r => r.citation_exact === "1").length, citations.length)
  } : null;
}

const comparisons = {};
for (const [first, second] of [["C0", "C1"], ["C1", "C2"], ["C0", "C2"]]) {
  const label = `${first}_vs_${second}`; comparisons[label] = {};
  for (const metric of ["modal_correct", "complete_preservation", "unsupported_addition"]) {
    const a = [], b = [];
    for (const paired of byCase.values()) { a.push(Number(paired[first][metric])); b.push(Number(paired[second][metric])); }
    const firstOnly = a.filter((v, i) => v === 1 && b[i] === 0).length;
    const secondOnly = a.filter((v, i) => v === 0 && b[i] === 1).length;
    comparisons[label][metric] = {
      rate_difference_second_minus_first: b.reduce((s, v) => s + v, 0) / b.length - a.reduce((s, v) => s + v, 0) / a.length,
      paired_bootstrap_95: pairedBootstrap(a, b),
      discordant_first_only: firstOnly,
      discordant_second_only: secondOnly,
      exact_mcnemar_two_sided_p: exactMcNemar(firstOnly, secondOnly)
    };
  }
}

const result = {
  status: "PROVISIONAL_SINGLE_CODEX_REVIEWER_PASS1",
  warning: "Do not use as a final paper result until delayed pass 2 or independent review and disagreement adjudication are complete.",
  run_id: path.basename(runDir),
  cases: byCase.size,
  confidence_interval_methods: { rates: "Wilson score 95%", paired_rate_differences: "20,000 paired bootstrap resamples, fixed LCG seed 20260903" },
  hypothesis_test: "Exact two-sided McNemar test; descriptive/provisional, with no multiple-comparison correction applied.",
  conditions: conditionSummary,
  comparisons
};
fs.writeFileSync(path.join(runDir, "analysis_pass1.json"), JSON.stringify(result, null, 2) + "\n");

const pct = v => `${(100 * v).toFixed(2)}%`;
const lines = [
  "# Provisional main-result analysis: masked pass 1", "",
  "> **Not final.** This analysis uses a masked Codex single-reviewer pass 1. A delayed pass 2 or independent review and adjudication are required before paper reporting.", "",
  "## Condition results", "",
  "| Condition | Modal accuracy | Complete preservation | Unsupported addition | Exact citation |", "|---|---:|---:|---:|---:|"
];
for (const c of ["C0", "C1", "C2"]) {
  const s = conditionSummary[c];
  lines.push(`| ${c} | ${s.modal_correct.successes}/${s.modal_correct.n} (${pct(s.modal_correct.rate)}) | ${s.complete_preservation.successes}/${s.complete_preservation.n} (${pct(s.complete_preservation.rate)}) | ${s.unsupported_addition.successes}/${s.unsupported_addition.n} (${pct(s.unsupported_addition.rate)}) | ${s.citation_exact ? `${s.citation_exact.successes}/${s.citation_exact.n} (${pct(s.citation_exact.rate)})` : "N/A"} |`);
}
lines.push("", "## Paired complete-preservation comparisons", "", "| Comparison | Difference (second - first) | Paired bootstrap 95% CI | Discordant first-only / second-only | Exact McNemar p |", "|---|---:|---:|---:|---:|");
for (const label of ["C0_vs_C1", "C1_vs_C2", "C0_vs_C2"]) {
  const x = comparisons[label].complete_preservation;
  lines.push(`| ${label.replaceAll("_", " ")} | ${pct(x.rate_difference_second_minus_first)} | ${pct(x.paired_bootstrap_95[0])} to ${pct(x.paired_bootstrap_95[1])} | ${x.discordant_first_only} / ${x.discordant_second_only} | ${x.exact_mcnemar_two_sided_p.toPrecision(4)} |`);
}
lines.push("", "## Interpretation boundary", "", "- C2 reached 72/72 in this pass, so ceiling effects and reviewer/gold-label dependence require particular scrutiny.", "- The oracle-evidence design evaluates generation under supplied evidence, not retrieval quality or end-to-end RAG.", "- Three frozen cases use modal-bearing language inside broader descriptive sentences; their gold actor and modal scope should be independently reviewed without changing this frozen run.", "- No causal or general model-performance claim should be made from one model snapshot, one corpus version, and one reviewer pass.", "");
fs.writeFileSync(path.join(runDir, "ANALYSIS_PASS1.md"), lines.join("\n"));
console.log(JSON.stringify({ status: result.status, conditions: result.conditions, complete_preservation_comparisons: Object.fromEntries(Object.entries(result.comparisons).map(([k,v]) => [k,v.complete_preservation])) }, null, 2));
