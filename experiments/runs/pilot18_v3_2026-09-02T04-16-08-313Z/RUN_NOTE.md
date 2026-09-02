# Full 18-case pilot v3

- Status: `COMPLETED`
- Purpose: prompt, schema, and scoring validation; excluded from main results
- Prompt bundle: C0 v3 + C1 v2 + C2 v2
- Model snapshot: `gpt-5.4-mini-2026-03-17`
- Cases: 18
- Calls and parsed responses: 54/54
- Token usage: 31,384 input + 7,512 output
- Estimated cost using the same USD 0.75/M input and USD 4.50/M output rates recorded for the dry run: USD 0.057342

## Deterministic provisional checks

| condition | modal class | exact citation |
|---|---:|---:|
| C0 | 5/18 | NA |
| C1 | 17/18 | 18/18 |
| C2 | 18/18 | 18/18 |

The single C1 modal mismatch is `PILOT-CAN-001`: the source modal `can` maps to capability, while the response emitted `permission`. Its Korean explanation retained the direct/indirect communication alternatives, so component preservation still requires blind human review rather than inference from this deterministic field alone.

No actor, condition, action, exception, complete-preservation, or unsupported-addition result is claimed before the 54-response blind review. These pilot outputs are not main-study evidence.

## Masked semantic review pass 1

Completed at 2026-09-02 13:25 KST.

| condition | complete preservation | unsupported addition |
|---|---:|---:|
| C0 | 0/18 | 18/18 |
| C1 | 18/18 | 0/18 |
| C2 | 18/18 | 0/18 |

Case IDs and experimental conditions were hidden during row-level scoring. However, the reviewer had already seen aggregate condition results and the identified C1 modal mismatch, so this is described as masked review rather than a fully independent blind review. The result remains provisional until a newly shuffled delayed pass 2 after 2026-09-03 13:25 KST.
