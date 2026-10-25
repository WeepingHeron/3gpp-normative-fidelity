"""Validate sealed manual reviews and apply the already frozen descriptive comparison/gate."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import argparse,hashlib,json,sqlite3,subprocess
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'experiments/generation_preservation_v1_20260909'
OUT=ROOT/'outputs/review/generation_preservation_v1_20260909'
ANALYSIS=OUT/'analysis'
PINS={'root_review':'4d8f99589c406034fee1299d1d403a79d04aac0a55f17831f690cfe84c324b48','fresh_review':'f6757fc0daa51bdc51235a0104696167d9813e8d2905e7324e01b258d15e03e9'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def rows(p):return [json.loads(x) for x in p.read_text().splitlines()]
def encode(obj,jsonl=False):return (''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in obj) if jsonl else json.dumps(obj,ensure_ascii=False,indent=2)+'\n').encode()
def count(rs,field,states):return {label:sum(r[field] is v if isinstance(v,bool) or v is None else type(r[field]) is int and r[field]==v for r in rs) for label,v in states}

COMPLETE=[('complete',1),('incomplete',0),('unresolved',None)]
CLAIM=[('distorted',True),('no_distortion',False),('claim_unresolved',None)]

def derive():
 execution=json.loads(subprocess.run(['node',str(ROOT/'tools/verify_generation_preservation_execution_20260913.mjs')],check=True,capture_output=True,text=True).stdout)
 packets={p['review_id']:p for p in rows(OUT/'reviewer/packets_18.jsonl')}
 protocol=read(BASE/'protocol.json');keys={x['review_id']:x for x in rows(OUT/'coordinator/keys_18.jsonl')}
 all_reviews={};seal_times={}
 for folder,pin in PINS.items():
  directory=OUT/folder;m=read(directory/'reviewer_manifest.json');assert sha(directory/'reviewer_manifest.json')==pin
  if folder=='root_review':
   for path,h in m['input_file_sha256'].items():assert sha(ROOT/path)==h
   for name,h in m['output_file_sha256'].items():assert sha(directory/name)==h
   assert sha(ROOT/'tools/record_generation_preservation_root_review_20260913.py')==m['recording_script_sha256']
   assert m['read_boundary']['condition_key_read_before_seal'] is False
   assert m['read_boundary']['other_reviewer_judgments_read_before_seal'] is False
  else:
   for item in m['input_files']+m['output_files']:assert sha(Path(item['path']))==item['sha256']
   allowed={str(BASE/'reviewer_instructions.md'),str(BASE/'evaluation_reference.json'),str(OUT/'reviewer/packets_18.jsonl'),str(directory/'judgments_18.jsonl')}
   assert set(m['actual_read_paths'])<=allowed
  seal_times[folder]=m['completed_at'];reviews=rows(directory/'judgments_18.jsonl')
  assert len(reviews)==18 and {r['review_id'] for r in reviews}==set(packets)
  for r in reviews:
   p=packets[r['review_id']];source=[p['target_text']]+[b['quote'] for b in p['reference_context_blocks']]
   assert r['overall_rationale'] and datetime.fromisoformat(r['reviewed_at'])<=datetime.fromisoformat(m['completed_at'])
   assert [x['requirement_id'] for x in r['requirement_coverage']]==[x['id'] for x in p['requirements']]
   vals=[]
   for x in r['requirement_coverage']:
    v=x['value'];assert (type(v) is int and v in (0,1)) or v is None
    assert x['rationale'] and x['source_quotes']
    assert all(q and q in p['explanation_ko'] for q in x['response_quotes'])
    assert all(q and any(q in s for s in source) for q in x['source_quotes'])
    if v==1:assert x['response_quotes']
    vals.append(v)
   claim=r['unsupported_or_distorted_claim'];assert type(claim) is bool or claim is None
   assert r['claim_rationale'] and all(q and q in p['explanation_ko'] for q in r['claim_evidence_quotes'])
   if claim is True:assert r['claim_evidence_quotes']
   meta=r['metadata_inconsistency'];assert type(meta) is bool or meta is None;assert r['metadata_rationale']
   expected=0 if 0 in vals or claim is True else None if None in vals or claim is None else 1
   assert type(r['full_context_target_completeness']) is int or r['full_context_target_completeness'] is None
   assert r['full_context_target_completeness']==expected
   citation=r['citation_diagnostic'];md=p['output_metadata_for_separate_audit']
   expected_citation=all(md['citation_'+k]==p['source'][v] for k,v in [('spec','spec_id'),('version','version'),('clause','clause_id')])
   assert citation['matches_source_fields']==expected_citation and citation['rationale']
   sentence=r['sentence_count_diagnostic'];assert type(sentence['sentence_count']) is int
   assert sentence['within_2_to_4']==(2<=sentence['sentence_count']<=4) and sentence['rationale']
  all_reviews[folder]={r['review_id']:r for r in reviews}
 joined=[];condition=[];requirements=[];paired=[];gates=[]
 for reviewer,rs in all_reviews.items():
  indexed={(keys[rid]['case_id'],keys[rid]['arm'],keys[rid]['replicate']):r for rid,r in rs.items()}
  for rid,r in rs.items():joined.append({'reviewer_set':reviewer,**keys[rid],**r})
  for arm in protocol['arms']:
   selected=[r for rid,r in rs.items() if keys[rid]['arm']==arm]
   condition.append({'reviewer_set':reviewer,'arm':arm,'n':6,**count(selected,'full_context_target_completeness',COMPLETE),**count(selected,'unsupported_or_distorted_claim',CLAIM)})
   for case in protocol['case_ids']:
    subset=[indexed[(case,arm,rep)] for rep in protocol['replicates']]
    for position,item in enumerate(subset[0]['requirement_coverage']):
     values=[r['requirement_coverage'][position]['value'] for r in subset]
     requirements.append({'reviewer_set':reviewer,'arm':arm,'case_id':case,'requirement_id':item['requirement_id'],'n':2,'preserved':sum(v==1 for v in values),'missing_or_wrong':sum(v==0 for v in values),'unresolved':sum(v is None for v in values)})
  for treatment,baseline in [protocol['primary_contrast']]+protocol['secondary_contrasts']:
   for case in protocol['case_ids']:
    for rep in protocol['replicates']:
     a=indexed[(case,baseline,rep)];b=indexed[(case,treatment,rep)]
     changes=[{'requirement_id':x['requirement_id'],'baseline':x['value'],'treatment':y['value']} for x,y in zip(a['requirement_coverage'],b['requirement_coverage'])]
     paired.append({'reviewer_set':reviewer,'baseline_arm':baseline,'treatment_arm':treatment,'case_id':case,'replicate':rep,'baseline_review_id':a['review_id'],'treatment_review_id':b['review_id'],'baseline_complete':a['full_context_target_completeness'],'treatment_complete':b['full_context_target_completeness'],'requirement_changes':changes})
  c={x['arm']:x for x in condition if x['reviewer_set']==reviewer};a,b=c['A0_BASE'],c['A2_MODAL_CHECK']
  pairs=[p for p in paired if p['reviewer_set']==reviewer and p['baseline_arm']=='A0_BASE' and p['treatment_arm']=='A2_MODAL_CHECK']
  changes=[x for p in pairs for x in p['requirement_changes']]
  modal=['STORAGE_RECOMMENDATION','LOCATION_UNLESS_RECOMMENDATION'];exceptions=['EMERGENCY_EXCEPTION','ECALL_EXCEPTION']
  conditions={'complete_run_and_sealed_reviews':execution['generated']==18 and len(all_reviews)==2,'robust_completeness_gain':b['complete']>a['complete']+a['unresolved'],'no_increase_in_distortion_upper_bound':b['distorted']+b['claim_unresolved']<=a['distorted'],'no_paired_complete_regression':not any(p['baseline_complete']==1 and p['treatment_complete']!=1 for p in pairs),'both_modality_and_exception_gain':all(any(x['requirement_id'] in group and x['baseline']==0 and x['treatment']==1 for x in changes) for group in [modal,exceptions])}
  gates.append({'reviewer_set':reviewer,'conditions':conditions,'passes':all(conditions.values()),'complete_bounds_A0':[a['complete'],a['complete']+a['unresolved']],'complete_bounds_A2':[b['complete'],b['complete']+b['unresolved']]})
 comparisons=[];overall_match=claim_match=coverage_match=0
 for rid in packets:
  a,b=(all_reviews[k][rid] for k in ['root_review','fresh_review']);diff=[]
  for field in ['full_context_target_completeness','unsupported_or_distorted_claim','metadata_inconsistency']:
   if a[field]!=b[field]:diff.append(field)
  for x,y in zip(a['requirement_coverage'],b['requirement_coverage']):
   if x['value']==y['value']:coverage_match+=1
   else:diff.append('requirement:'+x['requirement_id'])
  overall_match+=a['full_context_target_completeness']==b['full_context_target_completeness']
  claim_match+=a['unsupported_or_distorted_claim']==b['unsupported_or_distorted_claim']
  comparisons.append({'review_id':rid,**keys[rid],'different_fields':diff,'root_review':a,'fresh_review':b})
 # Independent SQLite aggregation validates counts without rewriting manual scores.
 db=sqlite3.connect(':memory:');db.execute('create table scores(reviewer text,arm text,complete integer,claim integer)')
 db.executemany('insert into scores values(?,?,?,?)',[(r['reviewer_set'],r['arm'],r['full_context_target_completeness'],r['unsupported_or_distorted_claim']) for r in joined])
 for reviewer,arm,n,yes,no,unknown,ct,cf,cu in db.execute('select reviewer,arm,count(*),sum(complete=1),sum(complete=0),sum(complete is null),sum(claim=1),sum(claim=0),sum(claim is null) from scores group by reviewer,arm'):
  expected=next(x for x in condition if x['reviewer_set']==reviewer and x['arm']==arm)
  assert [n,yes,no,unknown,ct,cf,cu]==[expected[k] for k in ['n','complete','incomplete','unresolved','distorted','no_distortion','claim_unresolved']]
 gate={'status':'READY_FOR_UNSEEN_CLAUSE_PLAN' if all(x['passes'] for x in gates) else 'HOLD_FOR_METHOD_REVISION','reviewers':gates,'rule_changed':False,'automatic_adjudication':False}
 validation={'status':'TWO_AI_SEMANTIC_REVIEWS_COMPLETE','unique_responses':18,'reviewers':2,'review_records':36,'requirement_judgments':108,'primary_agreement':{'completeness':{'same':overall_match,'total':18},'claim':{'same':claim_match,'total':18},'requirements':{'same':coverage_match,'total':54}},'sqlite_group_count_check':True,'review_seal_times':seal_times,'progression_status':gate['status'],'metadata_comparability':'WITHHELD: some fresh diagnostics compare metadata to source instead of metadata to explanation; preserve raw values and report post-seal clarification separately.','semantic_scores_automatically_inferred':False,'human_expert_review':False}
 return {'joined_reviews_36.jsonl':encode(joined,True),'condition_results_6.jsonl':encode(condition,True),'requirement_results_54.jsonl':encode(requirements,True),'paired_results_36.jsonl':encode(paired,True),'comparison_18.jsonl':encode(comparisons,True),'progression_gate.json':encode(gate),'validation_report.json':encode(validation)}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['build','verify']);mode=ap.parse_args().mode
 data=derive()
 if mode=='build':ANALYSIS.mkdir(exist_ok=False)
 for name,body in data.items():
  p=ANALYSIS/name
  if mode=='build':p.write_bytes(body)
  else:assert p.read_bytes()==body,name
 print(json.dumps(read(ANALYSIS/'validation_report.json'),ensure_ascii=False))
if __name__=='__main__':main()
