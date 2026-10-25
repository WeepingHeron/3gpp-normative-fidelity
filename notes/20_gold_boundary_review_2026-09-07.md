# 경계 사례의 gold와 의미 평가 기준 검토

2026-09-07. 상태: `SOURCE_REVIEW_COMPLETE_FOR_LISTED_CASES / RUBRIC_CANDIDATE_NOT_APPLIED`.

이번 작업은 논문 보완의 첫 단계인 정답 라벨·채점 경계 정리다. 기존 경계 사례 5건에 문맥·양화 사례를 더해 확인하고, NOTE 누락 원인을 추적하는 과정에서 추가로 찾은 사례를 포함했다. 아래 9건에 구체적인 처리안을 작성했다. 전체 72건의 새로운 의미 점수, 논문 v5, 새 API 실험은 만들지 않았다. 판정자는 기존 실험을 아는 동일 Codex이며 독립 전문가 합의가 아니다.

## 핵심 결과

1. `MAIN-MAY-001`은 gold_summary에서 capability를 ‘권한’으로 바꿨고, action 필드에서 **능력 보유**를 **제어 행동**으로 평탄화했다. 수정 제안이 필요하다.
2. `MAIN-CAN-004`와 추가 발견한 `MAIN-MAY-005`는 각각 원본의 NOTE 2 안에 있다. 기존 NOTE 제외 규약과 충돌하는 표본 적격성 문제다. 그 문장의 한국어 설명에 대한 단순 성공/실패와 분리해야 한다.
3. `MAIN-CAN-008`은 실제 context 수립이 필요하다는 관계를 채점해야 한다. 첫 문장이 약한 표현이어도 전체 설명이 그 관계를 명확히 복원하면 자동 실패가 아니다.
4. `MAIN-SD-009`의 respectively 대응은 같은 페이지 전후 문맥으로도 단일 연결을 확정하기 어렵다. 모호한 부분을 정답으로 확정해 채점하지 않도록 별도 상태가 필요하다.
5. `MAIN-SDN-010`의 congestion은 추출 입력 문장에 없고 질문과 상위 문맥에 있다. `MAIN-SDN-002`의 2% 부연은 98%와 같은 권고 범위를 설명하는 파생 표현이다. 각각 입력 문맥 부족과 양화 보존으로 분리한다.

기존 v4의 61/72, 71/72, 65/72, 68/72는 덮어쓰지 않았다. 다만 아래 적격성 오류와 gold 쟁점이 해결되기 전에는 ‘72개 적격 사례에서 검증된 확정 성능’으로 승격하면 안 된다. 무결성 해시 일치는 원본의 선정·해석이 옳았다는 뜻이 아니다.

## 확인한 근거

