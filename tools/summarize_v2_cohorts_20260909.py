"""Frozen-cohort descriptive bounds from adjudicated v2 outcomes; no new scoring."""
import argparse,collections,csv,datetime,hashlib,itertools,json,sqlite3
from pathlib import Path
import adjudicate_v2_disagreements_20260909 as adj
ROOT=adj.ROOT;OUT=ROOT/'outputs/review/v2_cohort_analysis_20260909';DOC=ROOT/'docs/28_v2_cohort_results_2026-09-09.md'
read,lines,write,write_lines,sha=adj.read,adj.lines,adj.write,adj.write_lines,adj.sha
PROTOCOL=ROOT/'experiments/posthoc_treatment_v1_20260908/protocol.json'
STATES=['PASS','FAIL','UNRESOLVED','NOT_SCORED']

def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def load():
 adj.verify();p=read(PROTOCOL);package=adj.prior.p2.v2.PACKAGE
 assert read(package/'coordinator/cohorts.json')==p['cohorts']
 rows=lines(adj.OUT/'adjudicated_view_255.jsonl');keys=read(package/'coordinator/keys.json')['pass2'];packets={r['review_id']:r for r in lines(adj.prior.p2.BASE/'packets.jsonl')}
 byid={k['review_id']:k for k in keys};assert len(byid)==255==len(rows)
 slots=[]
 for r in rows:
  k=byid[r['review_id']];src=packets[r['review_id']]['source']
  assert r['response_record_sha256']==k['response_binding']['record_sha256'] and r['reference_id']==k['reference_id']
  assert r['semantic_judgment'] in STATES
  value={'PASS':1,'FAIL':0,'UNRESOLVED':None,'NOT_SCORED':0}[r['semantic_judgment']]
  assert type(r['complete_preservation']) is type(value) and r['complete_preservation']==value
  memberships=[n for n,c in p['cohorts'].items() if k['case_id'] in c['case_ids']];assert memberships==k['cohorts']
  slots.append({'case_id':k['case_id'],'condition':k['condition'],'review_id':r['review_id'],'reference_id':r['reference_id'],'response_record_sha256':r['response_record_sha256'],'adjudicated_record_sha256':adj.prior.p2.v2.digest(r),'semantic_judgment':r['semantic_judgment'],'complete_preservation':value,'gold_status':r['gold_status'],'delivery_status':r['delivery_status'],'spec_id':src['spec_id'],'clause_id':src['clause_id'],'cluster_key':src['spec_id']+'|'+src['clause_id'],'cohorts':memberships})
 assert len({(r['case_id'],r['condition']) for r in slots})==255
 assert len({r['response_record_sha256'] for r in slots})==255
 union=set().union(*(set(c['case_ids']) for c in p['cohorts'].values()))
 assert len(union)==51 and {(r['case_id'],r['condition']) for r in slots}==set(itertools.product(union,p['conditions']))
 for n,c in p['cohorts'].items():assert len(c['case_ids'])==len(set(c['case_ids']))==c['n'] and c['conditions']==p['conditions']
 return p,sorted(slots,key=lambda r:(r['case_id'],p['conditions'].index(r['condition'])))
