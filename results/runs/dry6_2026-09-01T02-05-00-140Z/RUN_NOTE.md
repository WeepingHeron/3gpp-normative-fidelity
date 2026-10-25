# Dry run status

- Status: `BLOCKED`
- Successful responses: 0
- Blocking code: `credit_balance_exhausted`
- Research use: none; this run contains no model output and must not be included in results.

The API key was accepted, but the API organization had no remaining credits. The first runner version treated every HTTP 429 as retryable, so eight planned requests each produced three failed attempts before the run was manually stopped. The runner was corrected after this run so `insufficient_quota` and `credit_balance_exhausted` stop immediately without retry.

After API credits become available, start a new run directory with `node experiments/run_pilot.mjs`. Do not resume or overwrite this blocked run.
