# Predeclared gold-scope sensitivity review

This review does not modify `data/main_cases.csv` or the frozen run. It records the three cases declared before delayed pass 2 as potentially ambiguous in modal-bearing sentence scope.

| Case | Frozen target | Alternative reading | Decision for frozen analysis |
|---|---|---|---|
| `MAIN-CAN-004` | `can`: authorized NFs can access shared UDSF data | The operative clause is implementation/deployment responsibility to ensure authorization, rather than NF capability | Keep frozen label; flag for independent telecom-expert review |
| `MAIN-SD-002` | `should`: Paging Policy should be applied according to application DSCP | The matrix clause states that the application sets DSCP; `should` occurs inside the policy being indicated | Keep frozen label; flag for independent telecom-expert review |
| `MAIN-CAN-008` | `can`: security can be activated after a context exists | The operative normative force may be `need to establish`, with AMF and UE as actors | Keep frozen label; flag for independent telecom-expert review |

All three are retained in the primary frozen analysis to avoid post-result label changes. A transparent sensitivity view should additionally report results after excluding these three cases (nine responses), without presenting that exclusion as a replacement gold set.
