# 05. ACK 2026 논문 구성

## 가제

**국문:** 3GPP 요구사항의 한국어 설명에서 규범적 의미 보존을 위한 증거 제약 생성 평가

**영문:** Evaluating Evidence-Constrained Generation for Preserving Normative Meaning in Korean Explanations of 3GPP Requirements

`RAG`라는 단어를 제목에 쓸지는 본 실험 구현 후 결정한다. 주 실험이 oracle evidence를 사용하면 `Evidence-Constrained Generation`이 더 정확한 표현이다.

## 1. 서론

- 3GPP 규격의 규모와 한국어 설명 필요
- `shall/should/may/can`이 공학적 의미를 구분한다는 문제
- 일반 QA 정확도로는 잡히지 않는 규범 의미 변형
- 연구 질문과 기여 2~3개

기여는 다음 정도로 제한한다.

1. 3GPP 규범 문장의 한국어 설명 오류를 modal·polarity·actor·condition·action·exception으로 분해한 평가 설계
2. 동일 증거를 사용한 Vanilla 생성과 Evidence-Constrained 생성의 paired comparison
3. 정확도 향상과 누락·강화·약화 오류 변화에 대한 실증 분석

## 2. 관련 연구

- 3GPP QA/RAG: TSpec-LLM, TelecomRAG, Telco-RAG
- Agentic/version-aware: TelcoAI, DeepSpecs
- 한국어 통신 Agent: TelAgentBench
- Normative 3GPP reasoning: CellularSpecSec-Bench
- 결론: 본 연구는 영·한 설명 과정의 규범 의미 보존으로 범위를 좁힘

## 3. 연구 방법

### 3.1 Dataset

- 공식 배포본과 대조 가능한 ETSI TS 123 501·TS 124 501(V18.12.0, Release 18) 고정 PDF
- 6개 modal class × 12개 = 72 cases
- source-grounded structured labels

### 3.2 Conditions

- C0: question only
- C1: question + gold source clause
- C2: question + gold source clause + structured evidence constraint

### 3.3 Metrics

- Modal Class Accuracy
- Complete Preservation Rate
- Unsupported Addition Rate
- Citation Exactness
- paired McNemar test and bootstrap confidence interval

## 4. 실험 결과

- 표 1: C0/C1/C2 전체 지표
- 표 2: 오류 유형별 빈도
- 그림 1: modal class별 complete preservation heatmap
- 전체 complete-preservation CI 막대와 구성요소 오류 그래프는 지면이 허용될 때만 사용
- 성공 사례와 실패 사례 각 1개

결과가 예상과 다르면 그대로 기술한다. C2가 개선하지 못했다면 구조화 오류, 한국어 표면형 모호성, 제약으로 인한 응답 누락을 분석한다.

## 5. 결론·한계

- 어떤 오류가 자주 발생했는지
- Evidence Constraint가 어떤 항목에서 효과가 있었는지
- 단일 표준·버전·주 모델·소규모 표본 한계
- oracle evidence를 사용했으므로 검색 성능으로 일반화할 수 없음
- 전문가 2차 검토가 없으면 single-annotator limitation 명시

## 지면 배분 제안

| 영역 | 지면 |
|---|---:|
| 제목·초록·서론 | 0.45쪽 |
| 관련 연구 | 0.35쪽 |
| 방법 | 0.70쪽 |
| 결과·표·그림 | 0.90쪽 |
| 결론·한계·참고문헌 | 0.60쪽 |

3쪽을 초과하면 예시 응답 수를 줄이고, 주 표와 그림은 유지한다.
