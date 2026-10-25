# v2 원문·정답 기준 사전 확인

2026-09-08. **51건 전체 확인 완료: SOURCE_SUPPORTED 49건, UNRESOLVED 2건.** 상태는 `PREFLIGHT_COMPLETE_WITH_UNRESOLVED`다. 동일 Codex 평가자의 원문 대조이며 독립 전문가 검증이 아니다. 모델 응답 의미 판정·새 모델 호출은 0건이다.

[완료 기록 JSONL](../outputs/review/v2_preflight_20260908/preflight_completed.jsonl), [사례별 요약 CSV](../outputs/review/v2_preflight_20260908/preflight_index.csv), [집합별 상태](../outputs/review/v2_preflight_20260908/summary.json), [검증 영수증](../outputs/review/v2_preflight_20260908/verification_receipt.json), [완료 해시 목록](../outputs/review/v2_preflight_20260908/completion_manifest.json).

## 확인 범위와 의미

51개 source·question·gold 참고 필드를 모두 읽고, 원본 PDF의 해당 38쪽을 다시 시각 확인했다. 저장 규칙 참조를 확인하기 위해 TS 24.501 Annex C의 추가 5쪽(PDF 1089–1093쪽)도 확인했다. 58개 source 명제를 수동으로 작성하고 규범 표현의 직접 적용 범위, 행위자, 행동·상태, 조건, 양화, 명제 간 관계를 기록했다. 각 기록은 원문 인용·규격·버전·조항·PDF 페이지와 연결되어 있다.

`SOURCE_SUPPORTED`는 **원문과 동결 v2 규칙으로 해석한 기준 명제가 지지됨**을 뜻한다. 기존 flat gold의 모든 필드나 한 줄 요약이 완전하다는 뜻은 아니다. 기존 동결 규칙이 요구하는 명제 분해를 적용했으며 새로운 gold 필드 패치는 적용하지 않았다. MAY-001에는 이미 동결된 overlay만 사용했다.

예를 들어 G005의 context 실제 수립 필요조건, G021의 Paging Policy에 걸리는 should, G037의 변경 능력 요구를 명시했다. G043에는 RAT의 TAC 분리 배치 필요성과 접근 허용 금지를 함께 남겼고, G049에는 target AMF가 전달하는 downlink NAS COUNT 최하위 8비트와 새 K_AMF 유도 금지 표시를 함께 남겼다. 이 source 내부 명제들을 flat gold 요약의 누락 때문에 무시하지 않는다. 목적·참조·집합 한정을 무조건 예외로 해석하지 않는다.

## 미확정 2건

| 기준 / 원본 사례 | 확인된 근거 | 미확정 이유와 처리 |
|---|---|---|
| G023 / MAIN-SD-005 | TS 24.501 §4.6.2.2, PDF 98쪽; Annex C.1 PDF 1090–1091쪽, C.2 PDF 1093쪽 | 본문의 allowed NSSAI 비휘발성 저장 권고는 확인됐다. 그러나 Annex C에는 가입자 연계, 긴급 서비스 등록·eCall-only에서의 비휘발성 저장 금지와 임시 저장 규칙이 있다. 현재 입력은 Annex C 이름만 제공하므로 일반 저장 권고와 전체 저장 방식 중 무엇을 충분히 설명해야 하는지 확정하기 어렵다. 추가 문맥을 모델이 받았다고 가정하거나 그 누락을 자동 오역으로 처리하지 않는다. |
| G028 / MAIN-SDN-003 | TS 23.501 §5.4.11.4, PDF 133쪽 | 정확한 위치정보가 없으면 요청 거절·deregistration을 피하라는 문장은 NR 위성 접속과 PLMN 운용 가능성 검증 단락에 속한다. 현재 source/question/gold에는 그 상위 적용 범위가 명시되지 않아 모든 NAS 요청의 일반 정책으로 읽힐 수 있다. 최소 제공 문맥과 평가 범위가 정해질 때까지 미확정으로 둔다. |

두 사례의 원문 자체가 틀렸다고 판정한 것은 아니다. **현재 제공 입력과 평가 기준의 범위 연결이 미해결**이라는 뜻이다. 기존 적격성 기록의 ELIGIBLE을 수정하거나 부적격으로 소급 변경하지 않았다. 정정 제안은 `PROPOSED_NOT_APPLIED`로 남겼다.

## 집합과 다음 검토

| 동결 집합 | 고정 분모 | 기준 지지 | 기준 미확정 |
|---|---:|---:|---:|
| PRIMARY_STRICT_49 | 49 | 47 | 2 |
| SENS_GOLD_50 | 50 | 48 | 2 |
| SENS_EXCEPTION_50 | 50 | 48 | 2 |
| SENS_GOLD_EXCEPTION_51 | 51 | 49 | 2 |

합집합에서 기준이 지지된 49건과 사후 주 분석 49건은 **구성이 다른 집합**이다. 주 분석에는 미확정 2건이 그대로 포함되어 있다. 미확정 사례를 빼서 분모를 47로 바꾸거나 모든 조건의 실패 0점으로 채우지 않는다. 두 기준은 5조건의 10개 응답 슬롯에 연결되지만, 이 사전 확인에서 그 응답들의 결과를 판정하지 않았다.

이제 255개 전체의 v2 pass 1 기록을 시작할 수 있다. 기준 미확정 사례는 PASS로 확정하지 않으며, 별도로 명백한 오류가 있는 FAIL은 근거와 `INDEPENDENT_CLEAR_ERROR`를 요구한다. 그 외 판단 불가는 UNRESOLVED/null을 유지한다. 생성 보류 1개 슬롯의 pipeline 처리는 이 기준 미확정과 구별한다. 24시간 간격은 앞으로 1차 검토 전체가 완료·봉인된 뒤 시작된다.

```sh
python3 tools/prepare_v2_review_package_20260908.py check-preflight \
  --preflight outputs/review/v2_preflight_20260908/preflight_completed.jsonl
```

## 원래 입력 제공 여부와 검증 한계

관리용 [입력 근거 기록](../outputs/review/v2_preflight_20260908/coordinator/input_provenance.json)은 가림 검토 자료와 분리했다. C3·C1M은 저장된 request의 해시를 확인했다. C0·C1·C2 main 실행은 원래 request body 로그가 없으므로 동결된 runner·template·dataset으로 입력을 재구성했다. 이를 캡처된 HTTP 요청이라고 표시하지 않았다. 선택된 추가 PDF 인용문이 이 입력에 직접 들어 있지 않음을 확인했으며, 문자열 부재만으로 모델의 배경지식 여부를 추정하지 않았다.

기존 처리 동결 파일 119개, 검토 패키지의 22개 파일과 지원 파일 2개는 보존했다. 원래 source·question·gold·응답·이전 점수·v4 원고·분모는 변경하지 않았다. 검증 도구는 기록 수, 참조 해시, 출처 인용의 실제 페이지 일치, 필수 필드 및 상태 조합을 검사한다. 의미 해석의 타당성 자체를 기계적으로 증명하지는 않는다.
