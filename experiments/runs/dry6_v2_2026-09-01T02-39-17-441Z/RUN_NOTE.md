# Dry run v2 result

- Status: `COMPLETED`
- Model snapshot: `gpt-5.4-mini-2026-03-17`
- Cases: 6, one per modal class
- Calls: 18, with C0/C1/C2 for every case
- Parsing: 18/18
- Token usage: 10,324 input + 2,547 output
- Estimated token cost at the execution-time list price: USD 0.019205

## Deterministic checks

| condition | modal accuracy | citation exactness |
|---|---:|---:|
| C0 | 0/6 | NA |
| C1 | 6/6 | 6/6 |
| C2 | 6/6 | 6/6 |

## Single-annotator pass 1

| condition | complete preservation | unsupported addition |
|---|---:|---:|
| C0 | 0/6 | 1/6 |
| C1 | 6/6 | 0/6 |
| C2 | 5/6 | 0/6 |

These are prompt and rubric debugging results, not research findings. The review is not independent and has not received the delayed second pass required by `scoring_v1.md`.

V2 improved C1 modal wording and removed the mislabeled exception. C2 still produced one natural-language modal-strength conflict even though its structured `normative_type` was correct. On this six-case pass C2 did not outperform C1 in complete preservation, so the proposed-method hypothesis is not supported by this dry run.

C0 returned `unclear` for every case even after target spec, version, and clause metadata were added. Before the full pilot, the study must decide whether C0 is a safe no-evidence baseline or a closed-book parametric-knowledge baseline. The current wording strongly encourages abstention and should not be presented as ordinary LLM knowledge accuracy.
