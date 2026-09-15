# 재현 자료 연결

이 묶음은 현재 저장소의 원본을 참조하는 로컬 색인이다. 단독 배포용 ZIP이나 공개 저장소가 아니다. 비밀 설정 파일을 포함하지 않으며 외부 게시·전송은 수행하지 않았다.

## 읽기 순서

1. 01_samples.md와 case_membership_72.csv로 분모를 확인한다.
2. 02_evaluation.md로 판정 면과 요구사항을 확인한다.
3. primary_response_trace_255.jsonl의 case_id/condition → review_id/reference_id를 따라 v2 coordinator keys, response_records 및 adjudicated_view를 조회한다. 원본 응답 및 판정 해시는 trace에 있다.
4. condition_results/paired_results의 결과와 원고 표를 대조한다.
5. 추가 진단은 별도 runs의 요청·원본 응답과 error_recheck_v2의 판정을 확인한다.

## 오프라인 검증

저장소 루트에서 Python 3 표준 라이브러리만으로 실행한다. API 호출이나 응답 재생성이 없다.

```sh
python3 tools/package_submission_evidence_20260914.py verify
python3 tools/summarize_v2_cohorts_20260909.py verify
```

첫 명령은 해시·분포·분모·trace를, 둘째는 원본 봉인·조정·SQLite 집계 및 미확정 열거 범위를 검증한다. 의미적 정답을 자동 증명하지 않는다. 생성 재실행은 비용·비결정성이 있는 별도 실험으로, 이 재현 절차에 포함하지 않는다.

## 파일 색인

