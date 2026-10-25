# 생성 보존 실험: 설계 검토·실행 전 동결 완료

2026-09-09. **설계 검토와 실행 전 동결을 완료했다. 상태는 `FROZEN_BEFORE_GENERATION`이며 새 API 생성은 0회다.** 동결 시각은 **2026-09-09 18:18:39.485 KST**다. 다음 단계는 동결된 18개 요청의 생성이다.

| 항목 | 확정 내용 |
|---|---|
| 범위 | 기존 개발 원문 3개 × 생성 지시 3조건 × 2회 = 18개 요청 |
| 조건 | A0 기존 FULL/NONE, A1 강도 보존 지시 추가, A2 명제 누락 점검까지 추가 |
| 주 비교 | A2−A0; A1−A0와 A2−A1은 보조 비교 |
| 평가 | 같은 9개 요구사항, 검토자당 응답 18개·항목 54개; 두 AI의 판정은 각각 봉인 후 비교 |
| 비용 | 생성 API 한도 $0.50, 계획 예약 추정 $0.1630125; 이번 생성 비용 $0 |
| 동결 | 요청·원문·평가·실행·검증 코드·검토 근거 등 53개 파일의 SHA-256 연결 |

설계 검토는 **진행 AI의 재검토**로 수행했다. 별도 AI의 독립 설계 검토나 사람 전문가 검증으로 표시하지 않는다. 보관 원문과 평가 요구사항을 읽고 기존 PDF·페이지 텍스트 해시를 확인했다. [설계 검토 상세](../outputs/review/generation_preservation_preflight_20260909/design_review.md)와 [검토 입력·시각·판정](../outputs/review/generation_preservation_preflight_20260909/design_review.json)을 보관했다.

보완한 부분은 18개 슬롯용 실행기, 평가자에게 제공할 정보의 범위, 전달 실패와 의미 미확정의 구분, 문장 수·출처·메타데이터 진단의 역할, 오류·비용 미확정·재실행 처리, 익명 평가 패킷의 원본 연결이다. **생성 프롬프트, 18개 요청 payload, 원문·질문·평가 요구사항과 다음 단계 진행 기준은 최초 초안과 동일하다.** 최초 초안은 검토 폴더의 draft_snapshot에 보존했다.

실행기에는 요청 전 비용 한도, 오류 후 중단, 자동 재시도 금지, 기존 실행 경로 재사용 금지, 원본 응답·usage·전체 슬롯 회계표 봉인을 구현했다. 다른 모델이 반환되거나 usage를 믿을 수 없으면 비용을 확정하지 않고 중단한다. 빈 설명·거절·잘림·schema 오류는 전달 실패로 남기며 의미 미확정 null 또는 왜곡 없음 false로 바꾸지 않는다.

오프라인 시험은 실행기 11개 묶음과 패킷 7개 묶음을 통과했다. 입력 변조, 통신 오류, 거절, 잘못된 usage·모델, 비용 초과, 재실행, 슬롯 교환·출력 변경·비용 변경 등을 확인했다. 시험 응답은 `SYNTHETIC_TEST_ONLY`이며 실제 실험 경로에는 생성 자료가 없다. [실행기 시험](../outputs/review/generation_preservation_preflight_20260909/runtime_test_report.json), [패킷 시험](../outputs/review/generation_preservation_preflight_20260909/packet_test_report.json).

검토의 남은 한계는 지시문 길이·강조 효과, 관찰할 수 없는 내부 점검 과정, 압축된 출력 길이, 이미 본 개발 사례 3개의 선택 편향이다. 이를 밝힌 개발 실험으로 진행하는 데 차단 사항은 없다고 판정했다. 실제 의미 성능은 아직 평가하지 않았다. 2단계 새 조항 12개는 별도 후보·평가 요구사항·비용 동결이 필요하며 이번 실행 범위에 포함하지 않는다.

[동결 manifest](../experiments/generation_preservation_v1_20260909/input_freeze_manifest.json)의 SHA-256은 다음과 같다.

```text
6c3c9955339d6f812f3a2a52ba5bf8615035cc1aa9326752fe515c3aa7f9de06
```

protocol 파일의 `READY_TO_FREEZE`는 동결 직전 값을 보관한 것이며, 현재 동결 상태는 manifest로 판별한다. 동결 파일은 읽기 전용으로 바꾸고 해시를 재검증했다. 이는 로컬 무결성 기록이며 외부 공인 시각 인증이나 변경 불가능한 보관 시스템을 뜻하지 않는다. 변경이 필요하면 이 기록을 덮어쓰지 않고 새 버전을 만든다.

```bash
python3 tools/freeze_generation_preservation_20260909.py verify
node experiments/run_generation_preservation_20260909.mjs verify-freeze
```

상세 실험 설계는 [계획서](31_generation_preservation_experiment_plan_2026-09-09.md), 최종 재검증은 [완료 확인](../outputs/review/generation_preservation_freeze_completion_20260909/verification.json)에 있다. 기존 문맥 실험과 v2 동결 결과, 원고는 유지했다.
