# 동결된 생성 보존 실험 18회 실행 완료

2026-09-13. **동결 요청 18회를 모두 실행하고 원본 응답을 봉인했다.** 18건 모두 지정 모델의 정상 JSON 설명을 받았으며 재시도·거절·잘림·schema 실패는 없었다. 현재 상태는 `GENERATION_COMPLETE_SEMANTICS_PENDING`이다. 생성 완료를 의미하며 설명의 정확도나 성능 향상은 아직 판정하지 않았다.

| 항목 | 실제 실행 기록 |
|---|---|
| 계획·시도·응답·사용 가능한 설명 | 각각 18건 |
| 조건 | A0/A1/A2 각각 6건, 기존 원문 3개×2회 |
| 모델 | gpt-5.4-mini-2026-03-17 |
| 실행 시각 | 2026-09-13 22:50:34.210–22:51:25.090 KST |
| 경과 시간 | 약 50.88초 |
| 입력 token | 19,668, 이 중 캐시 입력 2,560 |
| 출력 token | 6,688 |
| 생성 API 비용 추정 | **$0.043119** / 한도 $0.50 |
| 의미 평가 | 아직 수행하지 않음 |

실행 전에 9월 9일 동결 manifest의 **53개 파일 해시**와 실행 경로가 비어 있음을 다시 확인했다. 9월 13일 [OpenAI 공식 모델 문서](https://developers.openai.com/api/docs/models/gpt-5.4-mini)에서 동일 snapshot과 백만 token당 입력 $0.75·캐시 입력 $0.075·출력 $4.50을 재확인했다. 단가 변경이 없어 동결 입력·실행기·평가 기준을 수정하지 않았다. [실행 전 확인 기록](../outputs/review/generation_preservation_execution_20260913/prelaunch.json).

비용은 반환 usage에 위 단가를 적용한 계산값이며 청구서가 아니다. 계산식은 `((19668−2560)×0.75 + 2560×0.075 + 6688×4.50) / 1000000 = 0.043119`다. Codex 검토의 계정 사용량이나 전체 연구 비용은 포함하지 않는다.

원본 요청·응답·해석된 JSON·전체 슬롯 회계표·시각·usage를 저장하고 출력 manifest와 읽기 전용 파일로 봉인했다. 요청 순서와 payload가 동결 계획에 정확히 일치하는지, 원본 response의 모델·JSON·usage가 회계표와 일치하는지, 파일 목록에 빠진 기록이 없는지 재검증했다. [실행 manifest](../experiments/runs/generation_preservation_v1_20260909/manifest.json), [원본 응답 18개](../experiments/runs/generation_preservation_v1_20260909/raw_responses.jsonl), [출력 봉인](../experiments/runs/generation_preservation_v1_20260909/output_freeze_manifest.json), [전달·비용 검증](../outputs/review/generation_preservation_execution_20260913/runtime_verification.json).

후속 평가를 위해 **익명 패킷 18개와 평가자당 요구사항 54개**를 준비했다. 패킷에는 원문·문맥·질문·평가 요구사항·응답을 넣고 조건명·슬롯 ID·생성 요청은 제외했다. 조건 연결표는 별도 coordinator 폴더에 있다. 실제 의미 점수는 생성하지 않았으며 평가자 간 비교도 하지 않았다. [익명 평가 패킷](../outputs/review/generation_preservation_v1_20260909/reviewer/packets_18.jsonl), [패킷 봉인 manifest](../outputs/review/generation_preservation_v1_20260909/packet_manifest.json).

다음 단계는 동결된 평가 지침에 따른 진행 AI와 새 문맥 AI의 개별 의미 평가, 두 판정의 봉인, 조건 연결·집계다. JSON 설명 18개를 얻었다는 사실만으로 전체 과제 완수나 강도·예외 보존 향상을 주장하지 않는다. 기존 v2의 미확정 판정과 이전 실험 결과·원고는 유지한다.

```bash
node tools/verify_generation_preservation_execution_20260913.mjs
python3 tools/freeze_generation_preservation_20260909.py verify
```

[실행 검증·완료 확인](../outputs/review/generation_preservation_execution_20260913/completion_verification.json), [검토·동결 기록](32_generation_preservation_design_review_and_freeze_2026-09-09.md).
