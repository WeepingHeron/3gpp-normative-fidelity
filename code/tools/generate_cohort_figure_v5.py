from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
ROOT=Path.cwd()
BASE=ROOT/"outputs/paper"
EVIDENCE=ROOT/"outputs/review/v2_cohort_analysis_20260909"
records=[json.loads(x) for x in (EVIDENCE/"condition_results.jsonl").read_text().splitlines()]
# Figure bounds are recomputed from sealed counts, not entered by hand.
cohorts=['PRIMARY_STRICT_49','SENS_GOLD_50','SENS_EXCEPTION_50','SENS_GOLD_EXCEPTION_51']
fig,ax=plt.subplots(figsize=(3.2,1.65),dpi=320)
for i,cohort in enumerate(cohorts):
    c={x['condition']:x for x in records if x['cohort']==cohort}
    lo=100*(c['C2']['PASS']-c['C1']['PASS']-c['C1']['UNRESOLVED'])/c['C1']['n']
    hi=100*(c['C2']['PASS']+c['C2']['UNRESOLVED']-c['C1']['PASS'])/c['C1']['n']
    ax.plot([lo,hi],[i,i],color='black',linewidth=2,marker='|',markersize=7)
    ax.text(hi+0.25,i,f'{lo:.2f}–{hi:.2f}',va='center',fontsize=7)
ax.set_yticks(range(4),['Primary 49','Gold 50','Exception 50','Both 51'],fontsize=8)
ax.invert_yaxis();ax.set_ylim(3.55,-.55);ax.set_xlim(0,24)
ax.set_xticks([0,5,10,15,20]);ax.tick_params(axis='x',labelsize=7)
ax.set_xlabel('C2 − C1 (percentage points)',fontsize=8,labelpad=3)
ax.spines[['top','right']].set_visible(False)
ax.grid(axis='x',color='.9',linewidth=.5);ax.set_axisbelow(True)
fig.subplots_adjust(left=.27,right=.99,top=.97,bottom=.25)
chart=BASE/'cohort_bounds_paper_v5.png';fig.savefig(chart,dpi=320);plt.close(fig)
