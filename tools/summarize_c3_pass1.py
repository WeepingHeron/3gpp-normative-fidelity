"""Recompute provisional reviewer results; never assign semantic judgments."""
import csv
import hashlib
import json
import math
import random
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / 'experiments/runs/main72_v3_2026-09-03T07-35-49-603Z'
RUN = ROOT / 'experiments/runs/c3_auto72_v1_2026-09-06T04-53-06-942Z'
REVIEW = RUN / 'review'
EXCLUDED = {'MAIN-CAN-004','MAIN-SD-002','MAIN-CAN-008'}
SEED = 2026090601
FIELDS = ['actor_preserved','polarity_preserved','condition_preserved',
          'action_preserved','exception_preserved','unsupported_addition']

def csv_rows(path):
    with path.open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f))

def verify(base, manifest):
    data=json.loads(manifest.read_text())
    for name,digest in data['file_sha256'].items():
        assert hashlib.sha256((base/name).read_bytes()).hexdigest()==digest, name
    return len(data['file_sha256'])

def write_csv(path, rows):
    assert rows
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def wilson(k,n):
    z=1.959963984540054
    d=1+z*z/n; mid=(k/n+z*z/(2*n))/d
    half=z*math.sqrt(k/n*(1-k/n)/n+z*z/(4*n*n))/d
    return [100*(mid-half),100*(mid+half)]

def exact(a,b):
    n=a+b
    return min(1.,2*sum(math.comb(n,k)*.5**n for k in range(min(a,b)+1))) if n else 1.

def quantile(values,q):
    pos=(len(values)-1)*q; lo=math.floor(pos); hi=math.ceil(pos)
    return values[lo]+(values[hi]-values[lo])*(pos-lo)

def paired(rows,first,second,excluded=()):
    arms={c:{r['case_id']:int(r['complete_preservation']) for r in rows
             if r['condition']==c and r['case_id'] not in excluded} for c in (first,second)}
    a,b=arms[first],arms[second]
    assert a.keys()==b.keys()
    ids=sorted(a); n=len(ids); diffs=[b[k]-a[k] for k in ids]
    rng=random.Random(SEED)
    boots=sorted(100*sum(rng.choices(diffs,k=n))/n for _ in range(20000))
    only_a=sum(d==-1 for d in diffs);only_b=sum(d==1 for d in diffs)
    return {'first':first,'second':second,'n':n,'first_successes':sum(a.values()),
            'second_successes':sum(b.values()),'second_minus_first_pp':100*sum(diffs)/n,
            'paired_bootstrap_95ci_pp':[quantile(boots,.025),quantile(boots,.975)],
            'first_only':only_a,'second_only':only_b,'exact_McNemar_two_sided_p':exact(only_a,only_b)}

