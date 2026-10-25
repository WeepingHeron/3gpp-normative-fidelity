"""Assemble explicit manual adjudication; never infer semantic labels from response text."""
import argparse,collections,csv,datetime,hashlib,json,subprocess,sys
from pathlib import Path
import compare_v2_review_passes_20260909 as prior
ROOT=prior.ROOT;OUT=ROOT/'outputs/review/v2_adjudication_20260909';DOC=ROOT/'docs/27_v2_disagreement_adjudication_2026-09-09.md'
SCOPE={'G001','G003','G004','G005','G006','G008','G009','G010','G025','G031','G037','G050'}
RULES={19:['R3','R4','R8'],70:['R1','R3','R4'],99:['R3','R4','R8'],106:['R1','R3'],151:['R3','R4','R8']}
read,lines,write,write_lines,sha=prior.read,prior.lines,prior.write,prior.write_lines,prior.sha

def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def input_data():
 prior.verify()
 a,b,pairs,comparison,diff=prior.data()
 pk={r['review_id']:r for r in pairs};bb={r['review_id']:r for r in b};aa={r['response_record_sha256']:r for r in a}
 manual=[]
 for line in (OUT/'manual_scope_review.tsv').read_text().splitlines():
  n,state,rationale=line.split('\t');rid=f'V2-P2-{int(n):03d}';assert state in {'PASS','FAIL','UNRESOLVED'} and len(rationale)>20
  manual.append({'review_id':rid,'semantic_judgment':state,'rationale':rationale})
 assert len(manual)==60 and len({r['review_id'] for r in manual})==60
 assert {r['review_id'] for r in manual}=={r['review_id'] for r in pairs if r['reference_id'] in SCOPE}
 diffids={r['pass2_review_id'] for r in diff};assert diffids=={f'V2-P2-{n:03d}' for n in RULES}
 # Agreed rows are checked for the specified issue; a discovered change must expand adjudication explicitly.
 assert all(r['review_id'] in diffids or r['semantic_judgment']==bb[r['review_id']]['semantic_judgment'] for r in manual)
 key=read(prior.p2.v2.PACKAGE/'coordinator/keys.json')['pass2']
 for ref in SCOPE:assert {r['condition'] for r in key if r['reference_id']==ref}=={'C0','C1','C2','C3','C1M'}
 return a,b,pk,bb,aa,manual,diffids

