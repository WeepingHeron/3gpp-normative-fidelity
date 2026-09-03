import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    path = ROOT / "data/main_freeze_manifest.json"
    manifest = json.loads(path.read_text(encoding="utf-8"))
    failures = []
    if manifest.get("status") != "FROZEN_SINGLE_ANNOTATOR":
        failures.append("freeze status mismatch")
    dataset = ROOT / manifest["dataset_path"]
    if sha256(dataset) != manifest.get("dataset_sha256"):
        failures.append("dataset SHA-256 mismatch")
    for relative, expected in manifest.get("file_sha256", {}).items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            failures.append(f"frozen file changed: {relative}")
    print(f"frozen_files={len(manifest.get('file_sha256', {}))}")
    print(f"failures={len(failures)}")
    for failure in failures:
        print(f"FAIL {failure}")
    if failures:
        raise SystemExit(1)
    print(f"PASS frozen dataset {manifest['dataset_sha256']}")


if __name__ == "__main__":
    main()
