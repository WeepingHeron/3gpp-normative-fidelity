# Main experiment result tables

> Source: `human_scores_adjudicated.csv`. Pass 1, delayed pass 2, and adjudication were performed by the same Codex reviewer; this is not independent expert validation.

## Table 1. Overall results

| Condition | JSON modal label accuracy | Explanation complete preservation | Unsupported addition | Citation ID exactness |
|---|---:|---:|---:|---:|
| C0 | 15/72 (20.83%) | 0/72 (0.00%) | 65/72 (90.28%) | N/A |
| C1 | 56/72 (77.78%) | 65/72 (90.28%) | 7/72 (9.72%) | 72/72 (100.00%) |
| C2 | 72/72 (100.00%) | 72/72 (100.00%) | 0/72 (0.00%) | 72/72 (100.00%) |

## Table 2. Paired complete-preservation comparisons

| Comparison | Difference | Paired bootstrap 95% CI | First-only / second-only | Exact McNemar p |
|---|---:|---:|---:|---:|
| C0 vs C1 | 90.28 pp | 83.33 pp to 97.22 pp | 0 / 65 | 5.42101e-20 |
| C1 vs C2 | 9.72 pp | 2.78 pp to 16.67 pp | 0 / 7 | 0.015625 |
| C0 vs C2 | 100.00 pp | 100.00 pp to 100.00 pp | 0 / 72 | 4.23516e-22 |

## Table 3. C1 complete-preservation failures

| Case | Modal | Failed fields | Unsupported addition |
|---|---|---|---:|
| `MAIN-CAN-004` | `can` | actor, force, action | 1 |
| `MAIN-CAN-008` | `can` | actor, force, action | 1 |
| `MAIN-SD-002` | `should` | actor, force, action | 1 |
| `MAIN-SDN-003` | `should_not` | force | 1 |
| `MAIN-SDN-005` | `should_not` | force | 1 |
| `MAIN-SDN-009` | `should_not` | force | 1 |
| `MAIN-SDN-010` | `should_not` | force | 1 |

## Reporting boundary

- C2 receives the gold structured fields; 72/72 is not evidence of automatic extraction or perfect general performance.
- JSON modal labels and Korean explanation judgments have different evaluation targets. See docs/09_reporting_errata_2026-09-06.md.
- Retrieval was not evaluated; citation exactness checks supplied identifier copying.
- Three gold-scope cases were recorded after pass 1 and before delayed pass 2. Excluding them: C1 65/69, C2 69/69, difference +5.80 pp, exact McNemar p=0.125.
