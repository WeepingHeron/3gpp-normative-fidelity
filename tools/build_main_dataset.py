import argparse
import csv
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANNOTATION_DIR = ROOT / "data/annotations"
CASE_PREFIX = {
    "shall": "SH",
    "shall_not": "SN",
    "should": "SD",
    "should_not": "SDN",
    "may": "MAY",
    "can": "CAN",
}
SOURCE_NORMALIZATIONS = {
    "CAND-04388": (
        "tr iggered",
        "triggered",
        "PDF text-extraction intra-word space removed after visual/source-line check",
    )
}
FROZEN_FILES = [
    "data/main_cases.csv",
    "data/main_selection_draft.csv",
    "data/main_selection_log.csv",
    "data/main_selection_audit.json",
    "data/main_dataset_audit.json",
    "data/annotations/main_shall_may.json",
    "data/annotations/main_can_shall_not.json",
    "data/annotations/main_should_should_not.json",
    "docs/06_main_difficulty_protocol.md",
    "experiments/prompts/c0_v3.md",
    "experiments/prompts/c1_v2.md",
    "experiments/prompts/c2_v2.md",
    "experiments/response_schema.json",
    "experiments/scoring_v1.md",
]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_annotations():
    merged = {}
    for path in sorted(ANNOTATION_DIR.glob("main_*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        overlap = set(merged) & set(data)
        if overlap:
            raise RuntimeError(f"duplicate annotation IDs: {sorted(overlap)}")
        merged.update(data)
    return merged


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--freeze", action="store_true")
    args = parser.parse_args()

    selection = list(csv.DictReader(
        (ROOT / "data/main_selection_draft.csv").open(encoding="utf-8-sig")
    ))
    annotations = load_annotations()
    selected_ids = {row["candidate_id"] for row in selection}
    if selected_ids != set(annotations):
        raise RuntimeError(
            f"annotation/selection mismatch missing={sorted(selected_ids-set(annotations))} "
            f"extra={sorted(set(annotations)-selected_ids)}"
        )
    source_manifest = json.loads((ROOT / "data/source_manifest.json").read_text(encoding="utf-8"))
    source_hash = {row["spec_id"]: row["sha256"] for row in source_manifest["sources"]}
    audit = json.loads((ROOT / "data/main_selection_audit.json").read_text(encoding="utf-8"))
    if audit["status"] != "PASS" or audit["audited_rows"] != 72:
        raise RuntimeError("main selection audit is not a 72-row PASS")

    counters = Counter()
    output = []
    required = ["actor", "action", "question_ko", "gold_summary_ko"]
    for selected in selection:
        candidate_id = selected["candidate_id"]
        annotation = annotations[candidate_id]
        missing = [field for field in required if not annotation.get(field, "").strip()]
        if missing:
            raise RuntimeError(f"{candidate_id}: empty required annotations {missing}")
        modal = selected["modal_class"]
        counters[modal] += 1
        source_text = selected["source_text_raw"]
        normalization_note = ""
        if candidate_id in SOURCE_NORMALIZATIONS:
            old, new, normalization_note = SOURCE_NORMALIZATIONS[candidate_id]
            if old not in source_text:
                raise RuntimeError(f"{candidate_id}: normalization source not found")
            source_text = source_text.replace(old, new)
        output.append({
            "case_id": f"MAIN-{CASE_PREFIX[modal]}-{counters[modal]:03d}",
            "candidate_id": candidate_id,
            "spec_id": selected["spec_id"],
            "release": selected["release"],
            "version": selected["version"],
            "clause_id": selected["clause_guess"],
            "pdf_page": selected["pdf_page"],
            "source_text_en": source_text,
            "source_normalization_note": normalization_note,
            "modal_class": modal,
            "polarity": annotation.get(
                "polarity", "negative" if modal in {"shall_not", "should_not"} else "positive"
            ),
            "actor": annotation["actor"],
            "condition": annotation.get("condition", ""),
            "action": annotation["action"],
            "exception": annotation.get("exception", ""),
            "question_ko": annotation["question_ko"],
            "gold_summary_ko": annotation["gold_summary_ko"],
            "difficulty_tier": selected["difficulty_tier_provisional"],
            "difficulty_basis": selected["difficulty_basis"],
            "source_sha256": source_hash[selected["spec_id"]],
            "split": "test",
            "review_status": "self_checked" if args.freeze else "draft",
        })

    out_path = ROOT / "data/main_cases.csv"
    with out_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(output[0]))
        writer.writeheader()
        writer.writerows(output)
    print(f"wrote {out_path.relative_to(ROOT)} rows={len(output)} status={output[0]['review_status']}")

    if args.freeze:
        manifest = {
            "status": "FROZEN_SINGLE_ANNOTATOR",
            "frozen_at_utc": datetime.now(timezone.utc).isoformat(),
            "dataset_path": "data/main_cases.csv",
            "dataset_sha256": sha256(out_path),
            "case_count": len(output),
            "conditions": ["C0", "C1", "C2"],
            "planned_api_calls": len(output) * 3,
            "provider": "OpenAI",
            "api": "Responses API",
            "model_requested": "gpt-5.4-mini-2026-03-17",
            "parameters": {
                "temperature": 0,
                "reasoning_effort": "none",
                "max_output_tokens": 600,
                "store": False,
            },
            "prompt_file_versions": {"C0": "v3", "C1": "v2", "C2": "v2"},
            "review_boundary": (
                "single-annotator source-grounded self-check; not independently second-reviewed"
            ),
            "file_sha256": {rel: sha256(ROOT / rel) for rel in FROZEN_FILES},
        }
        manifest_path = ROOT / "data/main_freeze_manifest.json"
        manifest_path.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"wrote {manifest_path.relative_to(ROOT)} sha256={manifest['dataset_sha256']}")


if __name__ == "__main__":
    main()
