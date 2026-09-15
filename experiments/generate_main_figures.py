#!/usr/bin/env python3
import csv
import datetime
import json
import math
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/3gpp-normative-fidelity-mpl")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "experiments/runs/main72_v3_2026-09-03T07-35-49-603Z"
SCORES = RUN / "human_scores_adjudicated.csv"
ANALYSIS = RUN / "analysis_adjudicated.json"
FIG_DIR = ROOT / "paper/figures"
TABLE_DIR = ROOT / "paper/tables"
FIG_DIR.mkdir(parents=True, exist_ok=True)
TABLE_DIR.mkdir(parents=True, exist_ok=True)

BLUE, GOLD, ORANGE = "#2563A6", "#C4931D", "#D66A2C"
INK, GRID, PALE = "#20252B", "#D9DEE5", "#F6F7F9"
COLORS = ["#BFC7D1", GOLD, BLUE]
HATCHES = ["///", "xx", "..."]
CONDITIONS = ["C0", "C1", "C2"]
MODALS = ["shall", "shall_not", "should", "should_not", "may", "can"]
MODAL_LABELS = ["shall", "shall not", "should", "should not", "may", "can"]

font_candidates = [
    "/Library/Fonts/Arial Unicode.ttf",
    "/System/Library/Fonts/AppleSDGothicNeo.ttc",
    "/Library/Fonts/NanumGothic.ttf",
]
for candidate in font_candidates:
    if Path(candidate).exists():
        font_manager.fontManager.addfont(candidate)
        plt.rcParams["font.family"] = font_manager.FontProperties(fname=candidate).get_name()
        break
plt.rcParams.update({
    "font.size": 9,
    "axes.titlesize": 12,
    "axes.labelsize": 9,
    "axes.edgecolor": INK,
    "axes.labelcolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "text.color": INK,
    "pdf.fonttype": 42,
    "svg.fonttype": "none",
    "svg.hashsalt": "3gpp-normative-fidelity-main72-v1",
})

with SCORES.open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
with ANALYSIS.open(encoding="utf-8") as f:
    recorded = json.load(f)

if len(rows) != 216:
    raise RuntimeError(f"Expected 216 rows, got {len(rows)}")
identities = {(r["case_id"], r["condition"]) for r in rows}
if len(identities) != 216:
    raise RuntimeError("Duplicate or missing case-condition identities")
for condition in CONDITIONS:
    selected = [r for r in rows if r["condition"] == condition]
    if len(selected) != 72:
        raise RuntimeError(f"Expected 72 rows for {condition}")

def wilson(successes, n, z=1.959963984540054):
    p = successes / n
    z2 = z * z
    d = 1 + z2 / n
    center = (p + z2 / (2 * n)) / d
    half = z * math.sqrt((p * (1 - p) + z2 / (4 * n)) / n) / d
    return max(0, center - half), min(1, center + half)

def save_all(fig, stem):
    for suffix in ("png", "pdf", "svg"):
        if suffix == "png":
            kwargs = {"dpi": 300, "metadata": {"Software": "3gpp-normative-fidelity/generate_main_figures.py"}}
        elif suffix == "pdf":
            fixed = datetime.datetime(2026, 9, 4, tzinfo=datetime.timezone.utc)
            kwargs = {"metadata": {"Creator": "3gpp-normative-fidelity/generate_main_figures.py", "CreationDate": fixed, "ModDate": fixed}}
        else:
            kwargs = {"metadata": {"Creator": "3gpp-normative-fidelity/generate_main_figures.py", "Date": "2026-09-04"}}
        output_path = FIG_DIR / f"{stem}.{suffix}"
        fig.savefig(output_path, bbox_inches="tight", facecolor="white", **kwargs)
        if suffix == "svg":
            normalized = "\n".join(line.rstrip() for line in output_path.read_text(encoding="utf-8").splitlines()) + "\n"
            output_path.write_text(normalized, encoding="utf-8")
    plt.close(fig)

