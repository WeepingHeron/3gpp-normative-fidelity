# 결과 표·그래프 검증 보고서

## 종합 판정: 제한사항을 명시하면 공유 가능

논문용 표와 그래프는 동결된 main 72 cases × 3 conditions의 `human_scores_adjudicated.csv`에서 생성했다. 수치·분모·Wilson 신뢰구간은 저장된 `analysis_adjudicated.json`과 독립 재계산 결과가 일치한다. 다만 pass 1, delayed pass 2, adjudication이 모두 동일 Codex 평가자에 의해 수행됐으므로 독립 통신 전문가 검증으로 표현하면 안 된다.

## 계산 검증

- 입력 행: 216개, `(case_id, condition)` 중복 없음
- 조건별 분모: C0·C1·C2 각각 72개
- complete preservation: C0 0/72, C1 65/72, C2 72/72
- C1 modal class 합계: 12 + 12 + 11 + 8 + 12 + 10 = 65
- C1 failure: 7개이며 `paper/tables/main_results.md`에 case ID와 실패 구성요소를 기록
- C1→C2 paired difference: +9.72%p, paired bootstrap 95% CI +2.78~+16.67%p, exact McNemar p=0.015625

## 시각화 검증

- Figure 1: 막대축 0 시작, Wilson 95% CI와 성공 수/72 직접 표기
- Figure 2: modal 6종 × 조건 3종의 모든 셀 n=12 확인, 성공 수와 비율 직접 표기
- Figure 3: actor·force·condition·action·exception은 적용 가능 응답을 분모로 사용하고, unsupported addition은 조건별 72개를 분모로 사용
- PNG 300 dpi와 PDF/SVG 벡터본 생성
- 세 PDF를 Poppler로 재렌더링하여 제목, 부제, 축, 범례, 셀 값, 주석의 잘림·겹침이 없음을 확인
- 색상 외에도 hatch와 직접 숫자를 사용해 흑백 인쇄 구분을 보조

## 반드시 함께 제시할 제한사항

- C2의 72/72는 이 동결된 oracle-evidence 데이터셋에서의 ceiling 결과이며 일반적인 완전 성능을 뜻하지 않는다.
- 본 실험은 retrieval 성능을 평가하지 않는다.
- 단일 모델 snapshot, 두 고정 규격 버전, 72개 문장에 한정된다.
- `MAIN-CAN-004`, `MAIN-SD-002`, `MAIN-CAN-008`은 사전 지정된 gold-scope sensitivity 대상이다.
- 독립 통신 전문가 검토가 없다면 single-reviewer limitation을 초록·방법·한계 중 적어도 방법과 한계에 명시해야 한다.

## 다음 조치

그래프와 표 자체에는 수정이 필요한 blocker가 없다. 다음 단계는 이 결과를 사용해 ACK 3쪽 초안을 작성하고, 가능하면 세 gold-scope 문장과 C1 실패 7건을 통신 전공자가 검토하는 것이다.
