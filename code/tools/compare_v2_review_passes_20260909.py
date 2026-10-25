"""Post-seal comparison and reviewable exports. No adjudication or condition effect estimates."""
import argparse, collections, csv, datetime, hashlib, json, subprocess, sys
from pathlib import Path
import finalize_v2_pass2_20260909 as p2
ROOT=p2.ROOT;OUT=p2.OUT;DOC=ROOT/'docs/26_v2_semantic_review_pass2_2026-09-09.md'
read,lines,sha,write,write_lines=p2.read,p2.lines,p2.sha,p2.write,p2.write_lines
QUESTIONS={
 'V2-P2-019':'마지막 조건이라는 말은 목적의 재언급인가, 적용 범위를 좁히는 새로운 필요조건인가?',
 'V2-P2-070':'능력이 있을 수 있다는 선택성이 뒤의 기술적 가능성 부연에도 유지되는가? R1의 범위 보존과 유형 명칭을 어떻게 함께 적용할 것인가?',
 'V2-P2-099':'수신 엔티티가 무결성 검사를 받았다는 명시적 주어를 메시지 검사로 읽을 수 있는가? 문법과 전문 독자의 복원을 구분해 판단한다.',
 'V2-P2-106':'이는 허용 또는 선택 가능이라는 부연의 지시 대상이 불분명할 때 R3의 UNRESOLVED인가, 보유 확정의 명백한 FAIL인가?',
 'V2-P2-151':'뒤의 검사 성공 시에만 처리 가능이라는 문장이 앞의 entity 검사 대상 오류를 실제로 정정하는가? 099와 함께 대칭 검토한다.'}
def data():
 p2.verify()
 a=lines(p2.P1/'pass1_completed.jsonl');b=lines(p2.SEAL/'pass2_completed.jsonl');packets=lines(p2.BASE/'packets.jsonl')
 byhash={r['response_record_sha256']:r for r in a};assert len(byhash)==255
 assert {r['response_record_sha256'] for r in b}==set(byhash)
 compare=[];different=[]
 for r,p in zip(b,packets):
  old=byhash[r['response_record_sha256']]
  for k in ['reference_id','delivery_status','gold_status','treatment_version','rubric_sha256']:assert old[k]==r[k]
  eq=(old['semantic_judgment'],old['complete_preservation'])==(r['semantic_judgment'],r['complete_preservation'])
  c={'response_record_sha256':r['response_record_sha256'],'reference_id':r['reference_id'],'pass1_review_id':old['review_id'],'pass2_review_id':r['review_id'],'pass1_state':old['semantic_judgment'],'pass2_state':r['semantic_judgment'],'same_state_and_value':eq,'adjudication_status':'NOT_REQUIRED_FOR_STATE_COMPARISON' if eq else 'PENDING','final_semantic_judgment':None}
  compare.append(c)
  if not eq:different.append(dict(c,source=p['source'],pdf=p['pdf'],question_ko=p['question_ko'],explanation_ko=p['explanation_ko'],pass1_rationale=old['rationale'],pass2_rationale=r['rationale'],pass1_reason_codes=old['reason_codes'],pass2_reason_codes=r['reason_codes'],propositions_and_relations=r['propositions_and_relations'],source_provenance=r['source_provenance'],adjudication_question=QUESTIONS.get(r['review_id'],'두 판정과 원문 전체를 대조하여 근거를 기록한다.')))
 groups=collections.defaultdict(set)
 for r,p in zip(b,packets):groups[(r['reference_id'],p['explanation_ko'])].add(r['semantic_judgment'])
 assert all(len(x)==1 for x in groups.values())
 return a,b,packets,compare,different

def csvwrite(path,rows,fields):
 with path.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader()
  for r in rows:w.writerow({k:json.dumps(r[k],ensure_ascii=False) if isinstance(r[k],(dict,list)) else r[k] for k in fields})