def build():
 assert not (OUT/'adjudications.jsonl').exists(),'Never overwrite adjudication results'
 a,b,pk,bb,aa,manual,diffids=input_data();stamp=now();review=[];adj=[]
 for m in manual:
  rid=m['review_id'];r=bb[rid];p=pk[rid];old=aa[r['response_record_sha256']]
  x=dict(m,reference_id=r['reference_id'],recorded_at=stamp,reviewer='Codex (same study evaluator; not independent expert)',review_scope='Targeted symmetry check; not a full third review of all 255 slots',response_record_sha256=r['response_record_sha256'],packet_sha256=r['packet_sha256'],source=p['source'],pdf=p['pdf'],question_ko=p['question_ko'],response_evidence_quote=p['explanation_ko'],source_provenance=r['source_provenance'],propositions_and_relations=r['propositions_and_relations'],pass1_review_id=old['review_id'],pass1_state=old['semantic_judgment'],pass2_state=r['semantic_judgment'])
  review.append(x)
  if rid in diffids:adj.append(dict(x,adjudication_id='V2-ADJ-'+rid[-3:],review_pass='adjudication_v1',treatment_version=r['treatment_version'],rubric_sha256=r['rubric_sha256'],applied_rules=RULES[int(rid[-3:])],complete_preservation={'PASS':1,'FAIL':0,'UNRESOLVED':None}[m['semantic_judgment']],gold_status=r['gold_status'],delivery_status=r['delivery_status'],pass1_rationale=old['rationale'],pass2_rationale=r['rationale'],adjudication_status='DISPOSED_AS_UNRESOLVED' if m['semantic_judgment']=='UNRESOLVED' else 'DECIDED',independent_reviewer=False))
 write_lines(OUT/'scope_review_60.jsonl',review);write_lines(OUT/'adjudications.jsonl',adj)
 byid={r['review_id']:r for r in adj};merged=[]
 for r in b:
  old=aa[r['response_record_sha256']];decision=byid.get(r['review_id'])
  if decision is None:assert (old['semantic_judgment'],old['complete_preservation'])==(r['semantic_judgment'],r['complete_preservation'])
  state=decision['semantic_judgment'] if decision else r['semantic_judgment'];val={'PASS':1,'FAIL':0,'UNRESOLVED':None,'NOT_SCORED':0}[state]
  merged.append({'review_id':r['review_id'],'reference_id':r['reference_id'],'review_pass':'adjudicated_view_v1','treatment_version':r['treatment_version'],'rubric_sha256':r['rubric_sha256'],'response_record_sha256':r['response_record_sha256'],'packet_sha256':r['packet_sha256'],'semantic_judgment':state,'complete_preservation':val,'gold_status':r['gold_status'],'delivery_status':r['delivery_status'],'disposition_basis':'EXPLICIT_ADJUDICATION' if decision else 'TWO_PASS_AGREEMENT','adjudication_id':decision['adjudication_id'] if decision else None,'assembled_at':stamp,'pass1_snapshot':{k:old[k] for k in ['review_id','semantic_judgment','complete_preservation','rationale','reviewed_at']},'pass2_snapshot':{k:r[k] for k in ['review_id','semantic_judgment','complete_preservation','rationale','reviewed_at']},'adjudication_rationale':decision['rationale'] if decision else None,'reason_codes':decision['applied_rules']+(['AMBIGUOUS_REFERENT'] if state=='UNRESOLVED' else []) if decision else r['reason_codes'],'source_provenance':r['source_provenance'],'propositions_and_relations':r['propositions_and_relations'],'input_context_gap':r['input_context_gap'],'input_availability_binding_file':'../v2_pass2_completed_20260909/input_provenance_bindings.jsonl'})
 write_lines(OUT/'adjudicated_view_255.jsonl',merged)
 unresolved=[dict(review_id=r['review_id'],reference_id=r['reference_id'],response_record_sha256=r['response_record_sha256'],complete_preservation=None,uncertainty_type='RESPONSE_REFERENT_AMBIGUITY' if r['reference_id']=='G010' else 'ANNEX_SCORING_SCOPE' if r['reference_id']=='G023' else 'UPPER_CONTEXT_SCORING_SCOPE',disposition='RETAIN_UNRESOLVED_IN_FROZEN_DENOMINATOR',rationale=r['adjudication_rationale'] or r['pass2_snapshot']['rationale']) for r in merged if r['semantic_judgment']=='UNRESOLVED']
 write_lines(OUT/'unresolved_register.jsonl',unresolved)
 counts=dict(collections.Counter(r['semantic_judgment'] for r in merged));summary={'status':'DISAGREEMENT_ADJUDICATION_COMPLETE_WITH_UNRESOLVED','assembled_at':stamp,'disagreement_slots':5,'disagreements_with_disposition':5,'unprocessed_disagreements':0,'adjudication_outcomes':dict(collections.Counter(r['semantic_judgment'] for r in adj)),'targeted_scope_slots':60,'targeted_scope_references':12,'additional_agreed_slots_checked':55,'additional_agreed_states_changed':0,'merged_slots':255,'merged_workflow_counts':counts,'unresolved_by_reference':dict(collections.Counter(r['reference_id'] for r in unresolved)),'changes_from_pass2':[r['review_id'] for r in merged if r['semantic_judgment']!=r['pass2_snapshot']['semantic_judgment']],'original_pass_agreement_count':250,'original_pass_agreement_denominator':255,'rubric_changed':False,'independent_reviewer':False,'full_third_pass_performed':False,'cohort_denominators_unchanged':[49,50,50,51],'new_model_generation_calls':0,'condition_metrics_computed':False,'paper_numbers_updated':False,'remaining_requirement':'Preserve unresolved bounds in downstream cohort reporting; defer definitive statistical tests for affected comparisons.'}
 write(OUT/'summary.json',summary)
 s=['# v2 불일치 조정 근거','','동일 평가자의 공개된 사후 조정 기록이다. 기존 두 차수의 봉인 자료는 그대로 보존한다. 조건별 결과를 보고 상태를 선택하지 않았으며 독립 검증으로 주장하지 않는다.','']
 for x in adj:s += [f"## {x['review_id']} · {x['reference_id']} · {x['semantic_judgment']}",'',f"1차 {x['pass1_state']} → 2차 {x['pass2_state']} → 조정 {x['semantic_judgment']}; 적용: {', '.join(x['applied_rules'])}.",'','원문: '+x['source']['source_text_en'],'','응답: '+x['response_evidence_quote'],'','1차 근거: '+x['pass1_rationale'],'','2차 근거: '+x['pass2_rationale'],'','조정 근거: '+x['rationale'],'',f"출처: {x['source']['spec_id']} v{x['source']['version']} §{x['source']['clause_id']}, PDF p.{x['pdf']['pdf_page']}. 기록 시각: {x['recorded_at']}.",'']
 (OUT/'adjudication_readable.md').write_text('\n'.join(s)+'\n')
 prior.csvwrite(OUT/'adjudication_index.csv',adj,['review_id','reference_id','pass1_state','pass2_state','semantic_judgment','complete_preservation','applied_rules','rationale'])
 prior.csvwrite(OUT/'scope_review_index.csv',review,['review_id','reference_id','pass1_state','pass2_state','semantic_judgment','rationale'])
 print(json.dumps(summary,ensure_ascii=False,indent=2))

