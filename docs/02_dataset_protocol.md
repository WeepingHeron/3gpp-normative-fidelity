# 02. 데이터셋 규약

## 1. 표본 구성

본 데이터셋은 6개 카테고리에서 각 12개씩, 총 72개를 목표로 한다.

| category | 의미 | 목표 수 |
|---|---|---:|
| `shall` | 필수 요구 | 12 |
| `shall_not` | 금지 | 12 |
| `should` | 권고 | 12 |
| `should_not` | 비권고 | 12 |
| `may` | 허용 | 12 |
| `can` | 가능·능력 | 12 |

`cannot`은 `can`의 부정 표본으로 넣을 수 있지만 `can` 12개 중 부정 문장이 몇 개인지를 별도 기록한다.

Main의 각 카테고리 12개는 TS 23.501에서 6개, TS 24.501에서 6개를 뽑는다. 이렇게 하면 특정 modal class와 특정 규격의 문체·절차 특성이 결합되는 교란을 줄일 수 있다.

| source | 고정 버전 | main 범주별 수 | 사용 조항 |
|---|---|---:|---|
| 3GPP TS 23.501 | V18.12.0 Release 18 | 6 | 4-8 |
| 3GPP TS 24.501 | V18.12.0 Release 18 | 6 | 4-6 |

## 2. 원문 선정 규칙

### 포함

- 선정한 두 공식 규격의 고정 버전 본문
- 행위자와 행동을 식별할 수 있는 문장
- 해당 modal verb가 요구·권고·허용·능력 의미로 쓰인 문장
- 조건이 있으면 규범 행동과 같이 추출 가능한 문장

### 제외

- 목차, 머리말, 저작권 고지의 modal verb
- 외부 문서 직접 인용
- 표·그림을 보지 않으면 의미를 확정할 수 없는 문장
- 문서 파서가 손상시킨 문장
- 하나의 사례에 독립적 요구가 여러 개이지만 분리하기 어려운 문장
- 해석에 도메인 전문가 합의가 필요하지만 확인할 수 없는 문장

제외한 후보도 `exclusions.csv`에 조항과 사유를 기록해 cherry-picking을 줄인다.

## 3. 수집 순서

1. 공식 버전 PDF를 `data/source/`에 보관한다.
2. `source_manifest.json`에 출처, 버전, Release, 다운로드일, SHA-256을 기록한다.
3. modal verb를 기준으로 후보를 찾되, 원문 순서를 유지한다.
4. exact duplicate와 near-duplicate를 표시하고 pilot/main 간 누출을 막는다.
5. 각 카테고리에서 동일한 선정·제외 규칙을 순차적으로 적용한다.
6. Main은 각 규격에서 범주별 6개씩 선택한다.
7. 자신의 예상 결과와 맞는 문장만 고르지 않는다.

## 4. 라벨 정의

| 필드 | 정의 |
|---|---|
| `case_id` | 변경하지 않는 사례 ID |
| `spec_id` | 예: `3GPP TS 23.501` |
| `release` | 표준 Release |
| `version` | 문서 정확 버전 |
| `clause_id` | 원문 조항 ID |
| `source_text_en` | 실험에 쓰는 영문 원문 |
| `modal_class` | 6개 카테고리 중 하나 |
| `polarity` | `positive` 또는 `negative` |
| `actor` | 요구·권고·허용·능력의 주체 |
| `condition` | `if/when/unless` 등의 적용 조건, 없으면 빈 값 |
| `action` | actor에게 연결된 핵심 행동 |
| `exception` | 예외·한계, 없으면 빈 값 |
| `question_ko` | 모델에게 제공할 한국어 질문 |
| `gold_summary_ko` | 최소 채점 기준용 한국어 설명 |
| `source_sha256` | 원문 바이트 해시 |
| `split` | `pilot`, `dev`, `test` |
| `review_status` | `draft`, `self_checked`, `second_reviewed` |

`gold_summary_ko`는 자연스러운 표현의 유일 정답이 아니다. actor, condition, modal class, polarity, action, exception을 채점하기 위한 참고 설명이다.

## 5. pilot과 본 데이터

- Pilot: 각 카테고리 3개, 총 18개. 두 규격에서 전체 9개씩 선택한다.
- `should_not` pilot은 TS 23.501 2개와 TS 24.501 1개를 사용한다. 다른 범주에서 반대 배분을 적용해 전체 source 수를 맞춘다.
- Main: pilot과 겹치지 않는 각 카테고리 12개, 총 72개. Pilot은 본 결과에 포함하지 않는다.
- 동일하거나 매우 유사한 요구는 pilot과 main에 나누어 넣지 않는다.
- Pilot에서 prompt와 채점 규칙을 수정한 후 main dataset을 작성한다.
- Main 실험 시작 후에는 gold label을 바꾸지 않는다. 분명한 오류를 발견하면 errata와 영향받은 case를 공개한다.

## 6. 품질 감사

각 사례에 다음을 확인한다.

- modal verb가 원문에 직접 존재한다.
- actor와 action이 원문에서 추적된다.
- condition과 exception을 임의로 추가하지 않았다.
- 조항 ID와 원문이 공식 문서와 일치한다.
- `question_ko`가 modal class를 질문 자체에서 직접 누설하지 않는다.
- 표본 수가 카테고리별로 균형이다.
- Main에서 각 modal 범주의 규격별 표본 수가 6개씩이다.
- exact/near duplicate가 pilot과 main 사이에 분리되지 않았다.

2차 검토자를 구할 수 없으면 전문가 검토를 받았다고 쓰지 않고, `single-annotator, source-grounded labels`라는 한계를 논문에 명시한다.
