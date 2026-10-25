import csv
import hashlib
import json
import re
from datetime import datetime, timezone
from collections import Counter
from pathlib import Path

from pypdf import PdfReader

from extract_modal_candidates import clean_page
from shortlist_main_candidates import jaccard, tokens


ROOT = Path(__file__).resolve().parents[1]
MODAL_RE = re.compile(r"\b(?:shall\s+not|should\s+not|shall|should|may|cannot|can)\b", re.I)
HEADING_RE = re.compile(r"^(\d+(?:\.\d+){1,6})\s+\S")
SOURCE_FILES = {
    "3GPP TS 23.501": ROOT / "data/source/ts_123501v181200p.pdf",
    "3GPP TS 24.501": ROOT / "data/source/ts_124501v181200p.pdf",
}


def word_tokens(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def find_sequence(haystack, needle):
    for index in range(len(haystack) - len(needle) + 1):
        if haystack[index:index + len(needle)] == needle:
            return index
    return None


def main():
    rows = list(csv.DictReader((ROOT / "data/main_selection_draft.csv").open(encoding="utf-8-sig")))
    pilot = list(csv.DictReader((ROOT / "data/pilot_cases.csv").open(encoding="utf-8-sig")))
    manifest = json.loads((ROOT / "data/source_manifest.json").read_text(encoding="utf-8"))
    manifest_hashes = {source["spec_id"]: source["sha256"] for source in manifest["sources"]}
    failures = []

    if len(rows) != 72 or len({row["candidate_id"] for row in rows}) != 72:
        failures.append("selection is not 72 unique candidates")
    if Counter(row["modal_class"] for row in rows) != Counter({
        "shall": 12, "shall_not": 12, "should": 12,
        "should_not": 12, "may": 12, "can": 12,
    }):
        failures.append("modal balance mismatch")
    if Counter(row["spec_id"] for row in rows) != Counter({
        "3GPP TS 23.501": 36, "3GPP TS 24.501": 36,
    }):
        failures.append("source balance mismatch")
    if Counter(row["difficulty_tier_provisional"] for row in rows) != Counter({
        "simple": 8, "conditional": 22, "compound": 42,
    }):
        failures.append("difficulty balance mismatch")

    readers = {spec: PdfReader(str(path)) for spec, path in SOURCE_FILES.items()}
    for spec, path in SOURCE_FILES.items():
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != manifest_hashes[spec]:
            failures.append(f"{spec}: source SHA-256 mismatch")

    clause_cache = {}
    for spec, reader in readers.items():
        current_clause = ""
        for page_number, page in enumerate(reader.pages, start=1):
            lines = (page.extract_text() or "").splitlines()
            page_tokens = []
            spans = []
            for line in lines:
                match = HEADING_RE.match(line.strip())
                if match:
                    current_clause = match.group(1)
                spans.append((len(page_tokens), current_clause))
                page_tokens.extend(word_tokens(line))
            clause_cache[(spec, page_number)] = (
                page_tokens,
                spans,
                word_tokens(clean_page(page.extract_text() or "")),
            )

    for row in rows:
        prefix = row["candidate_id"]
        text = row["source_text_raw"]
        if len(MODAL_RE.findall(text)) != 1:
            failures.append(f"{prefix}: expected exactly one modal occurrence")
        page_key = (row["spec_id"], int(row["pdf_page"]))
        page_tokens, spans, cleaned_page_tokens = clause_cache[page_key]
        source_tokens = word_tokens(text)
        if find_sequence(cleaned_page_tokens, source_tokens) is None:
            failures.append(f"{prefix}: full normalized source sentence not found on PDF page")
            continue
        position = find_sequence(page_tokens, source_tokens[:min(12, len(source_tokens))])
        if position is None:
            failures.append(f"{prefix}: source prefix not locatable for clause audit")
            continue
        active_clause = ""
        for start, clause in spans:
            if start > position:
                break
            active_clause = clause
        if active_clause != row["clause_guess"]:
            failures.append(
                f"{prefix}: clause mismatch selection={row['clause_guess']} source={active_clause}"
            )

    pilot_tokens = [(row["case_id"], tokens(row["source_text_en"])) for row in pilot]
    for row in rows:
        row_tokens = tokens(row["source_text_raw"])
        for pilot_id, other_tokens in pilot_tokens:
            score = jaccard(row_tokens, other_tokens)
            if score >= 0.72:
                failures.append(
                    f"{row['candidate_id']}: pilot near duplicate {pilot_id} ({score:.3f})"
                )

    for index, left in enumerate(rows):
        for right in rows[index + 1:]:
            if left["modal_class"] != right["modal_class"]:
                continue
            score = jaccard(tokens(left["source_text_raw"]), tokens(right["source_text_raw"]))
            if score >= 0.60:
                failures.append(
                    f"{right['candidate_id']}: main near duplicate of {left['candidate_id']} ({score:.3f})"
                )

    print(f"audited_rows={len(rows)}")
    print(f"failures={len(failures)}")
    for failure in failures:
        print(f"FAIL {failure}")
    report = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "PASS" if not failures else "FAIL",
        "audited_rows": len(rows),
        "checks": [
            "72 unique candidates",
            "modal balance",
            "source balance",
            "difficulty balance",
            "source PDF SHA-256",
            "full normalized sentence on declared PDF page",
            "active clause at sentence position",
            "pilot near-duplicate threshold 0.72",
            "same-modal main near-duplicate threshold 0.60",
        ],
        "failures": failures,
    }
    (ROOT / "data/main_selection_audit.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    if failures:
        raise SystemExit(1)
    print("PASS main selection structural and source-trace audit")


if __name__ == "__main__":
    main()
