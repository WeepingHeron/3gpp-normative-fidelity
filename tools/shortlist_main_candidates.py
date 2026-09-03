import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRE_SCREEN_OVERRIDES = {
    "CAND-04388": "Complete should_not list sentence retained for manual compound review",
    "CAND-05502": "One self-contained compound V2X sentence retained; structurally similar A2X and ProSe variants remain excluded",
}


def tokens(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def jaccard(a, b):
    return len(a & b) / len(a | b) if a | b else 1.0


def automatic_exclusion(row):
    text = row["source_text_raw"]
    if not 45 <= len(text) <= 420:
        return "LENGTH_OUT_OF_RANGE"
    if re.search(r"\((?:e\.g|i\.e)\.$", text, re.I):
        return "TRUNCATED_SENTENCE"
    if re.search(r"\b(?:Figure|Table|NOTE|EXAMPLE)\b", text):
        return "LAYOUT_OR_NOTE_FRAGMENT"
    if re.search(r"\b(?:3GPP\s+)?TS\s+\d", text, re.I):
        return "EXTERNAL_SPEC_DEPENDENCY"
    if re.search(r"\b(?:as follows|the following)\b", text, re.I) or re.search(r":\s*(?:[a-z0-9]+\))", text, re.I):
        return "LIST_CONTEXT_REQUIRED"
    if re.search(r"\b\d+(?:\.\d+){1,5}\s+[A-Z][A-Za-z-]+", text):
        return "HEADING_MERGED_INTO_SENTENCE"
    if len(re.findall(r"\b(?:shall\s+not|should\s+not|shall|should|may|cannot|can)\b", text, re.I)) != 1:
        return "MULTIPLE_MODAL_OCCURRENCES"
    if re.search(r"\b(?:may exist|can be found|shall be possible)\b", text, re.I):
        return "NON_NORMATIVE_OR_IMPERSONAL_MODAL"
    if text.count(" - ") or re.search(r"\s[-•]\s", text):
        return "BULLET_FRAGMENT"
    if re.search(r"(?:^|\.\s+)[a-z]\)\s", text) or re.match(r"^(?:N26|WB-E-UTRA)\b", text):
        return "CONTINUATION_FRAGMENT"
    if re.search(r"\bthis action\b", text, re.I):
        return "UNRESOLVED_LOCAL_REFERENCE"
    return ""


def quota():
    q = {}
    specs = ["3GPP TS 23.501", "3GPP TS 24.501"]
    for modal in ["shall", "may", "can"]:
        for spec in specs:
            q[(spec, modal, "simple")] = 1
            q[(spec, modal, "conditional")] = 2
            q[(spec, modal, "compound")] = 3
    for spec in specs:
        q[(spec, "shall_not", "conditional")] = 2
        q[(spec, "shall_not", "compound")] = 4
    q[(specs[0], "should", "simple")] = 1
    q[(specs[0], "should", "conditional")] = 1
    q[(specs[0], "should", "compound")] = 2
    q[(specs[1], "should", "simple")] = 1
    q[(specs[1], "should", "conditional")] = 3
    q[(specs[1], "should", "compound")] = 4
    q[(specs[0], "should_not", "conditional")] = 2
    q[(specs[0], "should_not", "compound")] = 6
    q[(specs[1], "should_not", "compound")] = 4
    return q


def main():
    pool = list(csv.DictReader(open(ROOT / "data/main_candidate_pool.csv", encoding="utf-8-sig")))
    pilot = list(csv.DictReader(open(ROOT / "data/pilot_cases.csv", encoding="utf-8-sig")))
    pilot_tokens = [(r["case_id"], tokens(r["source_text_en"])) for r in pilot]
    eligible = defaultdict(list)
    reason_counts = Counter()
    for row in pool:
        reason = "" if row["candidate_id"] in PRE_SCREEN_OVERRIDES else automatic_exclusion(row)
        if not reason:
            t = tokens(row["source_text_raw"])
            closest_id, similarity = max(((pid, jaccard(t, pt)) for pid, pt in pilot_tokens), key=lambda x: x[1])
            if similarity >= 0.72:
                reason = f"PILOT_NEAR_DUPLICATE:{closest_id}:{similarity:.3f}"
        if reason:
            reason_counts[reason.split(":", 1)[0]] += 1
            continue
        eligible[(row["spec_id"], row["modal_class"], row["difficulty_tier_provisional"])].append(row)

    out = []
    for key, target in quota().items():
        reserve = target * 4 + 2
        candidates = eligible[key][:reserve]
        for rank, row in enumerate(candidates, start=1):
            row = dict(row)
            row.update({"quota_spec": key[0], "quota_modal": key[1], "quota_tier": key[2], "quota_target": target,
                        "document_order_rank": rank, "pre_screen_override": PRE_SCREEN_OVERRIDES.get(row["candidate_id"], ""),
                        "manual_status": "unreviewed", "manual_reason": ""})
            out.append(row)
    fields = list(out[0])
    with open(ROOT / "data/main_candidate_shortlist.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(out)
    print("shortlist", len(out))
    print("automatic exclusions", dict(reason_counts))
    for key, target in sorted(quota().items()):
        print(key, "target", target, "eligible", len(eligible[key]), "shortlisted", min(target * 4 + 2, len(eligible[key])))


if __name__ == "__main__":
    main()
