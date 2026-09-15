# 다음 작업

## 우선: 동결한 처리 기준으로 v2 재평가 준비 (2026-09-08)

- [x] 경계 사례와 NOTE 누락 원인을 원본 PDF 문맥·배치와 대조하고 9건의 처리안 작성: [검토 기록](docs/20_gold_boundary_review_2026-09-07.md)
- [x] 설명 전체의 필요조건·규범 적용 대상·양화·상충 표현을 구분하는 [채점 기준 v2 후보](experiments/scoring_v2_candidate.md) 작성
- [x] 72건 전체의 원본 51쪽 적격성 확인: 일반 적격 50, 사전 예외 조건부 적격 1, 부적격 10(NOTE 3·목록 7), 보류 11. [전수 감사와 개별 근거](docs/21_main72_eligibility_audit_2026-09-08.md)
- [x] 부적격 10건·보류 11건을 유지하고 사전 목록 예외 처리 기준 동결. 사후 주 분석 49건 및 민감도 50/50/51건: [동결 기록](docs/22_posthoc_treatment_freeze_2026-09-08.md)
- [x] MAY-001의 평가용 gold overlay와 SD-009 보류를 C0/C1/C2/C3/C1M에 대칭 적용하는 기준 및 scoring v2 동결. 원본 입력·gold는 보존
- [x] 동결 검증 후 별도 v2 검토 패키지 준비: 51개 기준·255개 슬롯, 가림 ID·빈 양식·24시간 2차 생성 검사. [패키지 안내](docs/23_v2_review_package_2026-09-08.md)
- [x] 합집합 51건의 source/gold 사전 확인: 기준 지지 49·미확정 2. `PREFLIGHT_COMPLETE_WITH_UNRESOLVED`; 기존 분모 유지, 응답 재채점 0건. [확인 기록](docs/24_v2_gold_preflight_2026-09-08.md)
- [x] 255개 응답 슬롯의 v2 pass 1 완료·봉인: PASS 169·FAIL 78·UNRESOLVED 7·생성 보류 1. 이전 점수 재사용 없이 별도 기록. [판정 근거](docs/25_v2_semantic_review_pass1_2026-09-08.md)
- [ ] 최소 24시간 후 v2 pass 2 → 불일치 조정. 2차 가능 시각: 2026-09-09 12:31:23.646276 KST 이후. 1차 점수·메모를 2차에 제공하지 않고 기존 v1 지연 검토도 재사용하지 않음
- [ ] 기준 변경 영향과 적격성 제외 분석을 별도 이력으로 보고한 뒤 본문 핵심 비교 보강

기존 동결 데이터·점수·v4 원고는 보존했다. 아래 완료 체크는 당시 수행 이력이며 새 적격성·gold 쟁점 해결을 의미하지 않는다. v2 처리 기준은 새 1차 기록 255개에만 적용했으며 2차 검토·조정·최종 비교는 미완료다. 기존 기준의 C1M 지연 검토와 혼용하지 않는다.

## 완료: 원문 동결과 `should_not` 후보 감사

실험 코드보다 먼저 **어느 표준 버전을 사용했는지 다시 확인할 수 있는 상태**를 만든다.

- [x] ETSI 공식 사이트에서 TS 23.501·TS 24.501 PDF 다운로드
- [x] 두 규격을 V18.12.0 Release 18로 고정
- [x] PDF를 `data/source/`에 보관
- [x] PDF SHA-256 계산 및 manifest 기록
- [x] `should_not` 원시 occurrence 35건 전수 감사
- [x] 적격 18건, 보류 8건, 제외 9건 판정
- [ ] 원문 전체 재배포 가능 여부는 별도로 확인

Main은 원칙적으로 각 modal 범주에서 TS 23.501 6개와 TS 24.501 6개를 사용한다. 사전 기록된 예외로 should는 4+8개, should_not은 8+4개이며 전체 source는 36+36개다.

## 완료: 18개 pilot 데이터셋

동결한 두 규격에서 `data/pilot_cases.csv` 18건을 구성했다.

- [x] TS 23.501 9개·TS 24.501 9개로 source 균형 구성
- [x] `shall` 3개
- [x] `shall_not` 3개
- [x] `should` 3개
- [x] `should_not` 3개
- [x] `may` 3개
- [x] `can` 3개
- [x] 각 case의 actor·condition·action·exception 라벨
- [x] 원문 clause·PDF page·SHA-256 연결 및 자체 검토
- [ ] 독립적인 2차 검토 후 gold label 확정
- [ ] 제외한 문장은 `data/exclusions.csv`에 사유 기록

`should_not`은 감사 완료 후보 중 TS 23.501 2개와 TS 24.501 1개를 선택한다. exact/near duplicate는 pilot과 main에 나누지 않는다.

## 완료: Pilot 실행 계약 동결

이제 18개를 늘리지 않고 먼저 C0/C1/C2 실행과 채점 절차가 재현되는지 확인한다. Pilot의 목적은 모델 순위가 아니라 다음 네 가지를 검증하는 것이다.

