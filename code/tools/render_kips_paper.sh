#!/bin/sh
# Reproduce the verified DOCX/PDF export with bundled document tools.
set -eu
task_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
runtime_root=/Users/taehoon/.cache/codex-runtimes/codex-primary-runtime/dependencies
skill_root=/Users/taehoon/.codex/plugins/cache/openai-primary-runtime/documents/26.905.11957/skills/documents
task_tmp=$(mktemp -d /tmp/kips-render.XXXXXX)
task_document=${1:-"$task_root/outputs/paper/ACK2026_3GPP_normative_fidelity_draft_v2.docx"}
cat > "$task_tmp/fonts.conf" <<EOF
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
<dir>/System/Library/Fonts</dir>
<dir>/System/Library/Fonts/Supplemental</dir>
<dir>/Users/taehoon/Library/Fonts</dir>
<cachedir>$task_tmp/font-cache</cachedir>
</fontconfig>
EOF
FONTCONFIG_FILE="$task_tmp/fonts.conf" "$runtime_root/python/bin/python3" "$skill_root/render_docx.py" \
  "$task_document" \
  --output_dir "$task_tmp/render" --emit_pdf
printf '%s\n' "$task_tmp/render"