def compute(p,slots):
 condition_rows=[];pair_rows=[];paired=[];idx={(r['case_id'],r['condition']):r for r in slots}
 comparisons=[p['primary_comparison']]+p['exploratory_comparisons']
 for name,c in p['cohorts'].items():
  n=c['n'];caseids=sorted(c['case_ids']);clusters={idx[(cid,p['conditions'][0])]['cluster_key'] for cid in caseids}
  cr={}
  for cond in p['conditions']:
   rr=[idx[(cid,cond)] for cid in caseids];count=collections.Counter(r['semantic_judgment'] for r in rr)
   assert sum(count.values())==n
   cr[cond]={'cohort':name,'condition':cond,'n':n,**{s:count[s] for s in STATES},'lower_numerator':count['PASS'],'upper_numerator':count['PASS']+count['UNRESOLVED'],'lower_rate':count['PASS']/n,'upper_rate':(count['PASS']+count['UNRESOLVED'])/n,'bound_kind':'LOGICAL_OUTER_BOUNDS_NOT_CONFIDENCE_INTERVAL','clause_clusters':len(clusters),'wilson95':None,'interval_status':'NOT_REPORTED_DESCRIPTIVE_BASELINE' if cond=='C0' else 'DEFERRED_UNRESOLVED','pipeline_failures_in_denominator':count['NOT_SCORED']}
   condition_rows.append(cr[cond])
  for spec in comparisons:
   ac,bc=spec['first'],spec['second'];a,b=cr[ac],cr[bc];cells=collections.Counter();uncertain=[];dlo=dhi=0
   for cid in caseids:
    x,y=idx[(cid,ac)],idx[(cid,bc)];cells[(x['semantic_judgment'],y['semantic_judgment'])]+=1
    xv=x['complete_preservation'];yv=y['complete_preservation'];lo=(0 if yv is None else yv)-(1 if xv is None else xv);hi=(1 if yv is None else yv)-(0 if xv is None else xv);dlo+=lo;dhi+=hi
    if xv is None or yv is None:uncertain.append(cid)
    paired.append({'cohort':name,'case_id':cid,'first':ac,'second':bc,'first_state':x['semantic_judgment'],'second_state':y['semantic_judgment'],'first_record_sha256':x['response_record_sha256'],'second_record_sha256':y['response_record_sha256'],'difference_lower':lo,'difference_upper':hi,'cluster_key':x['cluster_key']})
   assert dlo==b['PASS']-a['PASS']-a['UNRESOLVED'] and dhi==b['PASS']+b['UNRESOLVED']-a['PASS']
   # Current frozen dataset has U in all specified comparisons. Do not silently invent an inference implementation.
   assert uncertain,'A comparison without U requires the frozen inferential pipeline before release'
   pair_rows.append({'cohort':name,'first':ac,'second':bc,'direction':bc+' minus '+ac,'comparison_role':'POSTHOC_PRIMARY' if name==p['primary_comparison']['cohort'] and (ac,bc)==('C1','C2') else 'POSTHOC_SENSITIVITY_OR_EXPLORATORY','n':n,'first_pass':a['PASS'],'first_unresolved':a['UNRESOLVED'],'second_pass':b['PASS'],'second_unresolved':b['UNRESOLVED'],'unresolved_pair_count':len(uncertain),'unresolved_case_ids':uncertain,'lower_difference_numerator':dlo,'upper_difference_numerator':dhi,'lower_difference':dlo/n,'upper_difference':dhi/n,'lower_pp':100*dlo/n,'upper_pp':100*dhi/n,'direction_across_allowed_assignments':'SECOND_HIGHER_WITHIN_REVIEWED_COHORT' if dlo>0 else 'FIRST_HIGHER_WITHIN_REVIEWED_COHORT' if dhi<0 else 'ORDER_NOT_FIXED','clause_clusters':len(clusters),'state_pair_counts':[{'first_state':x,'second_state':y,'count':v} for (x,y),v in sorted(cells.items())],'statistical_status':'DEFERRED_UNRESOLVED','exact_mcnemar_p':None,'case_bootstrap95':None,'cluster_bootstrap95':None})
 return condition_rows,pair_rows,paired

def build():
 assert not OUT.exists(),'Never overwrite a completed analysis directory';p,slots=load();cr,pr,paired=compute(p,slots);OUT.mkdir()
 write_lines(OUT/'bound_slots_255.jsonl',slots);write_lines(OUT/'condition_results.jsonl',cr);write_lines(OUT/'paired_results.jsonl',pr);write_lines(OUT/'paired_cases.jsonl',paired)
 adj.prior.csvwrite(OUT/'condition_results.csv',cr,['cohort','condition','n']+STATES+['lower_numerator','upper_numerator','lower_rate','upper_rate','bound_kind','clause_clusters','interval_status'])
 adj.prior.csvwrite(OUT/'paired_results.csv',pr,['cohort','first','second','n','first_pass','first_unresolved','second_pass','second_unresolved','unresolved_pair_count','lower_pp','upper_pp','direction_across_allowed_assignments','statistical_status'])
 extras=[r for r in slots if r['case_id'] in {'MAIN-MAY-001','MAIN-SDN-011'}];write_lines(OUT/'sensitivity_added_cases.jsonl',extras)
 summ={'status':'COHORT_BOUNDS_COMPLETE_INFERENCE_DEFERRED','generated_at':now(),'treatment_version':p['version'],'unique_cases':51,'unique_response_slots':255,'condition_result_rows':len(cr),'paired_result_rows':len(pr),'paired_case_memberships':len(paired),'cohort_case_counts':{k:c['n'] for k,c in p['cohorts'].items()},'inference_deferred_comparisons':len(pr),'cohorts_overlap':True,'uncertainty_intervals_are_confidence_intervals':False,'semantic_judgments_changed':0,'new_model_generation_calls':0,'paper_updated':False,'independent_expert_validation':False}
 write(OUT/'summary.json',summ)
 print(json.dumps({'conditions':cr,'comparisons':[{k:r[k] for k in ['cohort','direction','lower_pp','upper_pp','clause_clusters','statistical_status']} for r in pr]},ensure_ascii=False,indent=2))

