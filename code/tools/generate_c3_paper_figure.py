"""Scientific figure from provisional per-row scores; no inferred scores."""
import csv
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
with (ROOT/'experiments/runs/c3_auto72_v1_2026-09-06T04-53-06-942Z/review/scores_pass1_unmasked.csv').open(encoding='utf-8-sig') as f: rows=list(csv.DictReader(f))
mods=['shall','shall_not','should','should_not','may','can']; arms=['C1','C2','C3']
counts=np.array([[sum(int(r['complete_preservation']) for r in rows if r['gold_modal_class']==m and r['condition']==c) for c in arms] for m in mods])
assert counts.sum(axis=0).tolist()==[61,71,65]
plt.rcParams.update({'font.size':8,'font.family':'DejaVu Sans'})
fig,ax=plt.subplots(figsize=(3.2,2.28),dpi=300)
ax.imshow(counts,vmin=0,vmax=12,cmap='Blues',aspect='auto')
ax.set_xticks(range(3),['C1 source','C2 oracle','C3 auto'])
ax.set_yticks(range(6),[m.replace('_',' ') for m in mods]);ax.tick_params(length=0)
for i in range(6):
 for j in range(3):ax.text(j,i,f'{counts[i,j]}/12',ha='center',va='center',color='white' if counts[i,j]>=9 else 'black',fontsize=8)
for s in ax.spines.values():s.set_visible(False)
fig.subplots_adjust(left=.24,right=.99,top=.98,bottom=.13)
out=ROOT/'outputs/paper/modal_preservation_paper_v3.png';fig.savefig(out,dpi=300);plt.close(fig)
print(counts.tolist())
