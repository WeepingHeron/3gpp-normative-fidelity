# Main 72건 표본 적격성 감사

2026-09-08. 상태: `REVIEW_COMPLETE_WITH_INELIGIBLE_AND_HOLD_CASES`.

**72건을 모두 확인한 결과, 일반 적격 50건·사전 기록 예외에 따른 조건부 적격 1건·부적격 10건·보류 11건이다. 현재 72건 전체를 적격성이 확정된 데이터셋으로 제시할 수 없다.** 이는 동일 Codex의 원문 기반 감사 결과이며 독립 전문가 검증이 아니다. 적격 판정도 gold 전체가 옳거나 모델 설명이 맞다는 보증은 아니다.

[보고서 HTML](../outputs/analysis/main72_eligibility_20260908/report.html), [72건별 근거 CSV](../outputs/analysis/main72_eligibility_20260908/eligibility_audit.csv), [원문·문맥·판정 JSON](../outputs/analysis/main72_eligibility_20260908/eligibility_audit.json), [재현 노트북](../outputs/analysis/main72_eligibility_20260908/reproduce_checks.ipynb).

## 1. 범위와 판정 기준

대상은 동결 `data/main_cases.csv`의 72건 전부다. TS 23.501·24.501 V18.12.0 Release 18 원본 PDF에서 해당 문장이 놓인 **51개 고유 페이지를 모두 렌더 이미지로 확인**하고, 전후 문맥 및 필요시 이전 페이지의 상위 조건·조항 제목을 대조했다. PDF page는 1부터 세며 인쇄면 번호는 여기서 1을 뺀 값이다.

직접 기준은 `docs/02_dataset_protocol.md`의 본문·주체/행동·조건 동시 추출·해석 가능성 규칙과 `docs/06_main_difficulty_protocol.md`의 **“표·목록·NOTE·깨진 문장과 외부 문서 직접 인용은 제외한다”**는 문구다. 목록 내부의 들여쓴 후속 문단도 목록에 속하는 것으로 판정했다. 목록이 끝난 뒤 본문 여백으로 돌아온 문장은 단순히 목록이 가까이 있다는 이유로 제외하지 않았다. 외부 규격을 참조한다는 사실 자체를 ‘직접 인용’으로 취급하지 않았으며, 그림 인접 문장도 그림 없이 핵심 명제를 확정할 수 있으면 제외하지 않았다.

상태는 서로 겹치지 않게 1건당 하나를 부여했다. 명백한 영역 제외 위반이 있으면 부적격이 우선이며 빠진 문맥도 추가 사유로 기록했다. 문맥의 적용 범위·대명사·대응 관계를 확정하지 못하거나 조항 메타데이터가 다르면 보류했다. 고정 목록 예외는 해당 후보 2건에만 좁게 적용하고 다른 목록 문장으로 확장하지 않았다.

| 상태 | 건수 | 의미 |
|---|---:|---|
| `ELIGIBLE` | 50 | 이번 선정·원문 범위 감사에서 제외 사유를 확인하지 않음 |
| `ELIGIBLE_WITH_RECORDED_EXCEPTION` | 1 | 일반 목록 제외 문구와 다르지만 실행 전 기록된 개별 예외 및 완전한 조건에 근거 |
| `INELIGIBLE` | 10 | 사전 NOTE·표·목록 제외 규칙 위반 확인 |
| `HOLD` | 11 | 조항 정정, 문맥 보충, 의미 중복 또는 대응 관계 검토가 필요 |

## 2. 명백한 부적격은 NOTE 3건과 목록 7건

| case | 규격 / 조항 / PDF쪽 | 확인한 영역과 문제 |
|---|---|---|
| CAN-004 | 23.501 / 4.2.5 / 51 | NOTE 2 내부 |
| MAY-005 | 23.501 / 4.3.1 / 76 | NOTE 2 내부 |
| SN-012 | 24.501 / 4.6.2.3 / 106 | Table 4.6.2.3.1 테두리 안 NOTE 2 마지막 문장 |
| SH-003 | 23.501 / 5.3.2.4 / 100 | 다른 PLMN의 두 번째 access라는 bullet 내부; 상위 조건 누락도 있음 |
| SD-004 | 23.501 / 5.3.4.1.1 / 106 | RAT restriction bullet 내부 |
| SDN-001 | 23.501 / 5.3.4.1.1 / 106 | Forbidden Area bullet 내부 |
| SN-004 | 23.501 / 5.3.4.1.1 / 107 | Service Area Restrictions의 Non-Allowed Area 하위 bullet |
| SDN-004 | 23.501 / 5.17.2.1 / 315 | dual-registration mode bullet의 후속 문단 |
| SD-007 | 24.501 / 5.4.1.3.7 / 255 | 전 페이지에서 시작한 c) MAC failure 내부; 상위 절차 누락 |
| SD-008 | 24.501 / 5.4.1.3.7 / 255 | 같은 c) MAC failure의 다른 mapping 분기; 상위 절차 누락 |

