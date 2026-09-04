# 03. 실험·평가 규약

## 1. 실험 통제

- C0/C1/C2에 같은 모델 버전을 사용한다.
- temperature, top-p, max output token, seed 지원 여부를 같게 유지한다.
- C1과 C2에는 완전히 같은 `source_text_en`을 제공한다.
- C2의 추가 정보는 구조화 단계에서 원문으로부터 추출된 필드로 한정한다.
- 응답 순서 효과를 줄이기 위해 case 순서와 C0/C1/C2 실행 순서를 기록한다.
- 파싱 실패를 임의로 재실행하지 않는다. 재시도 규칙은 본 실험 전에 고정한다.

## 2. 주 평가 지표

### 2.1 Modal Class Accuracy

모델 응답이 원문의 카테고리를 정확히 보존했는지 평가한다.

- `shall`: 반드시, ~해야 한다
- `shall_not`: ~해서는 안 된다, 금지된다
- `should`: ~하는 것이 권고된다
- `should_not`: ~하지 않는 것이 권고된다
- `may`: ~할 수 있다, 허용된다
- `can`: ~할 수 있는 능력·가능성이 있다

`may`와 `can`은 한국어 표면형이 같을 수 있으므로, 응답이 허용을 뜻하는지 능력·가능성을 뜻하는지를 문맥으로 판정한다.

### 2.2 Component Preservation

각 필드를 0/1로 평가한다.

- `actor_preserved`
- `polarity_preserved`
- `condition_preserved`
- `action_preserved`
- `exception_preserved`

원문에 condition 또는 exception이 없으면 해당 필드는 `not_applicable`로 처리하고 분모에서 제외한다.

### 2.3 Complete Preservation Rate

해당 사례의 적용 가능한 필드가 모두 정확할 때만 1이다. 하나라도 누락·변형되면 0이다. 이 지표를 C1과 C2 비교의 주 지표로 사용한다.

### 2.4 Unsupported Addition Rate

원문에 없는 주요 의무, 금지, 권고, 허용, 조건, 예외을 추가한 응답의 비율이다.

### 2.5 Citation Exactness

모델이 인용을 출력하는 조건에서 `spec_id + version + clause_id`가 gold source와 일치하는지 평가한다. 인용을 요구하지 않은 C0에는 적용하지 않을 수 있다.

## 3. 오류 분류

| code | 설명 |
|---|---|
| `MODAL_WEAKENED` | 의무·금지를 권고·가능으로 약화 |
| `MODAL_STRENGTHENED` | 권고·허용을 의무로 강화 |
| `POLARITY_FLIPPED` | 부정을 긍정으로, 또는 그 반대로 변경 |
| `ACTOR_CHANGED` | 요구 주체 변경 |
| `CONDITION_DROPPED` | 적용 조건 누락 |
| `EXCEPTION_DROPPED` | 예외·한계 누락 |
| `ACTION_CHANGED` | 핵심 행동의 의미 변경 |
| `UNSUPPORTED_ADDITION` | 원문에 없는 규범 주장 추가 |
| `CITATION_WRONG` | 표준·버전·조항 오류 |
| `REFUSED` | 답변 가능한 사례에서 불필요한 보류 |

하나의 응답에 여러 error code를 부여할 수 있다.

## 4. 통계

- C0/C1/C2의 개별 비율에는 Wilson score 95% confidence interval을 보고한다.
- 조건 간 paired rate difference에는 고정 seed의 paired bootstrap 95% confidence interval을 보고한다.
- 같은 case의 C1과 C2 이진 결과는 McNemar test로 비교한다.
- 절대 차이와 상대 차이를 함께 보고한다.
- 표본이 작으므로 p-value만으로 결론내지 않고 effect size와 case-level 오류를 함께 제시한다.
- 카테고리별 결과는 탐색적 분석으로 표시한다.

## 5. 최소 결과표

### 표 1. 조건별 품질

| Condition | Modal accuracy | Complete preservation | Unsupported addition | Citation exactness |
|---|---:|---:|---:|---:|
| C0 | TBD | TBD | TBD | N/A |
| C1 | TBD | TBD | TBD | TBD |
| C2 | TBD | TBD | TBD | TBD |

### 표 2. 오류 유형

| Error type | C0 | C1 | C2 |
|---|---:|---:|---:|
| Weakened | TBD | TBD | TBD |
| Strengthened | TBD | TBD | TBD |
| Polarity flipped | TBD | TBD | TBD |
| Actor/condition/action changed | TBD | TBD | TBD |

### 그림 1. 카테고리별 Complete Preservation Rate

6개 modal class × C0/C1/C2 heatmap을 사용한다. 각 셀의 성공 수/12와 비율을 직접 표기한다. 2~3쪽 지면을 고려해 본문 그림은 이 한 장을 우선하고, 전체 조건 막대와 의미 구성요소 오류 그래프는 발표·검토용 보조 산출물로 둔다.

## 6. 판정 경계

- 구조화 필드가 원문에서 직접 파생되었는지와 그 내용이 올바른지를 구분한다.
- 코드 파싱 성공은 의미 정확성을 입증하지 않는다.
- LLM-as-a-Judge를 쓰더라도 주 지표의 gold 판정을 대체하지 않는다.
- 실험에서 사용한 `oracle evidence`는 실제 검색 성능을 입증하지 않는다.