- [data/main_cases.csv](../../data/main_cases.csv)
- [data/main_freeze_manifest.json](../../data/main_freeze_manifest.json)
- [experiments/c3_lib.mjs](../../experiments/c3_lib.mjs)
- [experiments/error_replication_v1_20260914/evaluation_reference.json](../../experiments/error_replication_v1_20260914/evaluation_reference.json)
- [experiments/error_replication_v1_20260914/generator_inputs.json](../../experiments/error_replication_v1_20260914/generator_inputs.json)
- [experiments/error_replication_v1_20260914/input_freeze_manifest.json](../../experiments/error_replication_v1_20260914/input_freeze_manifest.json)
- [experiments/error_replication_v1_20260914/plan.json](../../experiments/error_replication_v1_20260914/plan.json)
- [experiments/error_replication_v1_20260914/protocol.json](../../experiments/error_replication_v1_20260914/protocol.json)
- [experiments/error_replication_v1_20260914/remaining8_authorization.json](../../experiments/error_replication_v1_20260914/remaining8_authorization.json)
- [experiments/posthoc_treatment_v1_20260908/case_policy.json](../../experiments/posthoc_treatment_v1_20260908/case_policy.json)
- [experiments/posthoc_treatment_v1_20260908/gold_overlay.json](../../experiments/posthoc_treatment_v1_20260908/gold_overlay.json)
- [experiments/posthoc_treatment_v1_20260908/protocol.json](../../experiments/posthoc_treatment_v1_20260908/protocol.json)
- [experiments/posthoc_treatment_v1_20260908/response_index.json](../../experiments/posthoc_treatment_v1_20260908/response_index.json)
- [experiments/runs/error_replication_remaining8_20260914/manifest.json](../../experiments/runs/error_replication_remaining8_20260914/manifest.json)
- [experiments/runs/error_replication_remaining8_20260914/output_freeze_manifest.json](../../experiments/runs/error_replication_remaining8_20260914/output_freeze_manifest.json)
- [experiments/runs/error_replication_remaining8_20260914/parsed_responses.jsonl](../../experiments/runs/error_replication_remaining8_20260914/parsed_responses.jsonl)
- [experiments/runs/error_replication_remaining8_20260914/raw_responses.jsonl](../../experiments/runs/error_replication_remaining8_20260914/raw_responses.jsonl)
- [experiments/runs/error_replication_remaining8_20260914/requests.jsonl](../../experiments/runs/error_replication_remaining8_20260914/requests.jsonl)
- [experiments/runs/error_replication_remaining8_20260914/slot_ledger.jsonl](../../experiments/runs/error_replication_remaining8_20260914/slot_ledger.jsonl)
- [experiments/runs/error_replication_v1_20260914/manifest.json](../../experiments/runs/error_replication_v1_20260914/manifest.json)
- [experiments/runs/error_replication_v1_20260914/output_freeze_manifest.json](../../experiments/runs/error_replication_v1_20260914/output_freeze_manifest.json)
- [experiments/runs/error_replication_v1_20260914/raw_responses.jsonl](../../experiments/runs/error_replication_v1_20260914/raw_responses.jsonl)
- [experiments/runs/error_replication_v1_20260914/requests.jsonl](../../experiments/runs/error_replication_v1_20260914/requests.jsonl)
- [experiments/runs/error_replication_v1_20260914/slot_ledger.jsonl](../../experiments/runs/error_replication_v1_20260914/slot_ledger.jsonl)
- [outputs/analysis/main72_eligibility_20260908/eligibility_audit.csv](../../outputs/analysis/main72_eligibility_20260908/eligibility_audit.csv)
- [outputs/paper/ACK2026_3GPP_normative_fidelity_validated_v7.docx](../../outputs/paper/ACK2026_3GPP_normative_fidelity_validated_v7.docx)
- [outputs/paper/ACK2026_3GPP_normative_fidelity_validated_v7.md](../../outputs/paper/ACK2026_3GPP_normative_fidelity_validated_v7.md)
- [outputs/paper/ACK2026_3GPP_normative_fidelity_validated_v7.pdf](../../outputs/paper/ACK2026_3GPP_normative_fidelity_validated_v7.pdf)
- [outputs/review/error_recheck_v2_20260914/rechecked_8.jsonl](../../outputs/review/error_recheck_v2_20260914/rechecked_8.jsonl)
- [outputs/review/error_recheck_v2_20260914/review.md](../../outputs/review/error_recheck_v2_20260914/review.md)
- [outputs/review/error_recheck_v2_20260914/seal.json](../../outputs/review/error_recheck_v2_20260914/seal.json)
- [outputs/review/v2_20260908/coordinator/keys.json](../../outputs/review/v2_20260908/coordinator/keys.json)
- [outputs/review/v2_20260908/coordinator/response_records.jsonl](../../outputs/review/v2_20260908/coordinator/response_records.jsonl)
- [outputs/review/v2_20260908/preflight/references.jsonl](../../outputs/review/v2_20260908/preflight/references.jsonl)
- [outputs/review/v2_adjudication_20260909/adjudicated_view_255.jsonl](../../outputs/review/v2_adjudication_20260909/adjudicated_view_255.jsonl)
- [outputs/review/v2_cohort_analysis_20260909/bound_slots_255.jsonl](../../outputs/review/v2_cohort_analysis_20260909/bound_slots_255.jsonl)
- [outputs/review/v2_cohort_analysis_20260909/completion_manifest.json](../../outputs/review/v2_cohort_analysis_20260909/completion_manifest.json)
- [outputs/review/v2_cohort_analysis_20260909/condition_results.csv](../../outputs/review/v2_cohort_analysis_20260909/condition_results.csv)
- [outputs/review/v2_cohort_analysis_20260909/condition_results.jsonl](../../outputs/review/v2_cohort_analysis_20260909/condition_results.jsonl)
- [outputs/review/v2_cohort_analysis_20260909/paired_cases.jsonl](../../outputs/review/v2_cohort_analysis_20260909/paired_cases.jsonl)
- [outputs/review/v2_cohort_analysis_20260909/paired_results.csv](../../outputs/review/v2_cohort_analysis_20260909/paired_results.csv)
- [outputs/review/v2_cohort_analysis_20260909/paired_results.jsonl](../../outputs/review/v2_cohort_analysis_20260909/paired_results.jsonl)
- [outputs/review/v2_cohort_analysis_20260909/sensitivity_added_cases.jsonl](../../outputs/review/v2_cohort_analysis_20260909/sensitivity_added_cases.jsonl)
- [outputs/review/v2_cohort_analysis_20260909/summary.json](../../outputs/review/v2_cohort_analysis_20260909/summary.json)
- [outputs/review/v2_cohort_analysis_20260909/validation_report.json](../../outputs/review/v2_cohort_analysis_20260909/validation_report.json)
- [tools/package_submission_evidence_20260914.py](../../tools/package_submission_evidence_20260914.py)
- [tools/summarize_v2_cohorts_20260909.py](../../tools/summarize_v2_cohorts_20260909.py)