- ETSI TS 123 501 V18.12.0, SHA-256 `2ef71f81a87c86967dc623741b5a3479338844661067a3bb13089fffe6fed2ac`: PDF 45, 51, 75, 76, 119, 192쪽을 텍스트와 렌더 이미지로 확인했다. 인쇄면 번호는 각각 한 쪽 작다.
- ETSI TS 124 501 V18.12.0, SHA-256 `fef06d660506abf6885d593e4129095c17140be4f2317e802daa8599233f1b06`: PDF 53, 69, 133, 197쪽을 텍스트와 렌더 이미지로 확인했다. 132쪽 전후 문맥도 텍스트로 대조했다.
- 동결 `data/main_cases.csv`, `experiments/scoring_v1.md`, `docs/02_dataset_protocol.md`, `docs/06_main_difficulty_protocol.md`.
- v4의 C1/C2/C3 조정 판정과 C1M 첫 판정 및 당시 근거. 새 검토가 행별 조건을 모르는 독립 평가였다고 주장하지 않는다.
- [ETSI 편집 체크리스트](https://portal.etsi.org/Portals/0/TBpages/edithelp/Docs/ETSI_editing_checklist.pdf): 본문 NOTE는 정보 제공이며 requirements를 담지 않도록 안내하고, 표·그림 NOTE는 별도로 취급한다. 모든 NOTE가 항상 비규범적이라는 일반화는 하지 않는다. 이번 적격성 판단의 직접 근거는 이 연구가 사전에 NOTE를 제외한 규약이다.

PDF 원본은 `data/source/ts_123501v181200p.pdf`, `data/source/ts_124501v181200p.pdf`다. 원문 제공 범위와 검토를 위해 추가로 읽은 문맥을 구분한다.

## 사례별 정리

### 1. MAIN-MAY-001: 능력 보유와 행동 허용

- 출처: TS 23.501, 4.2.3, PDF 45쪽의 Figure 4.2.3-3을 설명하는 본문 마지막 문장. NOTE 영역 밖이다.
- 문맥: 서로 다른 PDU Session에 두 SMF를 선택하는 구조를 설명한 뒤, 한 PDU Session에서 각 SMF가 local/central UPF를 모두 제어할 능력을 갖추는 선택지를 덧붙인다.
- 원문의 구문 범위: `each SMF / may / have the capability [to control both a local and a central UPF] / within a PDU Session`.
- 기존 gold_summary는 ‘제어할 수 있는 권한이 있을 수 있다’이고 action은 `control both a local UPF and a central UPF`다. capability는 권한으로 번역하면 안 되고, may가 걸린 능력 보유 상태도 action에서 빠지면 안 된다.
- 제안 action: `have the capability to control both a local and a central UPF within a PDU Session`. actor와 may는 유지하되 nested capability를 별도 명제로 설명한다.
- 제안 한국어 기준: **각 SMF가 하나의 PDU Session에서 local UPF와 central UPF를 모두 제어할 수 있는 능력을 갖추는 것은 선택 사항이다.** 모든 SMF가 이미 그 능력을 보유한다고 단정하거나, 제어 행위에 대한 별도의 권한 부여로 바꾸지 않는다.
- 처리: `GOLD_CORRECTION_PROPOSED`. 기존 C2 성공과 C1M 성공을 수정 gold에서도 그대로 성공이라고 가정하지 않는다. 영향받는 네 조건 모두 같은 기준으로 재검토해야 한다. 문맥상 자연스러운 가능성 표현과 규격 may의 선택성 사이의 경계도 계속 공개한다.

### 2. MAIN-CAN-004: NOTE 영역에서 들어온 표본

- 출처: TS 23.501, 4.2.5, PDF 51쪽 **NOTE 2의 두 번째 문장**. 렌더 이미지에서 NOTE 본문 들여쓰기가 다음 문장까지 이어지는 것을 확인했다.
- 문제: `docs/06_main_difficulty_protocol.md`는 NOTE를 제외한다. 문장 자체에서 NOTE라는 문자열이 떨어져 나가도 적격성이 바뀌지 않는다.
- 의미 진단: ‘권한 있는 NF만 접근할 수 있도록 보장하는 일은 구현·배포에 달려 있다’는 책임 관계와 접근 범위를 보존해야 한다. ‘접근 제한 능력이 있어야 한다’만으로 대체하는 것은 같은 관계가 아니다. 그러나 이 진단을 main의 적격성 판단보다 먼저 적용하지 않는다.
- 처리: `INELIGIBLE_UNDER_ORIGINAL_PROTOCOL`. 기존 기록을 삭제하거나 모델 실패 0으로 바꾸지 않는다. 규약 준수 표본을 보고할 때는 모든 조건에서 동일하게 별도 제외하는 사후 분석으로만 다룬다. 새 표본을 기존 run에 끼워 넣지 않는다.

### 3. MAIN-MAY-005: 같은 원인으로 추가 발견한 NOTE 표본

- 출처: TS 23.501, 4.3.1, PDF 76쪽 **NOTE 2의 두 번째 문장**. interworking 대상이 아닌 UE를 interworking 전용이 아닌 entity가 서비스할 수 있다는 문장이다.
- NOTE는 Figure 4.3.1-1 아래에 있다. 표·그림 주석의 규범성에 대한 일반 법칙을 임의 적용하지 않고, 본 연구의 NOTE 제외 규약에 따라 처리한다.
- 처리: `INELIGIBLE_UNDER_ORIGINAL_PROTOCOL`. CAN-004와 동일한 대칭적 처리 원칙을 적용한다.

### 4. MAIN-CAN-008: 실제 수립과 수립 능력

- 출처: TS 24.501, 4.4.2.1.1, PDF 53쪽 본문. 다음 문장은 보안 context가 생성되는 절차를 설명한다.
- 필수 명제: **AMF와 UE가 5G NAS security context를 실제로 수립하는 것이 security 활성화의 선행 필요조건이다.** 원문이 다른 모든 활성화 조건까지 충분히 열거했다고 보지 않는다.
- `can`은 security의 활성화에 걸리고, `need to establish`는 AMF/UE의 실제 수립 필요를 말한다. 하나의 can 라벨로 문장 전체를 능력 진술로 바꾸면 안 된다.
- C3는 ‘context를 설정할 기술적 가능성’과 ‘이는 전제조건’만 말해 실제 수립을 명시하지 못한다. 기존 실패 근거가 유지된다.
- C1M은 첫 문장에 능력 표현이 있지만, 둘째 문장에서 실제 context establish가 보안 활성화의 전제라고 명시한다. 능력 보유가 필요하다는 약한 진술은 실제 수립 필요와 논리적으로 충돌하지 않는다. **이유 없이 C1M을 실패로 뒤집는 대신, 설명 전체가 실제 수립의 필요조건을 명확히 보존하는지 판정한다.** ‘능력만 있으면 충분’이라고 쓰면 실패다.
- 처리: `GOLD_RELATION_CLARIFICATION`. 실제 수립 전제를 별도 명제로 추가하는 후보안. C1M의 기존 성공은 전체 명제 기준에서 방어 가능한 판정이며 독립 검증 완료는 아니다.

### 5. MAIN-SD-002: should의 적용 대상

- 출처: TS 23.501, 5.4.3.2, PDF 119쪽 본문.
- 구분할 명제: (a) PPD 지원 시 application이 DSCP를 설정해 표시한다. (b) 표시 내용은 해당 IP packet에 적용할 Paging Policy다. should는 policy 적용에 걸린다.
- 제안 한국어 기준: **5GS가 PPD를 지원할 때 application은 DSCP를 설정하여 특정 IP packet에 적용할 Paging Policy를 5GS에 표시한다. 이때 should가 적용되는 대상은 해당 Paging Policy의 적용이다.** 규범 강도는 원문 should의 권고 해석을 유지한다.
- C1M의 ‘application이 DSCP를 설정하는 것이 권고된다’는 규범 대상을 바꿨으므로 실패 근거가 유지된다. C3의 보류를 모호성 정정의 성공으로 바꾸지 않는다.
- 처리: `GOLD_RELATION_CLARIFICATION`. 문장에 들어 있는 보조 동작과 규범이 직접 걸린 동작을 분리한다.

### 6. MAIN-SD-009: respectively의 불명확한 대응

- 출처: TS 24.501, 4.9.2, PDF 133쪽 본문. 앞뒤에 PLMN/SNPN identity를 기억·제거하는 문장이 있으나 대상 문장의 respectively에 대한 유일한 대응은 확정되지 않는다.
- 확실한 부분: no available network slices로 인한 N1 mode 비활성화, UE의 기억 권고, PLMN/SNPN identity와 SNPN list라는 대상 표현.
- 미확정 부분: `identity of the PLMN or SNPN ... or the list of SNPNs ..., respectively`를 특정 네트워크 종류에 정확히 일대일 대응시키는 규칙.
- 기준안: 명시된 대상과 원인을 보존하는 원문에 가까운 설명은 허용하되, 각각의 대응을 원문보다 강하게 확정하지 않는다. 단어가 모두 나왔다는 이유만으로 원문에 없는 대응까지 성공 처리하지 않는다.
- 처리: `UNRESOLVED_SOURCE_MAPPING`. 이전 C1/C1M 실패와 C2 성공의 차이가 이 대응 해석에 의존하는 부분은 재검토 대상으로 둔다. 이 행 하나를 일부 조건에서만 제외하지 않는다. 미확정을 gold 수정 완료나 모델 오류 확정으로 표시하지 않는다.

### 7. MAIN-SDN-002: 98%와 2% 부연

- 출처: TS 23.501, 5.7.3.4, PDF 192쪽 본문. 바로 앞은 Non-GBR QoS Flow의 congestion 관련 drops/delays를 설명한다.
- 필수: 비혼잡 조건, packets의 98%, 5QI PDB 초과 지연의 비권고. 주변 문맥의 Non-GBR 범위는 별도 출처로 표시하고 원래 입력 문장에 있었다고 간주하지 않는다.
- 기존 exception의 ‘나머지 최대 2%는 권고 밖’은 원문에 별도 예외 문장으로 주어진 것이 아니라 양화에 대한 부연이다. 98%를 보존한 설명에 2% 문장을 반드시 반복하도록 요구하지 않는다.
- 2%를 실제 발생 비율, 명시적인 초과 허용, 하드 성능 보장으로 바꾸지 않는다. 미래의 구조 표현은 `quantifier`와 `exception`을 구별한다.
- 처리: `QUANTIFIER_CLARIFICATION`. C3는 98%를 설명에 복원했으므로 추출 단계에서의 누락과 최종 설명 실패를 동일시하지 않는다.

### 8. MAIN-SDN-010: 입력 밖의 congestion 문맥

- 출처: TS 24.501, 5.3.9, PDF 197쪽. source는 AMF 비거절 권고와 a)~g) 목록이고, congestion 조건은 그 앞 문장에 있다.
- 제공 범위: 추출기는 대상 source 문장만 받았다. 생성기는 congestion을 명시한 한국어 질문도 받았다. C2 gold에도 같은 문맥이 들어 있다.
- 처리: `INPUT_CONTEXT_GAP`, gold 내용의 규격 근거 자체는 확인됨. 추출에 없는 조건이므로 그 누락을 모델이 원문에서 놓친 오류로만 집계하면 안 된다. 다음 설계에서는 최소 문맥을 공통으로 제공하거나, 문장 단독 추출 평가에서는 입력 밖 필드를 별도로 보고한다.
- 요청 7종을 한 범주로 뭉개거나 mobile terminated를 다른 대상으로 바꾸지 않는 기준은 유지한다. 기존 C2의 ‘이동 종료’ 표현은 착신 의미의 용어 문제이며 이 입력 부족과 별개다.
- 선정 코드에 이 완결 목록을 수동 검토에 남기는 사전 override가 있다(`CAND-04388`). NOTE에서 문장만 떨어져 들어온 두 사례와 동일한 사유라고 단정하지 않는다.

