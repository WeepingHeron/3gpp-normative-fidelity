"""Read masked material and assemble explicit reviewer decisions; no semantic inference."""
import csv, json, sys
from pathlib import Path

FIELDS = ['actor_preserved', 'polarity_preserved', 'condition_preserved',
          'action_preserved', 'exception_preserved', 'unsupported_addition']

def read_csv(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def assemble(source, decisions_path, output):
    rows = read_csv(source); decisions = {}
    for line in Path(decisions_path).read_text().splitlines():
        if not line or line.startswith('#'): continue
        rid, sig, errors, uncertainty, note = line.split('\t')
        assert rid not in decisions and len(sig) == 6 and set(sig) <= set('01N'), rid
        assert note.strip() and uncertainty in ('none', 'scope', 'wording'), rid
        decisions[rid] = sig, errors, uncertainty, note
    assert set(decisions) == {r['review_id'] for r in rows}, 'Missing or extra explicit decisions'
    for r in rows:
        sig, errors, uncertainty, note = decisions[r['review_id']]
        r.update({f: 'NA' if v == 'N' else v for f, v in zip(FIELDS, sig)})
        for f, g in [('condition_preserved', 'gold_condition'), ('exception_preserved', 'gold_exception')]:
            assert (r[f] == 'NA') == (not r[g]), r['review_id']
        assert all(r[f] != 'NA' for f in (FIELDS[0], FIELDS[1], FIELDS[3], FIELDS[5]))
        r['complete_preservation'] = str(int(all(r[f] in ('1', 'NA') for f in FIELDS[:5]) and r[FIELDS[5]] == '0'))
        assert (errors == '-') == (r['complete_preservation'] == '1'), r['review_id']
        r.update(error_codes='' if errors == '-' else errors, review_uncertainty=uncertainty, reviewer_note=note)
    assert not Path(output).exists(), 'Do not overwrite an existing assembled review'
    with Path(output).open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(json.dumps({'rows': len(rows), 'output': str(output)}))

if __name__ == '__main__':
    if sys.argv[1] == 'read':
        for r in read_csv(sys.argv[2])[int(sys.argv[3])-1:int(sys.argv[4])]:
            print('\n'+r['review_id']+' '+r['gold_modal_class']+' SRC '+r['source_text_en'])
            print('G '+' | '.join(k[5:]+':'+v for k,v in r.items() if k.startswith('gold_') and k!='gold_modal_class'))
            print('KO '+r['explanation_ko'])
    elif sys.argv[1] == 'assemble':
        assemble(*sys.argv[2:5])
