# v2 의미 검토 2차 완료 및 불일치 기록

2026-09-09. **합집합 51개 사례 × 5조건 = 255개 응답 슬롯의 2차 검토를 완료·봉인했다.** 1차와 다른 가림 순서로 원문과 설명 전체를 검토했고, 255개 판정을 모두 봉인한 뒤 두 차수를 대조했다. 상태는 `PASS2_SEALED_ADJUDICATION_PENDING`이다. 동일 평가자의 반복 검토이며 독립 전문가 검증이나 최종 조정 결과가 아니다.

| 2차 기록 상태 | 슬롯 수 | 의미 |
|---|---:|---|
| PASS | 165 | 동결 v2 기준에 따라 의미 보존으로 판단 |
| FAIL | 81 | 원문과 응답의 구체적인 오류를 기록 |
| UNRESOLVED | 8 | 의미 또는 기준 범위를 확정하지 않음; 값은 null |
| NOT_SCORED | 1 | 설명 미생성; 의미 오역과 분리하고 pipeline 결과만 0 |
| 합계 | 255 | 각 기준 사례에 정확히 5개 슬롯 |

위 수치는 **2차 검토 상태의 건수**다. 조건별 최종 성능, 255개를 독립 표본으로 취급한 정확도·신뢰구간, 효과 크기·통계 검정 및 원고 수치는 산출·갱신하지 않았다. 주 분석과 세 민감도 집합의 동결 분모 49/50/50/51을 유지한다.

## 24시간 간격과 검토 방식

- 1차 봉인: **2026-09-08 12:31:23.646276 KST**.
- 2차 자료 공개: **2026-09-09 13:41:29.277481 KST**. 1차 봉인에서 **25시간 10분 5.631205초**가 지나 동결된 24시간 게이트를 통과했다.
- 2차 봉인: **2026-09-09 13:52:05.557516 KST**.

공개된 2차 packet의 순서대로 255건을 직접 읽고 판정·이유·응답 인용을 작성했다. 원문·질문·source/gold 사전 확인 명제·동결 rubric을 사용했으며, 의미 판정 중 1차 판정 파일과 조건 매핑을 열지 않았다. 전체 판정 작성 후 원본 응답 레코드 해시를 결합했고, 봉인 이후에만 1차 결과를 열어 비교했다. 문자열 규칙으로 의미 상태를 생성하거나 1차 점수를 복사하지 않았다.

다만 동일 평가자가 1차 검토를 수행했으며 대화에도 이전 검토 내용이 있었다. 새 순서와 조건 가림, 시간 간격은 완전한 눈가림이나 평가자 독립성을 보장하지 않는다. 이 기록을 독립 전문가 간 신뢰도 또는 정답 타당도의 증거로 해석하지 않는다.

## 두 차수 대조: 250건 동일, 5건 조정 대기

원본 응답 레코드 SHA-256으로 255쌍을 대응시켰다. 의미 상태와 값이 모두 같은 것은 **250건**, 다른 것은 **5건**이다. 동일한 250건에는 두 차수 모두 UNRESOLVED인 7건과 NOT_SCORED인 1건도 포함된다. 따라서 250을 정답 수로 해석하지 않는다.

| 1차 → 2차 | 슬롯 수 |
|---|---:|
| PASS → PASS | 165 |
| FAIL → FAIL | 77 |
| UNRESOLVED → UNRESOLVED | 7 |
| NOT_SCORED → NOT_SCORED | 1 |
| PASS → FAIL | 4 |
| FAIL → UNRESOLVED | 1 |

| 2차 ID | 1차 ID | 기준 | 변화 | 조정 쟁점 |
|---|---|---|---|---|
| V2-P2-019 | V2-P1-005 | G031 | PASS → FAIL | paging 회피를 ‘조건’으로 재언급한 것이 목적 설명인지 적용 범위 축소인지 |
| V2-P2-070 | V2-P1-041 | G010 | PASS → FAIL | ‘능력이 있을 수 있다’의 선택성과 ‘기술적 가능성’ 부연을 함께 읽는 방식 |
| V2-P2-099 | V2-P1-045 | G050 | PASS → FAIL | 무결성 검사의 대상을 메시지가 아닌 수신 엔티티로 명시한 한국어 구문의 해석 |
| V2-P2-106 | V2-P1-092 | G010 | FAIL → UNRESOLVED | 능력 보유 확정 뒤 선택 가능 부연의 지시 대상 불명확성을 R3에서 처리하는 방식 |
| V2-P2-151 | V2-P1-039 | G050 | PASS → FAIL | 뒤 문장이 앞 문장의 무결성 검사 대상 오류를 분명하게 복원하는지 |

