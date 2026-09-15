"""Read-only reproduction of the 2026-09-06 research review checks.

Run from any directory with Python 3. No API calls or file writes.
"""
import csv
import hashlib
import json
import math
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "experiments/runs/main72_v3_2026-09-03T07-35-49-603Z"


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def verify_hashes(base, manifest):
    return {name: hashlib.sha256((base / name).read_bytes()).hexdigest() == digest
            for name, digest in manifest["file_sha256"].items()}


def paired(rows, excluded=()):
    arms = {
        c: {r["case_id"]: int(r["complete_preservation"]) for r in rows
            if r["condition"] == c and r["case_id"] not in excluded}
        for c in ("C1", "C2")
    }
    a, b = arms["C1"], arms["C2"]
    assert a.keys() == b.keys()
    first = sum(a[k] > b[k] for k in a)
    second = sum(a[k] < b[k] for k in a)
    discordant = first + second
    p = (min(1, 2 * sum(math.comb(discordant, k) * 0.5 ** discordant
                       for k in range(min(first, second) + 1)))
         if discordant else 1)
    return {"n": len(a), "C1_successes": sum(a.values()), "C2_successes": sum(b.values()),
            "difference_pp": 100 * (sum(b.values()) - sum(a.values())) / len(a),
            "discordant_C1_only": first, "discordant_C2_only": second,
            "exact_McNemar_two_sided_p": p}


def main():
    dataset = read_csv(ROOT / "data/main_cases.csv")
    rows = read_csv(RUN / "human_scores_adjudicated.csv")
    parsed = [json.loads(line) for line in (RUN / "parsed_responses.jsonl").read_text().splitlines()]
    raw = [json.loads(line) for line in (RUN / "raw_responses.jsonl").read_text().splitlines()]
    fields = ("actor_preserved", "polarity_preserved", "condition_preserved",
              "action_preserved", "exception_preserved")
    assert len(dataset) == len({r["case_id"] for r in dataset}) == 72
    assert len(rows) == len({(r["case_id"], r["condition"]) for r in rows}) == 216
    assert {(r["case_id"], r["condition"]) for r in rows} == {
        (r["case_id"], c) for r in dataset for c in ("C0", "C1", "C2")}
    for r in rows:
        assert all(r[f] in ("0", "1", "NA") for f in fields)
        assert r["unsupported_addition"] in ("0", "1")
        complete = all(r[f] in ("1", "NA") for f in fields) and r["unsupported_addition"] == "0"
        assert int(complete) == int(r["complete_preservation"])
    result = {
        "dataset_rows": len(dataset), "score_rows": len(rows),
        "dataset_freeze_hashes": verify_hashes(ROOT, json.loads((ROOT / "data/main_freeze_manifest.json").read_text())),
        "output_freeze_hashes": verify_hashes(RUN, json.loads((RUN / "output_freeze_manifest.json").read_text())),
        "unique_source_clauses": len({(r["spec_id"], r["clause_id"]) for r in dataset}),
        "difficulty_counts": dict(Counter(r["difficulty_tier"] for r in dataset)),
        "raw_attempts": len(raw), "http_status_counts": dict(Counter(r.get("http_status") for r in raw)),
        "primary": paired(rows),
        "sensitivity": paired(rows, {"MAIN-CAN-004", "MAIN-SD-002", "MAIN-CAN-008"}),
        "conditions": {},
    }
    for c in ("C0", "C1", "C2"):
        selected = [r for r in rows if r["condition"] == c]
        usage = [r["usage"] for r in parsed if r["condition"] == c]
        result["conditions"][c] = {
            "success_counts": {f: sum(r[f] == "1" for r in selected)
                               for f in ("modal_correct", "polarity_preserved", "complete_preservation", "unsupported_addition")},
            "complete_but_JSON_modal_incorrect": [r["case_id"] for r in selected
                                                    if r["complete_preservation"] == "1" and r["modal_correct"] == "0"],
            "token_totals": {k: sum(u[k] for u in usage) for k in ("input_tokens", "output_tokens", "total_tokens")},
        }
    assert all(result["dataset_freeze_hashes"].values())
    assert all(result["output_freeze_hashes"].values())
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
