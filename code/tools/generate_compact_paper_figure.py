"""Generate the compact scientific result figure using the project plotting runtime."""
from pathlib import Path
import csv
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs/paper/ACK2026_3GPP_normative_fidelity_draft_v2.docx"

# Rebuild the same matrix at its actual column width; the v1 embedded crop
# retained fragments of a clipped y-axis label.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
score_path = ROOT / 'experiments/runs/main72_v3_2026-09-03T07-35-49-603Z/human_scores_adjudicated.csv'
with score_path.open(encoding='utf-8-sig', newline='') as handle:
    scores = list(csv.DictReader(handle))
modals = ['shall', 'shall_not', 'should', 'should_not', 'may', 'can']
matrix = []
for modal in modals:
    row = []
    for condition in ['C0', 'C1', 'C2']:
        sample = [s for s in scores if s['gold_modal_class'] == modal and s['condition'] == condition]
        assert len(sample) == 12
        row.append(sum(s['complete_preservation'] == '1' for s in sample))
    matrix.append(row)
fig, ax = plt.subplots(figsize=(3.2, 2.2))
ax.imshow(matrix, cmap='Blues', vmin=0, vmax=12, aspect='auto')
ax.set_xticks(range(3), ['C0', 'C1', 'C2'], fontsize=8)
ax.set_yticks(range(6), [m.replace('_', ' ') for m in modals], fontsize=8)
for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        ax.text(j, i, f'{value}/12', ha='center', va='center', fontsize=8,
                color='white' if value >= 8 else '#171717')
ax.set_xticks(np.arange(-.5, 3, 1), minor=True)
ax.set_yticks(np.arange(-.5, 6, 1), minor=True)
ax.grid(which='minor', color='white', linewidth=1)
ax.tick_params(which='both', length=0)
fig.subplots_adjust(left=.25, right=.98, top=.98, bottom=.12)
chart = OUTPUT.with_name('modal_preservation_paper_v2.png')
fig.savefig(chart, dpi=300)
plt.close(fig)