짧은 ID는 모두 `MAIN-` 접두어를 생략한 것이다. 표 NOTE가 항상 비규범적이라는 일반 명제를 근거로 삼지 않았다. 이번 SN-012의 직접 제외 근거는 연구 자체의 표·NOTE 제외 규칙이다. 목록의 완전한 규범 문장도 이 연구가 목록을 제외한다고 정한 이상 무기록 예외로 통과시키지 않았다.

SD-008은 특히 중요하다. 원문은 MAC failure 뒤 mapping을 점검한 결과가 올바르면 authentication을 종료하는 절차다. 발췌만 보면 정상적인 mapping일 때 일반적으로 인증을 거절하라는 규칙처럼 읽힐 수 있다. 이는 모델의 단순한 should 번역 오류와 구분해야 하는 **입력 단위의 문제**다.

## 3. 보류 11건은 일괄 오답이나 확정 제외가 아니다

| case | PDF쪽 | 보류 근거 | 다음 처리 |
|---|---:|---|---|
| SH-004 | 23.501:42 | PILOT-SH-001과 CP NF service-based interaction이라는 actor/action 중복 가능성. Jaccard 0.375는 기계 임계값 미만이나 의미 중복을 보증하지 않음 | only와 where identified 차이를 고려해 중복 여부 확정 |
| SH-007 | 24.501:56 | then이 잇는 single-registration·N26·S1→N1·5GMM-CONNECTED mapped context 생성 조건 부족 | 상위 조건 포함한 새 추출 단위 검토 |
| SH-011 | 24.501:56 | 같은 문단에서 newly derived K'_AMF의 도출 조건이 앞 문장에 있음 | 위와 동일한 조건 범위 검토 |
| MAY-010 | 24.501:66 | emergency PDU session 및 integrity failure는 있지만 SERVICE/CONTROL PLANE SERVICE REQUEST라는 대상 메시지 범위가 빠짐 | 메시지 범위를 포함한 단위 검토 |
| CAN-003 | 23.501:93 | The architecture의 지시 대상은 IETF DetNet 통합 구조이며 현 질문은 일반 5GS architecture로 표현 | 지시 대상 명시 필요 |
| CAN-005 | 23.501:59 | 동결 4.2.8.1 ↔ 실제 **4.2.8.1A** | 메타데이터 errata; 기존 인용 결과는 소급 정정 금지 |
| SN-007 | 24.501:66 | emergency session 비해제 문장만 남아 앞 service request 처리 조건이 빠짐 | 일반적인 영구 해제 금지로 확대하지 않도록 단위 보충 |
| SD-009 | 24.501:133 | respectively의 PLMN/SNPN identity·SNPN list 대응을 단일하게 확정하지 못함 | 대응 모호성을 해소하거나 별도 보류 유지 |
| SDN-002 | 23.501:192 | 앞 문장의 **Non-GBR QoS Flows** 범위가 추출 문장·질문·gold에서 빠짐 | Non-GBR 조건 포함. 98%/2% 양화 문제와 분리 |
| SDN-006 | 23.501:338 | 조항은 NAS MM congestion control에만 적용. 현 문장/질문에는 CM-CONNECTED만 있음 | congestion 처리 범위 포함 여부 검토 |
| SDN-010 | 24.501:197 | 7개 목록은 완전하고 사전 예외도 있으나 congestion이 질문·앞 문맥에만 있음 | source와 question의 문맥 출처를 분리하고 단위 보완 |

위 보류 중 8건은 문맥 범위, 1건은 조항 메타데이터, 1건은 respectively 대응, 1건은 pilot 의미 중복이다. 문맥 판단에는 보수적인 해석이 포함돼 있으므로 확정 부적격 10건과 합쳐 ‘오류 21건’으로 부르지 않는다.

## 4. 사전 목록 예외와 gold 문제를 분리한다

동결 `main_selection_draft.csv`의 `pre_screen_override`에는 다음 두 후보의 개별 예외가 실제로 기록돼 있다. main freeze 시각은 2026-09-03 07:31:31 UTC이며 이번 판단을 위해 새로 만든 예외가 아니다.

- **SDN-010 / CAND-04388:** 완전한 should_not 목록 유지. 목록 위반만으로 일반 부적격에 합산하지 않았으나 문맥 부족 때문에 보류했다.
- **SDN-011 / CAND-05502:** self-contained V2X 복합 문장 유지. capability bit의 두 대안 중 하나 **AND** UDM subscription 조건이 함께 있어 `ELIGIBLE_WITH_RECORDED_EXCEPTION`으로 구분했다. 문서의 일반 목록 제외 문구와 일치하는 일반 적격으로 표현하면 안 된다.

