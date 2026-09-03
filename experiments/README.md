# Experiments

## 예정 구조

```text
experiments/
├── README.md
├── prompts/
│   ├── c0_v1.md
│   ├── c1_v1.md
│   └── c2_v1.md
├── runs/
│   └── <run_id>/
│       ├── manifest.json
│       ├── raw_responses.jsonl
│       └── parsed_responses.jsonl
└── evaluation/
    ├── scores.csv
    ├── errors.csv
    └── summary.json
```

## 실행 원칙

- raw response는 수정하지 않는다.
- 파싱 결과와 raw response를 별도로 보존한다.
- run manifest에 model, provider, parameter, prompt hash, dataset hash, 실행일을 기록한다.
- API 재시도·파싱 재시도는 attempt별로 남긴다.
- 실패한 응답을 임의로 제외하지 않는다.
- 응답을 본 후 prompt를 바꿔 같은 main dataset에 재실행하지 않는다.

## 동결된 실행 계약 v1

- 공통 출력: `response_schema.json`의 JSON schema
- C0: 한국어 질문만 제공
- C1: 질문 + gold 영문 원문 + 출처 식별자
- C2: C1과 동일한 원문 + actor·condition·normative type·polarity·action·exception
- C0/C1/C2의 규범 유형 정의와 출력 형식은 동일하다.
- 기본 모델: `gpt-5.4-mini-2026-03-17` snapshot
- 기본 설정: temperature 0, reasoning effort none, max output 600, response storage off
- 재시도: 전송 오류·일시적 HTTP 429·5xx만 최대 2회 재시도하며 모든 attempt를 raw log에 남긴다. `insufficient_quota`와 `credit_balance_exhausted`는 재시도하지 않고 run을 `blocked`로 종료한다. 파싱·의미 실패도 재실행하지 않는다.

## 실행

```bash
node experiments/run_pilot.mjs --prompt-version=v3
node experiments/score_run.mjs experiments/runs/<run_id>
node experiments/merge_review.mjs experiments/runs/<run_id>
```

기본 실행은 modal class별 첫 사례 1개씩 총 6개에 C0/C1/C2를 적용하는 18-call dry run이다. 18개 pilot 전체 54-call 실행은 prompt와 rubric 검토가 끝난 뒤 `--full-pilot`으로 수행한다.

V1과 V2 dry run 결과 C0가 모든 사례에서 `unclear`를 선택해, C0를 safe-abstention이 아니라 closed-book forced-answer baseline으로 다시 정의했다. Prompt bundle v3는 C0만 `c0_v3.md`로 변경하고 C1·C2는 검증된 v2 파일을 그대로 사용한다. 따라서 v2→v3 비교에서 변한 실험 요소는 C0 정의뿐이다. 이 결과는 작은 단일-검토자 점검이며 성능 주장에 사용하지 않는다.

V3 dry run에서 C0는 6건 모두 답했지만 modal class와 complete preservation이 모두 0/6이었고 unsupported addition은 6/6이었다. C1과 C2는 모두 6/6 complete preservation이었다. 따라서 exact evidence의 필요성은 관찰됐지만 C2가 C1보다 낫다는 차이는 관찰되지 않았다.

24시간 이상 간격을 둔 동일 평가자의 재무작위화 blind pass 2에서 응답 단위 18/18, 적용 가능한 이진 판정 105/105, 오류 코드 18/18이 pass 1과 일치했다. Aggregate Cohen's κ는 1.0이다. 이는 독립 평가자 간 신뢰도가 아니라 평가자 내 재현성 근거다. 예외 보존은 해당 6개 사례에 양성 예외가 없어 κ를 계산하지 않았다. 불일치가 없으므로 rubric v1과 prompt bundle v3를 수정 없이 동결한다.

자동 채점은 schema parse, modal class, exact citation처럼 문자열 규칙으로 판정 가능한 항목에 한정한다. actor·condition·action·exception·unsupported addition은 `blind_review.csv`에서 사람이 채점한다. 이 파일에는 case ID와 실험 조건을 숨기고 원문·gold 필드만 제공한다. 상세 판정 규칙은 `scoring_v1.md`를 따른다. 의미 보존을 단순 문자열 일치로 점수화하지 않는다.

## 첫 실행 목적

첫 실행은 성능 주장이 아니라 출력 스키마, prompt, 채점 재현성을 검증하는 것이다. Dry run 결과는 main 결과에 포함하지 않는다.

## 전체 18-case pilot

동결된 v3 bundle로 2026-09-02에 18개 사례×3조건, 총 54개 응답을 생성했고 54/54가 API 및 JSON parsing에 성공했다. 결정적 임시 검사는 modal class가 C0 5/18, C1 17/18, C2 18/18이었고 C1·C2의 exact citation은 36/36이었다. C1의 한 오류는 `PILOT-CAN-001`의 `can`을 `permission`으로 분류한 사례다.

Masked pass 1에서 complete preservation은 C0 0/18, C1 18/18, C2 18/18이었고 unsupported addition은 C0 18/18, C1 0/18, C2 0/18이었다. C1의 `PILOT-CAN-001`은 자연어 설명이 통신 능력을 보존해 component score는 통과했지만 JSON normative type은 `permission`이어서 deterministic modal score에는 오류가 남는다.

24시간 이상 뒤 새 ID·새 순서로 수행한 pass 2는 응답 단위 54/54, 적용 가능한 이진 판정 324/324, 오류 코드 54/54가 pass 1과 일치했고 aggregate Cohen's κ는 1.0이었다. 불일치가 없어 adjudication으로 점수를 변경하지 않았다.

행별 case ID와 조건은 두 pass에서 숨겼지만 검토자가 사전에 조건별 집계와 해당 C1 오류를 본 상태였으므로 완전 독립·완전 blind 검토는 아니다. 이 결과는 동일 평가자의 지연 재검토로만 해석한다. 또한 C1과 C2의 complete preservation이 모두 18/18이므로 C2 우월성은 관찰되지 않았고, main에서는 모델 결과를 보기 전에 정의한 문장 난도 층화로 ceiling risk를 줄인다. 전체 pilot은 main 결과에 포함하지 않는다.