### 9. MAIN-CAN-002: not all과 NOTE 경계 대조

- 출처: TS 23.501, 4.2.16, PDF 75쪽. NOTE 2 다음에 위치하지만 본문 들여쓰기와 별도 단락으로 돌아온 문장이다. NOTE 안에 있다고 오탐하지 않는다.
- 필수: 모든 event가 UPF에 직접 subscribe 가능한 것은 아니라는 범위. 기존 positive 라벨 하나로 ‘전부 가능’과 ‘전부는 아님’을 구분할 수 없다.
- 처리: `QUANTIFIER_CLARIFICATION`. `not all`에서 모든 것이 불가능하다는 결론도, 그 문장만으로 특정 event 또는 최소 한 event의 가능성을 보장하는 결론도 만들지 않는다. 완전한 판정에는 전체 설명과 제공 문맥이 필요하다.

## 공통 기준과 후속 적용

상세 후보 기준은 `experiments/scoring_v2_candidate.md`에 작성했다. 적격성 → gold 근거 → 명제·범위 → 설명 전체 → 미지원 추가 순으로 판정한다. 현재의 PASS/FAIL 이진 점수와 새 `UNRESOLVED`, 적격성 상태를 분리한다. C1M의 성공에만 엄격한 기준을 적용하거나 C2의 정답 힌트에 맞는 표현만 성공으로 취급하지 않는다.