def main():
    hashes={
        'main_inputs':verify(ROOT,ROOT/'data/main_freeze_manifest.json'),
        'main_outputs':verify(MAIN,MAIN/'output_freeze_manifest.json'),
        'c3_inputs':verify(ROOT,RUN/'input_freeze_manifest.json'),
        'c3_outputs':verify(RUN,RUN/'output_freeze_manifest.json'),
        'blank_review':verify(REVIEW,REVIEW/'review_manifest.json'),
        'pass1_decisions':verify(REVIEW,REVIEW/'pass1_freeze_manifest.json'),
    }
    key=json.loads((REVIEW/'blind_key.json').read_text())
    rows=csv_rows(REVIEW/'blind_explanations_pass1.csv')
    gold={r['case_id']:r for r in csv_rows(ROOT/'data/main_cases.csv')}
    assert len(rows)==216 and len({r['review_id'] for r in rows})==216
    parsed=[json.loads(s) for p in (MAIN,RUN) for s in (p/'parsed_responses.jsonl').read_text().splitlines()]
    response={(r['case_id'],r['condition']):r for r in parsed}
    for r in rows:
        r.update(key[r['review_id']]); g=gold[r['case_id']]
        assert r['source_text_en']==g['source_text_en']
        assert r['explanation_ko']==(response[(r['case_id'],r['condition'])].get('parsed') or {}).get('explanation_ko','')
        assert all(r[f] in ('0','1','NA') for f in FIELDS[:5])
        assert r['unsupported_addition'] in ('0','1') and r['reviewer_note']
        assert int(r['complete_preservation'])==int(all(r[f] in ('1','NA') for f in FIELDS[:5]) and r['unsupported_addition']=='0')
    assert {(r['case_id'],r['condition']) for r in rows}=={(k,c) for k in gold for c in ('C1','C2','C3')}
    conditions={}
    for c in ('C1','C2','C3'):
        arm=[r for r in rows if r['condition']==c]; k=sum(int(r['complete_preservation']) for r in arm)
        conditions[c]={'n':len(arm),'complete':k,'complete_pct':100*k/len(arm),'wilson_95ci_pct':wilson(k,len(arm)),
                       'unsupported_additions':sum(int(r['unsupported_addition']) for r in arm),
                       'components':{f:{'success':sum(r[f]=='1' for r in arm),'denominator':sum(r[f]!='NA' for r in arm)} for f in FIELDS[:5]},
                       'failed_case_ids':[r['case_id'] for r in arm if r['complete_preservation']=='0']}
    old={(r['case_id'],r['condition']):r for r in csv_rows(MAIN/'human_scores_adjudicated.csv')}
    changed=[]
    for r in rows:
        if r['condition']=='C3':continue
        o=old[(r['case_id'],r['condition'])]
        if r['complete_preservation']!=o['complete_preservation']:
            changed.append({'review_id':r['review_id'],'case_id':r['case_id'],'condition':r['condition'],
                            'archived_complete':o['complete_preservation'],'fresh_pass1_complete':r['complete_preservation'],
                            'fresh_reason':r['reviewer_note'],'archived_note':o['reviewer_note']})
    extraction=csv_rows(REVIEW/'extraction_review_pass1.csv')
    assert len(extraction)==72 and {r['case_id'] for r in extraction}==set(gold)
    bycase={r['case_id']:r for r in extraction}
    c3=[r for r in rows if r['condition']=='C3']
    types={'shall':'obligation','shall_not':'prohibition','should':'recommendation',
           'should_not':'discouragement','may':'permission','can':'capability'}
    # Explicit modal readings of rows whose reviewed polarity/modality failed.
    # All other readings follow their manually reviewed polarity=1 decision.
    modal_readings={'E005':'permission','E009':'permission','E029':'permission','E037':'NO_RESPONSE',
                    'E047':'UNCLEAR_SCOPE','E052':'permission','E078':'prohibition','E102':'capability',
                    'E126':'UNCLEAR_SCOPE','E127':'prohibition','E129':'prohibition','E141':'capability',
                    'E174':'prohibition','E191':'UNCLEAR_SCOPE','E203':'permission','E211':'prohibition'}
    alignment=[]
    for r in rows:
        assert (r['polarity_preserved']=='0')==(r['review_id'] in modal_readings)
        natural=modal_readings.get(r['review_id'],types[r['gold_modal_class']])
        predicted=(response[(r['case_id'],r['condition'])].get('parsed') or {}).get('normative_type','NO_RESPONSE')
        alignment.append({'review_id':r['review_id'],'case_id':r['case_id'],'condition':r['condition'],
                          'JSON_normative_type':predicted,'reviewed_explanation_modal':natural,
                          'JSON_explanation_modal_agreement':'NA' if natural in ('UNCLEAR_SCOPE','NO_RESPONSE') else str(int(predicted==natural)),
                          'complete_preservation':r['complete_preservation'],
                          'reviewer_note':r['reviewer_note']})
    transitions=[]
    for r in c3:
        e=bycase[r['case_id']]
        transitions.append({'case_id':r['case_id'],'review_id':r['review_id'],
                            'structure_content':e['structural_content_preserved'],
                            'extraction_JSON_modal_correct':e['extraction_JSON_modal_correct'],
                            'extraction_polarity_correct':e['extraction_polarity_correct'],
                            'explanation_complete':r['complete_preservation'],
                            'extraction_flags':e['diagnostic_flags'],
                            'extraction_note':e['reviewer_note'],'explanation_note':r['reviewer_note']})
    summary={'status':'PROVISIONAL_CODEX_PASS1_NOT_INDEPENDENT_EXPERT_VALIDATION',
             'hashes_verified_counts':hashes,'conditions':conditions,
             'primary_C1_C3_all72':paired(rows,'C1','C3'),
             'primary_C1_C3_excluding_original3':paired(rows,'C1','C3',EXCLUDED),
             'secondary_C3_C2_all72':paired(rows,'C3','C2'),
             'secondary_C3_C2_excluding_original3':paired(rows,'C3','C2',EXCLUDED),
             'extraction':{'n':72,'cross_slot_structure_content_preserved':sum(int(r['structural_content_preserved']) for r in extraction),
                           'JSON_modal_correct':sum(int(r['extraction_JSON_modal_correct']) for r in extraction),
                           'JSON_polarity_correct':sum(int(r['extraction_polarity_correct']) for r in extraction),
                           'structure_and_JSON_both_correct':sum(r['structural_content_preserved']=='1' and r['extraction_JSON_modal_correct']=='1' and r['extraction_polarity_correct']=='1' for r in extraction),
                           'slot_counts':{f:{'success':sum(r[f+'_semantic_preserved']=='1' for r in extraction),'denominator':sum(r[f+'_semantic_preserved']!='NA' for r in extraction)} for f in ('actor','condition','action','exception')}},
             'structure_to_explanation_counts':dict(Counter(r['structure_content']+'->'+r['explanation_complete'] for r in transitions)),
             'archived_main_complete_decisions_changed':len(changed),
             'JSON_explanation_alignment':{c:{'agree':sum(r['JSON_explanation_modal_agreement']=='1' for r in alignment if r['condition']==c),
                                              'disagree':sum(r['JSON_explanation_modal_agreement']=='0' for r in alignment if r['condition']==c),
                                              'not_assessable':sum(r['JSON_explanation_modal_agreement']=='NA' for r in alignment if r['condition']==c)} for c in ('C1','C2','C3')},
             'bootstrap':{'unit':'case','iterations':20000,'seed':SEED},
             'caveats':['Same reviewer with prior results knowledge; masked IDs are not independent validation.',
                        'Provisional first pass; delayed review and adjudication remain.',
                        'C1/C2 generated September 3 and C3 September 6; comparisons are exploratory.',
                        'Extraction slot and cross-slot diagnostics defined after generation.',
                        'No causal proof that correct explanations repaired extraction: generation also sees the original source.']}
    assert exact(0,0)==1 and exact(0,7)==.015625
    write_csv(REVIEW/'scores_pass1_unmasked.csv',rows)
    if changed:write_csv(REVIEW/'archived_vs_fresh_pass1.csv',changed)
    write_csv(REVIEW/'extraction_to_explanation_pass1.csv',transitions)
    write_csv(REVIEW/'JSON_explanation_alignment_pass1.csv',alignment)
    (REVIEW/'summary_pass1.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
