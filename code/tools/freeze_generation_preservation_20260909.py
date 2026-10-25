"""Freeze reviewed inputs before generation, or verify their unchanged hashes."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'experiments/generation_preservation_v1_20260909'
REVIEW = ROOT / 'outputs/review/generation_preservation_preflight_20260909'
RUN = ROOT / 'experiments/runs/generation_preservation_v1_20260909'
MANIFEST = BASE / 'input_freeze_manifest.json'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(p):
    return json.loads(p.read_text())


def verify():
    frozen = read(MANIFEST)
    assert frozen['status'] == 'FROZEN_BEFORE_GENERATION' and frozen['planned_calls'] == 18
    for p, expected in frozen['file_sha256'].items():
        assert sha(ROOT / p) == expected, p
    assert (BASE / 'request_plan.jsonl').read_bytes() == (BASE / 'request_plan.preview.jsonl').read_bytes()
    subprocess.run([sys.executable, str(ROOT / 'tools/prepare_generation_preservation_plan_20260909.py'), 'verify'], check=True, capture_output=True)
    subprocess.run(['node', str(ROOT / 'experiments/run_generation_preservation_20260909.mjs'), 'verify-freeze'], check=True, capture_output=True)
    return {'ok': True, 'status': frozen['status'], 'frozen_at': frozen['frozen_at'],
            'planned_calls': 18, 'bound_files': len(frozen['file_sha256']),
            'input_manifest_sha256': sha(MANIFEST), 'live_api_calls_by_this_tool': 0}


def freeze():
    assert not MANIFEST.exists() and not RUN.exists(), 'Already frozen or generation directory exists'
    protocol = read(BASE / 'protocol.json')
    assert protocol['status'] == 'READY_TO_FREEZE'
    review = read(REVIEW / 'design_review.json')
    assert review['freeze_approved'] is True and review['open_blockers'] == []
    for p, expected in review['reviewed_input_sha256'].items():
        assert sha(ROOT / p) == expected, p
    assert read(REVIEW / 'runtime_test_report.json')['ok'] is True
    assert read(REVIEW / 'packet_test_report.json')['ok'] is True
    assert read(REVIEW / 'runtime_test_report.json')['runner_sha256'] == sha(ROOT / 'experiments/run_generation_preservation_20260909.mjs')
    assert read(REVIEW / 'packet_test_report.json')['adapter_sha256'] == sha(ROOT / 'tools/prepare_generation_preservation_review_20260909.py')
    subprocess.run([sys.executable, str(ROOT / 'tools/prepare_generation_preservation_plan_20260909.py'), 'verify'], check=True, capture_output=True)
    subprocess.run(['node', str(ROOT / 'experiments/run_generation_preservation_20260909.mjs'), 'check-draft'], check=True, capture_output=True)
    with (BASE / 'request_plan.jsonl').open('xb') as f:
        f.write((BASE / 'request_plan.preview.jsonl').read_bytes())
    support = ['docs/31_generation_preservation_experiment_plan_2026-09-09.md',
               'tools/prepare_generation_preservation_plan_20260909.py',
               'tools/prepare_generation_preservation_review_20260909.py',
               'tools/freeze_generation_preservation_20260909.py',
               'experiments/run_generation_preservation_20260909.mjs',
               'experiments/test_generation_preservation_runtime_20260909.mjs',
               'tools/test_generation_preservation_packets_20260909.py']
    paths = list(BASE.iterdir()) + [ROOT / p for p in support] + [p for p in REVIEW.rglob('*') if p.is_file()]
    old = ROOT / protocol['source_experiment']
    paths += [old / 'input_freeze_manifest.json'] + [ROOT / p for p in read(old / 'input_freeze_manifest.json')['file_sha256']]
    for c in read(BASE / 'generator_inputs.json'):
        for block in c['context_blocks']:
            paths.extend([ROOT / block['pdf_path'], ROOT / block['page_text_path']])
    paths = sorted(set(paths))
    frozen = {'experiment_id': protocol['experiment_id'], 'status': 'FROZEN_BEFORE_GENERATION',
              'frozen_at': datetime.now(timezone.utc).isoformat(), 'planned_calls': 18,
              'live_api_calls_at_freeze': 0, 'generation_authorized_by_freeze': False,
              'design_review': 'COORDINATOR_AI_REVIEW_WITH_LIMITATIONS',
              'file_sha256': {str(p.relative_to(ROOT)): sha(p) for p in paths}}
    with MANIFEST.open('x') as f: f.write(json.dumps(frozen, ensure_ascii=False, indent=2) + '\n')
    # Read-only files plus hashes detect accidental changes; this is not external timestamp certification.
    for p in list(BASE.iterdir()) + [ROOT / p for p in support] + [p for p in REVIEW.rglob('*') if p.is_file()]:
        p.chmod(0o444)
    BASE.chmod(0o555)
    return verify()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['freeze', 'verify'])
    mode = parser.parse_args().mode
    print(json.dumps(freeze() if mode == 'freeze' else verify()))
