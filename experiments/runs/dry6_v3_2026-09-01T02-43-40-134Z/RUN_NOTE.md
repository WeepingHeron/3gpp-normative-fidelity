# Dry run v3 result

- Status: `COMPLETED`
- Prompt bundle: C0 v3 + C1 v2 + C2 v2
- Model snapshot: `gpt-5.4-mini-2026-03-17`
- Cases: 6, one per modal class
- Calls: 18, with C0/C1/C2 for every case
- Parsing: 18/18
- Token usage: 10,420 input + 2,538 output
- Estimated token cost at the execution-time list price: USD 0.019236

## Deterministic checks

| condition | modal accuracy | citation exactness |
|---|---:|---:|
| C0 | 0/6 | NA |
| C1 | 6/6 | 6/6 |
| C2 | 6/6 | 6/6 |

## Delayed same-reviewer blind review

| condition | complete preservation | unsupported addition |
|---|---:|---:|
| C0 | 0/6 | 6/6 |
| C1 | 6/6 | 0/6 |
| C2 | 6/6 | 0/6 |

Pass 2 was performed after more than 24 hours with a newly shuffled blind order and new review IDs. It was saved before pass 1 was reopened.

- Response-level exact agreement: 18/18
- Applicable binary decisions: 105/105
- Aggregate Cohen's κ: 1.0
- Error-code agreement: 18/18
- Disagreements requiring adjudication: 0

This is delayed intra-rater agreement, not independent inter-rater reliability. Exception preservation has no positive exception example in this six-case dry run, so its κ is undefined. These remain prompt and rubric debugging results, not research findings.

C0 was changed from an abstention-friendly prompt to a closed-book forced-answer baseline. It answered all six cases but confused every modal pair or strength: shall as recommendation, shall-not as obligation, should as obligation, should-not as obligation, may as capability, and can as permission. Every C0 response also introduced at least one unsupported detail in the pass-1 review.

C1 and C2 both achieved complete preservation in this run. This supports the value of exact source evidence on the six dry-run cases, but it provides no evidence that structured Evidence Constraint outperforms raw oracle evidence. The six-case sample is too small for inferential claims and was used during prompt development.

Because the two blind passes agreed completely, `scoring_v1.md` and prompt bundle v3 are frozen without adjudication changes for the full 18-case pilot.