def condition_rows(condition):
    return [r for r in rows if r["condition"] == condition]

# Independent calculation and reconciliation against the saved analysis.
overall = []
for condition in CONDITIONS:
    selected = condition_rows(condition)
    successes = sum(r["complete_preservation"] == "1" for r in selected)
    lo, hi = wilson(successes, len(selected))
    saved = recorded["conditions"][condition]["complete_preservation"]
    if successes != saved["successes"] or len(selected) != saved["n"]:
        raise RuntimeError(f"Saved analysis mismatch for {condition}")
    if max(abs(lo - saved["wilson_95"][0]), abs(hi - saved["wilson_95"][1])) > 1e-12:
        raise RuntimeError(f"Wilson interval mismatch for {condition}")
    overall.append((successes, len(selected), successes / len(selected), lo, hi))

# Figure 1: overall rate with Wilson intervals.
fig, ax = plt.subplots(figsize=(5.5, 3.45))
x = np.arange(3)
rates = np.array([x[2] for x in overall]) * 100
lower = rates - np.array([x[3] for x in overall]) * 100
upper = np.array([x[4] for x in overall]) * 100 - rates
bars = ax.bar(x, rates, width=0.58, color=COLORS, edgecolor=INK, linewidth=0.8)
for bar, hatch in zip(bars, HATCHES): bar.set_hatch(hatch)
ax.errorbar(x, rates, yerr=np.vstack([lower, upper]), fmt="none", ecolor=INK, elinewidth=1.0, capsize=4)
for i, (successes, n, rate, _, _) in enumerate(overall):
    y = min(rate * 100 + 4.5, 106)
    ax.text(i, y, f"{successes}/{n}\n({rate*100:.1f}%)", ha="center", va="bottom", fontsize=9, fontweight="bold")
ax.set_title("Complete preservation by generation condition", loc="left", y=1.105, pad=0, fontweight="bold")
ax.text(0, 1.035, "Adjudicated main set; Wilson 95% CI; n=72 per condition", transform=ax.transAxes, ha="left", va="bottom", fontsize=8, color="#59636E")
ax.set_ylabel("Complete preservation (%)")
ax.set_xticks(x, ["C0\nQuestion only", "C1\nSource clause", "C2\nStructured constraint"])
ax.set_ylim(0, 112)
ax.set_yticks(np.arange(0, 101, 20))
ax.grid(axis="y", color=GRID, linewidth=0.7)
ax.set_axisbelow(True)
ax.spines[["top", "right"]].set_visible(False)
ax.text(0, -0.24, "C2 reached the ceiling; results reflect one model snapshot and same-reviewer adjudication.", transform=ax.transAxes, fontsize=7.5, color="#59636E")
fig.subplots_adjust(bottom=0.27, top=0.79, left=0.13, right=0.98)
save_all(fig, "figure1_overall_complete_preservation")

# Figure 2: balanced modal-class matrix.
matrix = np.zeros((len(MODALS), len(CONDITIONS)))
counts = np.zeros_like(matrix, dtype=int)
denoms = np.zeros_like(matrix, dtype=int)
for i, modal in enumerate(MODALS):
    for j, condition in enumerate(CONDITIONS):
        selected = [r for r in rows if r["gold_modal_class"] == modal and r["condition"] == condition]
        denoms[i, j] = len(selected)
        counts[i, j] = sum(r["complete_preservation"] == "1" for r in selected)
        if len(selected) != 12:
            raise RuntimeError(f"Unbalanced cell {modal}/{condition}: {len(selected)}")
        matrix[i, j] = 100 * counts[i, j] / len(selected)
