"""Read masked packets and persist explicitly authored review decisions; no scoring inference."""
import argparse
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'outputs/review/v2_20260908'
PREFLIGHT = ROOT / 'outputs/review/v2_preflight_20260908/preflight_completed.jsonl'
OUT = ROOT / 'outputs/review/v2_pass1_20260908'

def rows(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('command', choices=['show', 'record'])
    ap.add_argument('--start', type=int)
    ap.add_argument('--stop', type=int)
    ap.add_argument('--decisions', type=Path)
    args = ap.parse_args()
    packets = rows(PACKAGE / 'reviewer/pass1/packets.jsonl')
    pf = {r['reference_id']: r for r in rows(PREFLIGHT)}
    if args.command == 'show':
        for p in packets[args.start-1:args.stop]:
            g = pf[p['reference_id']]
            print(f"\n{p['review_id']} {p['reference_id']} [{g['gold_status']}] {p['delivery_status']}")
            print('SOURCE:', p['source']['source_text_en'])
            print('QUESTION:', p['question_ko'])
            print('REFERENCE:', ' | '.join(f"{x['action_or_state']}; {x['condition']}; {x['relation']}" for x in g['propositions_and_relations']))
            print('ANSWER:', p['explanation_ko'])
        return
    existing_path = OUT / 'judgments_working.jsonl'
    assert not (OUT / 'seal/completion_manifest.json').exists(), 'Pass 1 already sealed; append is disabled'
    existing = rows(existing_path) if existing_path.exists() else []
    done = {r['review_id'] for r in existing}
    blanks = {r['review_id']: r for r in rows(PACKAGE / 'reviewer/pass1/judgments_blank.jsonl')}
    byid = {r['review_id']: r for r in packets}
    authored = list(csv.DictReader(args.decisions.open(), delimiter='\t'))
    new = []
    for d in authored:
        rid = d['review_id']
        assert rid not in done, rid
        done.add(rid)
        r = blanks[rid]
        p, g = byid[rid], pf[r['reference_id']]
        assert d['semantic_judgment'] in {'PASS', 'FAIL', 'UNRESOLVED', 'NOT_SCORED'}
        assert d['rationale'].strip() and d['response_evidence'].strip()
        if p['delivery_status'] == 'EXPLANATION':
            assert d['response_evidence'] in p['explanation_ko'], (rid, 'Response evidence not verbatim')
        r.update(reviewer='Codex (same study evaluator; not independent domain expert)',
                 reviewed_at=datetime.now(timezone.utc).isoformat(),
                 semantic_judgment=d['semantic_judgment'],
                 complete_preservation={'PASS': 1, 'FAIL': 0, 'UNRESOLVED': None, 'NOT_SCORED': 0}[d['semantic_judgment']],
                 gold_status=g['gold_status'], reason_codes=d['reason_codes'].split('|'),
                 rationale=d['rationale'], response_evidence=d['response_evidence'],
                 source_provenance=g['source_provenance'], propositions_and_relations=g['propositions_and_relations'],
                 packet_sha256=hashlib.sha256(json.dumps(p, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
                 input_context_gap=g['input_context_gap'])
        new.append(r)
    OUT.mkdir(parents=True, exist_ok=True)
    existing_path.write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in existing+new))
    print(json.dumps({'appended': len(new), 'reviewed_total': len(existing+new), 'automatic_semantic_inference': False}))

if __name__ == '__main__':
    main()