1. 라벨을 원문에서 일관되게 추출할 수 있는가?
2. C0/C1/C2의 차이가 정확히 통제되는가?
3. 응답을 두 번 채점해도 같은 결과가 나오는가?
4. 오류 code로 실패 사례를 설명할 수 있는가?

- [x] 세 조건에서 공통으로 사용할 질문·응답 형식 v1 동결
- [x] C0(질문만)·C1(원문 evidence)·C2(구조화 evidence) 입력 차이 점검
- [x] temperature·seed 지원 여부·모델 snapshot·실행일 기록 규칙 확정
- [x] v1·v2 소규모 dry run과 single-annotator blind pass 1
- [x] 최소 24시간 후 동일 평가자의 재무작위화 blind pass 2
- [x] C0를 closed-book forced-answer knowledge baseline으로 확정
- [x] prompt bundle v3(C0 v3·C1 v2·C2 v2) dry run 및 최종 동결
- [x] `PILOT-CAN-001` 라벨 수정이 반영된 검토 workbook v2 재생성
- [x] 최종 prompt bundle 동결 후 18개 전체 pilot 실행
- [x] pass 1·2 비교: 응답 18/18, 적용 가능 이진 판정 105/105 일치, 불일치 0건
- [x] 불일치 사례가 없어 rubric 수정 없이 v1 유지한 이력 기록

같은 평가자의 시간차 재평가이므로 이는 독립 평가자 간 신뢰도가 아니라 평가자 내 재현성 점검이다. 예외 항목은 해당 6개 문장에 양성 사례가 없어 κ를 계산하지 않는다.

## 다음: 전체 Pilot 실행

- [x] 동결된 v3 bundle로 18개×C0/C1/C2, 총 54개 응답 생성 및 54/54 파싱 확인
- [x] 결정적 검사 수행: modal C0 5/18, C1 17/18, C2 18/18; C1·C2 citation 36/36
- [x] `blind_review.csv`의 54개 응답에 대한 masked 의미 채점 pass 1 수행
- [x] 최소 24시간 후 재무작위화 masked 의미 채점 pass 2 수행
- [x] pass 1·2 비교: 응답 54/54, 적용 가능 이진 판정 324/324, 오류 코드 54/54 일치
- [x] 불일치 0건 확인 및 adjudication 불필요 판정
- [x] Pilot 결과에서 main 설계 수정 필요 여부 판단: C1·C2 ceiling을 고려한 난도 층화 필요

Pass 1은 2026-09-02 13:25 KST, pass 2는 2026-09-03 15:04 KST 이후 새 ID·새 순서로 완료했다. 행별 case ID와 조건은 가렸지만 검토자가 사전에 조건별 집계와 C1 오류 1건을 본 상태였으므로 완전 독립·완전 blind라고 부르지 않는다. 이는 동일 평가자의 지연 재검토 결과다.

## 다음: Main 72개 데이터셋

- [x] 모델 결과를 보기 전에 문장 난도 층화 기준 동결
- [x] 공식 PDF에서 7,727개 modal 후보 추출
- [x] 사전 제외 규칙과 문서 순서로 72개 source selection 초안 구성
- [x] modal 12개씩, source 36+36, 난도 8/22/42 구조 검사
- [x] 선언 PDF page·active clause·SHA-256 연결 및 pilot/main 중복 검사
- [x] modal class 6종×12개, 총 72개 source-grounded label 작성
- [x] pilot 18개와 exact/near duplicate가 없는지 검사
- [x] 원문·clause·page·SHA-256 연결의 기계 감사
- [x] 72개 actor·condition·action·exception과 한국어 질문 수동 검수
- [x] main prompt·dataset 최종 동결

`data/main_cases.csv`는 72개 source-grounded label의 단일 평가자 자체 검토를 마쳤고 `data/main_freeze_manifest.json`으로 동결했다. 이는 독립적인 2차 검토 완료를 의미하지 않는다. 동결 후 변경이 필요하면 파일을 조용히 덮어쓰지 말고 errata와 새 manifest를 만든다.

## Pilot 후에만 할 일

- [x] 본 데이터 72개 수집
- [x] 실행 스크립트 작성
- [x] 동결 main 72개×3조건, 총 216개 응답 생성 및 216/216 파싱 확인
- [x] main API 원본·파싱 결과·결정적 채점 결과 해시 동결
- [x] 216개 응답의 masked Codex 단일 평가자 의미 채점 pass 1
- [x] pass 1 paired 통계와 신뢰구간 자동화
- [x] 최소 24시간 후 새 순서의 masked pass 2
- [x] pass 1·2 점수 불일치 29건 adjudication
- [x] 1차 평가 후·지연 2차 평가 전에 기록한 gold-scope ambiguity 3건을 별도 sensitivity 문서로 고정
- [x] adjudicated 결과로 최종 통계 생성
- [x] adjudicated 결과 그래프와 논문용 표 생성·PDF 렌더 검증
- [x] ACK 양식에 맞춘 논문 초안 v2와 방법·통계 서술 보완

## 2026-09-06 보완과 확장