fig, ax = plt.subplots(figsize=(5.5, 4.05))
im = ax.imshow(matrix, cmap=matplotlib.colors.LinearSegmentedColormap.from_list("blue_scale", ["#F5F7FA", "#9FC1E3", BLUE]), vmin=0, vmax=100, aspect="auto")
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        color = "white" if matrix[i, j] >= 65 else INK
        ax.text(j, i, f"{counts[i,j]}/{denoms[i,j]}\n{matrix[i,j]:.0f}%", ha="center", va="center", color=color, fontsize=8.5, fontweight="bold")
ax.set_title("Complete preservation by modal class", loc="left", y=1.105, pad=0, fontweight="bold")
ax.text(0, 1.035, "Balanced cells; n=12 per modal class and condition", transform=ax.transAxes, ha="left", va="bottom", fontsize=8, color="#59636E")
ax.set_xticks(np.arange(3), CONDITIONS)
ax.set_yticks(np.arange(6), MODAL_LABELS)
ax.set_xlabel("Generation condition")
ax.set_ylabel("Frozen gold modal class")
ax.set_xticks(np.arange(-.5, 3, 1), minor=True)
ax.set_yticks(np.arange(-.5, 6, 1), minor=True)
ax.grid(which="minor", color="white", linewidth=1.5)
ax.tick_params(which="minor", bottom=False, left=False)
cbar = fig.colorbar(im, ax=ax, fraction=0.045, pad=0.04)
cbar.set_label("Complete preservation (%)")
fig.subplots_adjust(left=0.22, right=0.9, top=0.79, bottom=0.13)
save_all(fig, "figure2_modal_complete_preservation")

# Figure 3: component failure rates, with each applicable denominator shown.
fields = ["actor_preserved", "polarity_preserved", "condition_preserved", "action_preserved", "exception_preserved", "unsupported_addition"]
labels = ["Actor", "Normative\nforce", "Condition", "Action", "Exception", "Unsupported\naddition"]
failure_rates = np.zeros((3, len(fields)))
failure_counts = np.zeros_like(failure_rates, dtype=int)
applicable_ns = np.zeros_like(failure_rates, dtype=int)
for ci, condition in enumerate(CONDITIONS):
    selected = condition_rows(condition)
    for fi, field in enumerate(fields):
        if field == "unsupported_addition":
            applicable = selected
            failures = sum(r[field] == "1" for r in applicable)
        else:
            applicable = [r for r in selected if r[field] != "NA"]
            failures = sum(r[field] == "0" for r in applicable)
        failure_counts[ci, fi] = failures
        applicable_ns[ci, fi] = len(applicable)
        failure_rates[ci, fi] = 100 * failures / len(applicable) if applicable else 0
fig, ax = plt.subplots(figsize=(7.2, 3.8))
x = np.arange(len(fields)); width = 0.24
for ci, condition in enumerate(CONDITIONS):
    bars = ax.bar(x + (ci - 1) * width, failure_rates[ci], width=width, color=COLORS[ci], edgecolor=INK, linewidth=0.7, hatch=HATCHES[ci], label=condition)
    for fi, bar in enumerate(bars):
        value = failure_rates[ci, fi]
        if value > 0:
            ax.text(bar.get_x()+bar.get_width()/2, value+1.4, f"{failure_counts[ci,fi]}/{applicable_ns[ci,fi]}", ha="center", va="bottom", fontsize=6.8, rotation=90)
ax.set_title("Semantic-component failure rates", loc="left", y=1.16, pad=0, fontweight="bold")
ax.text(0, 1.09, "Failure count/applicable n shown; unsupported addition uses n=72", transform=ax.transAxes, ha="left", va="bottom", fontsize=8, color="#59636E")
ax.set_ylabel("Failure rate (%)")
ax.set_xticks(x, labels)
ax.set_ylim(0, 118)
ax.set_yticks(np.arange(0, 101, 20))
ax.grid(axis="y", color=GRID, linewidth=0.7)
ax.set_axisbelow(True)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False, ncol=3, loc="lower right", bbox_to_anchor=(1, 1.075), borderaxespad=0)
fig.subplots_adjust(left=0.09, right=0.99, top=0.75, bottom=0.18)
save_all(fig, "figure3_semantic_component_failures")

