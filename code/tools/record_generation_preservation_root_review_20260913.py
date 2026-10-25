"""Serialize 18 individually decided coordinator judgments; never infer semantic scores from keywords."""
from pathlib import Path
from datetime import datetime, timezone
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs/review/generation_preservation_v1_20260909/root_review'
PACKET=ROOT/'outputs/review/generation_preservation_v1_20260909/reviewer/packets_18.jsonl'
# Per row: manual requirement values, individual reasons, claim, claim reason/evidence, cross-field diagnostic/reason.
D={
1:([1,1],['능력을 가질 수도 있고 그 보유가 선택적임을 명시한다. 마지막 문장은 그 능력의 내용을 한정하며 새로운 only-if 조건을 만들지 않는다.','하나의 PDU Session에서 local과 central UPF 모두를 제어하는 능력을 보존한다.'],False,'주변의 복수 Session 예시와 단일 Session 능력의 관계도 제공 문맥으로 지지된다.',[],None,'capability 라벨과 control action은 대상의 may-have 규범 구조를 정확히 표시하지 않지만, 능력 보유가 필수라는 명시적 필드 주장은 없어서 설명과의 논리적 모순까지 확정하지 않는다.'),
2:([0,1,0,None],['기본 저장 should를 저장해야 한다는 의무로 강화했다. Annex C 연결도 설명에는 구체적이지 않다.','SUPI 동반 저장, 일치 시에만 사용, 불일치 삭제가 모두 있다.','긴급 등록 시 비휘발성/USIM 금지와 ME 임시 저장은 있으나 긴급 서비스 등록 해제 시 삭제가 없다.','eCall 세 삭제 계기는 있으나 동일하게 저장하지 않고가 앞의 ME 임시 저장까지 승계하는지 비휘발성 저장 금지만 승계하는지 명확하지 않아 임시 저장 보존은 미확정이다.'],True,'대상 및 Annex C의 should 저장 권고를 무조건 저장해야 한다고 바꿨다.',['ME의 비휘발성 메모리에 저장해야 하며'],False,'obligation 라벨도 원문에는 잘못됐지만 설명의 저장 의무화와는 일치한다. 이 원문 오류를 필드 간 모순으로 중복 판정하지 않는다.'),
3:([1,1],['각 SMF의 선택적 능력 보유를 명시하고 제어 행동 허용과 구별한다.','단일 PDU Session 내 local과 central UPF 모두라는 범위를 보존한다.'],False,'설명은 능력 보유와 복수 Session 예시의 대비를 충실하게 설명한다.',[],None,'action은 have the capability를 보존한다. capability 유형과 exception의 추가로 허용하는 취지라는 말은 설명의 허용이 아니라와 긴장하지만, 능력 보유 가능성을 가리키는 허용일 수도 있어 확정 모순으로 두지 않는다.'),
4:([None,1],['첫 문장은 선택적 능력 보유를 보존하지만 마지막의 두 UPF를 제어하는 구성을 추가로 허용한다는 말은 능력 보유 구성인지 제어 행동의 허용인지 결정하기 어렵다. 전체 설명의 명제 대상을 null로 남긴다.','두 UPF 모두와 하나의 PDU Session이라는 행동 내용·범위는 유지된다.'],None,'구성 허용이 선택적 capability 구성의 재표현인지 실제 제어의 별도 허용 주장인지 불분명하다. 첫 문장이 정확하다는 이유만으로 후문의 모호함을 없애지 않는다.',['두 UPF를 함께 제어하는 구성을 추가로 허용하는 것으로 읽어야 하며'],None,'metadata action은 능력 보유를 가리킨다. 설명 후문의 구성 허용이 무엇에 걸리는지 모호해 필드 간 모순도 확정하지 않는다.'),
5:([1,1],['능력 보유의 선택성과 비의무를 명시한다. 특정 조건에서만 허용된다는 제한이 없다는 것은 주어진 추가 문맥에서 별도의 필요조건을 제시하지 않았다는 범위로 읽힌다.','단일 PDU Session 내 두 UPF 모두의 제어 능력이 있다.'],False,'비로밍·두 네트워크·복수 Session 예시 및 선택적 능력은 원문에 있다.',[],None,'capability/control 필드는 대상의 선택적 보유 구조와 맞지 않지만 필수 보유나 강제 제어를 단정한 값은 아니므로 명시적 논리 모순은 미확정이다.'),
6:([0,1,0],['처음 비권고를 맞추지만 이어 정확해야만 판단할 수 있고 마지막에는 해서는 안 된다고 단정하여 필요조건·강제 금지로 강화한다.','NR satellite access 사용 UE라는 범위를 설명한다.','AMF가 검증할 수 있다는 말은 있으나 망이 PLMN 운용 가능 여부 검증을 하도록 설정되는 조건은 빠졌다.'],True,'후문이 앞의 권고를 강제 금지와 유일한 허용 조건으로 바꾼다.',['위치정보가 충분히 정확해야만 예외적으로 거절 또는 등록해제 판단을 할 수 있다','요청 거절이나 등록해제를 해서는 안 된다는 취지이다'],True,'discouragement 라벨 및 이 권고라는 exception과 설명 마지막의 단정적 금지가 상충한다.'),
7:([0,1,0],['해서는 안 된다와 경우에만 가능하다는 강제 금지·허용 필요조건으로 should not을 강화한다.','NR satellite access의 문맥임을 명시한다.','네트워크의 위치 검증 수행 문맥은 말하지만 PLMN 운용 가능 여부를 검증하도록 설정된 망이라는 조건은 제시하지 않는다.'],True,'권고를 금지로 강화한 설명이다.',['UE를 등록 해제해서는 안 되며','경우에만 예외적으로 가능하다'],True,'discouragement 라벨에 비해 한국어 설명은 단정적인 prohibition이다.'),
8:([0,1,0],['두 번째 문장에서 권고라고 붙여도 첫 문장의 경우에만 거절/해제할 수 있다는 독립적인 필요조건 주장은 남는다.','NR satellite access 위치 검증 맥락을 보존한다.','Selected PLMN ID/ULI 연결만 있고 망이 검증하도록 설정되는 조건은 빠졌다.'],True,'첫 문장이 비권고 예외를 유일한 허용 요건으로 강화한다.',['판단할 수 있는 경우에만 요청을 거절하거나 UE를 등록해제할 수 있다'],True,'유형은 비권고인데 condition은 정확한 정보 보유로 적고 exception은 미보유로 뒤집었다. 설명의 정확한 정보 보유 시 가능하다는 연결과 맞지 않는다.'),
9:([0,1,1,0],['원문의 can 저장 가능성은 설명하지만 대상 should 저장 권고는 전달하지 않는다. Annex C 참조만으로 빠진 강도가 복구되지 않는다.','SUPI 동반 저장·일치 사용·불일치 삭제가 모두 있다.','긴급 등록의 두 저장 위치 금지, ME 임시 저장, 등록 해제 시 삭제가 모두 있다.','eCall의 특정 상태가 무엇인지 명시하지 않았다. 전원/USIM 계기만으로 eCALL-INACTIVE 진입 조건 전체를 충족하지 않는다.'],False,'저장할 수 있다는 문장은 제공 문맥의 can으로 지지된다. 권고 및 구체적 상태 생략은 완수 실패지만 그 자체로 반대 사실을 단정한 것은 아니다.',[],False,'recommendation 라벨은 설명에 빠진 정보를 갖고 있지만 can이라는 가능성과 권고는 양립 가능하다. 라벨만으로 설명 누락을 보완하지 않는다.'),
10:([1,1],['선택적 능력 보유를 말하고 후문도 그런 capability를 부여하는 구성이라고 분명히 지정하므로 제어 행동 허용으로 바꾸지 않는다.','단일 Session에서 local과 central 둘 다라는 범위를 보존한다.'],False,'능력 구성의 가능성과 비의무성은 대상 및 문맥에 부합한다.',[],False,'permission/action have the capability는 설명의 선택적 보유 명제와 일치한다.'),
11:([1,1],['규범 표현이 능력 보유에 걸림을 명시하고 필수 보유/사용과 구별한다.','단일 Session에서 두 UPF 모두 제어라는 능력 내용이 남아 있다.'],False,'비로밍 구조와 선택적 능력 보유에 관한 내용은 제공 문맥으로 지지된다.',[],None,'capability/control이라는 필드 표현이 may-have의 대상을 정확히 표시하지 않으나 설명과 명시적으로 반대되는 명제까지 단정하기 어렵다.'),
12:([0,0,0],['충분한 정보가 있을 때 거절하거나 등록 해제하는 쪽으로 처리해야 한다는 긍정 권고를 추가한다. 원문은 비권고 예외이며 문맥상 등록 해제는 may이다.','NR satellite access라는 범위를 설명하지 않는다.','Selected PLMN ID/ULI만 설명하고 망의 검증 설정 조건은 설명하지 않는다.'],True,'등록 해제까지 긍정적인 처리 권고 대상으로 묶었다. 뒤의 부정 권고가 이 추가 주장을 취소하지 않는다.',['요청을 거절하거나 UE를 등록해제하는 쪽으로 처리해야 한다는 권고를 받습니다'],True,'discouragement 메타 유형 및 조건/예외 구조에 비해 설명 첫 문장은 거절·등록 해제에 대한 긍정 권고이다.'),
13:([0,1,1,1],['can 가능성과 저장 위치를 설명하지만 should 저장 권고를 보존하지 않는다.','SUPI 동반 저장·일치 사용·불일치 삭제를 모두 명시한다.','긴급 등록의 저장 금지·ME 임시 저장·등록 해제 삭제가 있다.','eCall의 금지 저장 위치·ME 임시 저장·세 삭제 계기를 모두 명시한다.'],False,'can과 PLMN identity 구성, 조건부 삭제는 제공 문맥에 있다. 권고 누락은 있으나 can이라고 설명한 사실 자체는 지지된다.',[],False,'capability 유형은 대상 should에는 부정확하지만 설명의 can 가능성 진술과는 명시적으로 모순되지 않는다.'),
14:([0,1,1,1],['저장될 수 있다는 가능성만 한국어 명제로 설명하고 should/can을 함께 묶어 어느 표현이 권고인지 구분하지 않는다. should 문자열만 남긴 것은 권고의 의미를 전달하지 못한다.','SUPI 동반 저장·일치 시 사용·불일치 삭제가 모두 있다.','긴급 서비스 등록의 금지 저장 위치·ME 임시 저장·등록 해제 삭제가 있다.','eCall의 금지 저장 위치·ME 임시 저장·상태 진입/전원/USIM 세 계기가 있다.'],False,'가능성은 문맥 can에 지지된다. should/can의 적용 대상이 저장 방식/위치라는 괄호는 강도 설명이 부족하지만 둘이 같은 강도라고 명시적으로 단정하지는 않는다.',[],None,'recommendation 라벨과 action의 can/should 병기가 설명의 같은 병기와 얽혀 있다. 명확한 반대 명제를 단정하기 어렵고, 권고 의미의 설명 누락은 따로 0으로 판정했다.'),
15:([0,1,0],['두 번째 문장의 권고 한정에도 첫 문장의 경우에만 거절/해제할 수 있다는 필요조건 주장이 남는다.','NR satellite access의 위치 검증 맥락을 명시한다.','UE의 능력과 ULI는 설명하지만 네트워크가 PLMN 운용 가능 여부 검증을 하도록 설정된 조건은 빠졌다.'],True,'비권고 예외를 유일한 허용 요건으로 만드는 첫 문장이 있다.',['판단할 수 있는 경우에만 요청을 거절하거나 UE를 등록해제할 수 있다'],True,'discouragement의 condition을 정확한 정보가 있는 경우로 적으면서 설명에서는 그때 거절/해제를 허용한다고 서술한다. 조건이 걸리는 극성이 맞지 않는다.'),
16:([0,1,1,1],['저장할 수 있음 can만 설명하고 should 권고를 보존하지 않는다.','SUPI 동반 저장·일치 사용·불일치 삭제를 모두 보존한다.','각각이라는 연결을 통해 긴급 등록에 등록 해제 시 삭제를 대응시켰고 두 금지 위치와 ME 임시 저장도 있다.','각각이라는 연결을 통해 eCall에 eCALL-INACTIVE/전원/USIM 계기를 대응시켰고 두 금지 위치와 ME 임시 저장도 있다.'],False,'HPLMN/VPLMN 조건부 저장·매핑도 제공 문맥에 있는 내용이다. 권고의 누락은 있으나 추가 주장은 지지된다.',[],False,'permission 라벨은 대상 should 분류에는 부정확하지만 설명의 can 저장 가능성과 명시적 반대 관계는 아니다.'),
17:([1,1,0,0],['should be stored를 그렇게 저장하는 것이 권고된다고 분명히 구별하고 비-SNPN·ME 비휘발성·Annex C 연결을 보존한다.','SUPI 동반 저장·일치 사용·불일치 삭제가 모두 있다.','긴급 등록의 금지 저장 위치와 ME 임시 저장은 있으나 각각의 삭제 시점이라는 추상 표현은 등록 해제 계기를 전달하지 않는다.','eCall의 금지 저장 위치와 ME 임시 저장은 있으나 eCALL-INACTIVE/전원/USIM 삭제 계기를 구체적으로 설명하지 않는다.'],False,'제시한 저장·사용·임시 저장 명제는 원문에 지지된다. 삭제 계기의 추상화는 누락으로 보며 반대 규칙을 만든 것은 아니다.',[],False,'recommendation과 설명의 명시적인 저장 권고가 일치한다. 메타데이터에 더 많은 삭제 정보가 있어도 설명의 누락을 복구하지 않는다.'),
18:([0,1,0],['해서는 안 된다와 경우에만 예외적으로 가능하다는 말로 부정 권고를 금지로 강화한다.','NR satellite access를 사용하는 UE로 적용 범위를 한정한다.','절 이름과 페이지는 있지만 PLMN 운용 가능 여부를 검증하도록 설정된 망이라는 조건은 없다.'],True,'충분한 정보가 없을 때의 비권고를 강제 금지로 바꿨다.',['UE를 등록 해제해서는 안 되며','요청 거절이나 deregistration을 해서는 안 된다'],True,'discouragement 라벨과 한국어 설명의 단정적인 금지가 충돌한다.')}

