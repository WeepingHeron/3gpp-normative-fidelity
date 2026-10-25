"""Serialize individually authored review decisions; no semantic inference rules."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'outputs/review/context_microstudy_v1_20260909'
OUT = BASE / 'root_review'

# Each entry was manually authored after reading its complete masked packet.
# Format: per-requirement (value, reason), unsupported/distorted, claim reason,
# metadata inconsistency, metadata reason. None records explicit uncertainty.
DECISIONS = {
 'MCR-001': ([(0,'해서는 안 되며와 취하지 않아야 한다로 should not을 강제 금지로 높인다.'),(0,'NR 위성 접속 범위가 설명에 없다. 이 문맥은 생성 입력에도 없었다.'),(0,'망의 위치 검증 설정 문맥을 설명하지 않는다. 추가 문맥 미제공이다.')], True,'해서는 안 되며는 원문의 비권고와 다르며 뒤의 문장도 강제 금지를 반복한다.',True,'discouragement 라벨과 설명의 강제 금지가 상충한다. condition 필드는 위치정보 예외를 전제로 옮겼다.'),
 'MCR-002': ([(1,'능력을 가질 수도 있음으로 각 SMF의 선택적 보유를 유지한다.'),(1,'하나의 PDU Session에서 local과 central UPF 모두가 능력의 대상이다.')],False,'추가 배치 조건을 추측하지 않는 부연은 기존 능력 보유 명제를 취소하지 않으며 미지원 세부를 단정하지 않는다.',False,'permission과 능력 보유 action이 설명의 중첩 범위와 일치한다.'),
 'MCR-003': ([(0,'해서는 안 되며 및 해서는 안 됩니다가 비권고를 금지로 강화한다.'),(0,'NR 위성 접속 범위를 설명하지 않는다. 입력 문맥 부족이다.'),(0,'망이 위치 검증을 하도록 설정되는 문맥이 없다. 입력에도 없다.')],True,'정확한 위치정보 예외를 담아도 should not을 강제 금지로 바꾼 오류는 남는다.',True,'discouragement 라벨과 한국어 금지가 다르며 exception 필드는 예외 자체 대신 위치정보 부족 시 금지를 담는다.'),
 'MCR-004': ([(0,'해서는 안 된다는 금지와 예외적으로 허용된다는 표현으로 비권고 관계를 바꾼다.'),(0,'NR 위성 접속으로 한정하지 않는다. 문맥은 입력에 없었다.'),(0,'위치정보 정확도 언급은 망의 검증 설정 조건을 복원하지 않는다.')],True,'비권고를 금지로 높였고 예외를 거절 허용의 확정 조건으로 설명한다.',True,'discouragement와 설명의 강제 금지가 상충한다. 메타 exception도 허용 조건으로 바뀌었다.'),
 'MCR-005': ([(0,'저장되어야 하며로 저장 권고를 의무로 강화한다.'),(0,'SUPI 결합·사용 시 일치·불일치 삭제가 없다. 추가 근거 미제공이다.'),(0,'긴급 예외를 확인할 수 없다고 밝혀 해당 저장·삭제 조건을 완수하지 못한다.'),(0,'eCall 예외를 확인할 수 없다고 밝혀 임시 저장·삭제 계기가 없다.')],True,'부속서 예외에 대한 유보 자체는 충실하지만 직접 문장의 저장 권고를 의무로 바꾼다.',True,'recommendation 라벨과 저장되어야 한다는 설명이 상충한다. 비-SNPN은 질문에서 제한한 사례 범위이며 조항 전체가 그 모드만 대상으로 한다고 확정할 근거는 아니다.'),
 'MCR-006': ([(0,'저장해야 하며는 should의 저장 권고를 의무로 높인다.'),(0,'사용 조건을 특정하지 못한다고 밝히며 SUPI 규정을 생략한다.'),(0,'긴급 등록 예외를 확인할 수 없다고 밝혀 완수하지 못한다.'),(0,'eCall 저장·삭제 예외를 확인하지 못했다고 명시한다.')],True,'문맥 부족을 밝힌 것은 적절하나 첫 문장의 저장 의무는 원문 강도를 보존하지 않는다.',True,'recommendation 라벨과 설명의 저장해야 하며가 상충한다.'),
 'MCR-007': ([(0,'경우에만 할 수 있다와 해서는 안 됩니다가 비권고를 강제 금지/허용 관계로 바꾼다.'),(1,'NR satellite access를 사용하는 UE의 위치 검증 맥락을 명시한다.'),(0,'위치 검증을 하도록 망이 설정된다는 문맥은 설명하지 않는다.')],True,'위성 접속 범위는 보존했지만 직접 should not을 금지로 바꾼 독립적인 오류가 있다.',True,'discouragement 라벨은 설명의 강제 금지와 상충한다. citation 필드에 spec/version/clause 접두어도 포함됐으며 이는 별도 메타데이터 오류다.'),
 'MCR-008': ([(1,'저장하는 것이 권고됨을 명시하고 annex C의 지정 방식과 연결한다. 방식 준거를 따르는 설명은 저장 자체를 의무로 바꾸지 않는다.'),(0,'SUPI 결합·일치·삭제가 없다. 해당 문맥은 제공되지 않았다.'),(0,'긴급 예외를 입력으로 확인하지 못했다고 밝혀 요구사항은 미완수다.'),(0,'eCall 예외를 확인하지 못했다고 밝혀 임시 저장·삭제 계기는 생략됐다.')],False,'권고 강도를 유지하고 없는 부속서 예외를 추측하지 않는다. 비-SNPN은 질문이 제한한 사례 범위로 읽으며 모든 조항에 대한 배타적 범위 주장은 없다.',False,'recommendation 라벨은 설명과 맞는다. 메타데이터의 비-SNPN 범위는 질문에서 온 것으로 직접 원문의 유일 범위로 확대하지 않는다.'),
 'MCR-009': ([(0,'등록 해제해서는 안 됩니다로 비권고를 금지로 강화하며 다음 문장의 경우에만 적용은 정보 부족 시 비권고와도 어긋난다.'),(0,'NR 위성 접속이라는 범위를 설명하지 않는다. FULL에 제공됐으므로 입력 부족이 아닌 생략이다.'),(0,'PLMN 운용 불가 판단 자체를 말할 뿐 망의 검증 설정 문맥은 없다.')],True,'금지로의 강화와 운용 불가라고 판단하는 경우에만 규칙이 적용된다는 범위 이동이 있다.',True,'discouragement 라벨과 금지 설명이 다르다. 메타 condition/exception에도 필요조건과 예외 구분 문제가 있다.'),
 'MCR-010': ([(1,'능력을 가질 수 있다로 선택적 능력 보유를 직접 보존한다.'),(1,'하나의 PDU Session 안의 local과 central UPF 모두를 명시한다.')],None,'해당 기능을 갖는 경우에만 적용된다는 후문이 제어 구성의 적용을 뜻하는지, 이미 능력을 보유한 경우에만 규정이 적용된다는 추가 조건인지 불명확하다. 첫 문장은 정확하므로 후문의 미지원 조건 여부를 임의 확정하지 않는다.',False,'permission/action은 첫 문장과 일치한다. 후문의 적용 지시 대상 문제는 설명의 의미 불확실성으로 따로 남긴다.'),
 'MCR-011': ([(1,'저장해야 하는 것이 아니라 권고한다고 명시적으로 강도를 구분하고 annex C에 연결한다.'),(1,'SUPI와 저장될 수 있음, 일치 시에만 사용, 불일치 삭제가 모두 있다.'),(0,'긴급 등록 시 금지·임시 ME 저장은 있으나 긴급 서비스 등록 해제 시 삭제가 설명에서 빠졌다.'),(0,'eCall의 세 삭제 계기는 있지만 eCall에 적용되는 비휘발성/USIM 금지와 임시 ME 저장을 명시하지 않는다.')],False,'추가 문맥의 명시적 주장은 근거가 있다. 긴급/eCall 일부 조건의 생략을 별도의 허위 주장으로 세지 않는다.',False,'권고 라벨과 설명은 일치한다. metadata는 target-only 지시보다 문맥 조건을 과도하게 포함하나 그 정보로 설명의 누락을 채우지 않는다.'),
 'MCR-012': ([(0,'해서는 안 됩니다와 취하지 말아야 합니다는 should not을 강제 금지로 바꾼다.'),(0,'제공된 NR 위성 접속 범위가 설명에서 빠졌다.'),(0,'위치정보 기반 판단을 말하지만 망이 검증을 하도록 설정된 문맥은 없다.')],True,'비권고를 금지로 강화한다. 위치정보 판단이라는 부연으로 권고 강도가 복원되지 않는다.',True,'discouragement 라벨과 강제 금지가 상충한다. citation 일부에 식별자 접두어를 포함한 별도 형식 오류가 있다.'),
 'MCR-013': ([(1,'능력을 가질 수 있음을 허용한다는 첫 문장이 능력 보유의 선택성을 보존하고 후문도 비의무를 명시한다.'),(1,'한 PDU Session에서 두 UPF 모두를 제어하는 능력이라는 대상을 유지한다.')],False,'후문의 구성 가능성과 두 UPF 범위는 첫 문장의 선택적 능력을 설명한다. 모든 SMF의 이미 확정된 능력이나 별도 전제는 추가하지 않는다.',False,'permission과 have the capability의 중첩 action이 한국어 설명과 일치한다.'),
 'MCR-014': ([(1,'각 SMF가 능력을 가질 수도 있다고 말하고 의무가 아님을 보충한다.'),(1,'하나의 PDU Session과 local/central UPF 모두를 명시한다.')],False,'추가 배치·절차를 확인할 수 없다고 한 것은 제공 범위를 구분한 것으로 원문 명제를 왜곡하지 않는다.',False,'permission과 능력 보유 action, 명시된 세션 범위가 설명과 맞는다.'),
 'MCR-015': ([(0,'경우에만 할 수 있음과 해서는 안 됩니다로 비권고를 강제 제한으로 높인다.'),(1,'NR satellite access 위치 검증 문맥을 명시한다.'),(0,'망의 위치 검증 설정 조건은 명시하지 않는다.')],True,'위성 접속 문맥이 추가됐어도 should not의 강도 강화가 남는다.',False,'prohibition 라벨은 잘못된 설명과는 일치하지만 원문 target의 discouragement를 틀리게 분류했다. 메타 오류와 필드 간 모순을 구별한다.'),
 'MCR-016': ([(0,'저장되어야 하며로 should를 저장 의무로 바꾼다.'),(1,'앞 문장의 USIM SUPI 결합과 후문의 일치 시 사용·불일치 삭제가 연결된다.'),(0,'긴급 서비스의 임시 저장은 있으나 등록 해제 시 삭제가 빠졌다.'),(0,'eCall의 삭제 시점은 있지만 해당 모드의 USIM/비휘발성 금지와 임시 ME 저장이 설명에 없다.')],True,'문맥의 shall 삭제 요구와 별개인 기본 저장 should를 의무로 높였다.',True,'recommendation 라벨과 저장 의무 설명이 상충한다. metadata에 긴급 등록 해제 삭제가 있어도 explanation 누락을 복구하지 않는다.'),
 'MCR-017': ([(1,'저장해야 한다고 권고된다는 전체 문장에 권고가 최상위 강도로 명시돼 있고 annex C 연결도 보존한다.'),(0,'SUPI와 사용·삭제 조건을 설명하지 않는다. 해당 문맥 미제공이다.'),(0,'긴급 등록 조건과 예외를 확인하지 못했다고 밝혀 관련 규칙은 없다.'),(0,'eCall 저장·삭제 예외를 확인하지 못했다고 명시한다.')],False,'제공 범위의 한계를 밝히며 없는 조건을 단정하지 않는다. 해야라는 어절만 떼지 않고 권고된다는 전체 구문으로 강도를 판단한다.',False,'recommendation 라벨은 설명의 최상위 권고와 일치한다. condition 필드에 저장 위치가 들어간 것은 역할 분류의 별도 약점이다.'),
 'MCR-018': ([(1,'능력을 가질 수도 있음과 선택적 capability라는 보충으로 선택적 보유가 명확하다.'),(1,'한 PDU Session 안의 local과 central UPF 둘 다를 보존한다.')],False,'추가 조건을 알 수 없다고 밝힐 뿐 미지원 배치나 의무를 추가하지 않는다.',False,'permission과 능력 보유 action이 설명과 일치한다.'),
 'MCR-019': ([(0,'저장해야 하며는 원문의 저장 권고를 의무로 바꾼다.'),(1,'USIM SUPI와 함께 저장, 일치 시만 사용, 불일치 삭제를 모두 명시한다.'),(0,'긴급 서비스 등록 해제 시 삭제가 한국어 설명에 없다.'),(0,'eCall의 세 삭제 계기는 있으나 해당 모드의 저장 금지와 임시 ME 저장은 설명하지 않는다.')],True,'기본 저장 권고를 의무로 강화한다. 추가 삭제 조건 일부의 누락과 이 강도 오류를 분리한다.',True,'recommendation 라벨과 저장해야 한다는 설명이 다르다. metadata의 상세 예외는 explanation을 대신하지 않는다.'),
 'MCR-020': ([(1,'능력을 가질 수도 있다고 하고 허용/선택이며 의무가 아니라고 보충한다.'),(1,'하나의 PDU Session 내 로컬/중앙 UPF 모두가 능력의 대상이다.')],False,'추가 조건을 확인하지 못한다고 제한해 미지원 사실을 단정하지 않는다.',False,'permission과 선택적 능력 보유 설명이 일치한다.'),
 'MCR-021': ([(1,'능력을 가질 수도 있음과 may의 허용/선택을 함께 보존한다.'),(1,'한 PDU Session 안 local과 central UPF 모두를 명시한다.')],False,'제공된 원문 범위만 반영한다고 설명하며 새 조건·역할을 추가하지 않는다.',False,'permission과 have the capability action, 단일 세션 범위가 설명과 같다.'),
 'MCR-022': ([(0,'저장되어야 하며는 should의 저장 권고를 의무로 바꾼다.'),(1,'SUPI와 결합해 저장, USIM과 저장 SUPI 일치 시만 사용, 불일치 삭제가 있다.'),(0,'긴급 서비스의 금지·임시 저장은 있지만 등록 해제 시 삭제가 빠졌다.'),(None,'eCall에도 동일하게 저장하지 않는다는 표현과 세 삭제 계기는 있다. 동일하게가 임시 ME 저장까지 이어받는지 금지만 받는지 불명확해 임시 저장 보존을 확정하지 않는다.')],True,'기본 저장을 의무화한 명시적 오류가 있으며 eCall 임시 저장의 모호성과 별개다.',False,'obligation 라벨은 잘못된 의무 설명과 일치하지만 원문 should와는 다르다. metadata가 eCall 임시 저장과 긴급 등록 해제 삭제를 명시해도 설명의 누락/모호성을 고치지 않는다.'),
 'MCR-023': ([(1,'능력을 가질 수도 있다고 하고 may의 허용/선택과 비의무를 명시한다.'),(1,'하나의 PDU Session에서 local과 central UPF 모두를 제어하는 능력이다.')],False,'능력 보유의 선택성과 범위를 설명 전체가 유지하며 추가 제약은 확인되지 않는다고 제한한다.',True,'한국어는 outer may의 선택적 능력 보유를 보존하지만 metadata는 capability와 control 행동만 남겨 target의 규범 대상과 맞지 않는다. 이 메타 오류로 설명 점수를 낮추지 않는다.'),
 'MCR-024': ([(0,'경우에만 제어 조치 가능과 해서는 안 된다로 비권고를 금지/허용 조건으로 강화한다.'),(0,'NR 위성 접속 범위가 없다. 원래 짧은 입력에도 없었다.'),(0,'정확도에 관한 설명만 있고 망의 위치 검증 설정 문맥은 없다.')],True,'직접 원문의 should not을 강제 금지로 바꾸고 충분한 정보가 있는 경우의 허용으로 바꾼다. 다른 사유에 대해 유보한 것은 이 오류를 복구하지 않는다.',False,'prohibition 라벨은 강제 금지 설명과 일치하지만 target의 discouragement를 틀리게 분류했다.'),
}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    assert not (OUT / 'reviewer_manifest.json').exists()
    packets = [json.loads(l) for l in (BASE/'reviewer/packets_24.jsonl').read_text().splitlines()]
    assert len(packets) == len(DECISIONS) == 24
    stamp = datetime.now(timezone.utc).isoformat()
    result = []
    for p in packets:
        coverage, claim, claim_reason, meta, meta_reason = DECISIONS[p['review_id']]
        assert len(coverage) == len(p['requirements'])
        values = [v for v, reason in coverage]
        overall = 0 if 0 in values or claim is True else None if None in values or claim is None else 1
        result.append({'review_id': p['review_id'], 'reviewer': 'root AI; protocol designer; prior study known; no fresh reviewer judgments read',
                       'reviewed_at': stamp,
                       'requirement_coverage': [{'requirement_id': req['id'], 'value': v,
                                                'response_quotes': [p['explanation_ko']], 'rationale': reason}
                                               for req, (v, reason) in zip(p['requirements'], coverage)],
                       'full_context_target_completeness': overall,
                       'unsupported_or_distorted_claim': claim, 'claim_evidence_quotes': [p['explanation_ko']],
                       'claim_rationale': claim_reason, 'metadata_inconsistency': meta, 'metadata_rationale': meta_reason,
                       'overall_rationale': ' / '.join([reason for v, reason in coverage] + [claim_reason]),
                       'input_context_gap_requirement_ids': [r['id'] for r in p['requirements'] if r['evidence_role']=='context' and not p['additional_context_supplied_to_generator']],
                       'source_evidence': {'target': p['target_text'], 'context_quotes': [b['quote'] for b in p['reference_context_blocks']],
                                           'additional_context_supplied_to_generator': p['additional_context_supplied_to_generator']}})
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT/'judgments_24.jsonl'
    target.write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in result))
    # Verification checks quotation/structure and arithmetic only, never semantics.
    for r, p in zip(result, packets):
        assert all(q in p['explanation_ko'] for q in r['claim_evidence_quotes'])
        assert all(v['rationale'] and all(q in p['explanation_ko'] for q in v['response_quotes']) for v in r['requirement_coverage'])
        assert all(type(x['value']) is int and x['value'] in (0,1) or x['value'] is None for x in r['requirement_coverage'])
    inputs = [BASE/'reviewer/packets_24.jsonl',BASE/'reviewer/REVIEW_GUIDE.md',ROOT/'experiments/context_microstudy_v1_20260909/protocol.json',
              ROOT/'experiments/context_microstudy_v1_20260909/cases.json',ROOT/'outputs/review/context_microstudy_preflight_20260909/review.json']
    manifest = {'reviewer': 'root AI', 'review_count': 24, 'completed_at': stamp,
                'timing_note': 'Timestamp is final recording after individual reading and manual decisions, not per-row reading duration.',
                'other_reviewer_judgments_read_before_completion': False,
                'known_design_and_prior_study': True, 'human_expert_validation': False,
                'method': 'Each coverage and claim/metadata judgment was manually authored; code combines authored items by the frozen outcome rule and verifies serialization.',
                'input_file_sha256': {str(p.relative_to(ROOT)):sha(p) for p in inputs},
                'file_sha256': {'judgments_24.jsonl': sha(target)},
                'authored_decision_source': str(Path(__file__).resolve().relative_to(ROOT)),
                'authored_decision_source_sha256': sha(Path(__file__).resolve())}
    (OUT/'reviewer_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    for p in OUT.iterdir():
        p.chmod(0o444)
    print(json.dumps({'status':'ROOT_MANUAL_REVIEW_SEALED','rows':24,'other_review_not_read':True,'recorded_at':stamp}))


if __name__ == '__main__':
    main()