def validate():
 p,slots=load();cr,pr,paired=compute(p,slots)
 assert lines(OUT/'bound_slots_255.jsonl')==slots and lines(OUT/'condition_results.jsonl')==cr and lines(OUT/'paired_results.jsonl')==pr and lines(OUT/'paired_cases.jsonl')==paired
 # Independent SQLite aggregation uses protocol memberships and frozen adjudicated rows via coordinator case binding.
 conn=sqlite3.connect(':memory:');conn.execute('CREATE TABLE results(cid TEXT, cond TEXT, state TEXT, PRIMARY KEY(cid,cond))');conn.execute('CREATE TABLE membership(cohort TEXT,cid TEXT,PRIMARY KEY(cohort,cid))')
 keys=read(adj.prior.p2.v2.PACKAGE/'coordinator/keys.json')['pass2'];byhash={k['response_binding']['record_sha256']:k for k in keys}
 raw=lines(adj.OUT/'adjudicated_view_255.jsonl')
 conn.executemany('INSERT INTO results VALUES(?,?,?)',[(byhash[r['response_record_sha256']]['case_id'],byhash[r['response_record_sha256']]['condition'],r['semantic_judgment']) for r in raw]);conn.executemany('INSERT INTO membership VALUES(?,?)',[(name,cid) for name,c in p['cohorts'].items() for cid in c['case_ids']])
 sql={(n,cond,s):v for n,cond,s,v in conn.execute('SELECT m.cohort,r.cond,r.state,count(*) FROM membership m JOIN results r ON m.cid=r.cid GROUP BY m.cohort,r.cond,r.state')}
 for r in cr:
  for state in STATES:assert r[state]==sql.get((r['cohort'],r['condition'],state),0)
 # Exhaustive U assignments verify pair-difference extrema without using the aggregate formula.
 for r in pr:
  records=[x for x in paired if x['cohort']==r['cohort'] and x['first']==r['first'] and x['second']==r['second']];known=0;signs=[]
  for x in records:
   for sign,state in [(-1,x['first_state']),(1,x['second_state'])]:
    if state=='UNRESOLVED':signs.append(sign)
    elif state=='PASS':known+=sign
  values=[known+sum(s*v for s,v in zip(signs,bits)) for bits in itertools.product([0,1],repeat=len(signs))]
  assert min(values)==r['lower_difference_numerator'] and max(values)==r['upper_difference_numerator']
  assert r['exact_mcnemar_p'] is None and r['case_bootstrap95'] is None and r['cluster_bootstrap95'] is None
 assert sum(r['PASS'] for r in cr if r['cohort']=='SENS_GOLD_EXCEPTION_51')==167
 # No one-sided complete-case filtering or denominator migration.
 assert all(sum(r[s] for s in STATES)==r['n'] and 0<=r['lower_rate']<=r['upper_rate']<=1 for r in cr)
 for name,c in p['cohorts'].items():
  for cond in p['conditions']:assert {r['case_id'] for r in slots if r['condition']==cond and name in r['cohorts']}==set(c['case_ids'])
 return {'ok':True,'assessment':'Share with caveats','checks':['prior sealed artifacts and frozen protocol hashes','255 unique response-record joins with no drop or expansion','four exact case masks applied to all five conditions','independent SQLite counts for all 20 result rows','all 16 pair bounds verified by exhaustive unresolved assignments','NOT_SCORED counted in denominator and U retained null','case-paired trace for 800 overlapping memberships','all affected inferential outputs withheld'],'semantic_truth_automatically_verified':False,'verified_at':now()}
def finish():
 assert DOC.exists() and not (OUT/'completion_manifest.json').exists();receipt=validate();write(OUT/'validation_report.json',receipt)
 write(OUT/'completion_manifest.json',{'status':'COHORT_BOUNDS_COMPLETE_INFERENCE_DEFERRED','completed_at':now(),'file_sha256':{str(p.relative_to(OUT)):sha(p) for p in sorted(OUT.iterdir()) if p.is_file()},'support_file_sha256':{str(p.relative_to(ROOT)):sha(p) for p in [DOC,Path(__file__).resolve()]},'input_file_sha256':{str(p.relative_to(ROOT)):sha(p) for p in [PROTOCOL,adj.OUT/'completion_manifest.json',adj.OUT/'adjudicated_view_255.jsonl',adj.prior.p2.v2.PACKAGE/'coordinator/keys.json']}})
 for p in OUT.iterdir():p.chmod(0o444)
def verify():
 m=read(OUT/'completion_manifest.json')
 for rel,h in m['file_sha256'].items():assert sha(OUT/rel)==h
 for rel,h in {**m['support_file_sha256'],**m['input_file_sha256']}.items():assert sha(ROOT/rel)==h
 print(json.dumps(validate(),ensure_ascii=False))
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('command',choices=['build','finish','verify']);v=a.parse_args();{'build':build,'finish':finish,'verify':verify}[v.command]()
