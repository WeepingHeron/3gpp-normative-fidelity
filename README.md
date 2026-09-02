# 3GPP 규범적 의미 보존 연구

> ACK 2026 학부생 논문경진대회를 목표로, 영문 3GPP 요구사항을 한국어로 설명할 때 LLM이 규범적 강도·행위자·조건·부정을 정확히 보존하는지 평가한다.

## 핵심 연구 질문

- **RQ1.** 일반 LLM은 `shall / shall not / should / should not / may / can` 차이를 한국어 설명에서 정확히 보존하는가?
- **RQ2.** 원문 조항을 제공하는 것만으로 오류가 줄어드는가?
- **RQ3.** `행위자·조건·규범 유형·행동·예외`를 먼저 구조화하는 Evidence Constraint가 일반 RAG보다 의미 보존을 개선하는가?

## 비교 조건

| ID | 조건 | 목적 |
|---|---|---|
| C0 | 질문만 제공하는 LLM | 사전지식 기준선 |
| C1 | 같은 정답 조항을 제공하는 Vanilla RAG | 원문 제공 효과 |
| C2 | 같은 조항 + 구조화된 Evidence Constraint | 제안 방법 효과 |

C1과 C2에는 동일한 원문 조항을 제공한다. 주 실험은 검색 실패를 제거한 `oracle evidence` 설정으로 진행하여, 발생한 차이를 생성 및 제약 방식의 효과로 해석한다. 실제 검색 파이프라인은 시간이 남을 때만 보조 실험으로 추가한다.

## 목표 산출물

- 72개 규범 문장 데이터셋
- C0/C1/C2 모델 응답과 실행 메타데이터
- 규범 유형, 부정, 행위자, 조건, 예외, 인용 정확도 평가
- 조건별 정확도, paired 차이, 95% 신뢰구간
- ACK 2026 학부생 논문 2~3쪽

## 문서 구조

- [`docs/01_research_plan.md`](docs/01_research_plan.md): 문제 정의, 범위, 가설, 일정
- [`docs/02_dataset_protocol.md`](docs/02_dataset_protocol.md): 문장 수집·라벨링·분할 규칙
- [`docs/03_evaluation_protocol.md`](docs/03_evaluation_protocol.md): 실험 통제와 평가 지표
- [`docs/04_related_work_and_novelty.md`](docs/04_related_work_and_novelty.md): 선행연구 중복 방지선
- [`docs/05_paper_outline.md`](docs/05_paper_outline.md): ACK 2~3쪽 논문 구성
- [`data/README.md`](data/README.md): 데이터 디렉터리와 필드 설명
- [`data/cases_template.csv`](data/cases_template.csv): 데이터셋 작성 템플릿
- [`experiments/README.md`](experiments/README.md): 실행 결과 보존 규칙

## 가장 먼저 할 일

1. `docs/01_research_plan.md`의 제외 범위까지 읽고 연구 질문을 동결한다.
2. 3GPP TS 23.501의 하나의 공식 버전을 고르고 PDF 파일과 SHA-256을 기록한다.
3. `shall / shall not / should / should not / may / can` 각 3개씩, 총 18개로 pilot dataset을 먼저 만든다.
4. C0/C1/C2를 수작업으로 18개에 실행해 응답 형식과 채점 규칙이 실제로 작동하는지 확인한다.
5. pilot이 닫힌 후에만 72개로 확장한다.

## 완료 경계

이 연구는 모델이 3GPP 전체를 이해한다는 것을 입증하지 않는다. 선정한 표준·버전·문장 표본·모델·프롬프트 조건에서 한국어 규범 의미 보존 오류를 관찰하는 통제 실험으로 한정한다.
