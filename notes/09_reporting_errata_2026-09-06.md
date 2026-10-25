# 동결 실험의 평가 정의와 보고 정정

2026-09-06. 원래 main 데이터·prompt·rubric·응답·채점은 유지한다. 이 문서는 보고 정의를 정정하며 점수를 재라벨링하지 않는다.

1. C2는 `main_cases.csv`의 평가 gold 구조와 같은 필드를 입력받았다. 자동 구조 추출 결과가 아니다. oracle source인 C1 대비 oracle structured인 C2 비교로 부른다.
2. `score_run.mjs`의 `modal_correct`는 JSON `normative_type` 정답 일치다. 동결 `scoring_v1.md`의 자연어 modal 정의와 달라 보고명은 **JSON modal label accuracy**로 정정한다. 한국어 설명 완전 보존과 별도로 보고하고, 새 자연어 modal 지표를 소급 추정하지 않는다.
3. `polarity_preserved`는 부정뿐 아니라 규범 강도를 함께 평가한다. citation_exact는 제공된 규격·버전·조항 식별자 복사 일치다.
4. 라벨 자체 검토·두 번의 의미 평가·adjudication은 Codex 기반이다. 독립 인간 전문가 타당도가 없으며 평가 전 조건별 집계를 본 이력도 공개한다. 동일 Codex 지연 재평가의 κ를 인간 평가자 간 신뢰도로 부르지 않는다.
5. 모호성 3건의 확인 가능한 최초 기록은 API 실행 후 pass 1 commit `81a4472`이다. `실행 전에 지정`을 `1차 평가 후 지연 2차 평가 전에 기록`으로 정정한다. 원래 데이터 사전 동결은 유효하다.
6. 원래 72건은 C1 65, C2 72, 차이 +9.72%p, exact McNemar p=0.015625다. 3건 제외 민감도는 C1 65/69, C2 69/69, 차이 +5.80%p, p=0.125다. 방향은 유지되지만 유의성은 유지되지 않는다. 69건 분석으로 원래 결과를 대체하지 않는다.
7. C1 token 합계 53,315, C2 59,194로 11.0% 증가했다. 자동 추출·gold 구축 비용과 요청별 정밀 지연은 포함하지 않는다.

현재 원고는 `outputs/paper/ACK2026_3GPP_normative_fidelity_draft_v2.docx`와 그 내용에서 생성한 v2 Markdown이다. v1과 이전 실행 보고서는 이력이며, 현 해석에는 이 정정을 함께 적용한다.

재현: `python3 tools/verify_main_freeze.py`, `python3 tools/review_project_20260906.py`.
