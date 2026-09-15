from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; B=R/'experiments/error_replication_v1_20260914'; O=R/'outputs/review/error_replication_v1_20260914'; run=R/'experiments/runs/error_replication_remaining8_20260914'
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
for folder in [R/'experiments/runs/error_replication_v1_20260914',run]:
 for n,digest in read(folder/'output_freeze_manifest.json')['file_sha256'].items():assert h(folder/n)==digest
for p,digest in read(B/'input_freeze_manifest.json')['file_sha256'].items():assert h(R/p)==digest
refs={x['case_id']:x for x in read(B/'evaluation_reference.json')['cases']}
data=[json.loads(l) for l in (run/'parsed_responses.jsonl').read_text().splitlines()]
manual={
'ERR-CTX-002-R1':([1,1,1,1],False,'비SNPN 저장 권고·SUPI 결합 및 불일치 삭제·긴급 등록과 eCall 각각의 비저장/임시 저장/삭제 사건을 설명에 보존했다. 저장 SUPI의 지시 대상은 앞 문장에서 복원 가능하다.'),
'ERR-CTX-003-R1':([0,1,0],True,'should not을 “등록해제해서는 안 된다”로 강제 금지화했다. 위성 접속 범위는 있으나 망이 검증하도록 설정된 경우라는 조건은 없다.'),
'ERR-CTX-001-R2':([1,1],False,'“능력을 가질 수도 있다”, “선택적으로 존재”가 능력 보유의 선택성을 보존하며 하나의 세션에서 두 UPF 모두를 명시한다. 메타데이터 capability만으로 설명을 실패 처리하지 않는다.'),
'ERR-CTX-002-R2':([1,1,1,0],False,'“저장해야 한다는 권고”는 권고임을 명시하므로 의무화로 단정하지 않는다. 긴급 등록의 비저장·임시 저장 뒤 eCall에는 삭제 사건만 기술하고 eCall 자체의 비저장 및 임시 저장 규칙은 보존하지 않았다.'),
'ERR-CTX-003-R2':([0,1,0],True,'첫 문장의 “있을 때에만 ... 등록해제해야 한다”는 원문의 비권고/예외를 처리 의무로 바꾼다. 뒤의 비권고 설명이 이 적극적 의무를 철회하지 않는다. 위성 범위는 있고 망 검증 설정 조건은 빠졌다.'),
'ERR-CTX-001-R3':([1,1],False,'능력을 가질 수도 있고 보유가 선택적이라고 명시하며 하나의 세션에서 양 UPF를 보존한다. 마지막 허용 부정은 제어 행동 허가와 능력 보유를 구분하는 문맥으로, 앞의 선택성을 철회하지 않는다.'),
'ERR-CTX-002-R3':([1,1,1,0],False,'should 권고와 SUPI 조건, 긴급 등록 예외를 보존한다. eCall 비저장·삭제 사건은 있으나 eCall 시 ME 임시 저장이 설명에서 빠졌다. action/exception 메타데이터의 임시 저장 표현으로 설명의 누락을 복구하지 않는다.'),
'ERR-CTX-003-R3':([0,1,0],True,'“등록해제해서는 안 된다”가 should not을 강제 금지로 바꾼다. 위성 접속 범위는 있으나 망 검증 설정이라는 적용 조건은 없다.')}
judgments=[]
for r in data:
 scores,distorted,reason=manual[r['slot_id']];ref=refs[r['case_id']]
 assert len(scores)==len(ref['requirements'])
 judgments.append({'slot_id':r['slot_id'],'case_id':r['case_id'],'response_id':r['response_id'],'request_sha256':r['request_sha256'],'explanation_ko':r['parsed']['explanation_ko'],'source':ref['source'],'requirements':dict(zip([x['id'] for x in ref['requirements']],scores)),'distorted':distorted,'complete':0 if 0 in scores or distorted else 1,'reason_ko':reason,'reviewer':'Current same Codex; manual first review, prior results known; not independent or delayed review','reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()})
assert len(judgments)==8
(O/'judgments_8.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in judgments))
lines=['# 추가 오류 재현 결과','', '기존 개발 원문 3개에 동일 A2 요청을 각 3회 계획했다. 9개 중 첫 SMF 슬롯은 통신 결과 미상이며 재시도하지 않았다. 승인 후 나머지 8개를 실행해 모두 정상 응답을 받았다. 결과 미상 1건은 의미 실패와 구분하며 9개 전체의 완수율을 산출하지 않는다. 완료 응답 8개는 완수 3개·미완수 5개·미확정 0개다. 동일 진행 AI의 수동 1차 판정으로 독립 전문가 검증이 아니다.','', '| 원문 | 계획 | 완료 | 완수 | 미완수 | 결과 미상 |','|---|---:|---:|---:|---:|---:|','| SMF | 3 | 2 | 2 | 0 | 1 |','| NSSAI | 3 | 3 | 1 | 2 | 0 |','| AMF | 3 | 3 | 0 | 3 | 0 |','', 'AMF 3개 모두 규범 강도 변경과 망 검증 설정 조건 누락이 관찰됐다. NSSAI 3개 중 2개는 eCall 복합 예외의 일부가 누락됐다. 이것은 알려진 3개 원문 내 반복 관찰이며 일반 오류율이나 새 조항 검증이 아니다. temperature 0에서도 실제 문구가 달랐으며 독립 표본으로 간주하지 않는다. 프롬프트 수정·재시도·성공 결과 선별 없이 전체 완료 출력을 평가했다.','', '8개 정상 응답의 반환 usage 기준 비용은 $0.01865325다. 최초 결과 미상 요청의 비용은 확인되지 않아 전체 실제 청구액은 미확정이다.','']
for j in judgments:
 lines += ['## '+j['slot_id'],'','출처: '+j['source']['spec_id']+' §'+j['source']['clause_id'],'','원문: '+j['source']['source_text_en'],'','실제 설명: '+j['explanation_ko'],'','판정: '+str(j['complete'])+' / '+j['reason_ko'],'']
(O/'results.md').write_text('\n'.join(lines))
summary={'planned':9,'completed':8,'transport_unknown':1,'complete':3,'incomplete':5,'unresolved_semantics':0,'observed_cost_usd':read(run/'manifest.json')['known_cost_usd'],'total_billing_known':False,'primary49_unchanged':True,'review_status':'SAME_AI_FIRST_REVIEW_COMPLETE','all_outputs_retained':True}
(O/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(O/'review_seal.json').write_text(json.dumps({'sealed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'file_sha256':{n:h(O/n) for n in ['judgments_8.jsonl','results.md','summary.json']}},indent=2)+'\n')
print(json.dumps(summary))
