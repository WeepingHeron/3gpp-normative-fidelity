"""Serialize coordinator's manually read primary judgments; no automatic semantic scoring."""
from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'outputs/review/proposition_pipeline_v1_20260913'
P={r['review_id']:r for r in map(json.loads,(B/'primary_packets_12.jsonl').read_text().splitlines())}
# All values/reasons below were selected by reading final explanations before any extraction output or condition key.
D={
1:([0,1,1,0],True,['저장되어야 하며라는 의무 표현으로 권고를 강화했다.','SUPI와 함께 저장하고 일치 시에만 사용하며 불일치하면 삭제한다.','비저장·ME 임시 저장·긴급 서비스 등록 해제 삭제를 모두 명시한다.','같은 비저장 원칙과 세 삭제 사건은 있지만 eCall 시 ME 임시 저장을 설명하지 않는다. 같은 비저장 원칙만으로 임시 저장 방식까지 보충하지 않는다.'],'should 저장 권고를 저장되어야 한다는 의무로 강화했다.'),
2:([1,1],None,['능력을 가질 수도 있고 보유의 선택성이라고 명시한다.','하나의 Session에서 local·central UPF 모두를 제어하는 능력을 보존한다.'],'능력을 실제로 보유한 경우에만 제어할 수 있다는 추가 문장은 능력의 뜻을 풀어쓴 것으로도, 원문에 없는 실행 필요조건을 추가한 것으로도 읽힌다. 대상의 선택성은 보존됐지만 추가 주장의 범위를 확정하지 않는다.'),
3:([0,1,0],True,['해서는 안 되며/해서는 안 됩니다라고 반복하고 권고 강도를 명시하지 않아 강제 금지로 강화한다.','NR satellite access에서 위치 검증하는 문맥을 명시한다.','망이 PLMN 운용 가능 여부를 검증하도록 설정된 조건을 누락한다.'],'should not을 예외 있는 강제 금지로 바꿨다.'),
4:([1,0,0],False,['정확한 위치정보가 없으면 거절·해제를 하지 않는 권고임을 첫 문장과 마지막 문장에서 보존한다. 중간의 필요조건은 거절 허용이 아니라 위치 판단의 충분성을 설명한다.','NR 위성 접속 범위를 설명하지 않는다.','망의 검증 설정 조건을 설명하지 않는다.'],'정확한 위치정보가 있어야 그 위치 판단을 할 수 있다는 설명은 원문의 충분성 관계로 읽힌다. 거절을 강제하거나 허용하는 새 규칙을 주장하지 않는다.'),
5:([0,1,1,1],False,['저장할 수 있으며로 설명하여 원문의 저장 권고를 누락한다.','SUPI 동반 저장·일치 시 사용·불일치 시 삭제를 모두 보존한다.','긴급 등록 비저장·임시 저장·등록 해제 삭제를 보존한다.','eCall 비저장·임시 저장·세 삭제 사건을 모두 보존한다.'],'저장할 수 있다는 설명은 제공 문맥의 can에 근거가 있다. 대상 권고의 누락은 요구사항 0으로 처리하며 새 허구 주장으로 중복 확정하지 않는다.'),
6:([1,1],False,['능력 보유의 선택성을 명시하고 필수 보유나 필수 행사로 바꾸지 않는다.','단일 Session의 두 UPF 모두를 제어하는 능력을 명시한다.'],'추가 의무나 조건을 만들지 않고 대상의 선택적 능력을 설명한다.'),
7:([1,0,0],False,['정확한 위치정보가 없는 경우의 비권고 및 충분한 정보가 있을 때 권고의 예외를 보존한다.','NR 위성 접속 문맥을 누락한다.','망의 검증 설정 조건을 누락한다.'],'예외에서 권고가 적용되지 않는다고 할 뿐 거절·해제 의무나 강한 허용 조건을 만들지 않는다.'),
8:([None,1],None,['앞에서는 선택적 능력 보유라고 정확히 설명하지만 끝에서는 함께 제어하는 경우를 허용한다고 한다. 능력의 가능한 구성을 풀어 쓴 것인지 행동 허용으로 바꾼 것인지 미확정이다.','단일 Session에서 local·central UPF 모두를 제어하는 내용을 보존한다.'],'선택적 능력과 제어 경우 허용을 함께 쓰므로 후자의 논리적 범위를 확정하지 않는다.'),
9:([0,1,1,0],True,['저장해야 하며로 권고를 의무화한다.','SUPI와 함께 저장하는 방식과 일치 시 사용·불일치 시 삭제를 보존한다.','긴급 등록의 비저장·ME 임시 저장·등록 해제 삭제를 모두 보존한다.','eCall의 세 삭제 사건은 있지만 비저장·ME 임시 저장 규칙을 eCall에 연결하지 않는다. 앞의 저장 규칙은 긴급 서비스 등록 조건으로 한정돼 있다.'],'should 저장 권고를 저장해야 한다는 의무로 강화한다.'),
10:([0,1,1,1],False,['저장할 수 있으며라는 표현과 Annex C 연결은 있지만 저장 권고는 없다.','SUPI 동반 저장·일치 시 사용·불일치 시 삭제를 보존한다.','긴급 등록 비저장·임시 저장·등록 해제 삭제를 보존한다.','eCall 비저장·임시 저장·세 삭제 사건을 모두 보존한다.'],'문맥의 can에 근거한 설명이다. 저장 권고의 누락은 완수 실패이며 이 표현 자체를 근거 없는 주장으로 보지 않는다.'),
11:([None,1],None,['선택적 능력 보유라고 한 뒤 제어하는 경우를 허용적으로 말한다고 덧붙인다. 능력 보유의 가능한 경우인지 행동의 허용인지 미확정이다.','단일 Session 안에서 두 UPF 모두를 제어하는 능력을 보존한다.'],'선택적 능력이라는 올바른 설명과 허용적 구성이라는 설명의 관계가 미확정이다.'),
12:([1,0,0],False,['비권고와 정확한 위치정보가 있을 때 그 권고가 적용되지 않는 관계를 보존한다.','NR 위성 접속 범위를 누락한다.','망의 검증 설정 조건을 누락한다.'],'조건 충족 후 필수 거절·해제까지 주장하지 않는다고 명시한다.')}
O=B/'primary_review';assert not O.exists();O.mkdir();records=[]
for n,(values,claim,reasons,claim_reason) in D.items():
 p=P[f'PPR-{n:03d}'];assert len(values)==len(p['requirements'])==len(reasons)
 cover=[{'requirement_id':q['id'],'value':v,'response_quotes':[p['explanation_ko']],'source_quotes':[p['target_text']]+[b['quote'] for b in p['reference_context_blocks']],'rationale':reason} for q,v,reason in zip(p['requirements'],values,reasons)]
 complete=0 if 0 in values or claim is True else None if None in values or claim is None else 1
 md=p['output_metadata_for_separate_audit'];citation=all(md[k]==p['source'][v] for k,v in [('citation_spec','spec_id'),('citation_version','version'),('citation_clause','clause_id')])
 records.append({'review_id':p['review_id'],'reviewer':'coordinator_ai','reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'requirement_coverage':cover,'unsupported_or_distorted_claim':claim,'claim_evidence_quotes':[p['explanation_ko']] if claim is not False else [],'claim_rationale':claim_reason,'full_context_target_completeness':complete,'citation_diagnostic':{'metadata_matches_source_fields':citation,'explanation_has_full_spec_version_clause':n in [5,10]},'sentence_count_diagnostic':{'sentence_count':4 if n in [9,10] else 3,'within_2_to_4':True},'metadata_audit_status':'NOT_SCORED_SEPARATE_DIAGNOSTIC_NOT_PRIMARY','overall_rationale':' / '.join(reasons)+' '+claim_reason})
path=O/'judgments_12.jsonl';path.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records))
notes=O/'review_notes.md';notes.write_text('# 진행 AI 1차 의미 검토\n\n최종 설명 12개와 원문·기존 요구사항을 수동으로 읽고 판정했다. 설계와 이전 실험을 알고 있으므로 독립 또는 완전 눈가림 평가가 아니다. 이번 실행의 추출 출력 및 coordinator_keys는 판정 봉인 전에 읽지 않았다. PPR-002·008·011의 추가 조건 또는 능력/허용 관계는 미확정으로 남겼다. 출처 필드·문장 수는 보조 진단이며 메타데이터 의미 점수는 산출하지 않았다.\n')
manifest={'sealed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'review_count':12,'requirement_count':36,'semantic_scores_automatically_inferred':False,'input_files':{'primary_packets_12.jsonl':hashlib.sha256((B/'primary_packets_12.jsonl').read_bytes()).hexdigest()},'file_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in O.iterdir()},'serializer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(O/'reviewer_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
for p in O.iterdir():p.chmod(0o444)
Path(__file__).chmod(0o444)
print(json.dumps({'status':'PRIMARY_REVIEW_SEALED','records':12,'requirements':36,'extraction_not_yet_read':True}))
