"""Manual primary judgments selected before opening current audit outputs or condition keys."""
from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'outputs/review/preservation_repair_v1_20260914';P={r['review_id']:r for r in map(json.loads,(B/'primary_packets_12.jsonl').read_text().splitlines())}
D={
1:([1,1],False,['선택적 능력 보유와 필수 보유·행사가 아님을 명시하며 마지막 문장도 가능성을 덧붙인다.','한 Session에서 두 UPF 모두를 제어하는 능력을 보존한다.'],'문맥의 복수 Session 예시와 단일 Session의 선택적 능력을 구분한다.'),
2:([0,1,1,0],True,['저장되어야 하며로 저장 권고를 의무화한다.','SUPI 동반 저장과 일치 시 사용·불일치 삭제를 보존한다.','긴급 비저장·임시 저장·등록 해제 삭제를 보존한다.','eCall은 세 삭제 사건만 명시한다. 긴급 조건에 한정된 비저장·임시 저장을 eCall에 연결하지 않는다.'],'should를 저장 의무로 강화했다.'),
3:([0,1,1,0],True,['저장해야 하며로 저장 권고를 의무화한다.','SUPI 동반 저장·일치 사용·불일치 삭제를 보존한다.','긴급 비저장·임시 저장·등록 해제 삭제를 보존한다.','eCall 조건과 삭제 사건은 있지만 eCall의 비저장·임시 저장은 누락한다.'],'should 저장 권고를 의무로 강화했다. partially allowed NSSAI의 저장도 같은 대상이라고 묶었지만 근거는 제공 문맥에 있다.'),
4:([None,0,0],None,['비권고와 위치 정확도의 예외는 보존하지만 PLMN이 운용되지 않는 지역을 사실상 비운용 지역으로 읽을지 운용 불허 지역의 축약으로 읽을지 미확정이다.','NR 위성 접속 범위를 누락한다.','망의 검증 설정 조건을 누락한다.'],'운용되지 않는과 운용이 허용되지 않는의 의미 범위가 일치하는지 미확정으로 남긴다. 위치조건 충족 뒤 거절·해제를 강제하지는 않는다.'),
5:([1,1],None,['선택적 능력 보유를 명시한다.','단일 Session에서 두 UPF를 함께 제어하는 능력을 보존한다.'],'능력을 가진 경우에만 제어할 수 있다는 추가 설명은 능력의 뜻을 풀어 쓴 것으로도 원문에 없는 실행 필요조건으로도 읽힌다. 이전 동일 논점과 같이 미확정이다.'),
6:([0,1,1,1],False,['저장될 수 있으며로 설명해 should 저장 권고를 누락한다.','SUPI 동반 저장·일치 시 사용·불일치 삭제를 보존한다.','긴급과 eCall에 공통인 비저장·임시 저장을 명시하고 긴급 등록 해제 삭제를 연결한다.','공통 비저장·임시 저장과 eCall의 세 삭제 사건을 연결한다.'],'저장 가능 표현은 제공 문맥의 can에 근거가 있다. 권고 누락은 완수 실패이며 추가 허구 주장으로 확정하지 않는다.'),
7:([1,1],False,['능력이 선택적으로 존재할 수 있음을 명시하고 필수 보유·행사가 아님을 보존한다.','단일 Session에서 두 UPF를 제어하는 능력을 보존한다.'],'추가 허용이나 의무를 만들지 않는다.'),
8:([0,1,1,0],True,['저장되어야 하며로 should를 의무화한다.','SUPI 동반 저장·일치 시 사용·불일치 삭제를 보존한다.','긴급 비저장·임시 저장·등록 해제 삭제를 보존한다.','같은 비저장 원칙과 세 삭제 사건은 있지만 eCall에서 ME 임시 저장한다는 설명은 없다.'],'저장 권고를 의무로 강화했다.'),
9:([1,1],None,['may의 능력 보유 선택성을 명시한다.','단일 Session에서 두 UPF를 함께 제어하는 능력을 명시한다.'],'능력 보유 SMF에 한해 구성이 가능하다는 문장은 능력의 의미를 풀어 쓴 것인지 추가 실행 제한인지 미확정이다. 이전 필요조건 논점과 일관되게 남긴다.'),
10:([1,1,1],False,['하지 않는 권고와 정확한 위치정보가 있을 때 그 권고가 적용되지 않는 관계를 보존한다.','NR satellite access의 위치 검증을 명시한다.','규제 준수를 위한 망의 선택적 위치 검증 설정과 Mobility/Session Management 문맥을 명시한다.'],'제공된 ULI·UE capability와 위치 검증 문맥을 설명하며 NAS 거절 의무나 권고의 강한 필요조건을 만들지 않는다.'),
11:([None,1,0],None,['첫 문장의 강한 금지와 둘째 문장의 권고가 함께 있어 전체 강도가 미확정이다. 운용되지 않는 지역도 불허 지역의 축약인지 미확정이다.','NR satellite access에서의 위치 검증 문맥을 보존한다.','망의 검증 설정 조건을 누락한다.'],'금지와 권고의 병치 및 운용되지 않는의 범위를 확정하지 않는다.'),
12:([0,1,0],True,['해서는 안 된다는 강한 금지를 두 번 쓰고 권고임을 설명하지 않는다.','NR satellite access에서의 위치 검증 문맥을 보존한다.','망의 검증 설정 조건을 누락한다.'],'should not의 강제 금지화에 더해 문맥의 should reject를 NAS 요청을 거절해야 한다는 의무로 강화한다.')}
O=B/'primary_review';assert not O.exists();O.mkdir();R=[]
for n,(v,cl,why,cr) in D.items():
 p=P[f'PRR-{n:03d}'];assert len(v)==len(p['requirements'])==len(why)
 cov=[{'requirement_id':q['id'],'value':x,'response_quotes':[p['explanation_ko']],'source_quotes':[p['target_text']]+[b['quote'] for b in p['reference_context_blocks']],'rationale':reason} for q,x,reason in zip(p['requirements'],v,why)]
 score=0 if 0 in v or cl is True else None if None in v or cl is None else 1
 R.append({'review_id':p['review_id'],'reviewer':'coordinator_ai','reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'requirement_coverage':cov,'unsupported_or_distorted_claim':cl,'claim_evidence_quotes':[p['explanation_ko']] if cl is not False else [],'claim_rationale':cr,'full_context_target_completeness':score,'sentence_count_diagnostic':{'sentence_count':4 if n in [2,3,8] else 3,'within_2_to_4':True},'metadata_and_citation_audit':'NOT_SCORED_SEPARATE_FROM_PRIMARY','overall_rationale':' / '.join(why)+' '+cr})
p=O/'judgments_12.jsonl';p.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in R))
(O/'review_notes.md').write_text('# 진행 AI의 1차 검토\n\n새 최종 설명 12개를 원문·동일 요구사항에 대조하여 수동 판정했다. 새 audit 출력과 조건 키는 아직 열지 않았다. 이전 초안·점수·설계를 알고 있으므로 독립/완전 눈가림 평가가 아니다. PRR-005·009의 능력 보유 필요조건 논점과 PRR-004·011의 비운용/불허 범위 및 금지/권고 관계를 미확정으로 남겼다. 이전 초안 판정은 변경하지 않았다.\n')
m={'sealed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'input_sha256':hashlib.sha256((B/'primary_packets_12.jsonl').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'file_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in O.iterdir()},'manual_semantic_review':True,'independent_review':False,'new_audit_not_read_before_seal':True}
(O/'reviewer_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
for p in O.iterdir():p.chmod(0o444)
Path(__file__).chmod(0o444)
print(json.dumps({'status':'PRIMARY_SEALED','records':12,'requirements':36}))
