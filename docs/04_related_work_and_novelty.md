# 04. 선행연구·차별성 관리

## 1. 중복 위험이 큰 주장

다음을 본 연구의 새로운 기여로 주장하지 않는다.

- 3GPP 문서에 RAG를 적용함
- 통신 질의응답에서 LLM을 평가함
- RAG가 LLM-only 정확도를 높임
- Agent가 여러 3GPP 조항을 탐색함
- Release 변화와 교차 참조를 추적함
- 한국어 통신 Agent 벤치마크를 만듦
- LLM 자기 확신도를 calibration함
- 일반적인 Verifier-RAG로 hallucination을 줄임

## 2. 본 연구의 제한된 차별성

본 연구의 차별점은 다음 교차영역으로 한정한다.

> **영문 3GPP 규범 문장을 한국어로 설명할 때, 의무 강도·부정·행위자·조건·예외의 변형을 paired experiment로 측정하고, 구조화된 Evidence Constraint의 효과를 평가한다.**

즉, 일반 통신 QA 정확도나 검색 Recall이 주 연구 대상이 아니다.

## 3. 필수 비교 문헌

| 문헌 | 이미 다룬 범위 | 본 연구와의 경계 |
|---|---|---|
| TSpec-LLM (2024) | Release 8~19 데이터셋, naive RAG QA | 한국어 규범 의미 보존 평가가 주제가 아님 |
| TelecomRAG / Telco-RAG | 3GPP 전문 RAG 정확도·검증성 | RAG 자체를 기여로 주장하지 않음 |
| TelAgentBench (2025) | 한국어 통신 Agent의 reasoning/planning/action/RAG | 영·한 paired normative fidelity 평가로 좁힘 |
| CellularSpecSec-Bench (2026) | 3GPP normative language, 교차참조, 보안 추론 | 한국어 설명에서의 modal·condition 보존을 직접 대상으로 함 |
| DeepSpecs (2026) | clause 교차참조, version diff, Change Request | Release-aware retrieval을 본 연구 기여에서 제외 |
| Twin-Pass Telco Confidence (2026) | TeleQnA/O-RAN/srsRAN confidence calibration | confidence calibration을 본 연구 기여에서 제외 |

## 4. 참고 URL

- TSpec-LLM: https://arxiv.org/abs/2406.01768
- TelecomRAG: https://arxiv.org/abs/2406.07053
- Telco-RAG: https://arxiv.org/abs/2404.15939
- TelAgentBench: https://aclanthology.org/2025.emnlp-industry.83/
- CellularSpecSec-Bench: https://arxiv.org/abs/2601.12716
- DeepSpecs: https://aclanthology.org/2026.findings-acl.1343/
- Enhancing Confidence Estimation in Telco LLMs: https://arxiv.org/abs/2604.13271
- ETSI TS 23.501 V18.10.0 예시: https://www.etsi.org/deliver/etsi_ts/123500_123599/123501/18.10.00_60/ts_123501v181000p.pdf

## 5. 문헌 조사 추가 키워드

논문 작성 전에 다음 조합을 Google Scholar, IEEE Xplore, ACM DL, ACL Anthology, arXiv에서 다시 검색한다.

- `3GPP normative language LLM Korean`
- `3GPP shall should may translation LLM`
- `telecom standards cross-lingual RAG Korean`
- `modality preservation technical standards generation`
- `requirements translation modal strength LLM`
- `evidence constrained generation normative requirements`

검색일, query, 검색 DB, 가장 가까운 문헌, 차이를 별도 로그에 기록한다. `동일한 연구가 없다`보다 `확인한 범위에서 영·한 규범 의미 보존을 직접 평가한 연구는 발견하지 못했다`로 제한해 표현한다.
