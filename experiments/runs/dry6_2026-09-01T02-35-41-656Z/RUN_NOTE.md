# Dry run v1 result

- Status: `COMPLETED`
- Model snapshot: `gpt-5.4-mini-2026-03-17`
- Cases: 6, one per modal class
- Calls: 18, with C0/C1/C2 for every case
- Parsing: 18/18
- Token usage: 7,966 input + 2,433 output
- Estimated token cost at the execution-time list price: USD 0.016923

## Deterministic checks

| condition | modal accuracy | citation exactness |
|---|---:|---:|
| C0 | 0/6 | NA |
| C1 | 4/6 | 6/6 |
| C2 | 6/6 | 6/6 |

## Single-annotator pass 1

| condition | complete preservation | unsupported addition |
|---|---:|---:|
| C0 | 0/6 | 4/6 |
| C1 | 4/6 | 1/6 |
| C2 | 5/6 | 0/6 |

These are prompt and rubric debugging results, not research findings. The review is not independent and has not received the delayed second pass required by `scoring_v1.md`.

The run exposed three design issues: C0 lacked target document metadata, canonical Korean wording did not prevent modal-strength contradictions, and `PILOT-CAN-001` incorrectly stored two alternative communication modes as an exception. These issues were addressed before v2. The original run and its hashes remain unchanged.
