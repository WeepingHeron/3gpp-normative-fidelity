"""Manual requirement-level audit review; counts derive only from explicitly recorded decisions."""
from pathlib import Path
import json,hashlib,datetime,collections
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'outputs/review/atomic_audit_v1_20260914'
def rows(p):return list(map(json.loads,p.read_text().splitlines()))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def write(p,o):p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
P={r['review_id']:r for r in rows(B/'review_packets_12.jsonl')};K={r['review_id']:r for r in rows(B/'coordinator_keys_12.jsonl')}
# For reference=0: detection 1 only if actual defect correctly identified. None denotes not applicable on ref=1.
# False alarm means asserting a missing/distorted preserved requirement, including conflicting additional rows.
D={
1:([None,1,1],[0,0,0],[['P6-MOD-1','P6-EXC-1'],['P3-SCP-1'],['P1-MOD-1','P1-SCP-1','P1-SCP-2']],['비권고와 unless 관계를 정확히 보존으로 표시한다.','NR 위성 접속의 NGAP 수신 범위 누락을 정확히 지적한다.','망의 선택적 검증 설정과 절차 범위 누락을 정확히 지적한다.']),
2:([0,None,None,0],[0,0,0,0],[['P1-MODALITY-1'],['P3-SCOPE-1','P7-SCOPE-1','P7-EXCEPTION-1'],['P8-MODALITY-1','P8-FOLLOWUP-1','P8-FOLLOWUP-2'],['P9-FOLLOWUP-1']],['should 의무화를 MODALITY 항목에서도 PRESERVED로 오판한다.','SUPI 동반 저장·일치 사용·불일치 삭제의 누락을 주장하지 않는다.','긴급 비저장·임시 저장·등록 해제 삭제를 보존으로 표시한다.','긴급 조건의 임시 저장 문장을 eCall의 임시 저장 근거로 가져와 누락을 놓쳤다.']),
3:([None,None],[0,0],[['C1','C2'],['C2','C3']],['선택적 능력 보유를 보존으로 판단한다. C4의 EXCEPTION 분류는 부정확하지만 필수 능력 보유 오류를 주장하지는 않는다.','한 Session의 두 UPF를 제어하는 능력을 보존으로 표시한다.']),
4:([0,None,None,0],[0,0,0,0],[['P1-MODALITY','P2-MODALITY'],['P3-SCOPE','P6-SCOPE','P6-EXCEPTION'],['P7-EXCEPTION','P7-FOLLOWUP'],['P8-EXCEPTION','P8-FOLLOWUP']],['should가 저장해야 한다로 변했는데 보존이라고 한다.','SUPI 결합과 일치/불일치 관계를 보존으로 판단한다.','긴급 예외를 보존으로 판단한다.','eCall의 비저장·임시 저장 누락을 놓치고 설명에 없는 인용을 제시한다. 비저장 인용은 메타데이터 action/exception에만 존재한다.']),
5:([0,None,0],[0,0,0],[['P1-M1'],['P2-S1'],['P5-M1','P5-A1']],['should not 강제 금지화를 MODALITY에서 보존으로 판단한다.','위성 범위를 보존으로 표시한다.','망 설정에 UNRESOLVED를 붙이고 설명에서 다루지 않아도 된다고 하므로 기존 필수 누락을 정확히 지적한 것으로 세지 않는다.']),
6:([None,None],[0,0],[['P1'],['P1']],['선택적 능력 보유 자체는 보존으로 판단한다. 추가 실행 필요조건이라는 미확정 주장은 지적하지 않는다.','단일 Session의 두 UPF 모두를 보존으로 판단한다.']),
7:([0,None,None,0],[0,0,0,0],[['P1'],['P3','P7'],['P8'],['P9']],['저장되어야 한다를 보존으로 처리한다. A1의 비SNPN 누락 주장은 이미 있는 범위를 빠졌다고 한 추가 오탐이지만 실제 저장 권고 왜곡은 발견하지 않는다.','SUPI 조건은 보존으로 처리한다.','긴급 예외를 보존으로 처리한다.','eCall 임시 저장 누락을 보존으로 처리한다.']),
8:([0,None,None,0],[0,1,1,0],[['P1','P2','A2'],['P6','A3'],['P7','A4'],['P8','A5']],['대상 should 의무화를 지적하지 않는다. can을 반영하라는 추가 문구는 권고 오류를 특정하지 않는다.','P6은 보존이라고 하면서 A3에서 이미 명확한 일치 사용·불일치 삭제를 누락으로 표시하여 오탐이다.','P7은 보존이라고 하면서 A4는 이미 있는 긴급 비저장·임시 저장·삭제를 누락이라 표시한다.','P8은 eCall을 보존이라고 하고 A5는 이미 있는 삭제 사건을 추가하라고 한다. 실제 빠진 비저장·임시 저장은 찾지 못한다.']),
9:([None,1,1],[0,0,0],[['P6'],['P3'],['P1','A1']],['비권고와 unless를 보존으로 표시한다.','위성 접속 위치 검증 누락을 지적한다.','망의 검증 설정 누락을 지적한다.']),
10:([0,None,1],[0,0,0],[['P1'],['P2'],['P5']],['강제 금지로 바뀐 초안을 보존으로 처리한다.','위성 접속 문맥을 보존으로 처리한다.','망의 검증 설정 누락을 정확히 지적한다.']),
11:([None,None],[0,0],[['P1'],['P1']],['선택적 능력 보유를 보존으로 처리한다. P2/P3의 원문 지원 미확정은 추출 명제 진단이며 설명의 필수 요건 오탐으로 세지 않는다.','두 UPF와 단일 Session을 보존으로 처리한다.']),
12:([None,None],[0,0],[['P1-MODALITY-1'],['P1-ACTOR_ACTION-1','P1-SCOPE_CONDITION-1']],['선택적 능력 보유 자체를 보존으로 판단하지만 추가 조건의 미확정은 지적하지 않는다.','두 UPF와 단일 Session을 보존으로 판단한다.'])}
O=B/'manual_review';assert not O.exists();O.mkdir();out=[]
for n,(det,false,refs,reasons) in D.items():
 rid=f'AAR-{n:03d}';p=P[rid];items={x.get('check_id',x['proposition_id']):x for g in p['audit'].values() for x in g};requirements=[]
 for old,d,f,ids,why in zip(p['sealed_seed_judgment']['requirement_coverage'],det,false,refs,reasons):
  assert (old['value']==0)==(d is not None)
  requirements.append({'requirement_id':old['requirement_id'],'reference_value':old['value'],'defect_correctly_detected':d,'false_alarm_on_preserved_requirement':bool(f),'audit_evidence_ids':ids,'audit_evidence':[items[i] for i in ids],'rationale':why,'reference_rationale':old['rationale']})
 bad=n in [5,9,10];advice={5:'P3-M1把should reject를 거절해야 한다로 강화하고 P5-M1에서 필요한 망 설정 문맥을 다루지 않아도 된다고 한다.',9:'P4는 should reject를 거절해야 한다로 강화한 수정을 요구한다.',10:'A1은 should reject를 거절해야 한다로 강화한다.'}.get(n,'확인된 규범 강화·필수 조건 삭제 지시는 없다. 배경 설명 확장 요구는 별도 진단이다.')
 if n==5:advice='P3-M1은 should reject를 거절해야 한다로 강화하고 P5-M1에서 필요한 망 설정 문맥을 다루지 않아도 된다고 한다.'
 out.append({'review_id':rid,'reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'coordinator_ai','requirements':requirements,'erroneous_repair_advice_case':bad,'repair_advice_rationale':advice,'unresolved_seed_claim_adequately_flagged':False if p['sealed_seed_judgment']['unsupported_or_distorted_claim'] is None else None,'limits':'Known AI reference labels, single coordinator; schema reveals arm. Findings are manual, never inferred from keyword presence.'})
(O/'judgments_12.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in out))
write(O/'reviewer_manifest.json',{'sealed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'input_sha256':sha(B/'review_packets_12.jsonl'),'script_sha256':sha(Path(__file__)),'file_sha256':{p.name:sha(p) for p in O.iterdir()},'manual_semantic_judgments':True,'independent_review':False})
for p in O.iterdir():p.chmod(0o444)
Path(__file__).chmod(0o444)
conditions=[]
for arm in ['C0_COARSE','C1_ATOMIC']:
 rr=[r for r in out if K[r['review_id']]['arm']==arm];q=[q for r in rr for q in r['requirements']];ds=[d for d in rows(B/'structural_diagnostics_12.jsonl') if K[d['review_id']]['arm']==arm];items=[i for d in ds for i in d['items']]
 conditions.append({'arm':arm,'audits':6,'known_requirement_defects':sum(q['reference_value']==0 for q in q),'correctly_detected_defects':sum(q['defect_correctly_detected']==1 for q in q),'preserved_requirements':sum(q['reference_value']==1 for q in q),'false_alarms_on_preserved_requirements':sum(q['false_alarm_on_preserved_requirement'] for q in q),'erroneous_repair_advice_cases':sum(r['erroneous_repair_advice_case'] for r in rr),'known_unresolved_claim_cases':sum(r['unresolved_seed_claim_adequately_flagged'] is not None for r in rr),'unresolved_claims_adequately_flagged':sum(r['unresolved_seed_claim_adequately_flagged'] is True for r in rr),'structural':{'audit_items':len(items),'source_exact':sum(i['source_exact'] for i in items),'source_whitespace_normalized':sum(i['source_whitespace_normalized'] for i in items),'explanation_nonempty':sum(i['explanation_nonempty'] for i in items),'explanation_exact':sum(i['explanation_exact'] for i in items),'all_propositions_covered':all(not d['missing_proposition_ids'] for d in ds)}})
A=B/'analysis';A.mkdir();write(A/'condition_results.json',conditions);a,b=conditions;criteria={'more_defects_detected':b['correctly_detected_defects']>a['correctly_detected_defects'],'no_increase_false_alarms':b['false_alarms_on_preserved_requirements']<=a['false_alarms_on_preserved_requirements'],'no_increase_erroneous_advice_cases':b['erroneous_repair_advice_cases']<=a['erroneous_repair_advice_cases']};write(A/'summary.json',{'status':'AUDIT_VALIDATION_COMPLETE','candidate_status':'FIRST_REVIEW_AUDIT_CANDIDATE' if all(criteria.values()) else 'IMPROVEMENT_NOT_CONFIRMED','candidate_checks':criteria,'prior_hold_unchanged':True,'new_final_explanations':0,'independent_review':False,'semantic_scores_automatically_inferred':False})
print(json.dumps({'conditions':conditions,'criteria':criteria},ensure_ascii=False))
