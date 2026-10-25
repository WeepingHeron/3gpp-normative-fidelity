# v2 재평가 패키지 준비 기록

2026-09-08. 상태: **`PREPARED_PREFLIGHT_PENDING`**. 동결된 `posthoc_treatment_v1_20260908`의 합집합 51건×5조건, 총 255개 슬롯을 새 검토 자료로 구성했다. 실제 gold 사전 확인·의미 재채점·새 모델 호출은 각각 0건이다. 패키지 준비 완료를 재평가 완료로 읽지 않는다.

## 범위와 파일

- [검토 시작 안내](../outputs/review/v2_20260908/REVIEW_GUIDE.md)
- [51개 source/gold 기준](../outputs/review/v2_20260908/preflight/references.jsonl), [읽기용 첫 묶음](../outputs/review/v2_20260908/preflight/readable/batch_01.md), [빈 기록 JSONL](../outputs/review/v2_20260908/preflight/judgments_blank.jsonl)
- [255개 1차 검토 응답](../outputs/review/v2_20260908/reviewer/pass1/packets.jsonl), [읽기용 첫 묶음](../outputs/review/v2_20260908/reviewer/pass1/readable/batch_01.md), [빈 기록 JSONL](../outputs/review/v2_20260908/reviewer/pass1/judgments_blank.jsonl), [동일한 CSV](../outputs/review/v2_20260908/reviewer/pass1/judgments_blank.csv)
- [패키지 상태](../outputs/review/v2_20260908/package_state.json), [파일 해시 목록](../outputs/review/v2_20260908/package_manifest.json)
- [검증 영수증](../outputs/analysis/v2_review_package_20260908/verification_receipt.json)

합집합은 동결된 민감도 51건과 같고, 5조건에 같은 사례를 배치했다. 사후 주 분석 49건, 민감도 50/50/51건의 매핑은 관리용 파일에 보존했다. 부적격 10건과 보류 11건은 재진입시키지 않았다. 원문·질문과 설명 문자열을 바꾸지 않았다. 평가용 gold 참고에는 지정된 MAY-001의 action·summary 정정만 적용했다. C2가 실제 생성 당시 잘못된 gold를 받았다는 이력은 그대로이며, 해당 사례를 주 분석에 복귀시키지 않는다.

254개 슬롯에는 설명이 있다. 나머지 1개는 MAIN-SD-002/C3의 `abstained_extraction_invalid_or_unclear` 레코드로, `NOT_GENERATED` 전달 상태로 연결했다. 이 단계에서는 의미 판정이나 결과값을 미리 채우지 않았다. 후속 검토에서 포함 사례의 생성 보류는 `NOT_SCORED`와 pipeline 결과 0으로 기록한다. 누락·해시 불일치 레코드와는 구별한다.

## 가림과 근거 출처

검토 자료에는 조건명, 원본 case ID, 이전 점수, mapping key를 넣지 않았다. 기준 ID `G001`–`G051`과 검토 ID `V2-P1-001`–`255`를 사용한다. 조건·집계 매핑과 원본 응답 전체 레코드는 `coordinator/`에 분리했다. 1차·2차 순서는 동결된 seed와 SHA-256 알고리즘으로 각각 계산하며, 2차는 순서만 관리용 key에 준비하고 검토용 응답·판정 양식은 아직 배포하지 않았다.

같은 평가자의 이전 실험 지식과 응답 표현에서 조건을 추측할 가능성은 남는다. 독립적이거나 완전한 눈가림 검토라고 주장하지 않는다. 폴더 분리와 24시간 검사도 접근 통제나 암호학적 시각 증명이 아닌 연구 절차 검증이다.