이번에 정리한 것은 수정 방향과 판단 규칙이다. **후보 기준으로 전체 결과를 다시 계산한 것은 아니다.** C1M의 예정된 지연 검토도 원래 기준과 새 후보 기준을 혼용하지 말고, 기준 버전 및 각 점수의 의미를 명시해야 한다. 기준 변경 후 검토를 이전 기준의 단순 반복 일치율로 합치지 않는다.

## NOTE 누락 원인과 검사 범위

`tools/extract_modal_candidates.py`는 문장 분리 후 sentence가 NOTE/EXAMPLE/Table/Figure로 시작하는지를 확인한다. `tools/shortlist_main_candidates.py`는 분리된 문장 안에 NOTE 등의 문자열이 있는지를 다시 본다. NOTE의 두 번째 문장에는 이 문자열이 없어 두 검사를 통과할 수 있다. 기존 선택 감사는 PDF 내 원문 위치·조항·중복·균형을 검사하지만 NOTE 영역의 소속을 판정하지 않는다. 이는 실제 선정 기록의 `CAND-00015`(CAN-004)와 `CAND-00051`(MAY-005)이 모두 `FIRST_ELIGIBLE_IN_DOCUMENT_ORDER`로 들어간 이력을 통해 추적했다.

72건에 대해 PDF 페이지의 주변 문맥과 레이아웃을 자동 선별 확인했다. 이것은 사람 수준의 72건 전체 적격성 검토가 아니다. 공백 분리 때문에 자동 위치 매칭이 되지 않은 2건도 ‘미위치’로 남겼으며, 그중 CAN-002는 시각 대조로 본문 위치를 확인했다. 시각·문맥 검토로 확정한 NOTE 위반은 현재 2건이다. 나머지 70건이 모두 적격이라고 보증하지 않는다.

