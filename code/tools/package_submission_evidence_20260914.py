"""Build/verify a local repository-linked submission evidence index; never calls API."""
from pathlib import Path
from collections import Counter
import csv,json,hashlib,sys,datetime
R=Path(__file__).resolve().parents[1];O=R/'outputs/submission_evidence_v7_20260914';A=R/'outputs/review/v2_cohort_analysis_20260909'
def read(p):return json.loads(p.read_text())
def rows(p):return list(map(json.loads,p.read_text().splitlines()))
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def csvrows(p):return list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
def writecsv(p,rs):
 with p.open('w',encoding='utf-8-sig',newline='')as f:
  w=csv.DictWriter(f,fieldnames=list(rs[0]));w.writeheader();w.writerows(rs)
def derive():
 cases={x['case_id']:x for x in csvrows(R/'data/main_cases.csv')};pol=read(R/'experiments/posthoc_treatment_v1_20260908/case_policy.json')['rows'];protocol=read(R/'experiments/posthoc_treatment_v1_20260908/protocol.json');slots=rows(A/'bound_slots_255.jsonl');members=[];dists=[]
 assert len(cases)==len(pol)==72
 for x in pol:
  c=cases[x['case_id']];members.append({'case_id':x['case_id'],'spec_id':c['spec_id'],'clause_id':c['clause_id'],'original_modal':c['modal_class'],'original_difficulty':c['difficulty_tier'],'audit_status':x['audit_status'],'treatment':x['treatment'],'cohorts':'|'.join(x['cohorts']),'reason':x['rationale_ko']})
 groups={'ORIGINAL_72':list(cases),**{n:c['case_ids']for n,c in protocol['cohorts'].items()}}
 for group,ids in groups.items():
  for field in ['spec_id','modal_class','difficulty_tier']:
   for value,num in sorted(Counter(cases[i][field]for i in ids).items()):dists.append({'cohort':group,'dimension':field,'value':value,'count':num,'N':len(ids)})
 for n,c in protocol['cohorts'].items():
  selected=[x for x in slots if n in x['cohorts']];assert len(selected)==c['n']*5
  for arm in protocol['conditions']:assert {x['case_id']for x in selected if x['condition']==arm}==set(c['case_ids'])
 return members,dists,protocol,slots
