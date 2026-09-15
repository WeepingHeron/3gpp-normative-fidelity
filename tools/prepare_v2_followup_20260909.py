"""Record a bounded source follow-up; stage review materials without rescoring."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'outputs/review/v2_followup_20260909'
ADJ = ROOT / 'outputs/review/v2_adjudication_20260909'
P2 = ROOT / 'outputs/review/v2_pass2_20260909'
COHORT = ROOT / 'outputs/review/v2_cohort_analysis_20260909'
BIND = ROOT / 'outputs/review/v2_pass2_completed_20260909/input_provenance_bindings.jsonl'
RUBRIC = ROOT / 'experiments/scoring_v2_frozen_20260908.md'
DOC = ROOT / 'docs/29_report_and_followup_review_2026-09-09.md'
REFS = {
    'G010': {
        'stem': 'ts_123501v181200p', 'pages': [45], 'rules': ['R1', 'R3'],
        'finding': 'may가 능력 보유에 걸린다는 원문은 재확인했다. 한국어 설명의 두 번째 문장 이는가 보유 여부를 명확히 정정하는지는 PDF로 결정할 수 없다.',
        'question': '두 문장을 함께 읽을 때 보유 여부의 선택성이 명확히 보존되는가? 능력 보유와 행동 허용의 대상, 지시어의 선행 표현을 인용해 판단한다.',
        'next_context_scope': '여러 PDU Session과 두 SMF를 설명하는 직전 문단 및 원문을 함께 검토한다. 원문 명제는 이미 R1에 반영돼 있으며, 응답 지시어를 원문 문맥으로 대신 해석하지 않는다.',
    },
    'G023': {
        'stem': 'ts_124501v181200p', 'pages': [98, 1089, 1090, 1091, 1092, 1093], 'rules': ['R7', 'section 2', 'section 6'],
        'finding': 'Annex C.1의 비-SNPN 모드와 긴급 등록/eCall 저장 예외, C.2의 SNPN 모드·자격증명 분기를 확인했다. 원래 입력에 없던 부속서 본문을 소급 필수 명제로 추가할 수 없고, 참조 유지만으로 충분한지에 대한 기존 채점 범위 불확실성이 남는다.',
        'question': '제공 문장이 Annex C를 참조할 때 부속서 참조를 유지한 설명의 완전 보존을 동결 R7/출처 규칙만으로 확정할 수 있는가? 추가 규칙이 필요하면 별도 제안으로 기록하고 미확정을 유지한다.',
        'next_context_scope': '새 사례는 비-SNPN 일반 등록, 긴급 등록, eCall only, SNPN 모드를 구분한다. C.1/C.2 제목과 해당 저장·삭제·신원 일치 규정을 함께 제공할 문맥 경계를 먼저 확정한다. 이 페이지 묶음은 Annex C 전체가 아니다.',
    },
    'G028': {
        'stem': 'ts_123501v181200p', 'pages': [132, 133, 134], 'rules': ['section 2', 'section 6'],
        'finding': '5.4.11은 NR 위성 접속 절이며 5.4.11.4의 망 설정과 위치 검증 문맥을 재확인했다. 과거 제공 문장에 없는 상위 범위를 사후 필수 명제로 바꾸지 않으며 입력 문맥 부족과 응답 오역을 분리한다.',
        'question': '원래 제공 문장/질문과 판정자 전용 NR 위성 접속 문맥을 구분했을 때 동결 규칙으로 설명을 확정할 수 있는가? 상위 범위의 누락과 명시적인 잘못된 일반화를 구분해 근거를 남긴다.',
        'next_context_scope': '새 버전은 5.4.11 제목·5.4.11.1 범위 및 5.4.11.4의 설정/위치 검증 문맥을 제공한다. 일반 NR 전체에 대한 규칙으로 확장하지 않는다. 주변 절과 NOTE는 경계 확인용이며 자동 필수 명제가 아니다.',
    },
}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def rows(p):
    return [json.loads(line) for line in p.read_text().splitlines() if line]


def write(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.suffix == '.jsonl':
        p.write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in value))
    else:
        p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def now():
    return datetime.now(timezone.utc).isoformat()


def build():
    assert not (OUT / 'completion_manifest.json').exists()
    stamp = now()
    packets = {p['review_id']: p for p in rows(P2 / 'packets.jsonl')}
    bindings = {p['review_id']: p for p in rows(BIND)}
    unresolved = rows(ADJ / 'unresolved_register.jsonl')
    request_checks = rows(OUT / 'archived_request_checks.jsonl')
    contexts = []
    for ref, info in REFS.items():
        page_records = []
        for page in info['pages']:
            name = f"{info['stem']}_p{page}"
            txt = OUT / 'source_pages' / (name + '.txt')
            png = OUT / 'source_pages' / (name + '.png')
            page_records.append({'pdf_page': page, 'printed_page': page - 1,
                                 'text_path': str(txt.relative_to(OUT)), 'text_sha256': sha(txt),
                                 'image_path': str(png.relative_to(OUT)), 'image_sha256': sha(png),
                                 'page_text': txt.read_text()})
        pdf = ROOT / 'data/source' / (info['stem'] + '.pdf')
        contexts.append({'reference_id': ref, 'status': 'DRAFT_CONTEXT_FOR_REVIEW_NOT_MODEL_INPUT',
                         'pdf_path': str(pdf.relative_to(ROOT)), 'pdf_sha256': sha(pdf),
                         'provenance': 'adjudication_only_context',
                         'supplied_to_original_model_as_extra_context': False,
                         'finding': info['finding'], 'next_context_scope': info['next_context_scope'],
                         'pages': page_records, 'exhaustive_annex_or_cross_reference_review': False})
    write(OUT / 'context_candidates.jsonl', contexts)
    dispositions = []
    for u in unresolved:
        p, b, info = packets[u['review_id']], bindings[u['review_id']], REFS[u['reference_id']]
        checks = [{k: r[k] for k in ['path', 'line_number', 'stage', 'request_sha256']}
                  for r in request_checks if r['case_id'] == b['case_id'] and r['condition'] == b['condition']]
        dispositions.append({**u, 'case_id': b['case_id'], 'condition': b['condition'],
                             'review_pass': 'source_followup_v1_20260909', 'reviewer': 'Codex (same evaluator)',
                             'recorded_at': stamp, 'treatment_version': 'posthoc_treatment_v1_20260908',
                             'rubric_sha256': sha(RUBRIC), 'semantic_judgment': 'UNRESOLVED',
                             'response_quote': p['explanation_ko'], 'source_quote': p['source']['source_text_en'],
                             'followup_finding': info['finding'], 'applicable_rules': info['rules'],
                             'source_context_reference': u['reference_id'],
                             'archived_request_bindings': checks,
                             'direct_request_verified': bool(checks),
                             'prior_input_availability': b['original_input_availability'],
                             'score_promotion_justified': False, 'score_changed': False})
    write(OUT / 'followup_dispositions.jsonl', dispositions)
    selected = [p for p in packets.values() if p['reference_id'] in REFS]
    # New stable order. This hides labels, but is not a claim of independent blinding.
    selected.sort(key=lambda p: hashlib.sha256(('followup-v1:' + p['review_id']).encode()).hexdigest())
    review, key, blanks = [], [], []
    for i, p in enumerate(selected, 1):
        rid = f'FOLLOWUP-{i:03d}'
        b = bindings[p['review_id']]
        availability = b['original_input_availability']
        generator_source = (availability['generator_if_extraction_usable']['source']
                            if b['condition'] == 'C3' else availability['source'])
        review.append({'review_id': rid, 'reference_id': p['reference_id'],
                       'source': p['source'], 'pdf': p['pdf'], 'question_ko': p['question_ko'],
                       'reference_source_available_to_original_generator': generator_source,
                       'additional_pdf_context_available_to_original_generator': False,
                       'delivery_status': p['delivery_status'], 'explanation_ko': p['explanation_ko'],
                       'context_reference': p['reference_id'], 'review_question': REFS[p['reference_id']]['question']})
        key.append({'review_id': rid, 'prior_review_id': p['review_id'], 'reference_id': p['reference_id'],
                    'case_id': b['case_id'], 'condition': b['condition'],
                    'response_record_sha256': b['response_binding']['record_sha256']})
        blanks.append({'review_id': rid, 'reviewer': '', 'qualification_or_role': '', 'reviewed_at': '',
                       'semantic_judgment': '', 'complete_preservation': None,
                       'source_provenance_quotes': [], 'response_evidence_quotes': [],
                       'rationale': '', 'frozen_rule_sufficient': None, 'new_rule_proposal_if_needed': ''})
    write(OUT / 'reviewer/packets_15.jsonl', review)
    write(OUT / 'reviewer/judgments_blank_15.jsonl', blanks)
    write(OUT / 'coordinator/keys_15.jsonl', key)
    write(OUT / 'summary.json', {
        'status': 'CURRENT_REPORT_RECORDED_FOLLOWUP_NO_SCORE_CHANGE', 'recorded_at': stamp,
        'current_report': str((ROOT / 'docs/28_v2_cohort_results_2026-09-09.md').relative_to(ROOT)),
        'reported_analysis_manifest_sha256': sha(COHORT / 'completion_manifest.json'),
        'current_union_counts': dict(Counter(r['semantic_judgment'] for r in rows(ADJ / 'adjudicated_view_255.jsonl'))),
        'followup_unresolved_slots': len(dispositions), 'references': 3, 'pdf_pages_checked': 10,
        'archived_requests_directly_verified': 9, 'next_review_packets': 15,
        'next_review_completed': False, 'independent_expert_review_completed': False,
        'current_scores_changed': 0, 'new_model_generation_calls': 0, 'paper_updated': False,
        'new_information': 'Expanded page context and direct archived-request provenance; no new semantic basis that resolves the frozen uncertainty.',
    })


def validate():
    subprocess.run([sys.executable, str(ROOT / 'tools/summarize_v2_cohorts_20260909.py'), 'verify'],
                   cwd=ROOT, check=True, capture_output=True, text=True)
    originals = {p['review_id']: p for p in rows(P2 / 'packets.jsonl')}
    bindings = {p['review_id']: p for p in rows(BIND)}
    unresolved = {p['review_id']: p for p in rows(ADJ / 'unresolved_register.jsonl')}
    decisions = rows(OUT / 'followup_dispositions.jsonl')
    assert len(decisions) == 8 and {d['review_id'] for d in decisions} == set(unresolved)
    for d in decisions:
        p, u = originals[d['review_id']], unresolved[d['review_id']]
        assert d['semantic_judgment'] == 'UNRESOLVED' and d['complete_preservation'] is None
        assert d['response_record_sha256'] == u['response_record_sha256']
        assert d['response_quote'] == p['explanation_ko'] and d['source_quote'] == p['source']['source_text_en']
        assert d['rubric_sha256'] == sha(RUBRIC) and not d['score_changed'] and not d['score_promotion_justified']
    checks = rows(OUT / 'archived_request_checks.jsonl')
    assert len(checks) == 9
    assert Counter((c['condition'], c['stage']) for c in checks) == {('C3', 'extraction'): 3, ('C3', 'generation'): 3, ('C1M', 'generation'): 3}
    for c in checks:
        raw = rows(ROOT / c['path'])[c['line_number'] - 1]
        digest = hashlib.sha256(json.dumps(raw['request'], ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()
        assert c['case_id'] == raw['case_id'] and c['request_sha256'] == raw['request_sha256'] == digest
        assert c['stage'] == raw.get('stage', 'generation')
        assert c['input'] == raw['request']['input']
        assert all(flag == (marker in c['input']) for marker, flag in c['pdf_context_markers_present'].items())
    contexts = rows(OUT / 'context_candidates.jsonl')
    assert {c['reference_id'] for c in contexts} == set(REFS)
    assert sum(len(c['pages']) for c in contexts) == 10
    for c in contexts:
        assert sha(ROOT / c['pdf_path']) == c['pdf_sha256']
        assert c['supplied_to_original_model_as_extra_context'] is False
        for p in c['pages']:
            assert (OUT / p['text_path']).read_text() == p['page_text']
            assert sha(OUT / p['text_path']) == p['text_sha256'] and sha(OUT / p['image_path']) == p['image_sha256']
    keys = rows(OUT / 'coordinator/keys_15.jsonl')
    review = rows(OUT / 'reviewer/packets_15.jsonl')
    blanks = rows(OUT / 'reviewer/judgments_blank_15.jsonl')
    assert len(keys) == len(review) == len(blanks) == 15
    assert Counter(k['reference_id'] for k in keys) == {r: 5 for r in REFS}
    assert len({k['prior_review_id'] for k in keys}) == 15
    for ref in REFS:
        assert {k['condition'] for k in keys if k['reference_id'] == ref} == {'C0', 'C1', 'C2', 'C3', 'C1M'}
    for k, r, b in zip(keys, review, blanks):
        assert k['review_id'] == r['review_id'] == b['review_id']
        orig, bind = originals[k['prior_review_id']], bindings[k['prior_review_id']]
        assert r['source'] == orig['source'] and r['explanation_ko'] == orig['explanation_ko']
        assert k['response_record_sha256'] == bind['response_binding']['record_sha256']
        assert not ({'condition', 'semantic_judgment', 'prior_review_id', 'gold_guidance'} & r.keys())
        assert b['reviewer'] == b['semantic_judgment'] == b['rationale'] == '' and b['complete_preservation'] is None
    summary = json.loads((OUT / 'summary.json').read_text())
    assert summary['current_union_counts'] == {'PASS': 167, 'FAIL': 79, 'UNRESOLVED': 8, 'NOT_SCORED': 1}
    assert summary['reported_analysis_manifest_sha256'] == sha(COHORT / 'completion_manifest.json')
    assert not summary['next_review_completed'] and summary['current_scores_changed'] == 0
    return {'ok': True, 'verified_at': now(), 'retained_unresolved': 8, 'source_pages': 10,
            'archived_requests': 9, 'staged_packets': 15, 'old_analysis_unchanged': True,
            'semantic_truth_automatically_verified': False}


def finish():
    assert DOC.exists() and (OUT / 'reviewer/REVIEW_GUIDE.md').exists()
    assert not (OUT / 'completion_manifest.json').exists()
    write(OUT / 'validation_report.json', validate())
    inputs = [COHORT / 'completion_manifest.json', ADJ / 'completion_manifest.json',
              ADJ / 'adjudicated_view_255.jsonl', ADJ / 'unresolved_register.jsonl',
              P2 / 'packets.jsonl', BIND, RUBRIC]
    inputs += sorted({ROOT / c['pdf_path'] for c in rows(OUT / 'context_candidates.jsonl')})
    inputs += sorted({ROOT / c['path'] for c in rows(OUT / 'archived_request_checks.jsonl')})
    write(OUT / 'completion_manifest.json', {
        'status': 'FOLLOWUP_COMPLETE_NO_SCORE_CHANGE_NEXT_REVIEW_STAGED', 'completed_at': now(),
        'file_sha256': {str(p.relative_to(OUT)): sha(p) for p in sorted(OUT.rglob('*')) if p.is_file()},
        'support_file_sha256': {str(p.relative_to(ROOT)): sha(p) for p in [DOC, Path(__file__).resolve()]},
        'input_file_sha256': {str(p.relative_to(ROOT)): sha(p) for p in inputs},
    })
    for p in OUT.rglob('*'):
        if p.is_file():
            p.chmod(0o444)


def verify():
    manifest = json.loads((OUT / 'completion_manifest.json').read_text())
    inventory = {str(p.relative_to(OUT)) for p in OUT.rglob('*') if p.is_file() and p.name != 'completion_manifest.json'}
    assert inventory == set(manifest['file_sha256'])
    for rel, digest in manifest['file_sha256'].items():
        assert sha(OUT / rel) == digest
    for rel, digest in {**manifest['support_file_sha256'], **manifest['input_file_sha256']}.items():
        assert sha(ROOT / rel) == digest
    print(json.dumps(validate(), ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['build', 'finish', 'verify'])
    {'build': build, 'finish': finish, 'verify': verify}[parser.parse_args().command]()
