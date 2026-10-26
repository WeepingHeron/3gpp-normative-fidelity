[English](README.md) | [한국어](README.ko.md)

# Evaluating Normative Fidelity in Korean Explanations of 3GPP Requirements

**KIPS_C2026B0055 · ACK 2026**
Paper (English translation): Evaluating Evidence-Constrained Generation for Preserving Normative Meaning in Korean Explanations of 3GPP Requirements

## Overview

This study evaluates how well LLM-generated Korean explanations of English 3GPP requirements preserve normative strength, actors, conditions, actions, and exceptions. Even with the same source text, explanations may change the strength of obligations or recommendations, or omit conditions and exceptions.

## Research objectives

- **RQ1.** Does a general-purpose LLM accurately preserve the distinctions among `shall / shall not / should / should not / may / can` in Korean explanations?
- **RQ2.** Does providing the source clause alone reduce errors?
- **RQ3.** Does adding a gold structure of `actor · condition · normative type · action · exception` to the source improve meaning preservation compared with the source alone?

## Approach

| ID | Condition | Purpose |
|---|---|---|
| C0 | LLM given only the question | Prior-knowledge baseline |
| C1 | Same gold source clause and instructions to preserve meaning | Oracle source baseline |
| C2 | Same clause + structured fields matching the evaluation gold | Oracle structured condition |
| C3 | Extract structure from the source alone → generate an explanation from the question, source, and extracted fields | Automatic structure extraction extension |
| C1M | C1 + only the gold normative type and negation | Separate comparison of modal hints |

C1 and C2 receive the same source clause. C2 additionally receives the interpretation used in the evaluation gold, so it does not separate the effect of structured formatting from the effect of providing the gold interpretation. C3 is an extension using automatically extracted structure. Actual retrieval performance is not evaluated.

## Verified results and limitations

The eligibility of the original 72 cases was audited post hoc, and treatment rules were frozen before reevaluation. The main analysis covers 49 cases from 33 clauses; sensitivity analyses cover overlapping sets of 50/50/51 cases. The table below reports complete preservation in Korean explanations after delayed rereview and disagreement adjudication by the same AI.

| Condition | Preserved P | Violated F | Unresolved U | Not generated NG | Complete preservation range |
|---|---:|---:|---:|---:|---:|
| C0 | 0 | 49 | 0 | 0 | 0.00% |
| C1 | 38 | 10 | 1 | 0 | 77.55–79.59% |
| C2 | 44 | 3 | 2 | 0 | 89.80–93.88% |
| C3 | 41 | 5 | 2 | 1 | 83.67–87.76% |
| C1M | 43 | 4 | 2 | 0 | 87.76–91.84% |

These are logical bounds for unresolved cases, calculated as `P/N ~ (P+U)/N`, **not 95% confidence intervals**. Cases without a generated explanation remain in the denominator. Post hoc sample treatment and evaluation by the same AI are limitations; no statistical superiority or generalization to all of 3GPP is claimed. [Aggregation and calculation evidence](notes/28_v2_cohort_results_2026-09-09.md)

A further review of 8 explanations generated from 3 separate development sources, against the designated requirements, found 3 with complete preservation and 5 with incomplete preservation. Changes in normative strength and omissions of conditions and exceptions remained. Correct metadata must be distinguished from preservation of meaning in the explanation. These are repeated observations on existing cases, not a performance estimate on a new independent sample. [Review of 8 responses](results/outputs/review/error_recheck_v2_20260914/review.md)

Semantic judgments include delayed rereview and disagreement adjudication by the same AI and do not replace independent expert validation. Matching data/code hashes and aggregates does not automatically establish whether semantic judgments are correct. Results are not generalized beyond the selected standards, versions, samples, models, and prompt conditions.

## Repository structure

| Path | Contents |
|---|---|
| `notes/` | Research plans, sampling protocols, reviews, and interpretation records |
| `references/` | Source-standard storage locations and source index; source PDFs are kept locally |
| `code/tools/` | Sampling, review, aggregation, and hash-verification tools |
| `data/` | Samples, annotations, selection manifests, and freeze manifests |
| `results/` | Execution, review, and aggregation results; some are local artifacts outside Git |
| `paper/` | Manuscript editing materials, including figures and tables |
| `submissions/2026_ACK/` | Final submitted PDF and verification SHA-256 |
| `experiments/` | Frozen Node execution bundles, prompts, and protocols |

