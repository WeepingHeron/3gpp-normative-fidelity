"""Validate manual C1M judgments, compare paired scores, and prepare empty delayed review."""
import hashlib, json, random
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from summarize_c3_pass1 import csv_rows, write_csv, verify, paired, wilson, quantile, FIELDS, EXCLUDED
ROOT=Path(__file__).resolve().parents[1]
RUN=ROOT/'experiments/runs/c1m_main72_v1_2026-09-06T05-26-29-574Z'; P=RUN/'review'
MAIN=ROOT/'experiments/runs/main72_v3_2026-09-03T07-35-49-603Z'
C3=ROOT/'experiments/runs/c3_auto72_v1_2026-09-06T04-53-06-942Z/review/delayed_pass2'

def cluster(rows,gold,first,second):
    score={(r['case_id'],r['condition']):int(r['complete_preservation']) for r in rows}
    groups=defaultdict(list)
    for cid,g in gold.items():groups[(g['spec_id'],g['clause_id'])].append(cid)
    stats=[(len(groups[k]),sum(score[(cid,second)]-score[(cid,first)] for cid in groups[k])) for k in sorted(groups)]
    rng=random.Random(2026090602); boot=[]
    for _ in range(20000):
        draw=rng.choices(stats,k=len(stats));boot.append(100*sum(d for n,d in draw)/sum(n for n,d in draw))
    boot.sort()
    return {'clusters':len(groups),'iterations':20000,'seed':2026090602,'cluster_bootstrap_95ci_pp':[quantile(boot,.025),quantile(boot,.975)]}

