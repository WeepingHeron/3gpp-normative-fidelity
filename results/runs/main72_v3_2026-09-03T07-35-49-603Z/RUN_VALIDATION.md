# Main experiment run validation

## Overall assessment

**API output collection: READY FOR MASKED REVIEW.** The frozen main run completed without request or parse failures. Deterministic scores are reproducible, but the study is not ready for final research claims until semantic pass 1, delayed pass 2, and disagreement adjudication are complete.

## Verified execution facts

- Run: `main72_v3_2026-09-03T07-35-49-603Z`
- Dataset: 72 unique cases, 12 per modal class
- Sources: 36 cases from TS 23.501 and 36 from TS 24.501
- Difficulty strata: 8 simple, 22 conditional, 42 compound
- Conditions: C0/C1/C2, 72 responses each
- API calls: 216/216 successful
- JSON parsing: 216/216 successful
- Model requested and returned: `gpt-5.4-mini-2026-03-17`
- Input tokens: 129,881; output tokens: 33,909; cached input tokens: 0
- Estimated token cost: USD 0.25000125
- Cost guard: USD 1.00; not reached
- Secret-pattern scan: no API-key-like value detected in the run directory

## Deterministic provisional results

| Condition | Modal class accuracy | Exact citation |
|---|---:|---:|
| C0 | 15/72 (20.83%) | N/A |
| C1 | 56/72 (77.78%) | 72/72 (100%) |
| C2 | 72/72 (100%) | 72/72 (100%) |

These results only cover schema-level modal classification and exact citation identifiers. They do not establish complete semantic preservation in the Korean explanation.

## Validation boundary and next gate

- The run answers an oracle-evidence generation question, not end-to-end retrieval or RAG performance.
- The dataset has a single-annotator source-grounded self-check, not independent expert validation.
- Actor, polarity, condition, action, exception, and unsupported additions remain unscored.
- `blind_review.csv` hides case ID and condition; `blind_key.json` must remain unopened during row-level scoring.
- `merge_review.mjs` is expected to fail until a completed `blind_review_pass1.csv` exists.
- Do not conclude that C2 outperforms C1 on complete preservation until the masked semantic review is complete.