`code/experiments` is a link that preserves existing execution entry conditions and frozen code hashes. The actual location of `experiments/runs` is `results/runs`. Existing paths such as `docs`, `tools`, and `outputs`, along with input/output paths under `code/`, remain as compatibility links. Use the actual categorized paths above when editing materials.

Key guides: [Research plan](notes/01_research_plan.md), [dataset protocol](notes/02_dataset_protocol.md), [evaluation protocol](notes/03_evaluation_protocol.md), [related work](notes/04_related_work_and_novelty.md), [data guide](data/README.md), and [experiment guide](experiments/README.md).

## Environment and reproduction

Use Python 3 and Node.js from the repository root. The following checks do not make new model API calls.

```bash
python3 -B code/tools/verify_main_freeze.py
node experiments/test_c3_contract.mjs
node experiments/test_c1m_contract.mjs
```

If the local results bundle is also available, submission evidence and aggregates can be cross-checked further.

```bash
python3 -B code/tools/package_submission_evidence_20260914.py verify
python3 -B code/tools/summarize_v2_cohorts_20260909.py verify
```

Cloning Git does not provide all review results and submission evidence under `results/outputs/`, or the source-standard PDFs. For missing files, consult the separately stored materials and their manifests. Document rendering and new experiments may require additional local dependencies or authentication settings. Generation experiments incur API costs and are distinct from the offline checks above.

Local evidence index: [Sample composition](results/outputs/submission_evidence_v7_20260914/01_samples.md), [evaluation table](results/outputs/submission_evidence_v7_20260914/02_evaluation.md), [reproduction guide](results/outputs/submission_evidence_v7_20260914/03_reproduction.md), and [final v7 cross-check](results/outputs/final_crosscheck_v7_20260914/REPORT.md). The 99 v7 cross-check items document consistency among files at that time; they do not constitute an independent review of the later final submission.

## Paper and submission status

The paper is listed in the ACK 2026 presentation program. Completion of the paper and presentation-video submissions is based on the user's confirmation. Awards are separate from presentation scheduling and submission completion; no confirmed award information is stated.

The final submitted PDF and the original were confirmed to have the same SHA-256. The submitted PDF bytes were not changed. Videos and presentation materials are stored locally and are not included in the public repository.

- [Final submitted PDF](submissions/2026_ACK/KIPS_C2026B0055%28김태훈%29.pdf)
- [Final PDF SHA-256](submissions/2026_ACK/SHA256SUMS)
- Earlier v7 manuscript: `results/outputs/paper/ACK2026_3GPP_normative_fidelity_validated_v7.pdf` and the DOCX with the same base name. These are historical materials and do not replace the final submitted PDF.

## Research history and preservation principles

### Preservation and public scope

Research history recorded in Git and frozen experimental materials are preserved. Raw credentials, virtual environments, videos, untracked presentation materials, personal work records, and backups are excluded from the public repository. Source-standard PDFs must be obtained separately; local artifacts absent from Git should be prepared against their manifests.

No new license has been granted. Check each source for the terms governing third-party standards, templates, and reference materials. When changing the folder structure, verify both compatibility paths and the hashes of frozen materials.

<details>
<summary>Expand dated design, execution, and evaluation records</summary>

Statuses and figures below are as of the dates stated. Use the results table above for the latest main analysis and the PDF linked in the submission-status section for the final submitted file. Manuscript versions and progress statuses below are historical records for their respective dates.

**2026-09-14 atomic comparison validation completed:** The same 6 drafts underwent 12 comparisons using the existing and finer-grained methods. Detection of known defects was 3/8 versus 2/8, providing no evidence of improvement. Cases included misjudgment of the strength item itself, reuse of citations from other conditions, and use of metadata as evidence for an explanation. Cost was $0.0895215; existing judgments and HOLD were retained without generating new explanations. [Comparison validation and evidence-boundary diagnosis](notes/41_atomic_audit_results_2026-09-14.md).

**2026-09-14 comparison-then-revision trial completed:** Direct rewriting and revision after proposition comparison were applied to all 6 existing P1 drafts, producing 12 final explanations and 6 comparisons. Initial task completion judged by the conducting AI was 1/6 versus 2/6 (1 unresolved in each), below the conservative improvement criterion. Although 3 requirements were restored, the comparison also missed normative-strength errors and gave incorrect revision instructions. Cost was $0.0795678; existing judgments and HOLD were retained. [Execution, evaluation, and comparison diagnosis](notes/39_preservation_repair_results_2026-09-14.md).

