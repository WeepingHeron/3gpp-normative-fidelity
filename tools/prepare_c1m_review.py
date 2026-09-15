"""Prepare fresh, entirely blank review data; never reuse previous scores."""
import csv,hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
from verify_c1m_run import verify,lines,sha,ROOT
def main():
 p=Path(sys.argv[1]).resolve();verify(p,p/'output_freeze_manifest.json')
 m=json.loads((p/'manifest.json').read_text());assert m['processed_cases']==72
 mainrun=ROOT/'experiments/runs/main72_v3_2026-09-03T07-35-49-603Z'
 verify(mainrun,mainrun/'output_freeze_manifest.json')
 with (ROOT/'data/main_cases.csv').open(encoding='utf-8-sig') as f:gold={r['case_id']:r for r in csv.DictReader(f)}
 allrows=[r for r in lines(mainrun/'parsed_responses.jsonl') if r['condition'] in ('C1','C2')]+lines(p/'parsed_responses.jsonl')
 assert len(allrows)==216 and len({(r['case_id'],r['condition']) for r in allrows})==216
 allrows.sort(key=lambda r:hashlib.sha256(('C1M-review-v1:'+r['case_id']+':'+r['condition']).encode()).hexdigest())
 out=p/'review';out.mkdir(exist_ok=False);rows=[];key={}
 for i,r in enumerate(allrows,1):
  rid=f'M{i:03d}';g=gold[r['case_id']];key[rid]={'case_id':r['case_id'],'condition':r['condition']}
  rows.append({'review_id':rid,'source_text_en':g['source_text_en'],'question_ko':g['question_ko'],
    **{'gold_'+f:g[f] for f in ['modal_class','actor','condition','action','exception']},
    'explanation_ko':(r['parsed'] or {}).get('explanation_ko',''),
    **{f:'' for f in ['actor_preserved','polarity_preserved','condition_preserved','action_preserved','exception_preserved','unsupported_addition','complete_preservation','error_codes','reviewer_note']}})
 with (out/'blind_explanations_blank.csv').open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 (out/'blind_key.json').write_text(json.dumps(key,indent=2)+'\n')
 (out/'review_manifest.json').write_text(json.dumps({'status':'BLANK_NOT_REVIEWED','created_at':datetime.now(timezone.utc).isoformat(),'rows':216,'conditions':['C1','C2','C1M'],
  'limitation':'Current Codex knows previous experiment results; masked rows are not independent expert validation.',
  'file_sha256':{f.name:sha(f) for f in out.iterdir()}},indent=2)+'\n')
 print('Prepared 216 blank C1/C2/C1M review rows; no semantic scores assigned.')
if __name__=='__main__':main()