def main():
    for base,manifest in [(ROOT,ROOT/'data/main_freeze_manifest.json'),(ROOT,RUN/'input_freeze_manifest.json'),
                          (RUN,RUN/'output_freeze_manifest.json'),(MAIN,MAIN/'output_freeze_manifest.json'),
                          (P,P/'review_manifest.json'),(P,P/'pass1_freeze_manifest.json'),(C3,C3/'adjudicated_freeze_manifest.json')]:verify(base,manifest)
    rows=csv_rows(P/'blind_explanations_pass1.csv');key=json.loads((P/'blind_key.json').read_text())
    gold={r['case_id']:r for r in csv_rows(ROOT/'data/main_cases.csv')}
    raw=[json.loads(s) for p in (MAIN,RUN) for s in (p/'parsed_responses.jsonl').read_text().splitlines()]
    response={(r['case_id'],r['condition']):r for r in raw}
    for r in rows:
        r.update(key[r['review_id']]);g=gold[r['case_id']]
        assert r['source_text_en']==g['source_text_en']
        assert r['explanation_ko']==(response[(r['case_id'],r['condition'])]['parsed'] or {}).get('explanation_ko','')
        assert int(r['complete_preservation'])==int(all(r[f] in ('1','NA') for f in FIELDS[:5]) and r[FIELDS[5]]=='0')
    assert len(rows)==216 and {(r['case_id'],r['condition']) for r in rows}=={(g,c) for g in gold for c in ('C1','C2','C1M')}
    canonical={(r['case_id'],r['condition']):r for r in csv_rows(C3/'scores_adjudicated.csv')}
    changed=[]
    for r in rows:
        if r['condition']=='C1M':continue
        o=canonical[(r['case_id'],r['condition'])]
        assert r['explanation_ko']==o['explanation_ko']
        for f in FIELDS:
            if r[f]!=o[f]:changed.append({'case_id':r['case_id'],'condition':r['condition'],'field':f,'c3_adjudicated':o[f],'c1m_pass1':r[f]})
    conditions={}
    for c in ('C1','C2','C1M'):
        arm=[r for r in rows if r['condition']==c];n=len(arm);k=sum(int(r['complete_preservation']) for r in arm)
        conditions[c]={'n':n,'complete':k,'complete_pct':100*k/n,'wilson_95ci_pct':wilson(k,n),
                       'unsupported_additions':sum(int(r['unsupported_addition']) for r in arm),
                       'components':{f:{'success':sum(r[f]=='1' for r in arm),'denominator':sum(r[f]!='NA' for r in arm)} for f in FIELDS[:5]},
                       'failed_case_ids':sorted(r['case_id'] for r in arm if r['complete_preservation']=='0')}
    s={'status':'PROVISIONAL_CODEX_C1M_PASS1_NOT_INDEPENDENT_EXPERT_VALIDATION','created_at':datetime.now(timezone.utc).isoformat(),
       'conditions':conditions,'C1_C2_differences_from_C3_delayed_adjudication':changed,
       'primary_C1_C1M_all72':paired(rows,'C1','C1M'),'primary_C1_C1M_excluding_original3':paired(rows,'C1','C1M',EXCLUDED),
       'secondary_C1M_C2_all72':paired(rows,'C1M','C2'),'secondary_C1M_C2_excluding_original3':paired(rows,'C1M','C2',EXCLUDED),
       'post_hoc_cluster_sensitivity':{'C1M-C1':cluster(rows,gold,'C1','C1M'),'C2-C1M':cluster(rows,gold,'C1M','C2')},
       'caveats':['C1M first review only; delayed review remains. C1/C2 were recently reviewed by the same Codex.',
                  'C1M is an oracle modal/polarity hint, not automatic extraction or new-clause generalization.',
                  'C1/C2 generated September 3; C1M September 6. Same model/settings do not remove all time/order effects.',
                  'C2 and C1M differ in original instructions as well as other structured fields; no pure field-level causal claim.',
                  'Non-significance is not proof of equivalence. Original-three exclusion cannot replace the full 72-case analysis.']}
    write_csv(P/'scores_pass1_unmasked.csv',rows)
    write_csv(P/'failures_pass1.csv',[r for r in rows if r['condition']=='C1M' and r['complete_preservation']=='0'])
    (P/'summary_pass1.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
    # New shuffled blank material, never copy reviewed scores or notes into pass 2.
    blanks=csv_rows(P/'blind_explanations_blank.csv')
    blanks.sort(key=lambda r:hashlib.sha256(('c1m-delayed-v1:'+r['review_id']).encode()).hexdigest())
    delayed=P/'delayed_pass2';delayed.mkdir(exist_ok=False);dkey={}
    for i,r in enumerate(blanks,1):
        rid=f'H{i:03d}';dkey[rid]=key[r['review_id']];r['review_id']=rid
        assert all(not r[f] for f in FIELDS+['complete_preservation','error_codes','reviewer_note'])
    write_csv(delayed/'blind_explanations_pass2_blank.csv',blanks)
    (delayed/'blind_key.json').write_text(json.dumps(dkey,ensure_ascii=False,indent=2)+'\n')
    earliest=json.loads((P/'pass1_freeze_manifest.json').read_text())['pass2_not_before']
    (delayed/'README.md').write_text(f'# C1M 지연 의미 검토\n\n준비만 완료했으며 의미 점수 216행은 모두 공란이다. {earliest} UTC offset 시각 이후에만 재검토한다. 조건 키·첫 평가 행별 점수와 근거를 열기 전에 전수 채점을 기록하고 동결한다. 같은 Codex의 지연 재검토이며 독립 전문가 검증이 아니다. 예약이나 자동 실행은 설정하지 않았다.\n')
    fs=['blind_explanations_pass2_blank.csv','blind_key.json','README.md']
    (delayed/'preparation_manifest.json').write_text(json.dumps({'status':'PREPARED_NOT_REVIEWED','prepared_at':datetime.now(timezone.utc).isoformat(),'not_before':earliest,'rows':216,'file_sha256':{f:hashlib.sha256((delayed/f).read_bytes()).hexdigest() for f in fs}},indent=2)+'\n')
    print(json.dumps(s,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