**2026-09-13 source-proposition extraction → explanation trial completed:** A fresh A2 run and an extraction → explanation method produced 12 final explanations and 6 extractions. Initial task completion judged by the conducting AI was 0/6 (2 unresolved) and 1/6 (1 unresolved), respectively, so improvement could not be established. In 6 cases, extracted requirements were lost from the explanation. Generation API cost was $0.05711625; existing freezes and judgments were preserved. [Execution, initial evaluation, and stage diagnosis](notes/37_proposition_pipeline_results_2026-09-13.md).

**2026-09-13 bounded cause analysis completed:** In 4 shared failures, the analysis traced how storage recommendations or network verification-configuration conditions present in the actual input were omitted from explanations. No signs of delivery failure or forced truncation were found; the effects of information selection and sentence limits remain untested hypotheses. The analysis also separated how evaluator differences blocked the progression criterion. Existing freezes and judgments were retained, with 0 new generations. [Cause analysis and evidence](notes/35_generation_preservation_bounded_cause_analysis_2026-09-13.md).

**2026-09-13 semantic evaluation by two AIs completed:** Each evaluated and sealed judgments for 18 frozen generated responses. Both evaluators found A2 task completion of 2/6. Emergency registration and eCall deletion exceptions were each preserved in 2/2, but storage recommendations and network verification-configuration conditions remained unresolved problems. Given interpretation differences and unresolved judgments, the criterion requiring both evaluators to pass was unmet: `HOLD_FOR_METHOD_REVISION`. Some meta-diagnostic aggregates were withheld because definitions were mixed; original judgments were preserved. [Full results, judgment differences, and progression criteria](notes/34_generation_preservation_semantic_review_2026-09-13.md).

**2026-09-13 execution of 18 frozen requests completed:** All 6 requests per A0/A1/A2 condition returned normal responses, with no retries or delivery failures. Estimated generation API cost was $0.043119; original requests, responses, usage, and accounting tables were sealed. The 18 anonymized evaluation packets were prepared. Status at this point was `GENERATION_COMPLETE_SEMANTICS_PENDING`; semantic evaluation had not yet occurred. [Execution results, costs, and verification evidence](notes/33_generation_preservation_execution_2026-09-13.md).

**2026-09-09 generation-preservation experiment design reviewed and frozen:** Following design review by the conducting AI, execution and evaluation handling rules were refined, and 18 requests plus 53 related files were frozen as `FROZEN_BEFORE_GENERATION`. Generation prompts, evaluation requirements, and progression criteria remained identical to the draft. Offline error tests and hash checks passed, with 0 new API generations. [Design review, freeze time, and verification evidence](notes/32_generation_preservation_design_review_and_freeze_2026-09-09.md).

**2026-09-09 next generation experiment plan prepared:** Three conditions compare existing generation instructions, added instructions explicitly preserving normative strength, and further instructions to check for omitted propositions, all with the same FULL context. Previews for 18 requests (3 development sources × 3 conditions × 2 repetitions), evaluation, cost, and progression criteria were prepared and checked offline. Status was `DRAFT_READY_FOR_REVIEW`, with 0 new API generations. [Experiment plan, prompts, and conditional evaluation of new clauses](notes/31_generation_preservation_experiment_plan_2026-09-09.md).

**2026-09-09 separate-AI review and context development experiment completed:** A separate AI's judgments on 15 existing responses all matched previous results, retaining 8 unresolved cases. Next, 24 actual generations (3 selected sources × 2 context levels × 2 hint levels × 2 repetitions) were run and evaluated by two AIs. Their overall task-completion judgments all agreed; additional context did not establish improved overall completion. SUPI conditions and satellite-access scope were better preserved in some cases, but normative-strength errors and omitted deletion conditions remained. [Execution, both evaluations, detailed differences, and scope of incorporation](notes/30_separate_ai_review_and_context_microstudy_2026-09-09.md). These are development findings; existing v2 performance figures and the manuscript are retained.

**2026-09-09 current-results report and follow-up evidence review completed:** The v2 results, including bounds for unresolved cases, remained the reporting basis. An additional 10 related PDF pages and 9 archived requests were cross-checked, but no new semantic evidence warranted score changes, leaving 8 cases unresolved. The next review set of 15 items (three sources × all five conditions) and candidate contexts were prepared; independent review and new model experiments had not yet been performed. [Report, follow-up checks, and incorporation criteria](notes/29_report_and_followup_review_2026-09-09.md).