# Exact paper tables and C1 failures.
paired = recorded["comparisons"]
def pct(v): return f"{100*v:.2f}%"
def pp(v): return f"{100*v:.2f} pp"
lines = [
    "# Main experiment result tables", "",
    "> Source: `human_scores_adjudicated.csv`. Pass 1, delayed pass 2, and adjudication were performed by the same Codex reviewer; this is not independent expert validation.", "",
    "## Table 1. Overall results", "",
    "| Condition | JSON modal label accuracy | Explanation complete preservation | Unsupported addition | Citation ID exactness |", "|---|---:|---:|---:|---:|",
]
for condition in CONDITIONS:
    s = recorded["conditions"][condition]
    citation = s["citation_exact"]
    lines.append(f"| {condition} | {s['modal_correct']['successes']}/{s['modal_correct']['n']} ({pct(s['modal_correct']['rate'])}) | {s['complete_preservation']['successes']}/{s['complete_preservation']['n']} ({pct(s['complete_preservation']['rate'])}) | {s['unsupported_addition']['successes']}/{s['unsupported_addition']['n']} ({pct(s['unsupported_addition']['rate'])}) | " + (f"{citation['successes']}/{citation['n']} ({pct(citation['rate'])})" if citation else "N/A") + " |")
lines += ["", "## Table 2. Paired complete-preservation comparisons", "", "| Comparison | Difference | Paired bootstrap 95% CI | First-only / second-only | Exact McNemar p |", "|---|---:|---:|---:|---:|"]
for key in ["C0_vs_C1", "C1_vs_C2", "C0_vs_C2"]:
    x = paired[key]["complete_preservation"]
    lines.append(f"| {key.replace('_vs_', ' vs ')} | {pp(x['rate_difference_second_minus_first'])} | {pp(x['paired_bootstrap_95'][0])} to {pp(x['paired_bootstrap_95'][1])} | {x['discordant_first_only']} / {x['discordant_second_only']} | {x['exact_mcnemar_two_sided_p']:.6g} |")
lines += ["", "## Table 3. C1 complete-preservation failures", "", "| Case | Modal | Failed fields | Unsupported addition |", "|---|---|---|---:|"]
for r in sorted([r for r in rows if r["condition"] == "C1" and r["complete_preservation"] == "0"], key=lambda x: x["case_id"]):
    failed = [name for name, field in [("actor","actor_preserved"),("force","polarity_preserved"),("condition","condition_preserved"),("action","action_preserved"),("exception","exception_preserved")] if r[field] == "0"]
    lines.append(f"| `{r['case_id']}` | `{r['gold_modal_class']}` | {', '.join(failed)} | {r['unsupported_addition']} |")
lines += ["", "## Reporting boundary", "", "- C2 receives the gold structured fields; 72/72 is not evidence of automatic extraction or perfect general performance.", "- JSON modal labels and Korean explanation judgments have different evaluation targets. See docs/09_reporting_errata_2026-09-06.md.", "- Retrieval was not evaluated; citation exactness checks supplied identifier copying.", "- Three gold-scope cases were recorded after pass 1 and before delayed pass 2. Excluding them: C1 65/69, C2 69/69, difference +5.80 pp, exact McNemar p=0.125.", ""]
(TABLE_DIR / "main_results.md").write_text("\n".join(lines), encoding="utf-8")

print(json.dumps({
    "status": "PASS",
    "rows": len(rows),
    "overall_complete": {c: {"successes": overall[i][0], "n": overall[i][1]} for i, c in enumerate(CONDITIONS)},
    "c1_failures": sum(r["condition"] == "C1" and r["complete_preservation"] == "0" for r in rows),
    "figures": sorted(p.name for p in FIG_DIR.iterdir()),
    "table": str(TABLE_DIR / "main_results.md"),
}, ensure_ascii=False, indent=2))
