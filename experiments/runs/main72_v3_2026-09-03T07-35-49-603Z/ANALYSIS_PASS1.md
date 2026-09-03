# Provisional main-result analysis: masked pass 1

> **Not final.** This analysis uses a masked Codex single-reviewer pass 1. A delayed pass 2 or independent review and adjudication are required before paper reporting.

## Condition results

| Condition | Modal accuracy | Complete preservation | Unsupported addition | Exact citation |
|---|---:|---:|---:|---:|
| C0 | 15/72 (20.83%) | 0/72 (0.00%) | 64/72 (88.89%) | N/A |
| C1 | 56/72 (77.78%) | 65/72 (90.28%) | 7/72 (9.72%) | 72/72 (100.00%) |
| C2 | 72/72 (100.00%) | 72/72 (100.00%) | 0/72 (0.00%) | 72/72 (100.00%) |

## Paired complete-preservation comparisons

| Comparison | Difference (second - first) | Paired bootstrap 95% CI | Discordant first-only / second-only | Exact McNemar p |
|---|---:|---:|---:|---:|
| C0 vs C1 | 90.28% | 83.33% to 97.22% | 0 / 65 | 5.421e-20 |
| C1 vs C2 | 9.72% | 2.78% to 16.67% | 0 / 7 | 0.01563 |
| C0 vs C2 | 100.00% | 100.00% to 100.00% | 0 / 72 | 4.235e-22 |

## Interpretation boundary

- C2 reached 72/72 in this pass, so ceiling effects and reviewer/gold-label dependence require particular scrutiny.
- The oracle-evidence design evaluates generation under supplied evidence, not retrieval quality or end-to-end RAG.
- Three frozen cases use modal-bearing language inside broader descriptive sentences; their gold actor and modal scope should be independently reviewed without changing this frozen run.
- No causal or general model-performance claim should be made from one model snapshot, one corpus version, and one reviewer pass.
