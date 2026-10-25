"""Prepare a new, explicitly developmental context ablation before any generation."""
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'experiments/context_microstudy_v1_20260909'
PAGES = ROOT / 'outputs/review/v2_followup_20260909/source_pages'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def extract(stem, page, start, end=None):
    p = PAGES / f'{stem}_p{page}.txt'
    text = p.read_text()
    left = text.index(start)
    right = text.index(end, left + len(start)) if end else len(text)
    quote = text[left:right].strip()
    return {'pdf_path': f'data/source/{stem}.pdf', 'pdf_page': page,
            'page_text_path': str(p.relative_to(ROOT)), 'page_text_sha256': sha(p),
            'quote': quote}


def write(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def main():
    assert not (OUT / 'input_freeze_manifest.json').exists()
    source_packets = [json.loads(x) for x in (ROOT / 'outputs/review/v2_pass2_20260909/packets.jsonl').read_text().splitlines()]
    selected = {ref: next(x for x in source_packets if x['reference_id'] == ref) for ref in ['G010', 'G023', 'G028']}
    ts23, ts24 = 'ts_123501v181200p', 'ts_124501v181200p'
    contexts = {
        'G010': [extract(ts23, 45, 'Figure 4.2.3-3 depicts')],
        'G023': [extract(ts24, 1089, 'Annex C (normative):', 'The following 5GMM parameters'),
                 extract(ts24, 1090, 'The following 5GMM parameters should', 'Each configured NSSAI'),
                 extract(ts24, 1091, 'The allowed NSSAI(s) can be stored', 'The partially allowed NSSAI'),
                 extract(ts24, 1091, 'If the UE is registered for emergency services', 'The "CAG information list"')],
        'G028': [extract(ts23, 133, '5.4.11 Support for integrating', '5.4.11.2 Support'),
                 extract(ts23, 133, '5.4.11.4 Verification', 'NOTE 1:')],
    }
    requirements = {
        'G010': [
            ('CAPABILITY_POSSESSION', '각 SMF의 능력 보유 여부가 선택적임을 보존한다. 이미 모든 SMF가 능력을 보유한다거나 제어 행동의 허용으로 바꾸지 않는다.', 'target'),
            ('BOTH_WITHIN_ONE_SESSION', '능력의 대상은 하나의 PDU Session에서 local UPF와 central UPF 모두를 제어하는 것이다.', 'target'),
        ],
        'G023': [
            ('STORAGE_RECOMMENDATION', '비-SNPN 모드에서 allowed NSSAI를 ME 비휘발성 메모리에 저장하는 권고 및 Annex C 연결을 보존한다. should를 무조건 의무로 바꾸지 않는다.', 'target'),
            ('IDENTITY_BINDING', 'SUPI와 함께 저장하고 일치할 때만 allowed NSSAI를 사용하며 불일치하면 삭제한다는 조건을 보존한다.', 'context'),
            ('EMERGENCY_EXCEPTION', '긴급 서비스 등록 시 USIM/비휘발성 저장은 금지되고 ME에 임시 저장하며 긴급 서비스 등록 해제 시 삭제한다.', 'context'),
            ('ECALL_EXCEPTION', 'eCall only 시 USIM/비휘발성 저장은 금지되고 ME에 임시 저장하며 eCALL-INACTIVE 진입, 전원 꺼짐 또는 USIM 제거 시 삭제한다.', 'context'),
        ],
        'G028': [
            ('LOCATION_UNLESS_RECOMMENDATION', 'PLMN 운용 불가 지역에 UE가 있음을 판단할 충분히 정확한 위치정보가 없는 한 AMF의 요청 거절 또는 UE 등록 해제를 하지 않는 권고를 보존한다.', 'target'),
            ('SATELLITE_SCOPE', 'NR 위성 접속의 위치 검증 문맥으로 범위를 한정한다. 모든 NR 접속에 무조건 확장하지 않는다.', 'context'),
            ('CONFIGURED_VERIFICATION', '망이 PLMN 운용 가능 여부를 검증하도록 설정된 위치 검증 문맥임을 설명한다. 위치 검증 자체를 항상 의무로 바꾸지 않는다.', 'context'),
        ],
    }
    cases = []
    for i, (ref, p) in enumerate(selected.items(), 1):
        question = p['question_ko']
        if ref == 'G023':
            question = 'SNPN access operation mode가 아닌 UE에서 allowed NSSAI를 ME에 저장하는 위치와 방식, 사용 조건 및 긴급 서비스 등록과 eCall only의 저장·삭제 예외를 설명해줘.'
        cases.append({'case_id': f'CTX-{i:03d}', 'development_reference': ref,
                      'source': p['source'], 'pdf': p['pdf'], 'target_text': p['source']['source_text_en'],
                      'question_ko': question, 'original_question_ko': p['question_ko'],
                      'question_changed': question != p['question_ko'], 'context_blocks': contexts[ref],
                      'modal_hint': {'normative_type': {'G010': 'permission', 'G023': 'recommendation', 'G028': 'discouragement'}[ref],
                                     'polarity': 'negative' if ref == 'G028' else 'positive'},
                      'requirements': [{'id': k, 'description_ko': d, 'evidence_role': role} for k, d, role in requirements[ref]]})
    write(OUT / 'cases.json', cases)
    write(OUT / 'protocol.json', {
        'experiment_id': 'CONTEXT_MICROSTUDY_V1_20260909', 'status': 'DRAFT_PENDING_SOURCE_PREFLIGHT',
        'prepared_at': datetime.now(timezone.utc).isoformat(),
        'design': '3 purposively selected previously reviewed sources x 2 context levels x 2 hint levels x 2 repeated calls',
        'case_ids': [c['case_id'] for c in cases], 'context_levels': ['SHORT', 'FULL'],
        'hint_levels': ['NONE', 'MODAL'], 'replicates': [1, 2], 'planned_calls': 24,
        'model': 'gpt-5.4-mini-2026-03-17', 'parameters': {'temperature': 0, 'reasoning_effort': 'none', 'max_output_tokens': 900, 'store': False},
        'execution_order_seed': 'context-microstudy-v1-20260909', 'max_estimated_cost_usd': 0.5,
        'pricing_usd_per_million': {'input': 0.75, 'cached_input': 0.075, 'output': 4.5},
        'pricing_source': 'https://developers.openai.com/api/docs/models/gpt-5.4-mini',
        'pricing_checked_date': '2026-09-09', 'retry_policy': 'no automatic retries; stop on uncertain transport, HTTP error or missing usage',
        'primary_outcome': 'full_context_target_completeness: all frozen target/context requirements are present and accurate; 1/0/null, with item-level evidence',
        'secondary_outcome': 'unsupported_or_distorted_claim: true/false/null, judged against actually supplied target, question and context; omission of unavailable context alone is not distortion',
        'missing_information_policy': 'Requirements absent from SHORT input remain in shared completeness denominator, but are marked INPUT_CONTEXT_GAP and not relabelled as mistranslation. Explicit insufficient-context statements can be faithful yet incomplete.',
        'ambiguity_policy': 'Unresolved semantics remain null; no forced binary. Refusal/empty/incomplete generation counts 0 for pipeline task completeness with separate delivery status.',
        'inferential_policy': 'descriptive counts and case/replicate paired changes only; no p-values, confidence intervals, population or generalization claims; two repeats per source are not independent cases',
        'comparison_policy': 'Compare SHORT/FULL within the same hint level. Hint contrasts are secondary. Same model, parameters, target, question, hint and output limit; FULL only adds context blocks. No C2 or C3 extraction variant in this focused experiment.',
        'review_policy': 'Root AI manual review plus a separate fresh AI context review before conditions/results are compared. Record disagreement; do not overwrite either. Human expert review is not performed.',
        'prior_results_policy': 'No rescoring or replacement of frozen v2 results. New prompt, question scope for CTX-002, context and outcome differ from prior v2.',
        'selection_limits': 'These are development cases selected after observed uncertainty, not held-out clauses. CTX-001 is a context control whose core requirement is already present in SHORT. No tuning or selecting successful retries after outputs.',
        'execution_requires_separate_source_preflight_approval': True,
        'assessment_surface': 'Both semantic outcomes and per-requirement coverage use explanation_ko only. Metadata fields are audited separately against target text; a correct label cannot repair the explanation, and an incorrect metadata label alone does not change explanation completeness. Cross-field contradiction is reported separately as JSON_EXPLANATION_INCONSISTENCY.',
        'compound_requirement_rule': 'Each enumerated conjunct and exception/deletion trigger in a requirement must be preserved for coverage=1; explicit contradiction or omission yields 0; genuinely ambiguous language yields null. Overall target completeness is 0 if any requirement is 0 or an unsupported/distorted claim is confirmed; otherwise null if any unresolved coverage/claim remains; else 1. Exact wording is not required.',
        'hint_contrast_interpretation': 'Both arms receive the same generic modality guidance. MODAL adds only case-specific normative_type/polarity labels for the target sentence; it does not add context-specific exception gold.',
    })
    template = '''당신은 3GPP 규격의 한국어 설명을 작성한다. 아래 대상 문장, 질문과 제공된 문맥만 근거로 대상 규칙의 행위자·규범 강도·행동·적용 범위·예외를 정확히 설명한다. 질문의 전제를 규격 사실로 무조건 채택하지 않는다. 대상 규칙과 무관한 주변 문장 전체를 요약하지 않는다. 대상의 해석에 필요한 조건과 예외는 생략하지 않는다. 문맥에 답을 결정할 정보가 없으면 부족한 정보를 밝히고 추측하지 않는다.
may have the capability처럼 규범 표현이 걸리는 대상을 보존하고, may=허용/선택, can=능력, should=권고, should not=비권고, shall=의무, shall not=금지를 혼동하지 않는다. JSON 유형 라벨만 맞추지 말고 한국어 설명 전체의 명제 연결을 보존한다.
explanation_ko는 필요한 내용을 담은 2~4문장으로 작성한다. 제공한 출처 식별자를 그대로 인용하며 출력은 JSON schema를 따른다. normative_type, actor, condition, action, exception 메타데이터는 대상 영문 문장을 기준으로 작성한다. 추가 문맥의 여러 규범 유형을 하나의 유형으로 합치지 않는다. explanation_ko에는 대상 규칙에 적용되는 문맥 조건과 예외를 함께 설명한다.

## 질문
{{question_ko}}
## 대상 영문 문장
{{target_text}}
## 추가 원문 문맥
{{context_text}}
{{hint_text}}
## 출처 식별자
spec: {{spec_id}}
version: {{version}}
clause: {{clause_id}}
'''
    (OUT / 'prompt_template.md').write_text(template)
    (OUT / 'response_schema.json').write_bytes((ROOT / 'experiments/response_schema.json').read_bytes())
    print(json.dumps({'status': 'DRAFT_READY_FOR_PREFLIGHT', 'cases': 3, 'planned_calls': 24}))


if __name__ == '__main__':
    main()