일반 목록 제외 문구만 문자 그대로 적용하는 민감도 관점에서는 두 건 모두 목록 제외에 해당한다. 그 경우 **일반 적격 50·부적격 12·보류 10**으로 바뀐다. 이 차이는 새로운 성능 분석이 아니라 선정 규칙 해석에 따른 표본 분류 민감도다.

MAY-001은 원문 표본 자체는 적격이지만 capability를 ‘권한’으로 바꾼 gold 및 action 범위 수정이 필요하다. CAN-008의 실제 context 설정 필요조건, SH-005의 `shall be able` 능력 요구, SD-002의 policy 적용에 걸린 should 역시 단어 분류와 명제 범위를 구분해야 한다. 기존 [경계 검토](20_gold_boundary_review_2026-09-07.md)와 연결하되 이번 작업은 72건 전체 gold 재동결이나 모델 설명 재채점이 아니다.

## 5. 기계 검증과 원문 판단은 다른 결과다

- 72개 ID·candidate가 고유하며 modal별 12개, 규격별 36개, 기존 tier 8/22/42 구성은 일치한다.
- 두 원본 PDF의 SHA-256은 source manifest와 일치하고 72건의 원문은 모두 해당 페이지에서 영숫자 연결 정규화로 찾았다. 이 정규화는 줄바꿈·키 표기 공백 등을 넘겨 위치를 찾는 방법이며 의미 동등성 판정이 아니다. 51쪽 시각 확인으로 영역을 따로 판단했다.
- 문자 접미사를 보존한 조항 추적에서 CAN-005의 4.2.8.1A 불일치 1건을 확인했다. 기존 숫자 전용 heading 정규식은 A를 놓쳤다.
- 같은 modal의 main 간 token-set Jaccard ≥0.60 쌍은 0개, pilot-main ≥0.72 쌍도 0개다. 하지만 SH-004의 의미 중복 가능성은 별도 보류했다. SDN-008/009는 Active Time/all-PLMN이라는 관련 주제를 공유하므로 표본의 독립성을 과장하지 않는다.
- 원래 main freeze 18개 파일과 이전 9월 7일 검토·gold 경계 manifest에 포함된 파일의 해시는 모두 유지됐다. 원고 v4와 기존 응답·점수·gold도 변경하지 않았다.

검증 코드는 `tools/audit_main72_eligibility_20260908.py`다. PDF 의존성이 있는 Python 환경에서 실행하면 JSON을 표준 출력으로 내보내며 원본 파일을 수정하지 않는다. 상세 결과는 `validation.json`과 `reviewed_pages.json`에 있다. 노트북은 기계 검증을 재실행할 수 있지만 사람/Codex의 영역·문맥 판단을 자동 입증하지 않는다.

노트북 코드 셀 3개는 Python 실행기로 실행해 검사를 통과했다(Jupyter 커널 실행 인증은 아님). HTML의 canonical payload·내장 reader·semantic fallback 구조 검증은 통과했으나, 패키저가 사용할 Chromium 실행 파일을 찾지 못해 브라우저 표시·상호작용 검증은 미실시다. `report_delivery_receipt.json`의 상태는 `structural_only`이며 HTML에는 스크립트 없이 읽을 수 있는 표와 본문도 포함돼 있다. 보고서 집계는 저장된 실제 감사 행을 SQLite로 조회한 결과와 대조했고 `report_queries.sql`에 조회를 보존했다.

## 6. 다음 단계와 이번 작업의 완료 경계

이번에 완료한 것은 **72건 전수 적격성 감사와 사례별 처리 근거 기록**이다. 연구 질문은 영문 3GPP 규범 문장의 한국어 의미 보존으로 유지하며, 표본 문제를 해결하기 위해 새 제품이나 별도 모델 연구로 범위를 확장하지 않는다.

다음에는 이 감사 결과를 기준으로 제외·보류·gold 수정의 처리 기준을 별도 버전으로 먼저 동결해야 한다. 기존 응답의 사후 제외 분석은 모든 조건에 같은 사례 집합을 적용하고 사후 분석임을 표시한다. 문맥이나 gold를 고친 입력으로 새 실험을 한다면 별도 데이터셋·실행 버전으로 다룬다. 남은 50/51건으로 단순히 분모만 바꾸면 modal·규격·난도 균형이 달라지므로 새 72건으로 간주할 수 없다.

미해결 질문은 목록 예외와 본문 규약을 어떤 방식으로 명시적으로 일치시킬지, 보류 사례의 적용 범위를 어디까지 포함할지, SH-004를 pilot의 의미 중복으로 볼지다. 이번에는 후보 pool 전체 재선정·새 API 호출·모델 재채점·논문 v5 작성은 수행하지 않았다.
