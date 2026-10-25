"""Assemble manually authored source/gold judgments; no automatic semantic decisions or API calls."""
import csv
import hashlib
import importlib.util
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'outputs/review/v2_20260908'
OUT=ROOT/'outputs/review/v2_preflight_20260908'
FREEZE=ROOT/'experiments/posthoc_treatment_v1_20260908'

def read(p):return json.loads(p.read_text(encoding='utf-8'))
def lines(p):return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip()]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(obj):return hashlib.sha256(json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def norm(s):return re.sub(r'[^a-z0-9]','',s.lower())
def write(p,value):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def csvout(p,rows):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def reference_evidence(ref, quote, location, page=None, clause=None):
 return {'quote':quote,'spec_id':ref['source']['spec_id'],'version':ref['source']['version'],
         'clause_id':clause or ref['source']['clause_id'],'pdf_page':page or ref['pdf']['pdf_page'],
         'evidence_location':location,'provenance':{'reference_source':'supplied_source','reference_question':'supplied_question_context','adjudication_only_context':'adjudication_only_context'}[location],
         'model_availability':'REFERENCE_ROLE_ONLY; actual per-stage availability is in coordinator/input_provenance.json',
         'available_to_extractor':False if location=='adjudication_only_context' else 'CONDITION_AND_STAGE_SPECIFIC',
         'available_to_generator':False if location=='adjudication_only_context' else 'CONDITION_AND_STAGE_SPECIFIC'}

# Additional evidence chosen manually after PDF review. These quotes are not model input.
EXTRA={
 'G023':[
  (1090,'C.1','The following 5GMM parameters should be stored in a non-volatile memory in the ME together with the SUPI from the USIM: - allowed NSSAI(s); and - partially allowed NSSAI(s).'),
  (1091,'C.1','If the UE is registered for emergency services, the UE shall not store the 5GMM parameters described in this annex on the USIM or in non-volatile memory.'),
  (1091,'C.1','Instead the UE shall temporarily store these parameters locally in the ME and the UE shall delete these parameters when the UE is deregistered from emergency services (e.g. before registering for normal service).'),
  (1091,'C.1','If the UE is configured for eCall only mode as specified in 3GPP TS 31.102 [22], the UE shall not store the 5GMM parameters described in this annex on the USIM or in non-volatile memory.'),
  (1093,'C.2','The 5GMM information for UEs operating in SNPN access operation mode are stored according to the following conditions:'),
 ],
 'G024':[(133,'4.9.2','The UE should memorize the identity of the PLMN or SNPN where N1 mode capability for 3GPP access was disabled and should use that stored information in subsequent PLMN or SNPN selections as specified in 3GPP TS 23.122 [5].')],
 'G028':[(133,'5.4.11.4','In this case, when the AMF receives a NGAP message containing User Location Information for a UE using NR satellite access, the AMF takes into account the capability of the UE in UE 5GMM Core Network Capability for the support by the UE of network verified UE location over NR NTN and may decide to verify the UE location.')],
 'G042':[(56,'4.4.2.2','Establishment of a mapped 5G NAS security context during inter-system change from S1 mode to N1 mode in 5GMM-CONNECTED mode')],
 'G049':[(57,'4.4.2.3','Establishment of a 5G NAS security context during N1 mode to N1 mode handover')],
}

def input_provenance(refs, refkey):
 protocol=read(FREEZE/'protocol.json')
 with (ROOT/'data/main_cases.csv').open(encoding='utf-8-sig',newline='') as f:cases={r['case_id']:r for r in csv.DictReader(f)}
 mainbase=Path(protocol['response_files']['C0']).parent
 manifest=read(ROOT/mainbase/'manifest.json')
 type_map={'shall':'obligation','shall_not':'prohibition','should':'recommendation','should_not':'discouragement','may':'permission','can':'capability'}
 templates={c:ROOT/f'experiments/prompts/{c.lower()}_{v}.md' for c,v in manifest['prompt_file_versions'].items()}
 for c,p in templates.items():assert sha(p)==manifest['prompt_sha256'][c]
 recorded={}
 for condition in ['C3','C1M']:
  path=Path(protocol['response_files'][condition]).parent/'requests.jsonl'
  for i,row in enumerate(lines(ROOT/path),1):
   # JSON.stringify-compatible encoding of the recorded request, preserving member order.
   request_hash=hashlib.sha256(json.dumps(row['request'],ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
   assert request_hash==row['request_sha256']
   key=(row['case_id'],condition,row.get('stage','generation'))
   recorded.setdefault(key,[]).append((row,path,i))
 result=[]
 for ref in refs:
  cid=refkey[ref['reference_id']];case=cases[cid]
  for cond in protocol['conditions']:
   for stage in (['extraction','generation'] if cond=='C3' else ['generation']):
    if cond in templates:
     values={**case,'normative_type':type_map[case['modal_class']]}
     prompt=re.sub(r'{{([a-z_]+)}}',lambda m:values.get(m[1],''),templates[cond].read_text())
     entries=[(prompt,{'evidence_type':'FROZEN_RUNNER_TEMPLATE_RECONSTRUCTION','prompt_file':str(templates[cond].relative_to(ROOT)),
       'prompt_sha256':sha(templates[cond]),'runner':'experiments/run_pilot.mjs','runner_sha256':sha(ROOT/'experiments/run_pilot.mjs'),
       'run_manifest':str(mainbase/'manifest.json'),'run_manifest_sha256':sha(ROOT/mainbase/'manifest.json'),
       'limitation':'Original main run retained outputs and frozen construction inputs, not request-body logs. This is reconstruction, not captured HTTP input.'})]
    else:
     entries=[(row['request']['input'],{'evidence_type':'RECORDED_REQUEST','request_file':str(path),'request_file_sha256':sha(ROOT/path),
       'line_number':i,'attempt':row['attempt'],'request_sha256':row['request_sha256'],'request_sha256_verified':True}) for row,path,i in recorded.get((cid,cond,stage),[])]
    if not entries:
     assert (cid,cond,stage)==('MAIN-SD-002','C3','generation')
     result.append({'reference_id':ref['reference_id'],'case_id':cid,'condition':cond,'stage':stage,'status':'NOT_GENERATED',
       'evidence_type':'RECORDED_ABSTENTION_AND_ABSENT_GENERATION_REQUEST','source_supplied':False,'question_supplied':False,
       'note':'Extraction abstention is bound by the immutable review package. No generator request exists.'})
     continue
    for prompt,evidence in entries:
     source_supplied=case['source_text_en'] in prompt;question_supplied=case['question_ko'] in prompt
     assert source_supplied==(cond!='C0')
     assert question_supplied==(stage!='extraction')
     checks=[{'pdf_page':page,'clause_id':clause,'quote_sha256':hashlib.sha256(quote.encode()).hexdigest(),
       'full_evidence_quote_present':norm(quote) in norm(prompt)} for page,clause,quote in EXTRA.get(ref['reference_id'],[])]
     assert not any(x['full_evidence_quote_present'] for x in checks)
     result.append({'reference_id':ref['reference_id'],'case_id':cid,'condition':cond,'stage':stage,'status':'INPUT_BOUND',
       **evidence,'input_sha256':hashlib.sha256(prompt.encode()).hexdigest(),'source_supplied':source_supplied,'question_supplied':question_supplied,
       'additional_context_quote_checks':checks,'note':'Full-quote presence is a mechanical check; it does not establish semantic equivalence of other wording.'})
 return result


def main():
 assert not (OUT/'completion_manifest.json').exists(), 'Completed preflight is immutable; use a new version'
 spec=importlib.util.spec_from_file_location('package_tools',ROOT/'tools/prepare_v2_review_package_20260908.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 module.verify_package(PACKAGE)
 refs=lines(PACKAGE/'preflight/references.jsonl');refmap={r['reference_id']:r for r in refs}
 annotations=read(OUT/'manual_annotations.json');manual=annotations['rows']
 assert len(manual)==51 and {r['reference_id'] for r in manual}==set(refmap)
 pages=read(OUT/'source_page_evidence.json')['rows'];pagemap={(r['spec_id'],r['pdf_page']):r for r in pages}
 complete=[]
 for a in manual:
  r=refmap[a['reference_id']];s=r['source'];page=pagemap[(s['spec_id'],r['pdf']['pdf_page'])]
  assert sha(ROOT/r['pdf']['path'])==r['pdf']['sha256']==page['pdf_sha256']
  assert norm(s['source_text_en']) in norm(page['page_text'])
  row={'reference_id':a['reference_id'],'reference_sha256':digest(r),'reviewer':annotations['reviewer'],'reviewed_at':a['reviewed_at'],
       'treatment_version':'posthoc_treatment_v1_20260908','rubric_sha256':sha(ROOT/'experiments/scoring_v2_frozen_20260908.md'),
       'gold_status':a['gold_status'],'propositions_and_relations':[],
       'source_provenance':[reference_evidence(r,s['source_text_en'],'reference_source'),reference_evidence(r,r['question_ko'],'reference_question')],
       'input_context_gap':a['input_context_gap'],'proposed_errata':a['proposed_errata'],'rationale':a['rationale'],'field_advisory':a['field_advisory'],
       'question_review':'Question premise checked against source and PDF context; see rationale and proposition conditions.',
       'judgment_scope':'Source/gold preflight only; not a model-response semantic judgment; SOURCE_SUPPORTED uses frozen rubric plus source propositions, not an endorsement of every flat gold field.',
       'additional_context_role':'Adjudication-only material; not retroactively supplied to original models.'}
  for i,p in enumerate(a['propositions_and_relations'],1):
   row['propositions_and_relations'].append({**p,'proposition_id':f"{a['reference_id']}-P{i:02d}",'evidence_quote':s['source_text_en'],'evidence_location':'reference_source','scoring_role':'SOURCE_REQUIREMENT'})
  for n,clause,quote in EXTRA.get(a['reference_id'],[]):
   assert norm(quote) in norm(pagemap[(s['spec_id'],n)]['page_text']), (a['reference_id'],n,quote)
   row['source_provenance'].append(reference_evidence(r,quote,'adjudication_only_context',n,clause))
  complete.append(row)
 module.check_preflight(complete,refs)
 (OUT/'preflight_completed.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in complete))
 # CSV is an index, not a replacement for the full structured provenance record.
 csvout(OUT/'preflight_index.csv',[{k:r[k] for k in ['reference_id','gold_status','input_context_gap','reviewed_at','rationale','field_advisory']} for r in complete])
 key=read(PACKAGE/'coordinator/reference_key.json')
 inputs=input_provenance(refs,key)
 write(OUT/'coordinator/input_provenance.json',{'rows':inputs,'counts':dict(Counter(r['evidence_type'] for r in inputs)),
       'scope':'Original source/question and selected additional context availability; no model outputs or previous scores are used for manual judgments.'})
 summaryrows=[{'reference_id':r['reference_id'],'case_id':key[r['reference_id']],'gold_status':r['gold_status'],'input_context_gap':r['input_context_gap'],'rationale':r['rationale']} for r in complete]
 csvout(OUT/'coordinator/case_index.csv',summaryrows)
 states={key[r['reference_id']]:r['gold_status'] for r in complete}
 protocol=read(FREEZE/'protocol.json')
 summary={'status':'PREFLIGHT_COMPLETE_WITH_UNRESOLVED','references_reviewed':len(complete),'gold_status_counts':dict(Counter(r['gold_status'] for r in complete)),
  'input_context_gap_counts':dict(Counter(r['input_context_gap'] for r in complete)),
  'unresolved_reference_ids':[r['reference_id'] for r in complete if r['gold_status']=='UNRESOLVED'],
  'unresolved_case_ids':[key[r['reference_id']] for r in complete if r['gold_status']=='UNRESOLVED'],
  'cohorts':{name:{'frozen_n':co['n'],'gold_status_counts':dict(Counter(states[cid] for cid in co['case_ids']))} for name,co in protocol['cohorts'].items()},
  'primary_source_pages_visually_reviewed':38,'additional_annex_pages_visually_reviewed':5,
  'reference_proposition_count':sum(len(r['propositions_and_relations']) for r in complete),
  'new_model_calls':0,'semantic_reviews_completed':0,'cohort_membership_changes':0,'original_gold_changes':0,
  'ready_for_pass1_recording':True,'unresolved_handling':'Keep all frozen case masks. UNRESOLVED gold cannot yield PASS; an independently clear error may justify FAIL with evidence. No response outcome is assigned by preflight.'}
 write(OUT/'summary.json',summary)
 print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