**2026-09-09 v2 aggregation by condition completed:** All 49 main-analysis cases and the three sensitivity sets of 50/50/51 were reported. The main-analysis logical bounds for C2−C1 were +10.20~+16.33 percentage points, with the same direction in all three sensitivity analyses. C2−C1M includes 0, so superiority cannot be established. [Full results, calculation checks, and interpretation limits](notes/28_v2_cohort_results_2026-09-09.md). Statistical testing was withheld because every specified comparison included unresolved judgments; these bounds are not confidence intervals. Manuscript figures and existing materials were preserved.

**2026-09-09 v2 disagreement adjudication completed:** The 5 cases were resolved as PASS 2, FAIL 2, and UNRESOLVED 1; symmetric application to 60 related responses was checked. After adjudication, the 255 cases comprised PASS 167, FAIL 79, UNRESOLVED 8, and 1 explanation not generated. [Adjudication evidence and remaining unresolved cases](notes/27_v2_disagreement_adjudication_2026-09-09.md). Both previous passes and frozen criteria were preserved; this was post hoc adjudication by the same evaluator. Subsequent aggregation by condition must report unresolved bounds alongside frozen denominators. The records below describe each stage at completion.

**2026-09-09 v2 second semantic review completed and sealed:** After the required 24-hour interval, 255 slots were reviewed in a new order, yielding PASS 165, FAIL 81, UNRESOLVED 8, and 1 explanation not generated. Comparison after sealing both passes found 250 agreements and 5 disagreements; adjudication was pending at this point. [Second-pass evidence and disagreement records](notes/26_v2_semantic_review_pass2_2026-09-09.md). This was repeated review by the same evaluator, not independent expert validation or final condition-level performance. Existing denominators, originals, and first-pass results were preserved, with 0 new model-generation API calls. Status descriptions below are historical records at each stage's completion.

**2026-09-08 v2 first semantic review completed and sealed:** All 255 slots were reviewed, yielding PASS 169, FAIL 78, UNRESOLVED 7, and 1 generation withheld. [Judgment evidence and completion record](notes/25_v2_semantic_review_pass1_2026-09-08.md). These were first-pass results; final comparisons by condition and manuscript figures had not yet been updated. Existing materials and denominators were preserved, with 0 new model API calls. The second pass was to use a separate order at least 24 hours later, **on or after 2026-09-09 12:31:23.646276 KST**. Status descriptions below are historical records at each stage's completion.

**2026-09-08 v2 source/gold preflight completed:** Of the union of 51 cases, the source and frozen rules supported the criteria for 49; 2 were unresolved (G023 storage exception and G028 NR satellite-access context). Both unresolved cases remained in the 49-case main analysis, and all frozen denominators were retained. [Preflight results](notes/24_v2_gold_preflight_2026-09-08.md). There had been 0 actual response rescoring or new model calls; the next step was v2 pass 1 for all 255 slots.

**2026-09-08 v2 review package prepared:** The 51 source/gold criteria and 255 response slots (254 explanations and 1 generation withheld) were assembled separately with condition names and previous scores masked. Status was `PREPARED_PREFLIGHT_PENDING`, with 0 gold preflight checks, rescoring, or new model calls so far. [Package and sequence](notes/23_v2_review_package_2026-09-08.md), [review guide](results/outputs/review/v2_20260908/REVIEW_GUIDE.md). The next step was source/gold preflight for the 51 criteria.

**2026-09-08 treatment criteria frozen:** The post hoc reevaluation criteria `posthoc_treatment_v1_20260908` were fixed as `FROZEN_NOT_APPLIED`. The main set of 49 and sensitivity sets of 50/50/51, varying gold corrections and inclusion of prespecified list exceptions, apply symmetrically to C0, C1, C2, C3, and C1M. MAY-001 retained source eligibility but was excluded from the main analysis because of gold contamination in the C2 input; it is assessed only in designated sensitivity analyses. [Frozen rules and rationale](notes/22_posthoc_treatment_freeze_2026-09-08.md), [frozen scoring criteria v2](experiments/scoring_v2_frozen_20260908.md). Rescoring, new model runs, and changes to historical scores had not yet occurred. Check command: `python3 code/tools/verify_posthoc_treatment_v1.py --self-test`.

