"""Manual extraction judgments plus deterministic joins; never infer semantic scores from keywords."""
from pathlib import Path
import json,hashlib,datetime,collections
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'outputs/review/proposition_pipeline_v1_20260913';RUN=ROOT/'experiments/runs/proposition_pipeline_v1_20260913';BASE=ROOT/'experiments/proposition_pipeline_v1_20260913'
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return json.loads(p.read_text())
def rows(p):return list(map(json.loads,p.read_text().splitlines()))
def write(p,o):p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def write_rows(p,o):p.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in o))
primary=B/'primary_review';manifest=read(primary/'reviewer_manifest.json')
for p,h in manifest['file_sha256'].items():assert sha((primary/p).read_bytes())==h
assert sha((B/'primary_packets_12.jsonl').read_bytes())==manifest['input_files']['primary_packets_12.jsonl']
P={r['review_id']:r for r in rows(B/'primary_packets_12.jsonl')};K={r['review_id']:r for r in rows(B/'coordinator_keys_12.jsonl')};J={r['review_id']:r for r in rows(primary/'judgments_12.jsonl')};S={r['slot_id']:r for r in rows(RUN/'parsed_stages.jsonl') if r['stage']=='extract'}
# Selected manually after primary seal, using fields, not source_quotes alone.
D={
'PPR-001':([0,1,1,1],[['P1','P2'],['P3','P7'],['P8'],['P9']],['shouldと非SNPN・非揮発性MEの各フィールドはあるがAnnex Cに指定された保存という接続がフィールドにない。','SUPI同伴保存・一致時使用・不一致時削除を保存。','緊急時の非保存・一時保存・登録解除時削除を保存。','eCall時の非保存・一時保存・三つの削除契機を保存。']),
'PPR-009':([0,1,1,1],[['P1','P2','P3'],['P3','P6'],['P7'],['P8']],['should는 P1/P2에 있지만 비휘발성 저장 위치는 can인 P3에 놓였고 Annex C 연결도 구조화 필드에 없다. 저장 권고 요구사항 전체는 불완전하다.','SUPI 동반 저장·일치 사용·불일치 삭제를 보존한다.','긴급 비저장·임시 저장·등록 해제 삭제를 보존한다.','eCall 비저장·임시 저장·세 삭제 사건을 보존한다.']),
'PPR-002':([1,1],[['P1'],['P1']],['may have the capability로 능력 보유의 선택성을 보존한다.','한 Session의 두 UPF 모두를 제어하는 능력을 보존한다.']),
'PPR-006':([1,1],[['P1'],['P1']],['may have the capability로 능력 보유의 선택성을 보존한다.','한 Session의 두 UPF 모두를 제어하는 능력을 보존한다.']),
'PPR-003':([1,1,1],[['P1'],['P2'],['P5']],['should not과 충분히 정확한 위치정보의 unless 관계를 보존한다.','NR satellite access에서의 위치 검증 문맥을 P2에 보존한다.','망이 PLMN 운용 가능 여부를 검증하도록 설정될 수 있음을 P5에 보존한다. 다만 각 명제의 적용 관계를 별도 연결선으로 표현하지는 않는다.']),
'PPR-012':([1,1,1],[['P6'],['P3'],['P1']],['should not과 충분히 정확한 위치정보의 unless 관계를 보존한다.','NR satellite access에서의 위치 검증 문맥을 P3에 보존한다.','망의 선택적 검증 설정 명제를 P1에 보존한다. 명제 간 적용 관계가 구조적으로 연결된 것은 아니다.'])}
D['PPR-001']=(D['PPR-001'][0],D['PPR-001'][1],['should·비SNPN·비휘발성 ME는 필드에 있지만 Annex C에 지정된 저장이라는 연결이 필드에는 없다. 인용문만으로 이 누락을 보충하지 않는다.','SUPI 동반 저장·일치 사용·불일치 삭제를 보존한다.','긴급 비저장·임시 저장·등록 해제 삭제를 보존한다.','eCall 비저장·임시 저장·세 삭제 사건을 보존한다.'])
O=B/'stage_analysis';assert not O.exists();O.mkdir();diagnostics=[];transitions=[];quotes=[]
for rid,(values,ids,reasons) in D.items():
 p=P[rid];x=S[K[rid]['slot_id']];props={q['id']:q for q in x['parsed']['propositions']};source=[p['target_text']]+[b['quote'] for b in p['reference_context_blocks']]
 cov=[]
 for q,v,ref,reason,final in zip(p['requirements'],values,ids,reasons,J[rid]['requirement_coverage']):
  assert q['id']==final['requirement_id']
  cov.append({'requirement_id':q['id'],'value':v,'proposition_ids':ref,'extraction_field_evidence':[{k:y for k,y in props[i].items() if k!='source_quotes'} for i in ref],'source_quotes':source,'rationale':reason})
  f=final['value'];status='UNRESOLVED' if v is None or f is None else {(0,0):'INCOMPLETE_FROM_EXTRACTION',(1,0):'LOST_IN_COMPOSITION',(0,1):'RECOVERED_IN_COMPOSITION',(1,1):'PRESERVED'}[(v,f)]
  transitions.append({'review_id':rid,'requirement_id':q['id'],'extraction':v,'explanation':f,'stage_class':status,'rationale':reason+' / 최종 설명: '+final['rationale']})
 for prop in props.values():
  for quote in prop['source_quotes']:
   quotes.append({'review_id':rid,'proposition_id':prop['id'],'quote':quote,'exact_substring':any(quote in s for s in source),'whitespace_normalized_substring':any(' '.join(quote.split()) in ' '.join(s.split()) for s in source)})
 diagnostics.append({'review_id':rid,'slot_id':K[rid]['slot_id'],'reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'extraction_response_id':x['response_id'],'requirement_coverage':cov,'all_generated_propositions':x['parsed']['propositions'],'limits':'Requirement coverage only, not certification of every extracted claim. SMF P2/P3 add capability-conditioned subclaims; their necessity is unresolved. Quotes do not repair omitted fields.'})
write_rows(O/'extraction_judgments_6.jsonl',diagnostics);write_rows(O/'requirement_transitions_18.jsonl',transitions);write_rows(O/'quote_diagnostics.jsonl',quotes)
conditions=[]
for arm in ['A2_FRESH','P1_EXTRACT_COMPOSE']:
 r=[J[i] for i,k in K.items() if k['arm']==arm];c=collections.Counter(x['full_context_target_completeness'] for x in r);t=collections.Counter(x['unsupported_or_distorted_claim'] for x in r)
 conditions.append({'arm':arm,'n':len(r),'complete':c[1],'incomplete':c[0],'unresolved':c[None],'complete_bounds':[c[1],c[1]+c[None]],'distorted':t[True],'not_distorted':t[False],'claim_unresolved':t[None]})
write(O/'condition_results.json',conditions)
pairs=[]
for cid in ['CTX-001','CTX-002','CTX-003']:
 for rep in [1,2]:
  ids={k['arm']:rid for rid,k in K.items() if k['case_id']==cid and k['replicate']==rep};a=J[ids['A2_FRESH']];t=J[ids['P1_EXTRACT_COMPOSE']]
  pairs.append({'case_id':cid,'replicate':rep,'A2_review_id':ids['A2_FRESH'],'P1_review_id':ids['P1_EXTRACT_COMPOSE'],'A2_complete':a['full_context_target_completeness'],'P1_complete':t['full_context_target_completeness']})
write_rows(O/'paired_results_6.jsonl',pairs)
a,t=conditions;criteria={'robust_completeness_gain':t['complete']>a['complete_bounds'][1],'no_paired_complete_regression':not any(x['A2_complete']==1 and x['P1_complete']!=1 for x in pairs),'no_distortion_upper_bound_increase':t['distorted']+t['claim_unresolved']<=a['distorted']}
write(O/'summary.json',{'status':'BOUNDED_RUN_AND_FIRST_REVIEW_COMPLETE','improvement_candidate':all(criteria.values()),'candidate_checks':criteria,'progression_status':'NOT_AUTHORIZED_BY_SINGLE_REVIEW','prior_experiment_hold_unchanged':True,'reviewers':1,'final_explanations':12,'extraction_outputs':6,'extraction_requirements':18,'stage_counts':dict(collections.Counter(r['stage_class'] for r in transitions)),'component_diagnostic':'Both NSSAI extractions contain should fields but final explanations use obligation wording. Full STORAGE_RECOMMENDATION extraction score remains 0 because Annex C linkage is absent; do not label full requirement 1->0.','quote_counts':{'total':len(quotes),'exact':sum(q['exact_substring'] for q in quotes),'whitespace_normalized':sum(q['whitespace_normalized_substring'] for q in quotes)},'no_automatic_semantic_scoring':True})
write(O/'analysis_manifest.json',{'sealed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'primary_review_sealed_at':manifest['sealed_at'],'primary_manifest_sha256':sha((primary/'reviewer_manifest.json').read_bytes()),'script_sha256':sha(Path(__file__).read_bytes()),'file_sha256':{p.name:sha(p.read_bytes()) for p in O.iterdir()}})
for p in O.iterdir():p.chmod(0o444)
Path(__file__).chmod(0o444)
print(json.dumps({'conditions':conditions,'candidate_checks':criteria,'stage_counts':dict(collections.Counter(r['stage_class'] for r in transitions))},ensure_ascii=False))
