import fs from "node:fs";
import path from "node:path";

function parseCsv(text) {
  const rows = []; let row = [], field = "", quoted = false;
  for (let i = 0; i < text.length; i++) { const c = text[i];
    if (quoted) { if (c === '"' && text[i + 1] === '"') { field += '"'; i++; } else if (c === '"') quoted = false; else field += c; }
    else if (c === '"') quoted = true; else if (c === ',') { row.push(field); field = ""; } else if (c === '\n') { row.push(field.replace(/\r$/, "")); rows.push(row); row = []; field = ""; } else field += c;
  }
  if (field.length || row.length) { row.push(field.replace(/\r$/, "")); rows.push(row); }
  const [header, ...body] = rows.filter(r => r.some(v => v !== ""));
  const clean = header.map(h => h.replace(/^\uFEFF/, ""));
  return { headers: clean, rows: body.map(r => Object.fromEntries(clean.map((h, i) => [h, r[i] ?? ""]))) };
}
function csvCell(v) { const s = String(v ?? ""); return /[",\n]/.test(s) ? `"${s.replaceAll('"', '""')}"` : s; }

const annotations = {
  S001: [1,1,1,1,"NA",1,0,"","규범 강도와 행위가 모두 보존됨"],
  S002: [1,0,1,1,"NA",0,1,"POLARITY_FLIPPED;MODAL_STRENGTHENED;UNSUPPORTED_ADDITION","금지를 의무로 반전하고 타이머 용도를 추가함"],
  S003: [1,1,1,1,"NA",1,0,"","허용과 조회 조건이 보존됨"],
  S004: [1,1,"NA",1,"NA",1,0,"","직접 또는 SCP 경유 통신 능력이 보존됨"],
  S005: [1,1,1,1,"NA",1,0,"","비활성만을 이유로 해제하지 말라는 권고가 보존됨"],
  S006: [0,0,1,0,"NA",0,1,"MODAL_STRENGTHENED;ACTOR_CHANGED;ACTION_CHANGED;UNSUPPORTED_ADDITION","권고를 의무로 강화하고 행위자와 RRC 정보 전송 행위를 변경함"],
  S007: [1,0,1,0,"NA",0,1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","부정 권고를 의무로 강화하고 재설정 행위를 추가함"],
  S008: [1,1,1,1,"NA",1,0,"","허용과 조회 조건이 보존됨"],
  S009: [1,1,1,1,"NA",1,0,"","금지 규범이 보존됨"],
  S010: [1,0,0,0,"NA",0,1,"MODAL_STRENGTHENED;CONDITION_DROPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","허용을 능력으로 바꾸고 IMSI 및 포트 조건과 행위를 변경함"],
  S011: [1,1,1,1,"NA",1,0,"","권고와 RRC 정보 전송 방식이 보존됨"],
  S012: [1,0,"NA",0,"NA",0,1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","통신 능력을 허용으로 바꾸고 HTTP/2 및 구독 동작을 새로 추가함"],
  S013: [1,1,1,1,"NA",1,0,"","부정 권고가 정확히 보존됨"],
  S014: [1,1,1,1,"NA",1,0,"","조건부 의무가 보존됨"],
  S015: [1,1,"NA",1,"NA",1,0,"","직접 및 간접 통신 능력이 보존됨"],
  S016: [1,1,1,1,"NA",1,0,"","권고와 갱신 방식이 보존됨"],
  S017: [1,1,1,1,"NA",1,0,"","조건부 의무가 보존됨"],
  S018: [0,0,0,0,"NA",0,1,"MODAL_WEAKENED;ACTOR_CHANGED;CONDITION_DROPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","의무를 권고로 약화하고 행위자·조건·행위를 변경하며 설계 주장을 추가함"],
};

const runDir = path.resolve(import.meta.dirname, "runs", "dry6_v3_2026-09-01T02-43-40-134Z");
const input = path.join(runDir, "blind_review_pass2_blank.csv");
const output = path.join(runDir, "blind_review_pass2.csv");
const { headers, rows } = parseCsv(fs.readFileSync(input, "utf8"));
for (const row of rows) {
  const a = annotations[row.review_id];
  if (!a) throw new Error(`Missing annotation for ${row.review_id}`);
  [row.actor_preserved, row.polarity_preserved, row.condition_preserved, row.action_preserved,
    row.exception_preserved, row.complete_preservation, row.unsupported_addition,
    row.error_codes, row.reviewer_note] = a.map(String);
}
fs.writeFileSync(output, "\uFEFF" + [headers.join(","), ...rows.map(r => headers.map(h => csvCell(r[h])).join(","))].join("\n") + "\n");
console.log(`saved ${rows.length} independent pass-2 annotations to ${output}`);