**2026-09-08 complete sample-eligibility audit finished:** Reviewing 51 source pages for 72 cases yielded 50 generally eligible cases, 1 conditionally eligible case under a previously recorded exception, 10 ineligible cases (3 NOTE and 7 list cases), and 11 on hold. CAN-005's actual clause is 4.2.8.1A; missing context, semantic duplication, and unresolved correspondence were also recorded. [Audit results and case evidence](notes/21_main72_eligibility_audit_2026-09-08.md), [report](results/outputs/analysis/main72_eligibility_20260908/report.html). This was a Codex audit, not independent expert validation. The older scores below were not recalculated, and the remaining 50/51 cases were not finalized as a new frozen sample.

**2026-09-07 boundary review:** Identified necessary corrections to MAY-001's gold wording and scope, violations of the NOTE-exclusion protocol for CAN-004/MAY-005, and unresolved correspondence for SD-009. [Source comparison and proposed handling](notes/20_gold_boundary_review_2026-09-07.md), [candidate scoring criteria v2](experiments/scoring_v2_candidate.md). Figures below are historical evaluations and were not rescored under the new criteria. Eligibility and gold issues take priority; v4 is not labeled as a finalized performance validation.

Generation for the main 72 cases × 3 conditions, followed by delayed rereview and disagreement adjudication by the same Codex evaluator, was completed. Complete explanation preservation was C0 0/72, C1 65/72, and C2 72/72. Independent expert validation had not been performed; excluding 3 ambiguous gold cases gave C1-C2 exact McNemar p=0.125.

Those figures record the earlier frozen evaluation. **2026-09-06 new semantic review pass 1** yielded C1 61/72, C2 71/72, and C3 65/72, differing from previous C1/C2 judgments in 9 cases. The 24-hour delayed rereview and adjudication on September 7 retained these scores. [Delayed review completed](notes/16_c3_delayed_review_2026-09-07.md). [Semantic evaluation report](notes/13_c3_semantic_review_pass1_2026-09-06.md). Existing frozen scores are preserved as history; the manuscript current at that stage uses the new delayed-adjudication results.

- Manuscript current at that stage: `results/outputs/paper/ACK2026_3GPP_normative_fidelity_draft_v4.docx`, a 2-page PDF, and synchronized Markdown. It incorporated delayed-adjudication results for C1/C2/C3 and C1M's initial evaluation of 68/72. C1M was provisional; v1/v2/v3 are preserved. [v3 incorporation and extension record](notes/15_paper_v3_and_priority_extensions_2026-09-06.md), [KIPS template validation](notes/11_kips_template_validation_2026-09-06.md).
- [Review report](notes/08_project_review_2026-09-06.md), [evaluation and methodology corrections](notes/09_reporting_errata_2026-09-06.md).
- Freeze verification: `python3 code/tools/verify_main_freeze.py`.
- Recompute aggregates and sensitivity analyses: `python3 code/tools/review_project_20260906.py`.
- Automatic structure extraction extension C3: Completed 72 extractions, 71 generated explanations, 1 withheld case, and semantic evaluation pass 1. Estimated API cost was $0.13229325, with no additional API calls for this semantic review. [Execution and verification record](notes/12_c3_execution_2026-09-06.md).
- Clause-level sensitivity: Completed 20,000 cluster-bootstrap repetitions over 44 clauses. The 95% interval for C3−C1's +5.56 percentage points was −2.53~+15.52 percentage points, which does not establish improvement.
- C1M extension: Completed generation and parsing for 72 cases and input/output integrity checks, at an estimated cost of $0.08409. JSON normative types and citation IDs were each correct in 72/72, while the completed first explanation evaluation gave C1M 68/72 (94.44%). The difference versus C1 was +9.72 percentage points, exact p=0.06543; this was provisional before delayed rereview. [Semantic evaluation](notes/17_c1m_semantic_review_pass1_2026-09-07.md). [Design](notes/14_modal_hint_extension_protocol.md), [completion record](notes/15_paper_v3_and_priority_extensions_2026-09-06.md).
- Next research steps at that stage: C1M delayed rereview and adjudication after September 8, 14:56:16 KST. The C3 delayed review was complete. Extractor v2 prompts, schema, source-link validator, and offline checks were ready; model execution had not occurred. [v2 preparation](notes/18_scope_extractor_v2_staging_2026-09-07.md). Codex reviews are conducted at the user's request and are not described as independent expert validation. Frozen inputs and responses for this experiment are retained.

### Scope of completion

This study does not demonstrate that a model understands all of 3GPP. It is limited to a controlled experiment observing errors in preserving Korean normative meaning under the selected standards, versions, sentence samples, models, and prompt conditions.

</details>
