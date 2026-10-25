"""Read masked batches and validate explicit, per-row Codex review decisions.

No model calls and no semantic scoring rules. All judgments are written by the
reviewer; this utility only validates coverage and derives the agreed AND metric.
"""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / 'experiments/runs/c3_auto72_v1_2026-09-06T04-53-06-942Z/review'
FIELDS = ['actor_preserved', 'polarity_preserved', 'condition_preserved',
          'action_preserved', 'exception_preserved', 'unsupported_addition']

def rows(name):
    with (REVIEW / name).open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

if __name__ == '__main__':
    if sys.argv[1] == 'extract':
        start, end = map(int, sys.argv[2:4])
        raw={r['case_id']:r for r in map(json.loads,(REVIEW.parent/'extractions.jsonl').read_text().splitlines())}
        for i,r in enumerate(rows('extraction_review.csv')[start-1:end],start):
            parsed=raw[r['case_id']].get('parsed') or {}
            print(f'\nX{i:03d} {r["case_id"]} {parsed.get("normative_type")} {parsed.get("polarity")}')
            print('SRC '+r['source_text_en'])
            for f in ['actor','condition','action','exception']:
                print(f+' G: '+r['gold_'+f]+'\n P: '+r['extracted_'+f])
    elif sys.argv[1] == 'read':
        start, end = map(int, sys.argv[2:4])
        for r in rows('blind_explanations_blank.csv')[start-1:end]:
            print('\n' + r['review_id'] + ' GOLD ' + r['gold_modal_class'])
            print('SRC ' + r['source_text_en'])
            print('GOLD ' + json.dumps({k[5:]:v for k,v in r.items() if k.startswith('gold_') and k != 'gold_modal_class'}, ensure_ascii=False))
            print('KO ' + r['explanation_ko'])
    elif sys.argv[1] == 'assemble':
        source = rows('blind_explanations_blank.csv')
        decisions = {}
        for line in (REVIEW / 'pass1_decisions.tsv').read_text().splitlines():
            if not line or line.startswith('#'):
                continue
            rid, signature, errors, uncertainty, note = line.split('\t')
            assert rid not in decisions, rid
            assert len(signature) == 6 and set(signature) <= set('01N'), rid
            assert note.strip() and uncertainty in ('none', 'scope', 'wording'), rid
            decisions[rid] = (signature, errors, uncertainty, note)
        assert set(decisions) == {r['review_id'] for r in source}, 'Incomplete or extra decisions'
        output=[]
        for r in source:
            signature, errors, uncertainty, note = decisions[r['review_id']]
            for field, value in zip(FIELDS, signature):
                r[field] = 'NA' if value == 'N' else value
            for field, gold in [('condition_preserved','gold_condition'), ('exception_preserved','gold_exception')]:
                assert (r[field] == 'NA') == (not r[gold]), r['review_id']
            assert all(r[f] != 'NA' for f in (FIELDS[0],FIELDS[1],FIELDS[3],FIELDS[5]))
            r['complete_preservation'] = str(int(all(r[f] in ('1','NA') for f in FIELDS[:5]) and r[FIELDS[5]] == '0'))
            assert (errors == '-') == (r['complete_preservation'] == '1'), r['review_id']
            r['error_codes'] = '' if errors == '-' else errors
            r['reviewer_note'] = note
            r['review_uncertainty'] = uncertainty
            output.append(r)
        target=REVIEW / 'blind_explanations_pass1.csv'
        with target.open('w', encoding='utf-8-sig', newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(output[0])); w.writeheader(); w.writerows(output)
        print(json.dumps({'rows':len(output),'status':'PROVISIONAL_CODEX_PASS1','output':str(target)}))
