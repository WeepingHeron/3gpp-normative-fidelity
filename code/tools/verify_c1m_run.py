"""Read-only, independent validation of the modal-only ablation run."""
import csv, hashlib, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TYPES={'shall':'obligation','shall_not':'prohibition','should':'recommendation','should_not':'discouragement','may':'permission','can':'capability'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def lines(p):return [json.loads(s) for s in p.read_text().splitlines() if s]
def verify(base,manifest):
 for n,h in json.loads(manifest.read_text())['file_sha256'].items():assert sha(base/n)==h,n
def main():
 p=Path(sys.argv[1]).resolve();m=json.loads((p/'manifest.json').read_text())
 verify(ROOT,p/'input_freeze_manifest.json');verify(p,p/'output_freeze_manifest.json')
 verify(ROOT,ROOT/'data/main_freeze_manifest.json')
 assert m['status']=='generation_complete_semantics_pending' and m['processed_cases']==72
 with (ROOT/'data/main_cases.csv').open(encoding='utf-8-sig') as f:g={r['case_id']:r for r in csv.DictReader(f)}
 projected=lines(p/'projected_inputs.jsonl');requests=lines(p/'requests.jsonl');raw=lines(p/'raw_responses.jsonl');parsed=lines(p/'parsed_responses.jsonl')
 assert {r['case_id'] for r in parsed}==set(g) and len(parsed)==72
 assert len(requests)==len(raw)==m['attempts']
 base=(ROOT/'experiments/prompts/c1_v2.md').read_text()
 template=base.replace('## 출처 식별자','## 규범 유형 힌트\n\n- normative_type: {{normative_type}}\n- polarity: {{polarity}}\n\n## 출처 식별자')
 assert (p/'prompt_template.md').read_text()==template
 bycase={r['case_id']:r for r in projected};last={};cost=0
 for req,res in zip(requests,raw):
  assert (req['case_id'],req['attempt'])==(res['case_id'],res['attempt'])
  cid=req['case_id'];r=g[cid]
  variables={k:r[k] for k in ['source_text_en','question_ko','spec_id','version','clause_id']}
  variables.update(normative_type=TYPES[r['modal_class']],polarity=r['polarity'])
  expected=re.sub(r'{{([a-z_]+)}}',lambda mt:variables[mt[1]],template)
  assert bycase[cid]['input']==variables and bycase[cid]['prompt']==expected
  request=req['request'];assert request['input']==expected
  assert hashlib.sha256(json.dumps(request,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()==req['request_sha256']
  assert request['model']==m['model'] and request['store'] is False
  assert request['temperature']==0 and request['reasoning']=={'effort':'none'} and request['max_output_tokens']==600
  assert request['text']['format']['schema']==json.loads((ROOT/'experiments/response_schema.json').read_text())
  if res['http_status']==200:
   b=res['response'];assert b['model']==m['model'];u=b['usage'];cached=u.get('input_tokens_details',{}).get('cached_tokens',0)
   assert 0<=cached<=u['input_tokens'] and u['output_tokens']>=0
   cost+=((u['input_tokens']-cached)*.75+cached*.075+u['output_tokens']*4.5)/1e6
   last[cid]=b
 for row in parsed:
  b=last[row['case_id']];assert row['response_id']==b['id'] and row['usage']==b['usage']
  if row['parsed'] is not None:
   assert b['status']=='completed'
   content=[x for msg in b['output'] if msg['type']=='message' for x in msg.get('content',[])]
   assert not any(x['type']=='refusal' for x in content)
   direct=json.loads(''.join(x['text'] for x in content if x['type']=='output_text'))
   assert direct==row['parsed']
 assert abs(cost-m['estimated_cost_usd'])<1e-10
 diagnostics={'status':'PASS_GENERATION_INTEGRITY_ONLY','cases':72,'attempts':len(requests),
  'parsed':sum(r['parsed'] is not None for r in parsed),
  'JSON_modal_correct':sum((r['parsed'] or {}).get('normative_type')==TYPES[g[r['case_id']]['modal_class']] for r in parsed),
  'citation_ID_correct':sum(bool(r['parsed']) and all(r['parsed'][a]==g[r['case_id']][b] for a,b in [('citation_spec','spec_id'),('citation_version','version'),('citation_clause','clause_id')]) for r in parsed),
  'estimated_cost_usd':cost,'actual_prompt_projection':'PASS_MODAL_AND_POLARITY_ONLY_ADDED',
  'meaning_preservation':'NOT_EVALUATED'}
 print(json.dumps(diagnostics,indent=2))
if __name__=='__main__':main()
