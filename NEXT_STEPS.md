# 다음 작업

## 완료: 원문 동결과 `should_not` 후보 감사

실험 코드보다 먼저 **어느 표준 버전을 사용했는지 다시 확인할 수 있는 상태**를 만든다.

- [x] ETSI 공식 사이트에서 TS 23.501·TS 24.501 PDF 다운로드
- [x] 두 규격을 V18.12.0 Release 18로 고정
- [x] PDF를 `data/source/`에 보관
- [x] PDF SHA-256 계산 및 manifest 기록
- [x] `should_not` 원시 occurrence 35건 전수 감사
- [x] 적격 18건, 보류 8건, 제외 9건 판정
- [ ] 원문 전체 재배포 가능 여부는 별도로 확인

Main은 각 modal 범주에서 TS 23.501 6개와 TS 24.501 6개를 사용한다. 단일 규격보다 source 균형을 고정해 modal class와 규격 문체의 교란을 줄인다.

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
- [ ] 최종 prompt bundle 동결 후 18개 전체 pilot 실행
- [x] pass 1·2 비교: 응답 18/18, 적용 가능 이진 판정 105/105 일치, 불일치 0건
- [x] 불일치 사례가 없어 rubric 수정 없이 v1 유지한 이력 기록

같은 평가자의 시간차 재평가이므로 이는 독립 평가자 간 신뢰도가 아니라 평가자 내 재현성 점검이다. 예외 항목은 해당 6개 문장에 양성 사례가 없어 κ를 계산하지 않는다.

## 다음: 전체 Pilot 실행

- [x] 동결된 v3 bundle로 18개×C0/C1/C2, 총 54개 응답 생성 및 54/54 파싱 확인
- [x] 결정적 검사 수행: modal C0 5/18, C1 17/18, C2 18/18; C1·C2 citation 36/36
- [x] `blind_review.csv`의 54개 응답에 대한 masked 의미 채점 pass 1 수행
- [ ] 최소 24시간 후 재무작위화 blind 의미 채점 pass 2 수행
- [ ] Pilot 결과에서 main 설계 수정 필요 여부 판단

Pass 1은 2026-09-02 13:25 KST에 완료했다. 행별 case ID와 조건은 가렸지만 검토자가 사전에 조건별 집계와 C1 오류 1건을 본 상태였으므로 완전 독립·완전 blind라고 부르지 않는다. 같은 평가자의 pass 2는 2026-09-03 13:25 KST 이후 수행한다.

## Pilot 후에만 할 일

- [ ] 본 데이터 72개 수집
- [ ] 실행 스크립트 작성
- [ ] 통계·그래프 자동화
- [ ] ACK 양식에 맞춘 논문 초안

Pilot이 안 닫혔는데 72개를 먼저 만들면 라벨과 prompt 오류를 대량으로 다시 고쳐야 한다. 따라서 원문 동결과 18개 pilot을 첫 마일스톤으로 본다.
