import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

from shortlist_main_candidates import quota


ROOT = Path(__file__).resolve().parents[1]

# TS 24.501 contains only four reviewable should-not candidates after the
# pre-model exclusions. Pinning their IDs makes the scarcity decision explicit
# and reproducible instead of depending on incidental CSV ordering.
PINNED_BY_CELL = {
    ("3GPP TS 24.501", "should_not", "compound"): [
        "CAND-04333",
        "CAND-04388",
        "CAND-05502",
        "CAND-07282",
    ]
}

MANUAL_EXCLUSIONS = {
    "CAND-00007": "FIGURE_DEPENDENT_DEPICTED_NETWORK_FUNCTIONS",
    "CAND-00013": "SOURCE_SENTENCE_GRAMMATICALLY_UNCLEAR",
    "CAND-00020": "UNRESOLVED_THIS_AUTHORISATION_REFERENCE",
    "CAND-03686": "UNRESOLVED_OTHER_MESSAGES_REFERENCE",
    "CAND-03687": "UNRESOLVED_THESE_CASES_REFERENCE",
    "CAND-03816": "UNRESOLVED_IN_THIS_CASE_REFERENCE",
}


def token_set(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def jaccard(left, right):
    return len(left & right) / len(left | right) if left | right else 1.0


def main():
    path = ROOT / "data/main_candidate_shortlist.csv"
    rows = list(csv.DictReader(path.open(encoding="utf-8-sig")))
    grouped = defaultdict(list)
    for row in rows:
        key = (row["quota_spec"], row["quota_modal"], row["quota_tier"])
        grouped[key].append(row)

    selected = []
    selection_log = []
    selected_tokens = defaultdict(list)
    for key, target in quota().items():
        candidates = grouped[key]
        pinned = PINNED_BY_CELL.get(key)
        if pinned:
            by_id = {row["candidate_id"]: row for row in candidates}
            missing = [candidate_id for candidate_id in pinned if candidate_id not in by_id]
            if missing:
                raise RuntimeError(f"Pinned candidates missing from {key}: {missing}")
            chosen = [by_id[candidate_id] for candidate_id in pinned]
        else:
            chosen = []
            for row in candidates:
                if row["candidate_id"] in MANUAL_EXCLUSIONS:
                    selection_log.append({
                        "candidate_id": row["candidate_id"],
                        "decision": "exclude",
                        "reason": MANUAL_EXCLUSIONS[row["candidate_id"]],
                        "related_candidate_id": "",
                    })
                    continue
                row_tokens = token_set(row["source_text_raw"])
                duplicate = next(
                    (
                        (chosen_id, jaccard(row_tokens, chosen_tokens))
                        for chosen_id, chosen_tokens in selected_tokens[row["modal_class"]]
                        if jaccard(row_tokens, chosen_tokens) >= 0.60
                    ),
                    None,
                )
                if duplicate:
                    selection_log.append({
                        "candidate_id": row["candidate_id"],
                        "decision": "exclude",
                        "reason": f"MAIN_SAME_MODAL_NEAR_DUPLICATE_JACCARD_{duplicate[1]:.3f}",
                        "related_candidate_id": duplicate[0],
                    })
                    continue
                chosen.append(row)
                selected_tokens[row["modal_class"]].append(
                    (row["candidate_id"], row_tokens)
                )
                if len(chosen) == target:
                    break
        if len(chosen) != target:
            raise RuntimeError(f"Quota shortfall for {key}: {len(chosen)} of {target}")

        for row in chosen:
            if pinned:
                selected_tokens[row["modal_class"]].append(
                    (row["candidate_id"], token_set(row["source_text_raw"]))
                )
            selection_log.append({
                "candidate_id": row["candidate_id"],
                "decision": "provisional_include",
                "reason": "PINNED_SCARCITY_CELL" if pinned else "FIRST_ELIGIBLE_IN_DOCUMENT_ORDER",
                "related_candidate_id": "",
            })
            selected.append(
                {
                    "selection_id": f"MAIN-DRAFT-{len(selected) + 1:03d}",
                    "candidate_id": row["candidate_id"],
                    "spec_id": row["spec_id"],
                    "release": row["release"],
                    "version": row["version"],
                    "pdf_page": row["pdf_page"],
                    "clause_guess": row["clause_guess"],
                    "source_text_raw": row["source_text_raw"],
                    "modal_class": row["modal_class"],
                    "difficulty_tier_provisional": row["difficulty_tier_provisional"],
                    "difficulty_basis": row["difficulty_basis"],
                    "pre_screen_override": row["pre_screen_override"],
                    "manual_status": "pending_pdf_check",
                    "manual_reason": "",
                    "replacement_candidate_id": "",
                }
            )

    ids = [row["candidate_id"] for row in selected]
    if len(selected) != 72 or len(ids) != len(set(ids)):
        raise RuntimeError("Selection must contain 72 unique candidates")

    modal_counts = Counter(row["modal_class"] for row in selected)
    spec_counts = Counter(row["spec_id"] for row in selected)
    tier_counts = Counter(row["difficulty_tier_provisional"] for row in selected)
    if set(modal_counts.values()) != {12}:
        raise RuntimeError(f"Modal balance failed: {modal_counts}")
    if spec_counts != Counter({"3GPP TS 23.501": 36, "3GPP TS 24.501": 36}):
        raise RuntimeError(f"Source balance failed: {spec_counts}")

    out = ROOT / "data/main_selection_draft.csv"
    with out.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(selected[0]))
        writer.writeheader()
        writer.writerows(selected)

    log_path = ROOT / "data/main_selection_log.csv"
    with log_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(selection_log[0]))
        writer.writeheader()
        writer.writerows(selection_log)

    print(f"wrote {out.relative_to(ROOT)} with {len(selected)} draft rows")
    print(f"wrote {log_path.relative_to(ROOT)} with {len(selection_log)} decisions")
    print("modal", dict(sorted(modal_counts.items())))
    print("spec", dict(sorted(spec_counts.items())))
    print("tier", dict(sorted(tier_counts.items())))


if __name__ == "__main__":
    main()