[불일치 5건의 원문·전체 응답·두 판정 근거](../outputs/review/v2_pass2_completed_20260909/disagreements_pending.md)에 각 쟁점을 함께 저장했다. 두 차수 중 하나를 자동 채택하거나 봉인 판정을 수정하지 않았다. 같은 원문에 연결된 표현은 함께 대조하고, 최종 조정은 별도 판정·근거·시각으로 남겨야 한다. 조정 과정에서 판정 기준 자체를 바꿀 필요가 생기면 관련 사례와 조건 모두에 대칭적으로 적용할 범위를 먼저 기록한다.

## 미확정과 설명 미생성

사전 확인의 G023·G028은 이번에도 합집합에 남아 있다. 이 두 기준에 연결된 10개 슬롯 가운데 7개는 UNRESOLVED다. 나머지 3개는 범위 문제와 독립적인 명백한 오류로 FAIL이며, 해당 사유를 `INDEPENDENT_CLEAR_ERROR`로 기록했다. 2차에서 추가된 G010/V2-P2-106의 지시 대상 불명확성 1건을 합해 UNRESOLVED는 총 8건이다.

V2-P2-202는 기존 기록에서 설명이 미생성된 슬롯이다. `NOT_SCORED`와 pipeline 값 0을 유지했으며 자료 누락을 미생성으로 바꾼 것이 아니다. 새로운 모델 생성 API 호출은 0건이다.

## 산출물과 검증

- [봉인 판정 JSONL](../outputs/review/v2_pass2_completed_20260909/seal/pass2_completed.jsonl), [봉인 manifest](../outputs/review/v2_pass2_completed_20260909/seal/completion_manifest.json).
- [255건 판정 색인 CSV](../outputs/review/v2_pass2_completed_20260909/judgments_index.csv), [요약 JSON](../outputs/review/v2_pass2_completed_20260909/summary.json).
- [두 차수 255쌍 비교](../outputs/review/v2_pass2_completed_20260909/pass_comparison.jsonl), [조정 대기 JSONL](../outputs/review/v2_pass2_completed_20260909/disagreements_pending.jsonl), [조정 색인 CSV](../outputs/review/v2_pass2_completed_20260909/disagreements_index.csv).
- [실제 생성 단계의 입력 가용성 연결](../outputs/review/v2_pass2_completed_20260909/input_provenance_bindings.jsonl). 이 파일은 2차 봉인 후 생성한 관리 자료이며 가림 검토 입력이 아니다. source/question과 판정자 전용 PDF 문맥을 구분하고, C2의 원래 gold 입력이 수정됐다고 소급하지 않는다.
- 원문·응답·판정 함께 읽기: [001–043](../outputs/review/v2_pass2_completed_20260909/readable/review_001_043.md), [044–086](../outputs/review/v2_pass2_completed_20260909/readable/review_044_086.md), [087–129](../outputs/review/v2_pass2_completed_20260909/readable/review_087_129.md), [130–172](../outputs/review/v2_pass2_completed_20260909/readable/review_130_172.md), [173–215](../outputs/review/v2_pass2_completed_20260909/readable/review_173_215.md), [216–255](../outputs/review/v2_pass2_completed_20260909/readable/review_216_255.md).
- [기계적 검증 기록](../outputs/review/v2_pass2_completed_20260909/verification_receipt.json), [전체 산출물 해시](../outputs/review/v2_pass2_completed_20260909/completion_manifest.json).

검증은 24시간 공개 게이트, 255개 ID와 동결 순서, 기준별 5개 슬롯, 254개 응답 인용의 실제 포함 여부, 미생성 1건, rubric·packet·원본 response 해시, 사전 확인 명제와 출처, 시각 순서, 미확정·pipeline 상태 조합, 같은 기준·같은 설명의 판정 일관성, 두 차수 봉인 및 비교 결과의 재계산을 확인한다. 기계적 검사는 의미 판정의 타당성을 증명하지 않는다.

기존 동결 파일 119개, 검토 패키지 22개와 지원 파일 2개, 1차 완료 자료의 해시 검증을 통과했다. 원본 source·question·gold·응답·이전 점수·v4 원고와 1차 판정은 보존했다. 2차 판정은 별도 경로에 저장했다.

```sh
python3 tools/finalize_v2_pass2_20260909.py verify
python3 tools/compare_v2_review_passes_20260909.py verify
```

다음 단계는 불일치 5건과 남은 미확정의 별도 조정이다. 그 결과와 불확실성을 고정한 후에 주 분석 및 세 민감도 집합을 함께 보고한다. 현재 자료의 존재만으로 조정 완료나 v2 최종 성능 확정을 선언하지 않는다.
