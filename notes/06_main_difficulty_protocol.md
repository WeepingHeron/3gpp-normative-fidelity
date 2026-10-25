# 06. Main 데이터 난도 층화 규약

## 목적

Pilot에서 C1과 C2의 complete preservation이 모두 18/18로 나타나 ceiling risk가 확인됐다. Main 문장은 C2에 유리한 결과를 만들기 위해 고르지 않고, **모델 응답을 생성하기 전에** 아래 표면 규칙으로 난도를 분류하고 표본 구성을 동결한다.

## 층화 단위

각 문장은 다음 세 단계 중 하나로 분류한다.

| tier | 판정 기준 | main 목표 |
|---|---|---:|
| `simple` | 명시적 조건·한정 표지가 없고 단일 행위자와 핵심 행동을 가진 긍정 modal 문장 | 긍정 modal별 2개 |
| `conditional` | `if`, `when`, `where`, `during`, `while`, `after`, `before`, `upon`, `once`, `until`, `because`, `provided that`, `as long as`, `in case`, `in the event` 또는 부정 modal 중 하나가 있으나 복합 기준에는 해당하지 않는 문장 | 긍정 modal별 4개, 부정 modal별 4개 |
| `compound` | 조건 표지 2개 이상, 또는 `only`, `unless`, `except`, `if any` 한정, 또는 조건을 동반한 부정 modal, 또는 독립적으로 보존해야 할 행동·대상이 둘 이상인 문장 | 긍정 modal별 6개, 부정 modal별 8개 |

여기서 긍정 modal은 `shall`, `should`, `may`, `can`, 부정 modal은 `shall_not`, `should_not`이다. 최종 목표는 `simple` 8개, `conditional` 22개, `compound` 42개다. `shall`, `may`, `can`은 규격마다 `1 simple + 2 conditional + 3 compound`를 사용하고, `shall_not`은 규격마다 `2 conditional + 4 compound`를 사용한다.

`should_not`은 후보 분포를 모델 출력 전에 점검한 결과 TS 24.501에서 pilot·깨진 목록·복수 modal·near duplicate를 제외한 독립 후보가 부족했다. 따라서 `should_not`은 TS 23.501에서 `2 conditional + 6 compound` 8개, TS 24.501에서 `4 compound` 4개를 사용한다. source 총량을 36대36으로 유지하기 위해 `should`은 반대로 TS 23.501에서 `1 simple + 1 conditional + 2 compound` 4개, TS 24.501에서 `1 simple + 3 conditional + 4 compound` 8개를 사용한다. 이 예외는 모델 응답 전에 정했고 selection log에 남긴다. 그 밖의 후보 부족은 모델 결과를 보기 전에 인접 tier로 최대 1개 이동하고 이유를 기록한다.

## 균형과 선택 순서

- modal class 6종마다 12개, 총 72개를 사용한다.
- 원칙적으로 각 modal에서 TS 23.501 6개와 TS 24.501 6개를 사용한다. 단, 위에서 사전 정의한 `should` 4+8과 `should_not` 8+4 예외를 적용하며 전체 source 합계는 36+36으로 유지한다.
- 각 규격의 candidate scope 안에서 문서 순서대로 검토한다.
- 포함 기준을 만족하는 첫 후보부터 quota를 채운다.
- Pilot 18개와 exact duplicate 또는 핵심 actor-condition-action이 같은 near duplicate는 제외한다.
- Main 내부에서도 같은 modal class 문장끼리 token-set Jaccard가 0.60 이상이면 뒤에 나온 후보를 제외하고 다음 문서 순서 후보를 사용한다. 이는 주체명만 바뀐 구조적 반복이 표본을 과점하지 않게 하는 사전 규칙이다.
- 모델 응답, 예상 성공 여부, C1/C2에 대한 주관적 유불리는 선정 기준으로 사용하지 않는다.

## 기계 분류와 수동 확인

후보 추출기는 조건 표지, 부정 modal, `only/unless/except/if any`, 접속 구조를 기록하고 provisional tier를 부여한다. 최종 tier와 gold label은 PDF 문맥을 사람이 확인한 뒤 확정한다. 표·목록·NOTE·깨진 문장과 외부 문서 직접 인용은 제외한다.

## 동결 조건

다음이 모두 충족돼야 main API 실행을 시작한다.

1. 72개 case ID가 유일하다.
2. modal별 12개와 규격별 6+6 균형이 맞는다.
3. tier 목표 또는 사전 기록된 이동 사유가 있다.
4. 원문, clause, PDF page, source SHA-256이 연결된다.
5. actor·condition·action·exception이 원문에서 직접 추적된다.
6. Pilot과 exact/near duplicate가 없다.
7. 질문이 modal class를 직접 누설하지 않는다.