if sys.argv[1]=='build':
 assert not O.exists();O.mkdir(parents=True);members,dists,p,slots=derive();writecsv(O/'case_membership_72.csv',members);writecsv(O/'sample_distributions.csv',dists)
 (O/'primary_response_trace_255.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n'for x in slots))
 lines=['# 표본 구성','', '기존 72건은 일반 적격 50·조건부 예외 1·부적격 10·보류 11로 재감사됐다. 일반 적격에서 C2 입력 오염 MAY-001을 제외해 주 분석 49건이다. Gold 50은 MAY-001, Exception 50은 SDN-011, Both 51은 둘 다 복원한다. 제외 기준의 기존 규약과 사후 분석 처리 동결을 구분한다.','', '아래 규범 유형·난도는 최초 표본의 층화 라벨이며 수정 정답의 규범 판정 분포를 뜻하지 않는다. 네 분석 집합은 겹친다. 사례 수를 더하거나 반복을 독립 표본으로 세지 않는다.','']
 for dim in ['spec_id','modal_class','difficulty_tier']:
  vals=sorted({x['value']for x in dists if x['dimension']==dim});groups=list(dict.fromkeys(x['cohort']for x in dists));lines+=['## '+dim,'','| 집합 | '+' | '.join(vals)+' | 합계 |','|---|'+'---:|'*(len(vals)+1)]
  for group in groups:
   rr={x['value']:x['count']for x in dists if x['cohort']==group and x['dimension']==dim};lines.append('| '+group+' | '+' | '.join(str(rr.get(v,0))for v in vals)+' | '+str(sum(rr.values()))+' |')
  lines.append('')
 lines+=['주 분석은 33개 규격·조항 군집이며 민감도 집합은 각각 34·34·35개다. 최초 규격별 36건·규범 유형별 12건의 균형은 49건에 자동 유지되지 않는다.','', '72건의 개별 포함/제외 이유: [case_membership_72.csv](case_membership_72.csv).']
 (O/'01_samples.md').write_text('\n'.join(lines))
 ref=read(R/'experiments/error_replication_v1_20260914/evaluation_reference.json')
 ev=['# 평가표와 해석 범위','', '사용자 요청에 따라 사람의 독립 검토는 생략했다. 모든 의미 판정은 동일 Codex 기반이며 점검 통과를 독립 전문가 검증으로 표현하지 않는다. 원고 v7에도 한계를 유지한다.','', '| 구분 | 대상 | 판정 방식 | 남은 제한 |','|---|---|---|---|','| 주 분석 | 49개 원문 × 5조건 | 동결 v2 기준, 두 차수와 불일치 조정 | 동일 AI·사후 처리·U 잔존 |','| 민감도 | 50/50/51개 원문 × 5조건 | 동일 조정 판정에 고정 집합 적용 | 중첩 집합, 새로운 반복 아님 |','| 추가 진단 | 알려진 3원문, 완료 8응답 | 사전 지정 9요구사항, 당일 동일 AI 재검토 | 원문 전체 완역 지표 아님; 통신 미상 1 별도 |','', '| 상태 | 의미 | 분모 처리 |','|---|---|---|','| P | 필수 의미 보존 및 미지원 규범 추가 없음 | 성공 1 |','| F | 명확한 누락·왜곡 | 성공 0 |','| U | 판정 미확정 | 제거하지 않음; 원자료 null |','| NG | 미생성 | 의미 오역과 구분, 고정 분모에서 성공 0 |','', '논리적 범위는 [P/N,(P+U)/N], B−A 차이는 [(P_B−P_A−U_A)/N,(P_B+U_B−P_A)/N]이다. 신뢰구간이나 통계적 유의성이 아니다. 추가 첫 통신 미상 슬롯은 결과 자체를 확인하지 못했으므로 확인된 NG와 혼동하지 않으며, 9개 전체 완수율을 보고하지 않는다.','', '## 추가 진단의 동결 요구사항','', '| 사례 | ID | 요구사항 |','|---|---|---|']
 for c in ref['cases']:
  for req in c['requirements']:ev.append('| '+c['case_id']+' | '+req['id']+' | '+req['description_ko']+' |')
 ev+=['', '복합 요구사항은 모든 접속항·예외 사건을 확인한다. explanation_ko만 의미 채점하며 action/exception 등 메타데이터로 누락을 복원하지 않는다. 명확한 누락 0과 해석 불확실 null을 구분한다.','', '## 경계 사례','', '- 성공: SMF가 능력을 가질 수도 있다고 하여 보유의 선택성을 보존한 설명. capability 메타데이터만으로 설명을 실패로 바꾸지 않는다.','- 성공: 저장해야 한다는 권고는 전체 표현의 권고 한정을 반영한다. 해야 한다만 검색해 의무화로 세지 않는다.','- 실패: eCall 임시 저장이 메타데이터에만 있고 설명에는 없는 경우. 긴급 등록의 규칙을 eCall에 자동 확장하지 않는다.','- 실패: NAS 메시지 대신 수신 엔티티가 검사를 받은 것으로 서술한 V2-P2-099.','- 미확정: V2-P2-106의 능력이 있다와 이는 선택 가능의 지시 대상이 불명확한 설명.','', '개별 전체 응답·근거: [추가 재검토](../review/error_recheck_v2_20260914/review.md), [v2 조정 사례](../review/v2_adjudication_20260909/adjudication_readable.md).']
 (O/'02_evaluation.md').write_text('\n'.join(ev))
 sources=['data/main_cases.csv','data/main_freeze_manifest.json','outputs/analysis/main72_eligibility_20260908/eligibility_audit.csv','experiments/posthoc_treatment_v1_20260908/protocol.json','experiments/posthoc_treatment_v1_20260908/case_policy.json','experiments/posthoc_treatment_v1_20260908/response_index.json','experiments/posthoc_treatment_v1_20260908/gold_overlay.json','outputs/review/v2_20260908/coordinator/keys.json','outputs/review/v2_20260908/coordinator/response_records.jsonl','outputs/review/v2_20260908/preflight/references.jsonl','outputs/review/v2_adjudication_20260909/adjudicated_view_255.jsonl','experiments/c3_lib.mjs','tools/summarize_v2_cohorts_20260909.py','tools/package_submission_evidence_20260914.py']
 for folder in ['outputs/review/v2_cohort_analysis_20260909','outputs/review/error_recheck_v2_20260914','experiments/error_replication_v1_20260914','experiments/runs/error_replication_v1_20260914','experiments/runs/error_replication_remaining8_20260914']:
  sources += [str(x.relative_to(R))for x in (R/folder).iterdir()if x.is_file()]
 sources += ['outputs/paper/ACK2026_3GPP_normative_fidelity_validated_v7'+ext for ext in ['.pdf','.docx','.md']]
 index=['# 재현 자료 연결','', '이 묶음은 현재 저장소의 원본을 참조하는 로컬 색인이다. 단독 배포용 ZIP이나 공개 저장소가 아니다. 비밀 설정 파일을 포함하지 않으며 외부 게시·전송은 수행하지 않았다.','', '## 읽기 순서','', '1. 01_samples.md와 case_membership_72.csv로 분모를 확인한다.','2. 02_evaluation.md로 판정 면과 요구사항을 확인한다.','3. primary_response_trace_255.jsonl의 case_id/condition → review_id/reference_id를 따라 v2 coordinator keys, response_records 및 adjudicated_view를 조회한다. 원본 응답 및 판정 해시는 trace에 있다.','4. condition_results/paired_results의 결과와 원고 표를 대조한다.','5. 추가 진단은 별도 runs의 요청·원본 응답과 error_recheck_v2의 판정을 확인한다.','', '## 오프라인 검증','', '저장소 루트에서 Python 3 표준 라이브러리만으로 실행한다. API 호출이나 응답 재생성이 없다.','', '```sh','python3 tools/package_submission_evidence_20260914.py verify','python3 tools/summarize_v2_cohorts_20260909.py verify','```','', '첫 명령은 해시·분포·분모·trace를, 둘째는 원본 봉인·조정·SQLite 집계 및 미확정 열거 범위를 검증한다. 의미적 정답을 자동 증명하지 않는다. 생성 재실행은 비용·비결정성이 있는 별도 실험으로, 이 재현 절차에 포함하지 않는다.','', '## 파일 색인','']
 for s in sorted(set(sources)):index.append('- ['+s+'](../../'+s+')')
 (O/'03_reproduction.md').write_text('\n'.join(index))
 (O/'README.md').write_text('# v7 제출 근거 자료\n\n표본 구성·평가표·재현 자료 정리를 완료했다. 사람의 독립 검토는 사용자 요청에 따라 생략했으며, 동일 AI 평가라는 한계를 유지한다. 새 생성·재채점·원고 수치 변경은 없다.\n\n- [표본 구성](01_samples.md)\n- [평가표](02_evaluation.md)\n- [재현 자료와 명령](03_reproduction.md)\n- [현재 v7 원고](../paper/ACK2026_3GPP_normative_fidelity_validated_v7.pdf)\n\n상태: 자료 정리 및 기계적 검증 완료. 독립 의미 검증·학회 제출 완료를 뜻하지 않는다. 이 색인은 저장소와 함께 사용한다.\n')
 files=[R/x for x in set(sources)]+list(O.iterdir())
 (O/'manifest.json').write_text(json.dumps({'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'independent_human_review':'OMITTED_BY_USER_REQUEST','file_sha256':{str(x.relative_to(R)):h(x)for x in sorted(set(files))}},ensure_ascii=False,indent=2)+'\n')
 print('BUILT',O)
elif sys.argv[1]=='verify':
 for p,d in read(O/'manifest.json')['file_sha256'].items():assert h(R/p)==d,p
 m,dist,p,s=derive();assert csvrows(O/'case_membership_72.csv')==[{k:str(v)for k,v in x.items()}for x in m];assert csvrows(O/'sample_distributions.csv')==[{k:str(v)for k,v in x.items()}for x in dist];assert rows(O/'primary_response_trace_255.jsonl')==s
 print(json.dumps({'ok':True,'cases':72,'primary':49,'trace_slots':len(s),'all_manifest_hashes_valid':True,'independent_human_review':False,'live_calls':0}))
else:raise ValueError('build or verify')
