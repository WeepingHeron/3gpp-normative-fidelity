"""Read-only verifier for a post-hoc treatment freeze; no scoring or model calls."""
import argparse
import copy
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = "experiments/posthoc_treatment_v1_20260908"
CONDITIONS = ["C0", "C1", "C2", "C3", "C1M"]
COHORT_SIZES = {"PRIMARY_STRICT_49": 49, "SENS_GOLD_50": 50,
                "SENS_EXCEPTION_50": 50, "SENS_GOLD_EXCEPTION_51": 51}
PATCH_AFTER = {
    "action": "have the capability to control both a local and a central UPF within a PDU Session",
    "gold_summary_ko": "각 SMF가 하나의 PDU Session에서 local UPF와 central UPF를 모두 제어할 수 있는 능력을 갖추는 것은 선택 사항이다.",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def record_sha(record):
    data = json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(data.encode()).hexdigest()


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def expected_cohorts(audit):
    eligible = {r["case_id"] for r in audit if r["status"] == "ELIGIBLE"}
    clean = eligible - {"MAIN-MAY-001"}
    return {"PRIMARY_STRICT_49": clean, "SENS_GOLD_50": eligible,
            "SENS_EXCEPTION_50": clean | {"MAIN-SDN-011"},
            "SENS_GOLD_EXCEPTION_51": eligible | {"MAIN-SDN-011"}}


def make_response_index(root, response_files):
    result = []
    for path in sorted(set(response_files.values())):
        for line_number, line in enumerate((root / path).read_text().splitlines(), 1):
            if not line.strip():
                continue
            record = json.loads(line)
            result.append({"case_id": record["case_id"], "condition": record["condition"],
                           "path": path, "line_number": line_number,
                           "record_sha256": record_sha(record)})
    return sorted(result, key=lambda r: (r["case_id"], CONDITIONS.index(r["condition"])))


def validate_contract(protocol, policy, gold, index, main, audit, actual_index):
    checks = {}
    mainmap = {r["case_id"]: r for r in main}
    auditmap = {r["case_id"]: r for r in audit}
    cohorts = expected_cohorts(audit)
    checks["frozen_not_applied"] = protocol["status"] == "FROZEN_NOT_APPLIED"
    checks["five_conditions"] = protocol["conditions"] == CONDITIONS
    checks["four_prespecified_cohorts"] = set(protocol["cohorts"]) == set(cohorts)
    checks["cohort_ids_counts_symmetry"] = all(
        name in protocol["cohorts"]
        and len(protocol["cohorts"][name]["case_ids"]) == COHORT_SIZES[name]
        and set(protocol["cohorts"][name]["case_ids"]) == cases
        and protocol["cohorts"][name]["n"] == len(cases)
        and protocol["cohorts"][name]["conditions"] == CONDITIONS
        for name, cases in cohorts.items())
    checks["72_unique_case_policies"] = len(policy) == len({r["case_id"] for r in policy}) == 72 and {
        r["case_id"] for r in policy} == set(mainmap)
    checks["unchanged_audit_dispositions_and_membership"] = all(
        r["case_id"] in auditmap and r["audit_status"] == auditmap[r["case_id"]]["status"]
        and r["conditions"] == CONDITIONS
        and r["cohorts"] == [k for k, ids in cohorts.items() if r["case_id"] in ids]
        for r in policy)
    checks["10_ineligible_11_hold_not_reintroduced"] = all(
        not r["cohorts"] for r in policy if r["audit_status"] in {"INELIGIBLE", "HOLD"})
    checks["cohort_composition_matches_source"] = all(
        protocol["cohorts"][k]["composition"] == {
            field: dict(Counter(mainmap[cid][field] for cid in sorted(ids)))
            for field in ("modal_class", "spec_id", "difficulty_tier")}
        for k, ids in cohorts.items())
    checks["one_gold_patch_only"] = len(gold["patches"]) == 1 and gold["patches"][0]["case_id"] == "MAIN-MAY-001"
    patch = gold["patches"][0]
    checks["gold_patch_exact_before_after"] = (
        set(patch["fields"]) == set(PATCH_AFTER)
        and all(patch["fields"][k] == {"before": mainmap["MAIN-MAY-001"][k], "after": value}
                for k, value in PATCH_AFTER.items())
        and patch["source_text_en"] == mainmap["MAIN-MAY-001"]["source_text_en"]
        and patch["apply_to_conditions"] == CONDITIONS
        and patch["changes_original_generation_input"] is False)
    checks["360_response_slots_bound"] = (len(index) == 360 and index == actual_index and
        {(r["case_id"], r["condition"]) for r in index} == {(cid, c) for cid in mainmap for c in CONDITIONS})
    checks["response_file_per_condition"] = all(
        r["path"] == protocol["response_files"][r["condition"]] for r in index)
    checks["application_not_started"] = protocol["application"] == {
        "new_model_calls": 0, "rescored_slots": 0, "union_case_count": 51,
        "planned_review_slots": 255, "existing_score_reuse": False}
    return checks


def validate_judgment(row, included):
    """Future outcome guard: unknown is never coerced to zero or silently dropped."""
    state, value, delivery = row["semantic_judgment"], row["complete_preservation"], row["delivery_status"]
    if delivery not in {"EXPLANATION", "REFUSED", "EMPTY", "PARSE_FAILURE", "NOT_GENERATED"}:
        return False
    if not included:
        return state == "NOT_SCORED" and value is None
    if delivery != "EXPLANATION":
        return state == "NOT_SCORED" and type(value) is int and value == 0
    if state == "UNRESOLVED":
        return value is None
    return type(value) is int and ((state == "PASS" and value == 1) or (state == "FAIL" and value == 0))


def self_test(objects):
    tests = []
    def reject(name, mutate):
        args = copy.deepcopy(objects)
        mutate(args)
        try:
            rejected = not all(validate_contract(**args).values())
        except (KeyError, IndexError, TypeError, ValueError):
            rejected = True
        tests.append({"name": name, "passed": rejected})
    reject("missing_case", lambda a: a["policy"].pop())
    reject("condition_asymmetry", lambda a: a["protocol"]["cohorts"]["PRIMARY_STRICT_49"].update(conditions=["C1", "C2"]))
    reject("hold_reintroduced", lambda a: a["protocol"]["cohorts"]["PRIMARY_STRICT_49"]["case_ids"].append("MAIN-SD-009"))
    reject("gold_input_contamination_in_primary", lambda a: a["protocol"]["cohorts"]["PRIMARY_STRICT_49"]["case_ids"].append("MAIN-MAY-001"))
    reject("extra_gold_field_patch", lambda a: a["gold"]["patches"][0]["fields"].update(actor={"before": "each SMF", "after": "network"}))
    reject("gold_before_value_changed", lambda a: a["gold"]["patches"][0]["fields"]["action"].update(before="wrong"))
    reject("response_record_hash_changed", lambda a: a["index"][0].update(record_sha256="0" * 64))
    for name, row, included, expected in [
        ("unknown_not_zero", {"semantic_judgment":"UNRESOLVED","complete_preservation":0,"delivery_status":"EXPLANATION"}, True, False),
        ("unknown_null_allowed", {"semantic_judgment":"UNRESOLVED","complete_preservation":None,"delivery_status":"EXPLANATION"}, True, True),
        ("refusal_counts_pipeline_zero", {"semantic_judgment":"NOT_SCORED","complete_preservation":0,"delivery_status":"REFUSED"}, True, True),
        ("excluded_not_model_failure", {"semantic_judgment":"NOT_SCORED","complete_preservation":0,"delivery_status":"EXPLANATION"}, False, False),
        ("missing_research_record_not_model_failure", {"semantic_judgment":"NOT_SCORED","complete_preservation":0,"delivery_status":"RECORD_MISSING"}, True, False),
    ]:
        tests.append({"name": name, "passed": validate_judgment(row, included) == expected})
    return tests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    folder = ROOT / BUNDLE
    manifest = read(folder / "freeze_manifest.json")
    failures = []
    for path, expected in manifest["file_sha256"].items():
        if not (ROOT / path).is_file() or sha(ROOT / path) != expected:
            failures.append("freeze hash mismatch: " + path)
    for reference in manifest["dependency_manifests"]:
        dependency = read(ROOT / reference["path"])
        for path, expected in dependency["file_sha256"].items():
            target = ROOT / reference["base"] / path
            if not target.is_file() or sha(target) != expected:
                failures.append("prior freeze mismatch: " + str(target.relative_to(ROOT)))
    if failures:
        print(json.dumps({"ok": False, "failures": failures}, ensure_ascii=False, indent=2))
        return 1
    with (ROOT / "data/main_cases.csv").open(encoding="utf-8-sig", newline="") as handle:
        dataset = list(csv.DictReader(handle))
    protocol = read(folder / "protocol.json")
    objects = {"protocol": protocol, "policy": read(folder / "case_policy.json")["rows"],
               "gold": read(folder / "gold_overlay.json"), "index": read(folder / "response_index.json")["rows"],
               "main": dataset, "audit": read(ROOT / "outputs/analysis/main72_eligibility_20260908/eligibility_audit.json")["rows"],
               "actual_index": make_response_index(ROOT, protocol["response_files"])}
    checks = validate_contract(**objects)
    tests = self_test(objects) if args.self_test else []
    ok = all(checks.values()) and all(t["passed"] for t in tests)
    print(json.dumps({"ok": ok, "status": protocol["status"], "frozen_files": len(manifest["file_sha256"]),
                      "prior_manifests_verified": len(manifest["dependency_manifests"]),
                      "checks": checks, "self_tests": tests, "new_model_calls": 0, "rescored_slots": 0},
                     ensure_ascii=False, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
