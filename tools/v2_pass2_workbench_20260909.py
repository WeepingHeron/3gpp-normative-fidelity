"""Pass 2 evidence workbench. Never infers semantic decisions or reads pass 1."""
import argparse, datetime, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'outputs/review/v2_pass2_20260909'
OUT=ROOT/'outputs/review/v2_pass2_completed_20260909'
def read(p): return [json.loads(x) for x in p.read_text().splitlines()]
def sha(x): return hashlib.sha256(x).hexdigest()
def canonical(x): return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
def main():
 a=argparse.ArgumentParser();a.add_argument('command',choices=['show','record']);a.add_argument('start',type=int,nargs='?',default=1);a.add_argument('end',type=int,nargs='?',default=25);a.add_argument('--input');v=a.parse_args()
 packets=read(BASE/'packets.jsonl');blank=read(BASE/'judgments_blank.jsonl');refs={x['reference_id']:x for x in read(ROOT/'outputs/review/v2_preflight_20260908/preflight_completed.jsonl')}
 if v.command=='show':
  for p in packets[v.start-1:v.end]:
   r=refs[p['reference_id']]
   print('\n'+p['review_id']+' '+p['reference_id']+' '+r['gold_status']+'\nSOURCE '+p['source']['source_text_en']+'\nQ '+p['question_ko']+'\nANSWER '+(p['explanation_ko'] or '[NOT_GENERATED]'))
  return
 OUT.mkdir(exist_ok=True);path=OUT/'judgments_working.jsonl';rows=read(path) if path.exists() else [];new=[]
 for line in Path(v.input).read_text().splitlines():
  n,state,codes,rationale,quote=line.split('\t');i=int(n)-1;p=packets[i];r=refs[p['reference_id']];b=blank[i].copy()
  assert i==len(rows)+len(new),(i,len(rows),len(new))
  assert state in ['PASS','FAIL','UNRESOLVED','NOT_SCORED']
  assert len(rationale)>15 and (quote and quote in p['explanation_ko'] if p['delivery_status']=='EXPLANATION' else quote=='NO_RESPONSE')
  assert (state=='NOT_SCORED')==(p['delivery_status']!='EXPLANATION')
  assert r['gold_status']!='UNRESOLVED' or state in ['UNRESOLVED','FAIL','NOT_SCORED']
  if r['gold_status']=='UNRESOLVED' and state=='FAIL': assert 'INDEPENDENT_CLEAR_ERROR' in codes
  b.update(reviewer='Codex (same study evaluator; not independent domain expert)',reviewed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),semantic_judgment=state,complete_preservation={'PASS':1,'FAIL':0,'UNRESOLVED':None,'NOT_SCORED':0}[state],gold_status=r['gold_status'],reason_codes=codes.split('|'),rationale=rationale,response_evidence_quote=quote,source_provenance=r['source_provenance'],propositions_and_relations=r['propositions_and_relations'],input_context_gap=r['input_context_gap'],packet_sha256=sha(canonical(p)))
  new.append(b)
 assert new
 with path.open('a') as f:
  for b in new:f.write(json.dumps(b,ensure_ascii=False)+'\n')
 print('Recorded',len(new),'total',len(rows)+len(new))
if __name__=='__main__':main()
