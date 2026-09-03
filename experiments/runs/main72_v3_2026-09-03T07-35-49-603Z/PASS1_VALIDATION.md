# Pass 1 validation report

## Overall assessment: Needs revision before paper reporting

The masked row-level pass 1 is complete and internally consistent, but it is a single Codex reviewer result rather than an independent human expert annotation. It is suitable for planning pass 2 and adjudication, not yet for a final paper claim.

## Verified calculations

- 216/216 rows contain all seven semantic score fields.
- Each condition contains 72 paired cases.
- Complete preservation: C0 0/72, C1 65/72, C2 72/72.
- Unsupported addition: C0 64/72, C1 7/72, C2 0/72.
- Exact citation: C1 72/72 and C2 72/72.
- C1 to C2 complete-preservation difference: +7/72, or +9.72 percentage points.
- Exact two-sided McNemar p for C1 versus C2 complete preservation: 0.015625.
- Paired bootstrap 95% interval for that difference: 2.78 to 16.67 percentage points.

## Material validity risks

1. **Single-reviewer bias:** The reviewer saw aggregate deterministic condition results before masked row scoring. Case IDs and conditions were hidden during scoring, but this is not a fully independent blind review.
2. **Perfect C2 result:** C2 reached 72/72, which requires scrutiny for ceiling effects and rubric alignment rather than immediate acceptance.
3. **Frozen gold-scope ambiguity:** `MAIN-CAN-004`, `MAIN-SD-002`, and `MAIN-CAN-008` contain modal-bearing language inside broader descriptive or prerequisite constructions. Their selected actor and modal scope may favor the structured constraint by construction. Do not change the frozen labels after observing results; obtain an independent judgment and report sensitivity if adjudication differs.
4. **Translation-strength judgment:** Several C1 failures turn English `should not` into Korean expressions such as `해서는 안 된다` or explicitly label them as prohibition. The rubric treats that as strengthening, but an independent Korean-language reviewer should confirm this boundary.
5. **Generalisability:** This is one OpenAI model snapshot, two 3GPP specifications at one Release/version, oracle evidence, and a constructed balanced sample. It does not measure retrieval performance or all telecom standards.

## Next gate

- Keep pass 1 unchanged.
- After at least 24 hours, prepare a newly reshuffled masked pass 2 from the same 216 responses; do not call the API again.
- Adjudicate only pass disagreements and the three predeclared gold-scope ambiguity cases.
- Recompute the paired analysis from adjudicated scores before drafting the result claim.
