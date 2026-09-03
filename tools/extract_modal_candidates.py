import csv
import hashlib
import re
import sys
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ("3GPP TS 23.501", ROOT / "data/source/ts_123501v181200p.pdf", 42, 611),
    ("3GPP TS 24.501", ROOT / "data/source/ts_124501v181200p.pdf", 49, 733),
]
MODAL_RE = re.compile(r"\b(shall\s+not|should\s+not|shall|should|may|cannot|can)\b", re.I)
HEADING_RE = re.compile(r"^(\d+(?:\.\d+){1,6})\s+\S")
MARKER_RE = re.compile(
    r"\b(if|when|where|during|while|after|before|upon|once|until|because|"
    r"provided\s+that|as\s+long\s+as|in\s+case|in\s+the\s+event)\b",
    re.I,
)
HARD_RE = re.compile(r"\b(only|unless|except)\b|\bif\s+any\b", re.I)


def clean_page(text: str) -> str:
    lines = []
    for line in (text or "").splitlines():
        s = line.strip()
        if not s or s == "ETSI":
            continue
        if re.match(r"^ETSI TS \d+ \d+ V\d+", s):
            continue
        if re.match(r"^\d*3GPP TS \d+\.\d+ version", s):
            continue
        lines.append(s)
    joined = " ".join(lines)
    joined = re.sub(r"(?<=\w)-\s+(?=\w)", "", joined)
    return re.sub(r"\s+", " ", joined).strip()


def modal_class(surface: str) -> str:
    return surface.lower().replace(" ", "_") if surface.lower() != "cannot" else "can"


def difficulty(sentence: str, modal: str):
    markers = MARKER_RE.findall(sentence)
    hard = HARD_RE.findall(sentence)
    coordination = len(re.findall(r"\b(?:and|or)\b|;", sentence, re.I))
    negative = modal in {"shall_not", "should_not", "can"} and bool(re.search(r"\b(?:not|cannot)\b", sentence, re.I))
    if len(markers) >= 2 or hard or (negative and markers) or coordination >= 2:
        tier = "compound"
    elif markers or negative:
        tier = "conditional"
    else:
        tier = "simple"
    basis = []
    if markers: basis.append("markers=" + "+".join(x.lower().replace(" ", "_") for x in markers))
    if hard: basis.append("hard_limit")
    if negative: basis.append("negative_modal")
    if coordination: basis.append(f"coordination={coordination}")
    return tier, ";".join(basis) or "single_unqualified_statement"


def sentence_spans(text: str):
    starts = [0]
    for match in re.finditer(r"(?<=[.!?])\s+(?=[A-Z(])", text):
        starts.append(match.end())
    starts.append(len(text))
    for a, b in zip(starts, starts[1:]):
        sentence = text[a:b].strip()
        if sentence:
            yield a, sentence


def page_token_map(raw_text: str, inherited_clause: str):
    """Return page tokens and the clause active at each source-line start."""
    tokens = []
    line_starts = []
    clauses = []
    current = inherited_clause
    for line in (raw_text or "").splitlines():
        line_starts.append(len(tokens))
        match = HEADING_RE.match(line.strip())
        if match:
            current = match.group(1)
        clauses.append(current)
        tokens.extend(re.findall(r"[a-z0-9]+", line.lower()))
    return tokens, line_starts, clauses, current


def clause_for_sentence(sentence: str, page_tokens, line_starts, clauses, fallback: str):
    target = re.findall(r"[a-z0-9]+", sentence.lower())
    position = None
    # A prefix is enough to locate the source line and tolerates PDF hyphenation.
    for length in range(min(len(target), 20), 7, -1):
        prefix = target[:length]
        for index in range(len(page_tokens) - length + 1):
            if page_tokens[index:index + length] == prefix:
                position = index
                break
        if position is not None:
            break
    if position is None:
        return fallback
    active = fallback
    for start, clause in zip(line_starts, clauses):
        if start > position:
            break
        active = clause
    return active


def main():
    output = ROOT / "data/main_candidate_pool.csv"
    rows, seen = [], set()
    for spec_id, pdf_path, first_page, last_page in SOURCES:
        reader = PdfReader(str(pdf_path))
        current_clause = ""
        for pdf_page in range(first_page, min(last_page, len(reader.pages)) + 1):
            raw = reader.pages[pdf_page - 1].extract_text() or ""
            page_tokens, line_starts, clauses, final_clause = page_token_map(raw, current_clause)
            text = clean_page(raw)
            for _, sentence in sentence_spans(text):
                if len(sentence) < 25 or len(sentence) > 700:
                    continue
                if sentence.startswith(("NOTE", "EXAMPLE", "Table ", "Figure ")):
                    continue
                for occurrence, match in enumerate(MODAL_RE.finditer(sentence), start=1):
                    surface = re.sub(r"\s+", " ", match.group(1).lower())
                    modal = modal_class(surface)
                    norm = re.sub(r"\W+", " ", sentence.lower()).strip()
                    digest = hashlib.sha256(norm.encode()).hexdigest()
                    key = (spec_id, digest, modal)
                    if key in seen:
                        continue
                    seen.add(key)
                    tier, basis = difficulty(sentence, modal)
                    rows.append({
                        "candidate_id": f"CAND-{len(rows)+1:05d}", "spec_id": spec_id,
                        "release": "18", "version": "18.12.0", "pdf_page": pdf_page,
                        "clause_guess": clause_for_sentence(
                            sentence, page_tokens, line_starts, clauses, current_clause
                        ), "modal_surface": surface,
                        "modal_class": modal, "source_text_raw": sentence,
                        "difficulty_tier_provisional": tier, "difficulty_basis": basis,
                        "normalized_sha256": digest, "eligibility_status": "unreviewed",
                        "exclusion_reason": "", "review_note": "",
                    })
            current_clause = final_clause
    fields = list(rows[0])
    with output.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)
    print(f"wrote {len(rows)} candidates to {output}")


if __name__ == "__main__":
    main()
