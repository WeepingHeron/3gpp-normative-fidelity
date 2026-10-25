# 결과 시각화 계약

## 공통 범위

- 분석 질문: 구조화된 evidence constraint가 3GPP 요구사항의 한국어 설명에서 규범 의미 보존과 오류 감소에 어떤 차이를 보이는가?
- 데이터: `human_scores_adjudicated.csv`, 72 cases × C0/C1/C2 = 216 responses
- 상태: delayed same-Codex-reviewer adjudication 완료; independent telecom-expert validation 아님
- 출력: ACK 논문 삽입용 PDF/SVG와 검토용 300 dpi PNG
- 팔레트: blue·gold·orange 3색 이내, 흑백 구분용 hatch·직접 값 병행
- QA: 모든 비율을 CSV에서 독립 재계산하고 `analysis_adjudicated.json`과 대조한 뒤 실제 PNG를 육안 검사

## Figure 1 — 전체 complete preservation

- 질문: C0/C1/C2의 전체 complete-preservation rate는 어떻게 다른가?
- 형태: 0–100% 세로 막대와 Wilson 95% CI
- 데이터: 조건별 72개 응답, 성공 수와 분모 직접 표기
- 핵심 해석: C0 0/72, C1 65/72, C2 72/72. C1→C2는 paired +9.72%p이지만 C2 ceiling을 함께 밝힘.

## Figure 2 — modal class별 complete preservation

- 질문: 전체 결과가 특정 modal class에만 의존하는가?
- 형태: 6 modal classes × 3 conditions heatmap, 각 셀에 성공 수/12와 비율 직접 표기
- 데이터 충분성: 각 셀 n=12로 균형화되어 있으나 세부 추론에는 표본이 작으므로 기술통계로 사용

## Figure 3 — 의미 구성요소별 실패율

- 질문: 각 조건에서 어떤 의미 구성요소가 가장 자주 보존되지 않는가?
- 형태: actor·normative force·condition·action·exception·unsupported addition의 조건별 grouped bar
- 분모: 앞의 다섯 항목은 해당 field가 적용 가능한 응답 수, unsupported addition은 조건별 전체 72개
- 주의: exception은 적용 가능한 표본 수가 다르므로 막대 위에 실패 수/분모를 직접 표기
