import fs from "node:fs";
import path from "node:path";

function parseCsv(text) {
  const rows = []; let row = [], field = "", quoted = false;
  for (let i = 0; i < text.length; i++) { const c = text[i];
    if (quoted) { if (c === '"' && text[i + 1] === '"') { field += '"'; i++; } else if (c === '"') quoted = false; else field += c; }
    else if (c === '"') quoted = true; else if (c === ',') { row.push(field); field = ""; } else if (c === '\n') { row.push(field.replace(/\r$/, "")); rows.push(row); row = []; field = ""; } else field += c;
  }
  if (field.length || row.length) { row.push(field.replace(/\r$/, "")); rows.push(row); }
  const [header, ...body] = rows.filter(r => r.some(v => v !== "")); const headers = header.map(h => h.replace(/^\uFEFF/, ""));
  return { headers, rows: body.map(r => Object.fromEntries(headers.map((h, i) => [h, r[i] ?? ""]))) };
}
function cell(v) { const s = String(v ?? ""); return /[",\n]/.test(s) ? `"${s.replaceAll('"', '""')}"` : s; }
const G = (note = "원문의 규범 요소가 자연어 설명에 보존됨") => [1,1,1,1,"NA",1,0,"",note];
const GN = (note = "조건 없는 원문의 행위자·규범 강도·행동이 보존됨") => [1,1,"NA",1,"NA",1,0,"",note];
const GE = (note = "원문의 조건·한정과 행동이 모두 보존됨") => [1,1,1,1,1,1,0,"",note];
const annotations = {
  S001:G(), S002:G(), S003:G(), S004:G(),
  S005:[1,0,1,0,"NA",0,1,"MODAL_WEAKENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","권고를 허용으로 약화하고 기존 식별자 유지 대안을 추가함"],
  S006:G(),
  S007:[1,1,1,0,"NA",0,1,"ACTION_CHANGED;UNSUPPORTED_ADDITION","보고 전송을 보고 처리·대기로 바꾸고 이유와 이후 동작을 추가함"],
  S008:[0,0,1,0,"NA",0,1,"MODAL_STRENGTHENED;ACTOR_CHANGED;ACTION_CHANGED;UNSUPPORTED_ADDITION","AMF 권고를 NG-RAN 의무로 바꾸고 RRC 정보 전송을 누락함"],
  S009:G(), S010:G(), S011:G(),
  S012:[1,0,0,0,"NA",0,1,"MODAL_STRENGTHENED;CONDITION_DROPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","timer 비중지 권고를 만료까지 교체 절차 유지 의무로 변경함"],
  S013:G(), S014:G(),
  S015:[1,1,1,0,"NA",0,1,"ACTION_CHANGED;UNSUPPORTED_ADDITION","삭제를 사용·유지로 바꾸고 보안 처리 주장을 추가함"],
  S016:[1,0,1,0,"NA",0,1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","선택적 multiple-record 지원을 필수 저장 능력으로 변경함"],
  S017:GE(), S018:G(),
  S019:[1,0,0,1,0,0,1,"MODAL_STRENGTHENED;CONDITION_DROPPED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","5GMM context 능력을 등록·PDU 상태 의무로 바꾸고 한정을 변경함"],
  S020:[0,0,0,0,"NA",0,1,"MODAL_WEAKENED;ACTOR_CHANGED;CONDITION_DROPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","architecture 의무를 NF 권고로 약화하고 직접 상호작용 예외를 추가함"],
  S021:[0,0,0,0,"NA",0,1,"MODAL_STRENGTHENED;ACTOR_CHANGED;CONDITION_DROPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","AMF 권고를 네트워크 의무로 바꾸고 UE별 상이한 값 규칙을 추가함"],
  S022:[1,0,1,0,"NA",0,1,"POLARITY_FLIPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","초기 NAS 절차 시작 금지를 대기·재시도 의무로 변경함"],
  S023:G(), S024:GN("자연어는 두 통신 방식을 능력으로 보존하며 JSON permission 오류는 자동 지표에 남김"), S025:G(), S026:G(), S027:G(),
  S028:G(), S029:G(), S030:G(), S031:G(), S032:G(),
  S033:[1,0,1,0,"NA",0,1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","비활성화하지 말라는 권고를 유지·재설정 의무로 변경함"],
  S034:G(), S035:G(),
  S036:[0,1,1,0,"NA",0,1,"ACTOR_CHANGED;ACTION_CHANGED;UNSUPPORTED_ADDITION","UE의 N3IWF 또는 TNGF IPsec 설정을 수동 표현·N3IWF 중심으로 바꾸고 트래픽 전달을 추가함"],
  S037:G(), S038:GE(),
  S039:[1,1,0,0,"NA",0,1,"CONDITION_DROPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","IMSI·port 조회 조건을 버리고 직접 보유 등 다른 경로를 추가함"],
  S040:G(), S041:GN(), S042:G(),
  S043:[1,1,"NA",0,"NA",0,1,"ACTION_CHANGED;UNSUPPORTED_ADDITION","직접 또는 SCP 경유 통신 대신 HTTP/2·비동기 동작을 추가함"],
  S044:G(),
  S045:[1,0,1,1,"NA",0,1,"POLARITY_FLIPPED;MODAL_STRENGTHENED;UNSUPPORTED_ADDITION","금지를 제공 의무로 반전하고 타이머 용도를 추가함"],
  S046:G(),
  S047:[1,0,1,0,"NA",0,1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","선택적 포함을 의무로 바꾸고 allowed NSSAI 내 포함 관계를 약화함"],
  S048:G(),
  S049:[1,1,"NA",1,1,1,0,"","W-5GAN 경로 한정이 보존됨"],
  S050:[1,1,"NA",0,0,0,1,"ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","W-5GAN 한정을 N3IWF·TNGF 경로로 대체함"],
  S051:[1,0,1,0,"NA",0,1,"POLARITY_FLIPPED;MODAL_WEAKENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","중지 금지를 중지 상태 유지 권고로 반전함"],
  S052:G(), S053:G(),
  S054:[1,1,"NA",1,1,1,0,"","W-5GAN만 가능하다는 한정이 보존됨"],
};

const runDir = path.resolve(import.meta.dirname, "runs", "pilot18_v3_2026-09-02T04-16-08-313Z");
const { headers, rows } = parseCsv(fs.readFileSync(path.join(runDir, "blind_review_pass2_blank.csv"), "utf8"));
for (const row of rows) {
  const a = annotations[row.review_id]; if (!a) throw new Error(`missing ${row.review_id}`);
  [row.actor_preserved,row.polarity_preserved,row.condition_preserved,row.action_preserved,row.exception_preserved,row.complete_preservation,row.unsupported_addition,row.error_codes,row.reviewer_note] = a.map(String);
  const applicable = [row.actor_preserved,row.polarity_preserved,row.condition_preserved,row.action_preserved,row.exception_preserved].filter(x => x !== "NA");
  const derived = applicable.every(x => x === "1") && row.unsupported_addition === "0" ? "1" : "0";
  if (derived !== row.complete_preservation) throw new Error(`complete mismatch ${row.review_id}`);
}
const out = "\uFEFF" + [headers.join(","), ...rows.map(r => headers.map(h => cell(r[h])).join(","))].join("\n") + "\n";
fs.writeFileSync(path.join(runDir, "blind_review_pass2.csv"), out);
console.log(`saved ${rows.length} delayed pass-2 reviews`);
