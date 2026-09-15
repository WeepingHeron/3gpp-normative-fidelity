from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];B=R/'outputs/review/error_replication_v1_20260914';O=R/'outputs/review/error_recheck_v2_20260914';O.mkdir(exist_ok=True)
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for n,d in json.loads((B/'review_seal.json').read_text())['file_sha256'].items():assert h(B/n)==d
j=[json.loads(x)for x in (B/'judgments_8.jsonl').read_text().splitlines()]
raw={x['slot_id']:x for x in map(json.loads,(R/'experiments/runs/error_replication_remaining8_20260914/parsed_responses.jsonl').read_text().splitlines())}
cases=json.loads((R/'experiments/error_replication_v1_20260914/generator_inputs.json').read_text())
for c in cases:
 for block in c['context_blocks']:assert h(R/block['page_text_path'])==block['page_text_sha256']
notes={
'ERR-CTX-001-R2':'전체 설명이 능력 보유의 선택성과 한 세션의 양 UPF를 모두 명시한다. 두 세션의 배경과 한 세션의 대안도 구분한다. metadata capability는 별도 진단이며 설명 실패 사유가 아니다.',
'ERR-CTX-001-R3':'마지막의 의무나 허용 부정이 앞의 선택적 능력 보유를 철회하는지 검토했다. 능력 보유가 선택적이라고 두 번 명시하므로 행위 허가와 구분하는 설명으로 읽힌다. 선택성 보존을 유지한다.',
'ERR-CTX-002-R1':'첫 문장의 함께 저장한 SUPI가 뒤의 일치 조건 비교 대상으로 복원된다. 긴급 등록과 eCall 각각의 비저장·임시 저장·삭제 조건이 명시된다. PLMN/HPLMN 매핑 등 문맥 전체의 모든 규칙을 망라했다는 성공은 아니며 동결된 네 요구사항에 대한 성공이다.',
'ERR-CTX-002-R2':'저장해야 한다는 권고는 권고임을 명시하므로 강도 오류로 세지 않는다. 긴급 등록인 경우의 비저장·임시 저장 뒤 eCall 모드에서는이라는 새 범위가 시작되며 삭제 사건만 따른다. 두 모드 모두/마찬가지라는 연결도 없어 앞 범위의 저장 방식을 eCall로 확장하려면 독자가 규칙을 보충해야 한다. 고정 복합 요구사항 아래 eCall=0 유지, 별도 왜곡은 확정하지 않는다.',
'ERR-CTX-002-R3':'eCall의 비저장 및 세 삭제 사건은 보존되지만 임시 저장은 긴급 등록 절에만 있다. 마지막에 삭제한다는 말로 어디에 어떤 방식으로 보관했는지 유일하게 복원할 수 없다. 원문은 eCall에도 별도로 temporarily store locally in ME를 명시한다. action/exception에 임시 저장이 있는 것은 확인했으나 채점 면은 explanation_ko이다.',
'ERR-CTX-003-R1':'앞뒤 문장 어디에도 권고 한정이 없어 해서는 안 된다를 should not과 동일하게 보지 않는다. 충분한 위치정보 및 위성 범위는 설명되지만 network may be configured라는 설정 조건은 별도 고정 요구사항에서 빠진다. 설정 누락은 이 범위 보존 기준의 누락이며 응답이 모든 망에 검증 의무를 명시했다고 확대하지 않는다.',
'ERR-CTX-003-R2':'둘째 문장의 해서는 안 된다고 권고된다만으로 실패 처리하지 않았다. 첫 문장의 등록해제해야 한다는 적극적 의무는 뒤 문장이 철회하지 않으며 원문의 may initiate deregistration과 다르다. 조건 제한을 적극적 처리 의무로 바꾼 점과 설정 범위 누락으로 미완수를 유지한다.',
'ERR-CTX-003-R3':'마지막 고려할 수 있다는 표현은 정확한 위치를 안 뒤의 처리 재량을 남기지만, 위치 미확보 시 강제 금지를 권고로 한정하지 않는다. 위성 범위는 보존했고 망의 설정 조건은 미보존이다. 위치 판단이라는 일반 문구만으로 사전 지정 설정 요구사항을 충족시키지 않는다.'}
new=[]
for x in j:
 assert x['explanation_ko']==raw[x['slot_id']]['parsed']['explanation_ko']
 new.append({**x,'previous_review_sha256':h(B/'judgments_8.jsonl'),'recheck_reason_ko':notes[x['slot_id']],'state_changed':False,'reviewer':'Same current Codex; prior labels visible; same-day focused second review, NOT independent, NOT >=24h delayed','rechecked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()})
(O/'rechecked_8.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n'for x in new))
nas='V2-P2-099: 전체 응답에서 엔티티가 무결성 검사를 받은 경우로 서술된다. 원문의 they는 NAS signalling messages를 가리킨다. 뒤의 어떤 NAS 시그널링 메시지도 처리해서는 안 된다는 절은 잘못 지정한 검사 대상을 수정하지 않는다. FAIL 유지. 단순 엔티티는이라는 화제와 검사 대상 생략 사례와 구분한다. 기존 조정 기록을 덮어쓰지 않는다.'
lines=['# 추가 8개 및 본문 오류 사례 재검토','', '같은 날 같은 Codex가 기존 판정을 보며 전체 원문·제공 문맥·전체 설명·메타데이터를 대조했다. 독립 검토나 24시간 지연 검토가 아니다. 새 API 생성은 하지 않았다. 8개는 완수 3·미완수 5·미확정 0으로 유지했고 본문 NAS 사례도 FAIL을 유지했다.','', '## 범위 명확화','', '주 분석 49건의 원래 입력·채점 기준과 점수는 유지한다. 추가 진단의 완수는 사전 동결한 SMF 2개, NSSAI 4개, AMF 3개의 총 9개 요구사항 및 추가 왜곡 여부에 대한 것이다. 문맥 전체의 모든 규칙을 망라한 번역 성능이 아니다. 메타데이터는 설명의 누락을 복구하지 않는다. 복합 요구사항은 비저장·임시 저장·삭제 사건 등 모든 접속항을 확인한다. 명확한 누락은 0, 해석을 확정할 수 없으면 null을 유지한다.','']
for x in new:lines += ['## '+x['slot_id'],'',x['explanation_ko'],'','재검토: '+x['recheck_reason_ko'],'']
lines += ['## 본문 NAS 사례','',nas,'','근거: outputs/review/v2_adjudication_20260909/adjudication_readable.md.','', '## C3 입력 확인','', 'experiments/c3_lib.mjs의 extractionInput은 source_text_en만 전달한다. generationInput은 question_ko·source_text_en·출처 식별자와 자동 추출 여섯 필드를 결합한다. 질문을 사용하지 않는 단계는 추출 단계뿐이다.']
(O/'review.md').write_text('\n'.join(lines))
files=[B/'judgments_8.jsonl',B/'review_seal.json',R/'outputs/review/v2_adjudication_20260909/adjudication_readable.md',R/'experiments/error_replication_v1_20260914/evaluation_reference.json',R/'experiments/c3_lib.mjs',O/'rechecked_8.jsonl',O/'review.md']
(O/'seal.json').write_text(json.dumps({'sealed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'unchanged_decisions':9,'file_sha256':{str(p.relative_to(R)):h(p)for p in files}},indent=2)+'\n')
print('RECHECK_COMPLETE: 8 outputs and 1 NAS case; all decisions retained')