def build():
 assert not (OUT/'summary.json').exists(),'Do not overwrite a completed export'
 a,b,packets,compare,different=data()
 write_lines(OUT/'pass_comparison.jsonl',compare);write_lines(OUT/'disagreements_pending.jsonl',different)
 csvwrite(OUT/'judgments_index.csv',b,['review_id','reference_id','semantic_judgment','complete_preservation','gold_status','delivery_status','reason_codes','rationale','response_evidence_quote','reviewed_at','response_record_sha256'])
 csvwrite(OUT/'disagreements_index.csv',different,['pass1_review_id','pass2_review_id','reference_id','pass1_state','pass2_state','pass1_rationale','pass2_rationale','adjudication_status','adjudication_question'])
 keys=read(p2.v2.PACKAGE/'coordinator/keys.json')['pass2'];av=read(p2.v2.PACKAGE/'coordinator/input_availability.json')
 bindings=[{'review_id':k['review_id'],'reference_id':k['reference_id'],'case_id':k['case_id'],'condition':k['condition'],'response_binding':k['response_binding'],'original_input_availability':av[k['condition']],'extra_pdf_context':av['extra_pdf_context'],'cohorts':k['cohorts'],'bound_after_pass2_seal':True} for k in keys]
 write_lines(OUT/'input_provenance_bindings.jsonl',bindings)
 readable=OUT/'readable';readable.mkdir()
 for start in range(0,255,43):
  end=min(start+43,255);s=['# v2 2차 검토 '+f'{start+1:03d}–{end:03d}','', '봉인한 수동 판정의 읽기용 사본. 최종 조정 결과가 아니며 조건별 성능을 뜻하지 않는다.','']
  for r,p in zip(b[start:end],packets[start:end]):
   source=p['source'];s += [f"## {r['review_id']} · {r['reference_id']} · {r['semantic_judgment']}",'',f"출처: {source['spec_id']} v{source['version']} §{source['clause_id']}, PDF p.{p['pdf']['pdf_page']}. 기준 상태: {r['gold_status']}.",'','원문: '+source['source_text_en'],'','질문: '+p['question_ko'],'','응답: '+(p['explanation_ko'] or '[설명 미생성]'),'','판정 이유: '+r['rationale'],'','응답 근거 인용: '+r['response_evidence_quote'],'','원문 명제·관계:']
   for prop in r['propositions_and_relations']:s += ['- '+prop['action_or_state']+'; 조건: '+prop['condition']+'; 관계: '+prop['relation']]
   s+=['',f"기록 시각: {r['reviewed_at']}; 원본 응답 SHA-256: `{r['response_record_sha256']}`",'']
  (readable/f'review_{start+1:03d}_{end:03d}.md').write_text('\n'.join(s)+'\n')
 s=['# v2 1·2차 판정 불일치: 조정 대기','','두 차수 모두 봉인한 뒤 응답 레코드 해시로 대조했다. 아래 판정을 덮어쓰거나 다수결·자동 규칙으로 최종 판정하지 않았다. 동일 평가자의 반복 검토이며 독립 전문가 일치율이 아니다.','']
 for r in different:
  s += [f"## {r['pass2_review_id']} · {r['reference_id']} · {r['pass1_state']} → {r['pass2_state']}",'',f"1차 ID: {r['pass1_review_id']}; 상태: PENDING.",'','원문: '+r['source']['source_text_en'],'','응답: '+r['explanation_ko'],'','1차 근거: '+r['pass1_rationale'],'','2차 근거: '+r['pass2_rationale'],'','조정 쟁점: '+r['adjudication_question'],'']
 (OUT/'disagreements_pending.md').write_text('\n'.join(s)+'\n')
 matrix=collections.Counter((r['pass1_state'],r['pass2_state']) for r in compare)
 release=read(p2.BASE/'release_manifest.json');seal=read(p2.SEAL/'completion_manifest.json');old=read(p2.P1/'completion_manifest.json')
 summary={'status':'PASS2_SEALED_ADJUDICATION_PENDING','recorded_at':p2.now(),'pass1_completed_at':old['completed_at'],'pass2_released_at':release['released_at'],'pass2_completed_at':seal['completed_at'],'pass2_delay_seconds':(datetime.datetime.fromisoformat(release['released_at'])-datetime.datetime.fromisoformat(old['completed_at'])).total_seconds(),'reviewed_slots':255,'source_references':51,'slots_per_reference':5,'pass2_workflow_counts':dict(collections.Counter(r['semantic_judgment'] for r in b)),'identical_state_and_value':255-len(different),'disagreements':len(different),'state_transition_counts':[{'pass1':x,'pass2':y,'count':n} for (x,y),n in sorted(matrix.items())],'adjudicated_rows':0,'final_condition_metrics_computed':False,'cohort_denominators_unchanged':[49,50,50,51],'new_model_generation_calls':0,'independent_reviewer':False,'fully_blind':False,'masking_limit':'Same study evaluator; earlier pass1 discussion existed in conversation. During pass2 semantic decisions only released shuffled packets, source/gold preflight and frozen rubric were consulted; pass1 results compared only after pass2 seal.','semantic_validity_automatically_verified':False}
 write(OUT/'summary.json',summary)
 write(OUT/'verification_receipt.json',{'ok':True,'verified_at':p2.now(),'checks':['24-hour release gate','255 unique rows in frozen pass2 order','51 references times five slots','254 verbatim response evidence quotes plus one not-generated sentinel','treatment and rubric hash','source propositions and provenance equal preflight','packet and original response record hashes','gold unresolved state restriction','UNRESOLVED=null and pipeline NOT_SCORED=0','review timestamps after release and monotonic','same reference and exact explanation state consistency','pass1 and pass2 seal hashes','119 original frozen files and 22 package files plus two support files','comparison by unique original response record hash only after pass2 seal'],'semantic_truth_automatically_verified':False})
 print(json.dumps(summary,ensure_ascii=False,indent=2))