def verify_payload():
 a,b,pk,bb,aa,manual,diffids=input_data();adj=lines(OUT/'adjudications.jsonl');scope=lines(OUT/'scope_review_60.jsonl');merged=lines(OUT/'adjudicated_view_255.jsonl');summ=read(OUT/'summary.json')
 mm={r['review_id']:r for r in manual};ad={r['review_id']:r for r in adj}
 assert set(ad)==diffids and len(adj)==5 and len(scope)==60
 for x in scope:
  m=mm[x['review_id']];assert x['semantic_judgment']==m['semantic_judgment'] and x['rationale']==m['rationale']
  p=pk[x['review_id']];r=bb[x['review_id']]
  assert x['response_evidence_quote']==p['explanation_ko'] and x['source']==p['source'] and x['pdf']==p['pdf']
  assert x['source_provenance']==r['source_provenance'] and x['propositions_and_relations']==r['propositions_and_relations']
  assert x['response_record_sha256']==r['response_record_sha256'] and x['packet_sha256']==r['packet_sha256']
 for x in adj:
  m=mm[x['review_id']];assert x['rationale']==m['rationale'] and x['semantic_judgment']==m['semantic_judgment']
  assert x['applied_rules']==RULES[int(x['review_id'][-3:])]
  assert x['complete_preservation']=={'PASS':1,'FAIL':0,'UNRESOLVED':None}[x['semantic_judgment']]
 assert len(merged)==255 and [x['review_id'] for x in merged]==[r['review_id'] for r in b]
 assert len({r['response_record_sha256'] for r in merged})==255
 for x in merged:
  r=bb[x['review_id']];old=aa[r['response_record_sha256']];expected=ad[x['review_id']]['semantic_judgment'] if x['review_id'] in ad else r['semantic_judgment']
  assert x['semantic_judgment']==expected and x['complete_preservation']=={'PASS':1,'FAIL':0,'UNRESOLVED':None,'NOT_SCORED':0}[expected]
  assert x['response_record_sha256']==r['response_record_sha256'] and x['gold_status']==r['gold_status'] and x['delivery_status']==r['delivery_status']
  for name,orig in [('pass1_snapshot',old),('pass2_snapshot',r)]:assert x[name]=={k:orig[k] for k in x[name]}
  if x['gold_status']=='UNRESOLVED':assert expected=='UNRESOLVED' or expected=='FAIL' and 'INDEPENDENT_CLEAR_ERROR' in x['reason_codes']
  assert datetime.datetime.fromisoformat(x['assembled_at'])>=datetime.datetime.fromisoformat(read(prior.p2.SEAL/'completion_manifest.json')['completed_at'])
 assert summ['merged_workflow_counts']==dict(collections.Counter(r['semantic_judgment'] for r in merged))
 assert {r['review_id'] for r in lines(OUT/'unresolved_register.jsonl')}=={r['review_id'] for r in merged if r['semantic_judgment']=='UNRESOLVED'}
 assert summ['unprocessed_disagreements']==0 and summ['condition_metrics_computed'] is False
 return {'ok':True,'adjudicated_disagreements':5,'focused_symmetry_checks':60,'merged_slots':255,'unchanged_earlier_seals':True,'semantic_truth_automatically_verified':False}
def finish():
 assert DOC.exists() and not (OUT/'completion_manifest.json').exists();receipt=verify_payload();write(OUT/'verification_receipt.json',dict(receipt,verified_at=now()))
 write(OUT/'completion_manifest.json',{'status':'DISAGREEMENT_ADJUDICATION_COMPLETE_WITH_UNRESOLVED','completed_at':now(),'file_sha256':{str(p.relative_to(OUT)):sha(p) for p in sorted(OUT.rglob('*')) if p.is_file()},'support_file_sha256':{str(p.relative_to(ROOT)):sha(p) for p in [Path(__file__).resolve(),DOC]},'prior_manifest_sha256':{str(p.relative_to(ROOT)):sha(p) for p in [prior.p2.P1.parent/'completion_manifest.json',prior.p2.OUT/'completion_manifest.json',prior.p2.SEAL/'completion_manifest.json']}})
 for p in OUT.iterdir():
  if p.is_file():p.chmod(0o444)
def verify():
 m=read(OUT/'completion_manifest.json')
 for rel,h in m['file_sha256'].items():assert sha(OUT/rel)==h
 for rel,h in {**m['support_file_sha256'],**m['prior_manifest_sha256']}.items():assert sha(ROOT/rel)==h
 print(json.dumps(verify_payload(),ensure_ascii=False))
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('command',choices=['build','finish','verify']);x=a.parse_args();{'build':build,'finish':finish,'verify':verify}[x.command]()
