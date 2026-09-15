"""Join sealed manual judgments; record manually inspected audit failures without automatic regrading."""
from pathlib import Path
import json,hashlib,datetime,collections
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'outputs/review/preservation_repair_v1_20260914';BASE=ROOT/'experiments/preservation_repair_v1_20260914';RUN=ROOT/'experiments/runs/preservation_repair_v1_20260914';OLD=ROOT/'outputs/review/proposition_pipeline_v1_20260913'
def read(p):return json.loads(p.read_text())
def rows(p):return list(map(json.loads,p.read_text().splitlines()))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,o):p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def write_rows(p,o):p.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in o))
for folder,m in [(B/'primary_review',B/'primary_review/reviewer_manifest.json'),(OLD/'primary_review',OLD/'primary_review/reviewer_manifest.json')]:
 for p,h in read(m)['file_sha256'].items():assert sha(folder/p)==h
P={r['review_id']:r for r in rows(B/'primary_packets_12.jsonl')};J={r['review_id']:r for r in rows(B/'primary_review/judgments_12.jsonl')};K={r['review_id']:r for r in rows(B/'coordinator_keys_12.jsonl')};O={r['review_id']:r for r in rows(OLD/'primary_review/judgments_12.jsonl')};OK={r['slot_id']:r for r in rows(OLD/'coordinator_keys_12.jsonl')};seeds={r['seed_id']:r for r in read(BASE/'seeds_6.json')};recipe={r['slot_id']:r for r in rows(BASE/'request_recipe_12.jsonl')};audits={r['slot_id']:r for r in rows(RUN/'parsed_stages.jsonl') if r['stage']=='audit'}
A=B/'analysis';assert not A.exists();A.mkdir();conditions=[]
for arm in ['R0_REWRITE','R1_AUDIT_REPAIR']:
 r=[J[i] for i,k in K.items() if k['arm']==arm];c=collections.Counter(j['full_context_target_completeness'] for j in r);cl=collections.Counter(j['unsupported_or_distorted_claim'] for j in r)
 conditions.append({'arm':arm,'n':6,'complete':c[1],'incomplete':c[0],'unresolved':c[None],'complete_bounds':[c[1],c[1]+c[None]],'distorted':cl[True],'not_distorted':cl[False],'claim_unresolved':cl[None]})