def main():
 assert not OUT.exists(),'Do not overwrite sealed review'
 packets=[json.loads(x) for x in PACKET.read_text().splitlines()]
 now=lambda:datetime.now(timezone.utc).isoformat()
 recorded=now();result=[]
 for p in packets:
  n=int(p['review_id'].split('-')[1]);vals,reasons,claim,cr,cq,meta,mr=D[n]
  assert len(vals)==len(p['requirements'])==len(reasons)
  fields=[]
  for req,v,reason in zip(p['requirements'],vals,reasons):
   rid=req['id']; sources=[p['target_text']]
   if rid=='STORAGE_RECOMMENDATION': sources += [p['reference_context_blocks'][0]['quote'],p['reference_context_blocks'][1]['quote']]
   if rid=='IDENTITY_BINDING':sources=[p['reference_context_blocks'][2]['quote']]
   if rid in ('EMERGENCY_EXCEPTION','ECALL_EXCEPTION'):sources=[p['reference_context_blocks'][3]['quote']]
   if rid=='SATELLITE_SCOPE':sources=[p['reference_context_blocks'][0]['quote']]
   if rid=='CONFIGURED_VERIFICATION':sources=[p['reference_context_blocks'][1]['quote']]
   fields.append({'requirement_id':rid,'value':v,'response_quotes':[p['explanation_ko']],'source_quotes':sources,'rationale':reason})
  assert all(q in p['explanation_ko'] for q in cq)
  overall=0 if 0 in vals or claim is True else None if None in vals or claim is None else 1
  md=p['output_metadata_for_separate_audit']
  match=all(md['citation_'+k]==p['source'][v] for k,v in [('spec','spec_id'),('version','version'),('clause','clause_id')])
  citation_reason='규격·버전·대상 절 필드가 제공 식별자와 정확히 일치한다.' if match else 'citation_clause가 4.6.2.2 / Annex C로 확장되어 정확한 필드 일치는 아니다. Annex C 자체는 제공 문맥에 있으므로 허위 출처로 보지는 않는다.'
  if n==17:citation_reason+=' 설명의 clause의 Annex C라는 표현은 부록 관계를 느슨하게 적었으나 식별자 필드는 맞다.'
  result.append({'review_id':p['review_id'],'reviewer':'coordinator_ai','reviewed_at':now(),'requirement_coverage':fields,'full_context_target_completeness':overall,'unsupported_or_distorted_claim':claim,'claim_evidence_quotes':cq,'claim_rationale':cr,'metadata_inconsistency':meta,'metadata_rationale':mr,'citation_diagnostic':{'matches_source_fields':match,'rationale':citation_reason},'sentence_count_diagnostic':{'sentence_count':3,'within_2_to_4':True,'rationale':'내용을 수동으로 읽어 종결 문장 3개로 확인했다. 규격·버전·절 번호의 마침표는 문장 경계가 아니다.'},'overall_rationale':' / '.join(reasons)+' 미지원·왜곡: '+cr})
 OUT.mkdir()
 out=OUT/'judgments_18.jsonl';out.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in result))
 inputs=[PACKET,ROOT/'experiments/generation_preservation_v1_20260909/reviewer_instructions.md',ROOT/'experiments/generation_preservation_v1_20260909/evaluation_reference.json',ROOT/'experiments/generation_preservation_v1_20260909/protocol.json']
 h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
 notes=OUT/'review_notes.md';notes.write_text('# 진행 AI 의미 평가\n\n18개 설명과 메타데이터, 세 원문의 인용 문맥을 읽고 54개 요구사항을 개별 판정했다. 모든 인용은 입력 그대로 보존했다. 전체 설명을 요구사항별 인용으로 기록해 첫 문장과 후문의 관계도 검토 가능하게 했다.\n\n진행 AI는 실험 설계와 과거 대화 결과를 알고 있다. 이번 판정 전에 현재 조건 키나 새 AI 판정 파일은 열지 않았으며 새로운 응답의 조건별 집계는 하지 않았다. protocol은 진행 기준 확인을 위해 읽었고, 실행 검증 도구는 완료 수·무결성만 반환했다. 메모리의 미확정 보존 원칙을 참고했지만 과거 의미 판정 파일은 새로 열지 않았다. PDF를 다시 시각 판독한 검토가 아니라 패킷의 원문 인용을 읽은 검토다.\n\n각 수치는 코드의 D에 수동으로 지정했으며 코드는 직렬화·인용 검증·전체 완수의 동결식 계산만 수행했다. 문장 수는 설명을 읽어 모두 세 문장으로 판정했다. 다른 검토자와의 차이는 이 봉인 후 별도로 대조한다.\n')
 manifest={'reviewer':'coordinator_ai','serialization_started_at':recorded,'completed_at':now(),'input_file_sha256':{str(p.relative_to(ROOT)):h(p) for p in inputs},'output_file_sha256':{p.name:h(p) for p in [out,notes]},'recording_script_sha256':h(Path(__file__)),'read_boundary':{'condition_key_read_before_seal':False,'other_reviewer_judgments_read_before_seal':False,'prior_design_known':True,'prior_results_known_from_conversation':True,'protocol_read':True,'memory_preference_read':'MEMORY.md:28-29','fresh_pdf_visual_review':False},'judgments':18,'requirement_judgments':54}
 (OUT/'reviewer_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
 for p in OUT.iterdir():p.chmod(0o444)
 OUT.chmod(0o555)
 print(json.dumps({'status':'COORDINATOR_REVIEW_SEALED','records':18,'manifest_sha256':h(OUT/'reviewer_manifest.json')}))
if __name__=='__main__':main()