def finish():
 assert DOC.exists() and not (OUT/'completion_manifest.json').exists()
 files=[p for p in OUT.rglob('*') if p.is_file()];support=[DOC,Path(__file__).resolve(),ROOT/'tools/finalize_v2_pass2_20260909.py',ROOT/'tools/v2_pass2_workbench_20260909.py']
 write(OUT/'completion_manifest.json',{'status':'PASS2_SEALED_ADJUDICATION_PENDING','manifested_at':p2.now(),'file_sha256':{str(p.relative_to(OUT)):sha(p) for p in sorted(files)},'support_file_sha256':{str(p.relative_to(ROOT)):sha(p) for p in support},'pass1_full_completion_manifest_sha256':sha(p2.P1.parent/'completion_manifest.json'),'release_manifest_sha256':sha(p2.BASE/'release_manifest.json')})
def verify():
 a,b,packets,c,d=data();m=read(OUT/'completion_manifest.json')
 for rel,h in m['file_sha256'].items():assert sha(OUT/rel)==h
 for rel,h in m['support_file_sha256'].items():assert sha(ROOT/rel)==h
 assert sha(p2.P1.parent/'completion_manifest.json')==m['pass1_full_completion_manifest_sha256']
 assert sha(p2.BASE/'release_manifest.json')==m['release_manifest_sha256']
 assert lines(OUT/'pass_comparison.jsonl')==c and lines(OUT/'disagreements_pending.jsonl')==d
 working=lines(OUT/'judgments_working.jsonl')
 assert working==[{k:v for k,v in r.items() if k!='response_record_sha256'} for r in b]
 s=read(OUT/'summary.json');assert s['pass2_workflow_counts']==dict(collections.Counter(r['semantic_judgment'] for r in b))
 assert s['disagreements']==len(d) and s['identical_state_and_value']==255-len(d)
 assert s['adjudicated_rows']==0 and s['final_condition_metrics_computed'] is False
 with (OUT/'judgments_index.csv').open(encoding='utf-8-sig',newline='') as f:csvrows=list(csv.DictReader(f))
 assert len(csvrows)==255 and [r['semantic_judgment'] for r in csvrows]==[r['semantic_judgment'] for r in b]
 for page in (OUT/'readable').glob('*.md'):assert page.stat().st_size>0
 print(json.dumps({'ok':True,'pass2_slots':255,'same_state':255-len(d),'disagreements_pending':len(d),'artifact_hashes_verified':len(m['file_sha256']),'support_hashes_verified':len(m['support_file_sha256']),'semantic_truth_automatically_verified':False},ensure_ascii=False))
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('command',choices=['build','finish','verify']);v=a.parse_args();{'build':build,'finish':finish,'verify':verify}[v.command]()