새 선정기에서는 PDF의 NOTE/EXAMPLE 영역 전체 소속과 영역 종료를 보존해야 한다. NOTE 바로 뒤 본문인 CAN-002 같은 경우도 구분해야 한다. 추출·선정 코드 자체의 변경은 이번 골드 기준 정리 범위를 넘어가므로 하지 않았다.

## 다음 단계에 넘길 항목

- MAY-001의 gold_summary와 action 수정안을 모든 조건에 대칭 적용해 영향 검토한다.
- CAN-004/MAY-005의 적격성 오류를 공개하고, 표본 적격성 전수 확인 뒤 사후 제외 분석의 대상·분모를 고정한다. 기존 72건을 임의의 새 72건으로 바꾸지 않는다.
- SD-009의 미확정 대응을 별도 상태로 유지한다. 전문가 또는 추가 규격 근거가 확보되면 근거 범위와 버전을 기록한다.
- 필요조건 복원·상충 문장·양화·참조·입력 문맥 규칙을 먼저 동결한 뒤 재평가한다. 유의성을 얻기 위해 판정이나 제외 대상을 선택하지 않는다.
- 본문 핵심 비교를 보강하는 두 번째 단계에서는 새 쟁점이 해결된 범위를 명시한다. 이번 발견 이전의 v4 숫자를 확정 결과로 소개하지 않는다.

기계 판독 가능한 검토 목록, 기존 설명 연결, 보존 검증은 `outputs/analysis/gold_boundary_review_20260907/`에 저장한다.
