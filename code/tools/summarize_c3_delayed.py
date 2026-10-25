"""Validate frozen delayed judgments and apply explicit adjudication only."""
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from summarize_c3_pass1 import csv_rows, write_csv, verify, paired, wilson, FIELDS, EXCLUDED
from semantic_review_io import assemble
ROOT=Path(__file__).resolve().parents[1]
RUN=ROOT/'experiments/runs/c3_auto72_v1_2026-09-06T04-53-06-942Z'
P=RUN/'review'; D=P/'delayed_pass2'

def agreement(pairs):
    n=len(pairs); same=sum(a==b for a,b in pairs)
    a=sum(int(x) for x,y in pairs)/n; b=sum(int(y) for x,y in pairs)/n
    pe=a*b+(1-a)*(1-b); po=same/n
    return {'n':n,'agree':same,'agreement_pct':100*po,'cohen_kappa':(po-pe)/(1-pe) if pe!=1 else None}

def main():
    for base,manifest in [(ROOT,ROOT/'data/main_freeze_manifest.json'),(ROOT,RUN/'input_freeze_manifest.json'),
                          (RUN,RUN/'output_freeze_manifest.json'),(P,P/'pass1_freeze_manifest.json'),
                          (ROOT,P/'pass1_package_manifest.json'),(D,D/'preparation_manifest.json'),(D,D/'pass2_freeze_manifest.json')]:
        verify(base,manifest)
    m1=json.loads((P/'pass1_freeze_manifest.json').read_text());m2=json.loads((D/'pass2_freeze_manifest.json').read_text())
    assert datetime.fromisoformat(m2['completed_at'])>=datetime.fromisoformat(m1['pass2_not_before'])
    k1=json.loads((P/'blind_key.json').read_text());k2=json.loads((D/'blind_key.json').read_text())
    p1={tuple(k1[r['review_id']][f] for f in ('case_id','condition')):r for r in csv_rows(P/'blind_explanations_pass1.csv')}
    p2=csv_rows(D/'blind_explanations_pass2.csv');gold={r['case_id']:r for r in csv_rows(ROOT/'data/main_cases.csv')}
    assert len(p2)==216
    changes=[]; expected=set(); applicable=[]; whole=[]
    for r in p2:
        key=k2[r['review_id']];old=p1[(key['case_id'],key['condition'])]
        assert all(r[f]==old[f] for f in ['source_text_en','explanation_ko','gold_actor','gold_condition','gold_action','gold_exception'])
        whole.append((old['complete_preservation'],r['complete_preservation']))
        for f in FIELDS:
            assert (old[f]=='NA')==(r[f]=='NA')
            if r[f]!='NA':applicable.append((old[f],r[f]))
            if old[f]!=r[f]:
                expected.add(r['review_id'])
                changes.append({'review_id':r['review_id'],**key,'field':f,'pass1':old[f],'pass2':r[f]})
    adjudications={line.split('\t')[0]:line for line in (D/'adjudication_decisions.tsv').read_text().splitlines() if line and not line.startswith('#')}
    assert set(adjudications)==expected
    decisions={line.split('\t')[0]:line for line in (D/'pass2_decisions.tsv').read_text().splitlines() if line and not line.startswith('#')}
    decisions.update(adjudications)
    decisionfile=D/'adjudicated_decisions.tsv'
    decisionfile.write_text('\n'.join(decisions[r['review_id']] for r in p2)+'\n')
    assembled=D/'blind_explanations_adjudicated.csv'
    assemble(D/'blind_explanations_pass2_blank.csv',decisionfile,assembled)
    final=csv_rows(assembled)
    for r in final:r.update(k2[r['review_id']])
    assert {(r['case_id'],r['condition']) for r in final}=={(g,c) for g in gold for c in ('C1','C2','C3')}
    finalby={r['review_id']:r for r in final}
    for r in changes:
        r['adjudicated']=finalby[r['review_id']][r['field']]
        r['reason']=finalby[r['review_id']]['reviewer_note']
    for r in p2:r.update(k2[r['review_id']])
    write_csv(D/'scores_pass2_unmasked.csv',p2)
    write_csv(D/'scores_adjudicated.csv',final)
    write_csv(D/'adjudication_log.csv',changes)
    conditions={}
    for c in ('C1','C2','C3'):
        arm=[r for r in final if r['condition']==c];n=len(arm);k=sum(int(r['complete_preservation']) for r in arm)
        conditions[c]={'n':n,'complete':k,'complete_pct':100*k/n,'wilson_95ci_pct':wilson(k,n),
                       'unsupported_additions':sum(int(r['unsupported_addition']) for r in arm),
                       'components':{f:{'success':sum(r[f]=='1' for r in arm),'denominator':sum(r[f]!='NA' for r in arm)} for f in FIELDS[:5]},
                       'failed_case_ids':sorted(r['case_id'] for r in arm if r['complete_preservation']=='0')}
    archived=csv_rows(P/'archived_vs_fresh_pass1.csv')
    bycase={(r['case_id'],r['condition']):r for r in final}
    retained=[]
    for r in archived:
        f=bycase[(r['case_id'],r['condition'])]
        retained.append({**r,'delayed_adjudicated_complete':f['complete_preservation'],'delayed_note':f['reviewer_note']})
    write_csv(D/'archived_main_discrepancies_rechecked.csv',retained)
    extended=EXCLUDED|{'MAIN-MAY-001','MAIN-SD-009'}
    s={'status':'CODEX_DELAYED_ADJUDICATED_NOT_INDEPENDENT_EXPERT_VALIDATION','created_at':datetime.now(timezone.utc).isoformat(),
       'explanation_complete_agreement':agreement(whole),'applicable_binary_agreement':agreement(applicable),
       'rows_with_component_disagreement':len(expected),'component_disagreements':len(changes),'conditions':conditions,
       'archived_main_discrepancies_rechecked':len(retained),'primary_C1_C3_all72':paired(final,'C1','C3'),
       'primary_C1_C3_excluding_original3':paired(final,'C1','C3',EXCLUDED),
       'secondary_C3_C2_all72':paired(final,'C3','C2'),
       'secondary_C3_C2_excluding_original3':paired(final,'C3','C2',EXCLUDED),
       'exploratory_excluding_scope5':{'excluded_case_ids':sorted(extended),'C1_C3':paired(final,'C1','C3',extended),'C3_C2':paired(final,'C3','C2',extended)},
       'caveats':['Same Codex with prior knowledge; agreement measures within-reviewer stability only.',
                  'Original frozen main results are preserved; newer judgments do not rewrite them.',
                  'Extraction structure diagnostics remain first-pass exploratory observations.',
                  'Five-case exclusion is post-hoc sensitivity; it does not replace the primary 72-case denominator.']}
    (D/'summary_adjudicated.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(s,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
