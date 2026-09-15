# C3 자동 구조 추출 확장 규약 v1

2026-09-06. 원래 main 72건의 결과를 확인한 뒤 설계한 후속 탐색 실험이다. 기존 본 실험의 사전 가설로 소급하지 않는다. 새 72개 표본이 아니며 별도 run으로 보존한다.

## 연구 질문과 비교

원문만으로 자동 추출한 구조를 제공한 C3가 기존 C1(oracle source)과 C2(oracle structured) 사이에서 어떤 성능을 보이는가? 추출 오류가 최종 설명에 전파되는지 구분한다. 같은 모델 스냅샷을 사용하되 C1/C2는 9/3, C3는 후속 실행이므로 실행일 차이가 있다.

표본은 동결 main 72건 전체다. 실패 사례만 고르지 않는다. 기존 216개 응답을 다시 생성하지 않으며 gold 3건의 범위 모호성도 원래 상태로 유지한다. 주 비교는 C1-C3 설명 완전 보존, C2-C3는 oracle 구조와의 차이를 보여주는 보조 비교다.

## 입력과 절차

1. 추출 API에는 source_text_en만 제공한다. case ID, modal_class, gold_summary_ko, gold actor/condition/action/exception, 난도, 기존 모델 답변은 제공하지 않는다.
2. 추출은 `c3_extract_v1.md`와 `c3_extraction_schema.json`으로 수행한다. 원문에 없는 필드는 추정하지 않고 조건·예외 부재는 빈 문자열로 출력한다. 해석 불가능하면 unclear를 허용한다.
3. 생성은 기존 `c2_v2.md`를 그대로 사용한다. 원문·질문·출처는 기존 C1/C2와 동일하고 구조 필드만 자동 추출 결과로 교체한다. 기존 `response_schema.json`과 출력 한도 600 tokens를 유지한다.
4. 추출 JSON 파싱/스키마/상태 실패 또는 unclear면 생성을 건너뛰고 보류로 기록한다. gold로 채우거나 C1으로 되돌아가지 않는다. 추출 modal-polarity 불일치도 보류한다.
5. source-only projection과 gold-field mutation 검사를 오프라인으로 먼저 통과시킨다. 순서는 고정 seed의 case hash 순이다. 각 case에서 extraction 다음 generation을 실행한다.

모델은 기존 `gpt-5.4-mini-2026-03-17`이다. 두 단계 temperature 0·reasoning effort none·store false를 사용한다. 추출 출력 상한은 1,200 tokens, 생성은 600이다. 요청 순서 seed는 모델 생성 seed가 아니다. 최대 성공 호출은 144회다. 추가 평가용 LLM 호출은 이 실행에 포함하지 않는다.

## 실행 보존과 중단

실행 전에 데이터·프로토콜·prompt·schema·runner·입력 projection의 SHA-256, 모델, 순서, 파라미터를 동결한다. 각 요청의 본문(키 제외), 응답 원본, HTTP 상태, attempt, 시작·종료·경과 시간, 실제 model, usage를 저장한다. completed 상태·스키마를 확인한 뒤에만 parsed로 분류한다.

429·5xx만 최대 2회 재시도하며 모든 attempt를 보존한다. 전송·timeout 오류는 서버 처리 여부가 불명확하므로 자동 재시도하지 않고 run을 중단한다. 인증·결제·모델 불일치·불명확 usage도 중단한다. 파싱·의미 오류는 재시도하지 않는다. API 중단 후에는 원래 run을 덮어쓰거나 통째로 다시 실행하지 않는다.

누적 추정 비용 상한은 $1이다. 매 요청 전 UTF-8 입력 byte 수와 출력 상한으로 보수적인 token 비용 예약액을 더해 상한을 넘으면 중단한다. 실제 청구액 보장이 아니라 당시 공개 요율을 사용한 실행 guard다. API 호출 시간은 extraction+generation 합계와 단계별로 기록한다. 기존 C1/C2에는 동등한 지연 계측이 없어 직접적인 지연 우위를 주장하지 않는다.

## 평가 계획

- 추출 JSON modal 정확도와 polarity 정확도는 동결 gold와 결정적으로 비교하되 의미 평가와 구분한다. gold 모호성 3건을 포함한 결과와 제외한 민감도를 함께 보고한다.
- 추출 actor·condition·action·exception의 의미 보존은 원문 대조 검토가 필요하다. 문자열 동일성을 의미 정확도로 간주하지 않는다.
- 최종 한국어 설명의 완전 보존과 unsupported addition은 기존 의미 rubric을 사용하되 `09_reporting_errata_2026-09-06.md`의 정의 정정을 적용한다. 정답 JSON과 자연어 의미, JSON–설명 일관성을 별도로 기록한다.
- 보류·파싱·스키마 실패는 전체 72개 분모에서 완전 보존 실패다. coverage와 답변한 사례의 오류율을 별도로 표시한다. 중단으로 미실행한 사례는 실패와 구분하고 partial run임을 명시한다.
- 새로운 masked review에 C1/C2/C3의 한국어 설명을 함께 섞고 동일한 절차로 새 판정을 받는 것이 권장된다. 기존 C1/C2 판정과 새 C3 판정을 직접 비교하면 평가 시점 차이가 남으므로 탐색적으로 제한한다.
- 보존율에는 Wilson CI, paired 차이에는 20,000회 case bootstrap, C1-C3에는 양측 exact McNemar를 사용한다. class별 분석과 C2-C3는 보조적이다. 보존 이외 2차 지표에서 유의성 주장을 늘리지 않는다.
- 독립 전문가 없이 현재 Codex가 검토하면 provisional로 남긴다. 빈 점수를 성공으로 채우지 않는다. delayed pass 2는 최소 24시간 이후 가능하며 오늘 완료로 표시하지 않는다.

결과가 예상과 달라도 데이터·prompt를 교체하지 않는다. 후속 개선은 새 버전과 별도 run으로 수행한다. 이번 추가 실험 결과는 검토 전까지 논문 본문의 확정 성능으로 넣지 않는다.

API 계약 참고: [모델 문서](https://developers.openai.com/api/docs/models/gpt-5.4-mini), [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs), 확인일 2026-09-06. 키 재사용은 사용자가 이 작업에서 승인했다.
