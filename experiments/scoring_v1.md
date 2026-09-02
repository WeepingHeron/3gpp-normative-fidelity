# Pilot scoring contract v1

## 범위

주 채점 대상은 `explanation_ko`다. 모델이 별도 JSON 필드에 올바른 값을 출력했더라도 자연어 설명이 그 의미와 충돌하면 설명을 기준으로 실패 처리한다. JSON 필드는 채점 보조와 오류 분석에 사용한다.

## Blind 절차

1. `score_run.mjs`가 응답 순서를 결정적으로 섞고 `review_id`를 부여한다.
2. 검토자는 `blind_review.csv`만 사용하며 case ID와 C0/C1/C2 조건을 보지 않는다.
3. 1차 채점 후 최소 24시간을 두고 같은 파일을 새 복사본에서 다시 채점한다.
4. 두 판정이 다르면 원문을 다시 확인하고 최종 판정과 변경 이유를 별도 adjudication log에 남긴다.
5. 채점 완료 후에만 `blind_key.json`으로 조건을 복원한다.

## 필드 판정

각 필드는 `1`, `0`, `NA` 중 하나다.

- `actor_preserved`: 원문의 규범 행위자가 동일하면 1. 다른 주체로 바꾸거나 주체를 식별할 수 없게 만들면 0.
- `polarity_preserved`: 긍정·부정 방향과 규범 강도가 모두 보존되면 1. 약화·강화·부정 반전이면 0.
- `condition_preserved`: 적용 조건의 범위를 보존하면 1. 조건을 삭제·확대·축소하면 0. gold가 비어 있으면 NA.
- `action_preserved`: 핵심 행동과 대상이 보존되면 1. 핵심 동작·대상·방향이 달라지면 0.
- `exception_preserved`: 예외나 한계를 보존하면 1. 누락·추가·변경하면 0. gold가 비어 있으면 NA.
- `unsupported_addition`: 원문에 없는 주요 의무·금지·권고·허용·조건·예외를 추가하면 1, 아니면 0.

문체 차이, 자연스러운 한국어 어순 변경, 약어의 풀어쓰기만으로는 실패 처리하지 않는다.

## 파생 지표

- `modal_correct`: 설명의 규범 유형이 gold modal class와 일치하면 1.
- `complete_preservation`: 적용 가능한 actor·polarity·condition·action·exception이 모두 1이고 unsupported addition이 0일 때만 1.
- `citation_exact`: C1/C2에서 spec ID·version·clause가 모두 정확할 때 1. C0는 NA.
- 파싱 실패·거절·빈 응답은 적용 가능한 보존 필드와 complete preservation을 0으로 처리하고 오류 code를 기록한다.

## 오류 code 우선순위

한 응답에 여러 code를 허용한다. `POLARITY_FLIPPED`, `MODAL_WEAKENED`, `MODAL_STRENGTHENED`, `ACTOR_CHANGED`, `CONDITION_DROPPED`, `EXCEPTION_DROPPED`, `ACTION_CHANGED`, `UNSUPPORTED_ADDITION`, `CITATION_WRONG`, `REFUSED` 중 해당 항목을 세미콜론으로 연결한다.

## Pilot 수정 규칙

Pilot 응답을 본 뒤 prompt나 rubric을 수정할 수 있지만 버전 파일을 덮어쓰지 않는다. 변경 시 `v2` 파일을 만들고 변경 이유, 영향 사례, 수정 전후 hash를 남긴다. Main 실행을 시작한 뒤에는 prompt와 gold label을 고정한다.
