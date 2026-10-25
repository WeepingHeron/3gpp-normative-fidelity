import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PREFIX = {
    "shall": "MAIN-SH-",
    "shall_not": "MAIN-SN-",
    "should": "MAIN-SD-",
    "should_not": "MAIN-SDN-",
    "may": "MAIN-MAY-",
    "can": "MAIN-CAN-",
}
QUESTION_LEAK_RE = re.compile(
    r"반드시|의무|금지|권고|허용|불가능|가능성|해서는\s*안|할\s*수\s*있|수\s*있는"
)


def norm(text):
    return re.sub(r"\W+", " ", text.lower()).strip()


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    dataset_path = ROOT / "data/main_cases.csv"
    rows = list(csv.DictReader(dataset_path.open(encoding="utf-8-sig")))
    selection = {
        row["candidate_id"]: row for row in csv.DictReader(
            (ROOT / "data/main_selection_draft.csv").open(encoding="utf-8-sig")
        )
    }
    source_manifest = json.loads((ROOT / "data/source_manifest.json").read_text(encoding="utf-8"))
    source_hashes = {row["spec_id"]: row["sha256"] for row in source_manifest["sources"]}
    failures = []

    if len(rows) != 72 or len({row["case_id"] for row in rows}) != 72:
        failures.append("dataset must contain 72 unique case IDs")
    if len({row["candidate_id"] for row in rows}) != 72:
        failures.append("dataset must contain 72 unique candidate IDs")
    if set(selection) != {row["candidate_id"] for row in rows}:
        failures.append("dataset candidate set differs from audited selection")
    if Counter(row["modal_class"] for row in rows) != Counter({modal: 12 for modal in EXPECTED_PREFIX}):
        failures.append("modal balance mismatch")
    if Counter(row["spec_id"] for row in rows) != Counter({
        "3GPP TS 23.501": 36, "3GPP TS 24.501": 36,
    }):
        failures.append("source balance mismatch")
    if Counter(row["difficulty_tier"] for row in rows) != Counter({
        "simple": 8, "conditional": 22, "compound": 42,
    }):
        failures.append("difficulty balance mismatch")

    required = [
        "case_id", "candidate_id", "spec_id", "release", "version", "clause_id",
        "pdf_page", "source_text_en", "modal_class", "polarity", "actor", "action",
        "question_ko", "gold_summary_ko", "difficulty_tier", "difficulty_basis",
        "source_sha256", "split", "review_status",
    ]
    for row in rows:
        case_id = row["case_id"]
        empty = [field for field in required if not row.get(field, "").strip()]
        if empty:
            failures.append(f"{case_id}: empty required fields {empty}")
        if not case_id.startswith(EXPECTED_PREFIX.get(row["modal_class"], "INVALID")):
            failures.append(f"{case_id}: case prefix/modal mismatch")
        if row["split"] != "test":
            failures.append(f"{case_id}: split must be test")
        if row["review_status"] not in {"draft", "self_checked"}:
            failures.append(f"{case_id}: invalid review status")
        if row["source_sha256"] != source_hashes.get(row["spec_id"]):
            failures.append(f"{case_id}: source hash mismatch")
        if QUESTION_LEAK_RE.search(row["question_ko"]):
            failures.append(f"{case_id}: question may reveal normative strength")

        selected = selection.get(row["candidate_id"])
        if selected:
            expected_source = selected["source_text_raw"]
            if row["candidate_id"] == "CAND-04388":
                expected_source = expected_source.replace("tr iggered", "triggered")
                if not row["source_normalization_note"]:
                    failures.append(f"{case_id}: missing documented source normalization")
            elif row["source_normalization_note"]:
                failures.append(f"{case_id}: unexpected source normalization note")
            if norm(row["source_text_en"]) != norm(expected_source):
                failures.append(f"{case_id}: final source differs from audited selection")
            if row["clause_id"] != selected["clause_guess"] or row["pdf_page"] != selected["pdf_page"]:
                failures.append(f"{case_id}: source locator differs from audited selection")

        gold = row["gold_summary_ko"]
        modal = row["modal_class"]
        if modal == "shall" and not re.search(r"반드시|해야\s*한다", gold):
            failures.append(f"{case_id}: shall gold lacks obligation strength")
        if modal == "shall_not" and not re.search(r"해서는\s*안|되어서는\s*안|초과해서는\s*안", gold):
            failures.append(f"{case_id}: shall_not gold lacks prohibition strength")
        if modal == "should" and "권고" not in gold:
            failures.append(f"{case_id}: should gold lacks recommendation strength")
        if modal == "should_not" and "권고" not in gold:
            failures.append(f"{case_id}: should_not gold lacks discouragement strength")
        if modal in {"may", "can"} and not re.search(r"수\s*(?:있|없)|불가능", gold):
            failures.append(f"{case_id}: {modal} gold lacks possibility wording")

    if len({row["question_ko"] for row in rows}) != len(rows):
        failures.append("duplicate Korean questions")

    report = {
        "status": "PASS" if not failures else "FAIL",
        "audited_rows": len(rows),
        "dataset_sha256": sha256(dataset_path),
        "review_status_counts": dict(Counter(row["review_status"] for row in rows)),
        "failures": failures,
    }
    (ROOT / "data/main_dataset_audit.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