- [x] C2의 oracle gold 입력, Codex 평가자, JSON modal과 설명 지표의 구분 명시
- [x] 모호한 3건 제외 분석의 exact McNemar p=0.125 계산·원고 반영
- [x] 실행 전 모호성 지정이라는 근거 부족 문구 정정
- [x] 제공된 Word 양식의 페이지·여백·2단 및 제목·저자 크기 대조
- [ ] 독립 통신 전문가 gold·응답 검토 — 미실시. 9/6 사용자 요청으로 현 검토는 Codex가 담당하며 전문가 검증을 완료 조건으로 두지 않음
- [x] 자동 구조 추출 C3 실행: 72건 추출, 71건 설명 생성, 1건 보류
- [x] C3 입력·출력 해시, 실제 요청의 gold 비노출, 비용·표본 커버리지 검증
- [x] 새 C1/C2/C3 masked 설명 평가 216행 및 추출 구조 검토 72행 준비
- [x] C3 추출 구조 72행의 의미 검토와 3조건 설명 216행의 의미 평가 pass 1
- [x] C3 설명 pass 1 후 최소 24시간 간격의 재검토·불일치 조정 및 paired 통계
- [x] C1/C2/C3 새 첫 평가와 한계를 논문 v3에 반영하고 KIPS 2쪽 렌더 검증
- [x] 44개 조항 cluster bootstrap·조항 하나씩 제외하는 민감도 분석
- [x] C1M modal·polarity 힌트 분리 비교 설계·입력 동결 및 72건 API 실행
- [x] C1M 실제 요청의 다른 gold 필드 비노출, 해시·파싱·비용 검증
- [x] C1/C2/C1M 216행의 새 masked 의미 검토 자료 준비
- [x] C1M 포함 216행 첫 의미 평가와 C3 지연 재검토 결과를 함께 검토
- [ ] C1M 24시간 지연 재검토·불일치 조정 — 2026-09-08 14:56:16 KST 이후
- [x] C3 지연 조정·C1M 첫 평가를 논문 v4에 반영하고 2쪽 렌더 검증
- [x] 추출기 v2의 원문 구절 연결·보호 어구·참조 역할 프롬프트 및 검증기 초안과 오프라인 검사
- [ ] 추출기 v2 API 실행 계약 동결·개발 비교 및 의미 평가
- [ ] 개발에 사용한 기존 72개와 분리된 새 조항 검증 표본 구성·실행

C3는 `experiments/runs/c3_auto72_v1_2026-09-06T04-53-06-942Z`에 보존했다. 생성 시점 manifest의 `generation_complete_semantics_pending`은 동결 이력이므로 수정하지 않는다. 최신 검토 상태는 `review/pass1_freeze_manifest.json`이며 C1 61/72, C2 71/72, C3 65/72의 잠정 결과다. 기존 판정 차이 9건과 남은 절차는 [의미 평가 보고서](docs/13_c3_semantic_review_pass1_2026-09-06.md)에 기록했다. pass 2는 2026-09-07 14:08:18 KST 이후 가능하다.

C1M은 `experiments/runs/c1m_main72_v1_2026-09-06T05-26-29-574Z`에 72/72 생성·파싱을 보존했다. 설명 의미 성능은 아직 평가하지 않았으며 준비된 검토 216행은 모두 빈 점수다. 최신 원고는 v3이고, 조항 단위 분석·C1M 완료 기록과 이후 우선순위는 [확장 보고서](docs/15_paper_v3_and_priority_extensions_2026-09-06.md)를 따른다. 모델 비교·검색 통합은 새 조항 검증 뒤로 둔다.

Main delayed pass 2와 adjudication까지 완료했다. complete-preservation 행 판정은 216개 중 213개(98.61%, Cohen's kappa 0.970)가 일치했고, 전체 적용 가능 이진 판정은 1,348개 중 1,322개(98.07%, kappa 0.955)가 일치했다. adjudicated complete preservation은 C0 0/72, C1 65/72, C2 72/72이다. `MAIN-CAN-004`, `MAIN-SD-002`, `MAIN-CAN-008`은 동결 label을 바꾸지 않고 gold-scope sensitivity 대상으로 남겼다. 이 결과는 동일 Codex 평가자의 지연 재검토·자체 adjudication이지 독립 통신 전문가 검증은 아니다. API를 다시 호출하거나 원하는 결과가 나올 때까지 반복하지 않는다.

## 2026-09-07 최신 상태

위 9월 6일 기록은 당시 상태다. C3 216행 지연 검토에서 완전 보존 216/216, 세부 판단 1,128/1,131 일치했고 2응답의 차이를 조정했다. C1 61/72, C2 71/72, C3 65/72다. C1M 첫 검토는 68/72이며 새 지연 검토 자료 216행을 준비했다. 최신 원고는 v4다. [C3 완료](docs/16_c3_delayed_review_2026-09-07.md), [C1M 첫 평가](docs/17_c1m_semantic_review_pass1_2026-09-07.md), [v2 준비](docs/18_scope_extractor_v2_staging_2026-09-07.md)를 따른다. 이번 재개 작업의 추가 API 호출은 0회다.
