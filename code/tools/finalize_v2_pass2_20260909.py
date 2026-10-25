"""Validate and seal pass 2 before any comparison. Semantic decisions are manual inputs."""
import argparse, collections, csv, datetime, hashlib, json
from pathlib import Path
import prepare_v2_review_package_20260908 as v2
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'outputs/review/v2_pass2_20260909'
OUT=ROOT/'outputs/review/v2_pass2_completed_20260909'
P1=ROOT/'outputs/review/v2_pass1_20260908/seal'
PF=ROOT/'outputs/review/v2_preflight_20260908/preflight_completed.jsonl'
SEAL=OUT/'seal'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def lines(p):return [json.loads(x) for x in p.read_text().splitlines()]
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def write_lines(p,x):p.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in x))
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def validate(rows):
 release=read(BASE/'release_manifest.json');old=read(P1/'completion_manifest.json')
 assert sha(P1/'completion_manifest.json')==release['pass1_completion_manifest_sha256']
 for f,h in old['file_sha256'].items():assert sha(P1/f)==h
 for f,h in release['file_sha256'].items():assert sha(BASE/f)==h
 assert release['package_manifest_sha256']==sha(v2.PACKAGE/'package_manifest.json')
 v2.delay_gate(old['completed_at'],v2.timestamp(release['released_at']))
 package=v2.verify_package(v2.PACKAGE)
 refs,_,packets,keys,_=v2.materials();p=packets['pass2'];pf=lines(PF);v2.check_preflight(pf,refs)
 assert lines(BASE/'packets.jsonl')==p
 assert len(rows)==255 and [r['review_id'] for r in rows]==[x['review_id'] for x in p]
 assert collections.Counter(r['reference_id'] for r in rows)=={r['reference_id']:5 for r in pf}
 # Reuse the frozen structural checker with a temporary pass label only; no decisions inferred.
 adapted=[dict(r,review_pass='pass1') for r in rows];v2.check_pass1(adapted,p,pf)
 byref={r['reference_id']:r for r in pf};last=v2.timestamp(release['released_at'])
 for r,x in zip(rows,p):
  assert r['review_pass']=='pass2' and r['packet_sha256']==v2.digest(x)
  t=v2.timestamp(r['reviewed_at']);assert t>=last;last=t
  g=byref[r['reference_id']]
  for k in ['source_provenance','propositions_and_relations','input_context_gap']:assert r[k]==g[k]
  assert r['reason_codes'] and len(r['rationale'])>15
  q=r['response_evidence_quote']
  assert q and q in x['explanation_ko'] if x['delivery_status']=='EXPLANATION' else q=='NO_RESPONSE'
 return package,pf,p,keys['pass2'],release

def seal():
 assert not SEAL.exists(),'Never overwrite an existing seal'
 rows=lines(OUT/'judgments_working.jsonl');package,pf,packets,keys,release=validate(rows)
 # All manual rows are complete before record hashes are attached. No old judgments read here.
 bound=[]
 for r,k in zip(rows,keys):
  assert r['review_id']==k['review_id'] and r['packet_sha256']==k['packet_sha256']
  bound.append(dict(r,response_record_sha256=k['response_binding']['record_sha256']))
 SEAL.mkdir()
 write_lines(SEAL/'pass2_completed.jsonl',bound);write_lines(SEAL/'preflight_completed.jsonl',pf)
 manifest={'status':'PASS2_SEALED_ADJUDICATION_PENDING','completed_at':now(),'release_manifest_sha256':sha(BASE/'release_manifest.json'),'pass1_completion_manifest_sha256':release['pass1_completion_manifest_sha256'],'package_manifest_sha256':release['package_manifest_sha256'],'rubric_sha256':sha(v2.RUBRIC),'file_sha256':{p.name:sha(p) for p in sorted(SEAL.glob('*.jsonl'))},'support_file_sha256':{str(p.relative_to(ROOT)):sha(p) for p in [Path(__file__).resolve(),ROOT/'tools/v2_pass2_workbench_20260909.py']},'reviewer_independence':'Same evaluator; prior conversation exposure; condition labels and pass1 decisions not read during current pass2 scoring; not fully blind or independent.','new_model_generation_calls':0}
 write(SEAL/'completion_manifest.json',manifest)
 for p in SEAL.iterdir():p.chmod(0o444)
 print(json.dumps({'status':manifest['status'],'completed_at':manifest['completed_at'],'rows':len(rows),'frozen_files_unchanged':package['frozen_files_unchanged'],'package_files_verified':package['package_files_verified']},ensure_ascii=False))

def verify():
 m=read(SEAL/'completion_manifest.json')
 assert m['status']=='PASS2_SEALED_ADJUDICATION_PENDING'
 assert m['release_manifest_sha256']==sha(BASE/'release_manifest.json')
 for f,h in m['file_sha256'].items():assert sha(SEAL/f)==h
 for f,h in m['support_file_sha256'].items():assert sha(ROOT/f)==h
 rows=lines(SEAL/'pass2_completed.jsonl');_,pf,_,keys,_=validate(rows)
 assert lines(SEAL/'preflight_completed.jsonl')==pf
 for r,k in zip(rows,keys):assert r['response_record_sha256']==k['response_binding']['record_sha256']
 assert v2.timestamp(m['completed_at'])>=max(v2.timestamp(r['reviewed_at']) for r in rows)
 print(json.dumps({'ok':True,'status':m['status'],'rows':len(rows)},ensure_ascii=False))
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('command',choices=['seal','verify']);args=a.parse_args();{'seal':seal,'verify':verify}[args.command]()