전후 PDF 문맥은 이전 적격성 감사의 추출문을 원문 출처·페이지·해시와 함께 연결했다. 이 패키지 준비에서 PDF를 새로 판독하거나 51개 gold 명제를 모두 확정하지 않았다. 기준 자료의 source/question과 판정자 전용 PDF 문맥을 분리하고, 가림 검토 후 관리자가 조건별 실제 입력 제공 여부를 연결한다. C0에는 source가 없고, C3 extractor는 source만 받는다. 생성 보류된 슬롯의 generator에 실제 입력이 전달되었다고 표시하지 않는다. 입력 경로 안내는 기존 동결 runner/prompt 구조에 근거하며 새 요청 실행 기록이 아니다.

## 사용 순서

1. 검증 명령을 실행한다. 패키지의 빈 양식은 수정하지 않고 별도 작업 디렉터리에 복사한다. JSONL이 검증 입력이고 CSV는 보조본이다.
2. 51건의 source/gold 사전 확인 기록을 작성한다. 기존 gold는 참고 자료이며 `SOURCE_SUPPORTED`를 기본값으로 채우지 않는다. 원문 명제·관계·양화·근거 출처·검토 시각을 기록하고 새 충돌은 `UNRESOLVED`로 남긴다. 미확정 사례의 조건별 분모는 바꾸지 않는다.
3. 사전 확인 파일 검증 후 255개를 모두 v2 pass 1으로 검토한다. 기존 점수를 가져오지 않는다. 미확정은 null이며 원문 판정 미확정과 pipeline 실패를 구별한다.
4. 완료한 1차 기록과 사전 확인 기록을 검증·봉인한다. 실제 봉인 시각을 저장하며 가장 늦은 검토 시각보다 빠를 수 없다.
5. 봉인 후 24시간이 지나면 새 순서의 pass 2를 별도 디렉터리에 생성한다. 1차 판정·메모는 복사하지 않는다. 이후 지연 재검토와 불일치 조정이 필요하다. 이 도구는 조정·집계·논문 갱신을 실행하지 않는다.

```sh
python3 tools/prepare_v2_review_package_20260908.py verify --self-test

# 아래 경로는 이후 작성할 작업 사본 예시이며 아직 존재하는 완료 결과가 아니다.
python3 tools/prepare_v2_review_package_20260908.py check-preflight \
  --preflight outputs/review/v2_work/preflight_completed.jsonl

python3 tools/prepare_v2_review_package_20260908.py seal-pass1 \
  --preflight outputs/review/v2_work/preflight_completed.jsonl \
  --judgments outputs/review/v2_work/pass1_completed.jsonl \
  --output outputs/review/v2_pass1_sealed

python3 tools/prepare_v2_review_package_20260908.py release-pass2 \
  --seal outputs/review/v2_pass1_sealed \
  --output outputs/review/v2_pass2
```

입력 기록의 구조·무결성·상태 조합 검증은 의미 판단의 타당성을 자동 증명하지 않는다. 사전 확인에 미확정이 있어도 근거와 상태를 빠짐없이 기록하면 검토 단계로 진행할 수 있다. gold 미확정에서 PASS는 허용하지 않으며, 독립적으로 명확한 오류가 있는 FAIL은 별도 reason code와 근거를 요구한다.

## 검증 범위

기존 동결 파일 119개 및 그 의존 manifest 9개를 확인한다. 패키지 검증은 51개 기준과 255개 응답의 전수 연결, 조건 대칭, source·question·gold overlay·응답 문자열의 원본 일치, 정해진 순서, 빈 판정 필드, CSV/JSONL 대응, 관리용 매핑, 2차 미배포를 확인한다. 합성 검증 fixture는 메모리에서만 사용하며 연구 판정으로 저장하지 않는다. 빈 사전 확인, 중복·누락, 다른 rubric/pass, 미확정의 0 변환, 전달 상태 변경, 검토 시간 역전, 24시간 미경과를 거부하는 동작을 검사한다.

기존 main gold, 생성 입력·응답, v1 점수, v4 원고, 앞서 동결한 처리 규칙은 변경하지 않았다. README/NEXT_STEPS의 진행 안내만 갱신했다. 다음 실제 연구 단계는 **51건의 source/gold 사전 확인**이다.
