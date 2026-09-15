"""Standalone scientific plot from reviewed observations; no DOCX authoring."""
from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs/paper/ACK2026_3GPP_normative_fidelity_draft_v4.docx'

def figure():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    sources=[ROOT/'experiments/runs/c3_auto72_v1_2026-09-06T04-53-06-942Z/review/delayed_pass2/scores_adjudicated.csv',
             ROOT/'experiments/runs/c1m_main72_v1_2026-09-06T05-26-29-574Z/review/scores_pass1_unmasked.csv']
    rows=[]
    for i,p in enumerate(sources):
        with p.open(encoding='utf-8-sig') as f:
            rows.extend(r for r in csv.DictReader(f) if i==0 or r['condition']=='C1M')
    mods=['shall','shall_not','should','should_not','may','can'];arms=['C1','C1M','C2','C3']
    a=np.array([[sum(int(r['complete_preservation']) for r in rows if r['condition']==c and r['gold_modal_class']==m) for c in arms] for m in mods])
    assert a.sum(axis=0).tolist()==[61,68,71,65]
    plt.rcParams.update({'font.size':8,'font.family':'DejaVu Sans'})
    fig,ax=plt.subplots(figsize=(3.2,2.28),dpi=300)
    ax.imshow(a,vmin=0,vmax=12,cmap='Blues',aspect='auto')
    ax.set_xticks(range(4),['C1','C1M*','C2','C3']);ax.set_yticks(range(6),[m.replace('_',' ') for m in mods]);ax.tick_params(length=0)
    for i in range(6):
        for j in range(4):ax.text(j,i,f'{a[i,j]}/12',ha='center',va='center',color='white' if a[i,j]>=9 else 'black',fontsize=8)
    for s in ax.spines.values():s.set_visible(False)
    fig.subplots_adjust(left=.24,right=.99,top=.98,bottom=.13)
    target=OUT.with_name('modal_preservation_paper_v4.png');fig.savefig(target,dpi=300);plt.close(fig)
    return target

if __name__=='__main__':print(figure())
