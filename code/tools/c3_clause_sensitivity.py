"""Post-hoc clause-cluster sensitivity of frozen provisional scores, no API."""
import csv, hashlib, json, random
from collections import defaultdict
from pathlib import Path
from summarize_c3_pass1 import verify, quantile
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'experiments/runs/c3_auto72_v1_2026-09-06T04-53-06-942Z/review'

def main():
    verify(P,P/'pass1_freeze_manifest.json')
    verify(ROOT,P/'pass1_package_manifest.json')
    with (ROOT/'data/main_cases.csv').open(encoding='utf-8-sig') as f: gold={r['case_id']:r for r in csv.DictReader(f)}
    with (P/'scores_pass1_unmasked.csv').open(encoding='utf-8-sig') as f: rows=list(csv.DictReader(f))
    score={(r['case_id'],r['condition']):int(r['complete_preservation']) for r in rows}
    groups=defaultdict(list)
    for cid,r in gold.items():groups[(r['spec_id'],r['clause_id'])].append(cid)
    keys=sorted(groups); assert len(keys)==44 and sum(map(len,groups.values()))==72
    out={'status':'POST_HOC_PROVISIONAL_CLUSTER_SENSITIVITY','clusters':len(keys),'cases':72,
         'cluster_unit':'spec_id + clause_id','cluster_size_counts':{},'seed':2026090602,'iterations':20000,
         'method':'Sample 44 clauses with replacement; carry all their paired cases; divide by sampled case count (micro rate). No model or expert uncertainty included.','comparisons':{}}
    for v in groups.values():out['cluster_size_counts'][len(v)]=out['cluster_size_counts'].get(len(v),0)+1
    for first,second in [('C1','C3'),('C3','C2')]:
        stats=[(len(groups[k]),sum(score[(cid,second)]-score[(cid,first)] for cid in groups[k])) for k in keys]
        rng=random.Random(out['seed']);samples=[]
        for _ in range(out['iterations']):
            sample=rng.choices(stats,k=len(keys));samples.append(100*sum(x[1] for x in sample)/sum(x[0] for x in sample))
        samples.sort();total=sum(x[1] for x in stats)
        loo=[{'spec_id':key[0],'clause_id':key[1],'remaining_cases':72-n,'difference_pp':100*(total-d)/(72-n)} for key,(n,d) in zip(keys,stats)]
        out['comparisons'][second+'-'+first]={'difference_pp':100*total/72,'cluster_bootstrap_95ci_pp':[quantile(samples,.025),quantile(samples,.975)],
                    'leave_one_clause_out_range_pp':[min(x['difference_pp'] for x in loo),max(x['difference_pp'] for x in loo)],'leave_one_clause_out':loo}
    dest=ROOT/'outputs/analysis';dest.mkdir(parents=True,exist_ok=True)
    (dest/'c3_clause_sensitivity_pass1.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({**out,'comparisons':{k:{a:b for a,b in v.items() if a!='leave_one_clause_out'} for k,v in out['comparisons'].items()}},indent=2))
if __name__=='__main__':main()