write(A/'condition_results.json',conditions)
pairs=[];transitions=[];diag=[];quote_rows=[]
# Manually selected audit findings, after all primary judgments were sealed.
findings={
'PRR-001':[('BACKGROUND_EXPANSION',['P4','P5','P6'],'이미 완수였던 seed에 배경 도표·복수 Session 설명 추가를 요구한다. 최종 설명은 완수를 유지했지만 이 확장은 완수 회복이 아니다.')],
'PRR-009':[('UNRESOLVED_CONDITION_UNFLAGGED',['P1','P2','P3'],'능력 보유를 제어의 필요조건으로 읽는 미확정 논점은 지적하지 않고 PRESERVED로 처리했다. 최종 설명도 미확정으로 남았다.')],
'PRR-003':[('MISSED_MODAL_DISTORTION',['P1','P2'],'should가 저장해야 한다로 강화된 초안을 PRESERVED로 처리했고 수정은 같은 의무 표현을 유지했다.'),('MISSED_COMPOUND_OMISSION',['P8'],'eCall에서 비저장·임시 저장이 빠진 초안을 PRESERVED로 처리했다. 추가 항목 A3는 TS 31.102 조건만 강조했고 핵심 누락은 남았다.')],
'PRR-006':[('MISSED_MODAL_DISTORTION',['P1'],'저장되어야 하며라는 의무화를 PRESERVED로 처리했다. 최종 설명은 can으로 바뀌어 왜곡 true는 없어졌지만 should 권고는 여전히 누락됐다.'),('MISSED_COMPOUND_OMISSION',['P9'],'eCall 임시 저장 누락을 PRESERVED로 처리했지만 최종 재작성에서는 비저장·임시 저장·삭제 사건이 복원됐다. 이를 대조의 정확한 지적에 따른 성공으로 세지 않는다.'),('CONTRADICTORY_AUDIT',['P4','P5','P6'],'체크 목록은 PLMN identity·HPLMN·매핑을 PRESERVED로 표시하면서 additional_source_findings A3/A4/A5는 같은 내용을 OMITTED로 표시한다. source_quotes 또는 모호한 저장 방식 문구가 실제 보존의 증거는 아니다.'),('FALSE_OMISSION',['A1'],'비SNPN 범위는 초안 첫 문장에 이미 있는데 추가 항목 A1이 OMITTED로 표시한다.')],
'PRR-010':[('DETECTED_AND_REPAIRED',['P1','P3'],'망 검증 설정과 NR 위성 범위 누락을 대조가 지적했고 최종 설명에서 둘 다 복원됐다.'),('DISTORTED_REPAIR_ADVICE',['P4'],'원문의 should reject를 NAS request를 거절해야 한다고 추가하라는 수정 지시로 강화했다. 이 위험한 지시는 이 최종 설명에는 반영되지 않았다.')],
'PRR-012':[('DETECTED_BUT_NOT_REPAIRED',['P5'],'망 검증 설정 누락을 OMITTED로 정확히 지적했지만 최종 설명에는 여전히 없다.'),('MISSED_MODAL_DISTORTION',['P1'],'초안의 should not 강제 금지화를 PRESERVED로 처리했다. 최종 설명에도 강제 금지가 남았다.'),('DISTORTED_ADVICE_APPEARS_IN_FINAL',['P3'],'대조가 should reject를 NAS 요청을 거절해야 한다는 의무로 추가하도록 지시했고 최종 설명에 그 의무 표현이 나타났다. 지시와 출력의 연결은 관찰했지만 내부 인과는 확정하지 않는다.')]}
for cid in ['CTX-001','CTX-002','CTX-003']:
 for rep in [1,2]:
  ids={k['arm']:rid for rid,k in K.items() if k['case_id']==cid and k['replicate']==rep};r0=ids['R0_REWRITE'];r1=ids['R1_AUDIT_REPAIR'];sid=recipe[K[r1]['slot_id']]['seed_id'];seed=seeds[sid];old=O[OK[sid]['review_id']]
  pairs.append({'case_id':cid,'seed_replicate':rep,'seed_id':sid,'seed_review_id':old['review_id'],'seed_complete':old['full_context_target_completeness'],'R0_review_id':r0,'R0_complete':J[r0]['full_context_target_completeness'],'R1_review_id':r1,'R1_complete':J[r1]['full_context_target_completeness']})
  for orig,new in zip(old['requirement_coverage'],J[r1]['requirement_coverage']):
   assert orig['requirement_id']==new['requirement_id'];a,b=orig['value'],new['value'];label='UNRESOLVED' if a is None or b is None else {(0,0):'STILL_INCOMPLETE',(0,1):'RECOVERED',(1,0):'REGRESSED',(1,1):'PRESERVED'}[(a,b)]
   transitions.append({'review_id':r1,'requirement_id':new['requirement_id'],'seed_value':a,'repaired_value':b,'transition':label,'seed_rationale':orig['rationale'],'repaired_rationale':new['rationale']})
  audit=audits[K[r1]['slot_id']]['parsed'];check_ids=[x['proposition_id'] for x in audit['checks']];expected=[x['id'] for x in seed['propositions']['propositions']]
  sources=[seed['source_input']['target_text']]+seed['source_input']['context_quotes'];draft=seed['draft']['explanation_ko'];all_items={x['proposition_id']:x for x in audit['checks']+audit['additional_source_findings']}
  for group,items in audit.items():
   for item in items:
    q=item['source_quote'];e=item['explanation_quote'];quote_rows.append({'review_id':r1,'group':group,'proposition_id':item['proposition_id'],'source_quote':q,'source_exact':bool(q) and any(q in s for s in sources),'source_whitespace_normalized':bool(q) and any(' '.join(q.split()) in ' '.join(s.split()) for s in sources),'explanation_quote':e,'explanation_quote_nonempty':bool(e),'explanation_exact':bool(e) and e in draft})
  f=[]
  for kind,refs,reason in findings[r1]:
   f.append({'kind':kind,'audit_item_ids':refs,'audit_item_evidence':[all_items[i] for i in refs],'manual_rationale':reason,'seed_explanation_quote':draft,'final_explanation_quote':P[r1]['explanation_ko']})
  diag.append({'review_id':r1,'seed_id':sid,'reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'expected_ids':expected,'actual_ids':check_ids,'all_ids_once':collections.Counter(check_ids)==collections.Counter(expected),'audit_output':audit,'manual_findings':f})
write_rows(A/'paired_results_6.jsonl',pairs);write_rows(A/'seed_to_repair_requirements_18.jsonl',transitions);write_rows(A/'audit_diagnostics_6.jsonl',diag);write_rows(A/'quote_diagnostics.jsonl',quote_rows)
a,b=conditions;criteria={'all_18_returned_and_12_usable':read(RUN/'manifest.json')['explanations']==12,'robust_completeness_gain':b['complete']>a['complete_bounds'][1],'no_distortion_upper_bound_increase':b['distorted']+b['claim_unresolved']<=a['distorted'],'no_R0_complete_regression':not any(p['R0_complete']==1 and p['R1_complete']!=1 for p in pairs),'no_original_complete_regression':not any(p['seed_complete']==1 and p['R1_complete']!=1 for p in pairs)}
summary={'status':'BOUNDED_REPAIR_TEST_AND_FIRST_REVIEW_COMPLETE','candidate_status':'FIRST_REVIEW_CANDIDATE' if all(criteria.values()) else 'IMPROVEMENT_NOT_CONFIRMED','criteria':criteria,'prior_hold_unchanged':True,'independent_review':False,'seed_to_R1_transitions':dict(collections.Counter(x['transition'] for x in transitions)),'audit_item_counts':{'checks':sum(len(d['audit_output']['checks']) for d in diag),'additional':sum(len(d['audit_output']['additional_source_findings']) for d in diag),'all_six_id_sets_complete':all(d['all_ids_once'] for d in diag)},'quote_counts':{'total':len(quote_rows),'source_exact':sum(q['source_exact'] for q in quote_rows),'source_whitespace_normalized':sum(q['source_whitespace_normalized'] for q in quote_rows),'explanation_nonempty':sum(q['explanation_quote_nonempty'] for q in quote_rows),'explanation_exact':sum(q['explanation_exact'] for q in quote_rows)},'limits':'Audit self-labels are not ground truth. Manual findings are bounded diagnostic examples, not exhaustive audit accuracy measurement. Fixed known seeds; no end-to-end or generalization claim.'}
write(A/'summary.json',summary)
write(A/'analysis_manifest.json',{'sealed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'primary_manifest_sha256':sha(B/'primary_review/reviewer_manifest.json'),'source_primary_manifest_sha256':sha(OLD/'primary_review/reviewer_manifest.json'),'script_sha256':sha(Path(__file__)),'file_sha256':{p.name:sha(p) for p in A.iterdir()}})
for p in A.iterdir():p.chmod(0o444)
Path(__file__).chmod(0o444)
print(json.dumps({'conditions':conditions,'summary':summary},ensure_ascii=False))
