"""Read-only checks for the 2026-09-08 manual eligibility audit.

This does not infer NOTE/list boundaries or judge response correctness.
Manual decisions are evidence-backed inputs, not automatically validated truths.
It never changes the dataset, prompts, scores, or frozen manifests.
"""
import csv
import hashlib
import itertools
import json
import re
from collections import Counter
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "outputs/analysis/main72_eligibility_20260908"
SOURCE_FILES = {
    "3GPP TS 23.501": "data/source/ts_123501v181200p.pdf",
    "3GPP TS 24.501": "data/source/ts_124501v181200p.pdf",
}
STATES = {"ELIGIBLE", "ELIGIBLE_WITH_RECORDED_EXCEPTION", "INELIGIBLE", "HOLD"}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path, delimiter=","):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def normalize(text):
    # PDF typography/line-wrap check only; does not establish semantic equality.
    return re.sub(r"[^a-z0-9]", "", text.lower())


def tokens(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def jaccard(left, right):
    a, b = tokens(left), tokens(right)
    return len(a & b) / len(a | b) if a | b else 1.0


def collect():
    rows = read_csv(ROOT / "data/main_cases.csv")
    decisions = read_csv(AUDIT / "decisions.tsv", "\t")
    pilot = read_csv(ROOT / "data/pilot_cases.csv")
    selection = read_csv(ROOT / "data/main_selection_draft.csv")
    source_manifest = json.loads((ROOT / "data/source_manifest.json").read_text())
    declared_hashes = {s["spec_id"]: s["sha256"] for s in source_manifest["sources"]}
    checks = {}
    checks["72_unique_cases"] = len(rows) == len({r["case_id"] for r in rows}) == 72
    checks["72_unique_candidates"] = len({r["candidate_id"] for r in rows}) == 72
    checks["72_explicit_decisions"] = (
        len(decisions) == len({r["case_id"] for r in decisions}) == 72
        and {r["case_id"] for r in decisions} == {r["case_id"] for r in rows}
        and all(r["status"] in STATES and r["rationale_ko"] and r["reason_code"] for r in decisions)
    )
    checks["modal_balance"] = Counter(r["modal_class"] for r in rows) == Counter({
        "shall": 12, "shall_not": 12, "may": 12, "can": 12, "should": 12, "should_not": 12})
    checks["source_balance"] = Counter(r["spec_id"] for r in rows) == Counter({k: 36 for k in SOURCE_FILES})
    checks["frozen_tier_counts"] = Counter(r["difficulty_tier"] for r in rows) == Counter({
        "simple": 8, "conditional": 22, "compound": 42})
    frozen_results = []
    for relative in ["data/main_freeze_manifest.json",
                     "outputs/analysis/review_resume_20260907_manifest.json",
                     "outputs/analysis/gold_boundary_review_20260907/manifest.json"]:
        manifest = json.loads((ROOT / relative).read_text())
        for file, expected in manifest["file_sha256"].items():
            frozen_results.append({"manifest": relative, "path": file,
                                   "matches": sha256(ROOT / file) == expected})
    checks["all_prior_frozen_hashes_unchanged"] = all(r["matches"] for r in frozen_results)
    source_checks = []
    for spec, relative in SOURCE_FILES.items():
        actual_hash = sha256(ROOT / relative)
        selected = [r for r in rows if r["spec_id"] == spec]
        checks[f"pdf_hash_{spec}"] = actual_hash == declared_hashes[spec]
        reader = PdfReader(ROOT / relative)
        clause = ""
        for page_number, page in enumerate(reader.pages, 1):
            if page_number > max(int(r["pdf_page"]) for r in selected):
                break
            spans, page_text = [], ""
            for line in (page.extract_text() or "").splitlines():
                # Preserve letter suffixes such as 4.2.8.1A. Legacy regex missed these.
                match = re.match(r"^(\d+(?:\.\d+[A-Za-z]?){1,7})\s+\S", line.strip())
                if match:
                    clause = match.group(1)
                spans.append((len(page_text), clause))
                page_text += normalize(line)
            for row in (r for r in selected if int(r["pdf_page"]) == page_number):
                position = page_text.find(normalize(row["source_text_en"]))
                found_clause = ""
                for start, active in spans:
                    if start > position:
                        break
                    found_clause = active
                source_checks.append({"case_id": row["case_id"], "source_match": position >= 0,
                                      "declared_clause": row["clause_id"], "source_clause": found_clause,
                                      "case_hash_matches": row["source_sha256"] == actual_hash})
    checks["all_source_text_located"] = len(source_checks) == 72 and all(r["source_match"] for r in source_checks)
    checks["all_case_source_hashes_match"] = all(r["case_hash_matches"] for r in source_checks)
    clause_mismatches = [r for r in source_checks if r["declared_clause"] != r["source_clause"]]
    # A mismatch is an audit finding; accounting for it is a completeness check.
    checks["clause_findings_accounted_for"] = all(
        any(d["case_id"] == r["case_id"] and "CLAUSE_ID_MISMATCH" in d["reason_code"] for d in decisions)
        for r in clause_mismatches)
    main_pairs = []
    for a, b in itertools.combinations(rows, 2):
        if a["modal_class"] != b["modal_class"]:
            continue
        score = jaccard(a["source_text_en"], b["source_text_en"])
        if score >= 0.60:
            main_pairs.append({"left": a["case_id"], "right": b["case_id"], "jaccard": score})
    pilot_pairs = sorted((
        {"main": a["case_id"], "pilot": b["case_id"],
         "jaccard": jaccard(a["source_text_en"], b["source_text_en"])}
        for a in rows for b in pilot), key=lambda r: r["jaccard"], reverse=True)
    checks["no_main_same_modal_jaccard_060"] = not main_pairs
    checks["no_pilot_jaccard_072"] = not any(r["jaccard"] >= 0.72 for r in pilot_pairs)
    checks["modal_token_present"] = all(
        re.search(r"\b" + r["modal_class"].replace("_", r"\s+") + r"\b", r["source_text_en"], re.I)
        for r in rows)
    counts = Counter(r["status"] for r in decisions)
    dmap = {d["case_id"]: d for d in decisions}
    by_modal, by_spec = {}, {}
    for field, target in [("modal_class", by_modal), ("spec_id", by_spec)]:
        for value in sorted({r[field] for r in rows}):
            target[value] = dict(Counter(dmap[r["case_id"]]["status"] for r in rows if r[field] == value))
    return {
        "audit_status": "REVIEW_COMPLETE_WITH_INELIGIBLE_AND_HOLD_CASES",
        "reviewer": "Codex; not independent; not domain-expert consensus",
        "review_date": "2026-09-08", "model_response_rescoring": False,
        "checks": checks, "all_mechanical_checks_pass": all(checks.values()),
        "case_count": len(rows), "decision_counts": dict(counts),
        "by_modal": by_modal, "by_spec": by_spec,
        "source_page_count": len({(r["spec_id"], r["pdf_page"]) for r in rows}),
        "source_checks": source_checks, "clause_mismatches": clause_mismatches,
        "recorded_exceptions": [{"candidate_id": r["candidate_id"], "reason": r["pre_screen_override"]}
                                for r in selection if r["pre_screen_override"]],
        "frozen_file_checks": frozen_results,
        "main_jaccard_threshold_pairs": main_pairs, "pilot_closest_pairs": pilot_pairs[:10],
        "semantic_overlap_review": [
            {"main": "MAIN-SH-004", "pilot": "PILOT-SH-001", "status": "HOLD",
             "note": "0.375 Jaccard is below threshold; shared CP NF service-based interaction needs semantic review."},
            {"main_pair": ["MAIN-SDN-008", "MAIN-SDN-009"], "status": "RELATED_NOT_AUTO_EXCLUDED",
             "note": "Active Time/all-PLMN allocation and indication are related but distinct actions; cluster dependence remains."}],
        "limits": ["Mechanical checks do not validate manual eligibility decisions.",
                   "No independent expert review or model-response re-scoring.",
                   "Not a full re-selection of the candidate pool; surviving counts are not a new frozen dataset."],
    }


if __name__ == "__main__":
    result = collect()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["all_mechanical_checks_pass"] else 1)
