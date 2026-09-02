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
const GE = (note = "원문의 한정 조건과 행동이 모두 보존됨") => [1,1,1,1,1,1,0,"",note];
const annotations = {
  R001:[1,1,0,0,"NA",0,1,"CONDITION_DROPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","IMSI·port 조건을 버리고 직접 보유 등 다른 획득 경로를 추가함"],
  R002:[1,0,1,0,"NA",0,1,"MODAL_WEAKENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","권고를 허용으로 약화하고 기존 식별자 유지 대안을 추가함"], R003:G(), R004:G(), R005:G(), R006:G(),
  R007:[1,1,"NA",1,1,1,0,"","W-5GAN만 가능하다는 경로 한정이 보존됨"], R008:G(),
  R009:[1,1,1,0,"NA",0,1,"ACTION_CHANGED;UNSUPPORTED_ADDITION","삭제를 사용·유지로 바꾸고 보안 처리 주장을 추가함"],
  R010:G(), R011:G(), R012:G(),
  R013:[1,0,1,1,"NA",0,1,"POLARITY_FLIPPED;MODAL_STRENGTHENED;UNSUPPORTED_ADDITION","금지를 제공 의무로 반전하고 타이머 용도를 추가함"], R014:G(),
  R015:[1,0,1,0,"NA",0,1,"POLARITY_FLIPPED;MODAL_WEAKENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","중지 금지를 중지 상태 유지 권고로 반전함"],
  R016:GE(), R017:GN("자연어는 지원되는 통신 능력을 보존하며 JSON permission 불일치는 별도 자동 지표에 남김"), R018:G(),
  R019:[1,0,1,0,"NA",0,1,"POLARITY_FLIPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","절차 시작 금지를 대기·재시도 의무로 변경함"],
  R020:[1,0,1,0,"NA",0,1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","선택적 지원을 필수 능력으로 바꾸고 multiple records 의미를 약화함"],
  R021:G(), R022:G(), R023:G(), R024:G(),
  R025:[1,0,0,0,"NA",0,1,"MODAL_STRENGTHENED;CONDITION_DROPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","PDU 설정 조건과 timer 비중지 권고를 교체 절차 유지 의무로 변경함"],
  R026:[1,1,"NA",0,0,0,1,"ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","W-5GAN 한정을 N3IWF·TNGF 경로로 대체함"], R027:GN(),
  R028:[1,1,"NA",0,"NA",0,1,"ACTION_CHANGED;UNSUPPORTED_ADDITION","직접 또는 SCP 경유 통신 대신 HTTP/2·비동기 통신을 추가함"],
  R029:[0,1,1,0,"NA",0,1,"ACTOR_CHANGED;ACTION_CHANGED;UNSUPPORTED_ADDITION","UE의 N3IWF 또는 TNGF 터널 설정을 수동 표현과 N3IWF 중심으로 바꾸고 트래픽 전달을 추가함"],
  R030:[1,1,1,0,"NA",0,1,"ACTION_CHANGED;UNSUPPORTED_ADDITION","보고 전송을 보고 처리·대기 상태로 바꾸고 이유와 이후 동작을 추가함"],
  R031:[1,1,"NA",1,1,1,0,"","W-5GAN 경로 한정이 보존됨"], R032:G(), R033:G(), R034:G(), R035:G(),
  R036:[0,0,0,0,"NA",0,1,"MODAL_STRENGTHENED;ACTOR_CHANGED;CONDITION_DROPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","AMF 권고를 네트워크 의무로 바꾸고 UE별 서로 다른 값이라는 구체 규칙을 추가함"],
  R037:G(),
  R038:[0,0,1,0,"NA",0,1,"MODAL_STRENGTHENED;ACTOR_CHANGED;ACTION_CHANGED;UNSUPPORTED_ADDITION","AMF 권고를 NG-RAN 의무로 바꾸고 RRC 정보 전송 행동을 누락함"],
  R039:G(), R040:G(), R041:G(),
  R042:[1,0,1,0,"NA",0,1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","선택적 포함을 의무로 바꾸고 allowed NSSAI 내 포함 관계를 약화함"],
  R043:G(),
  R044:[0,0,0,0,"NA",0,1,"MODAL_WEAKENED;ACTOR_CHANGED;CONDITION_DROPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","architecture 의무를 NF 권고로 약화하고 직접 상호작용 예외와 결합도 주장을 추가함"],
  R045:G(),
  R046:[1,0,1,0,"NA",0,1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","비활성화를 피하라는 권고를 유지·재설정 의무와 연결 가능성 보장으로 변경함"],
  R047:G(), R048:G(), R049:G(), R050:G(), R051:G(),
  R052:[1,0,0,1,0,0,1,"MODAL_STRENGTHENED;CONDITION_DROPPED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","5GMM context 기반 능력을 등록 완료·PDU 허용 상태의 의무로 변경함"],
  R053:G("if any 조건과 삭제 의무가 보존됨"), R054:GE(),
};

const runDir = path.resolve(import.meta.dirname, "runs", "pilot18_v3_2026-09-02T04-16-08-313Z");
const { headers, rows } = parseCsv(fs.readFileSync(path.join(runDir, "blind_review.csv"), "utf8"));
for (const row of rows) {
  const a = annotations[row.review_id]; if (!a) throw new Error(`missing ${row.review_id}`);
  [row.actor_preserved,row.polarity_preserved,row.condition_preserved,row.action_preserved,row.exception_preserved,row.complete_preservation,row.unsupported_addition,row.error_codes,row.reviewer_note] = a.map(String);
  const applicable = [row.actor_preserved,row.polarity_preserved,row.condition_preserved,row.action_preserved,row.exception_preserved].filter(x => x !== "NA");
  const derived = applicable.every(x => x === "1") && row.unsupported_addition === "0" ? "1" : "0";
  if (derived !== row.complete_preservation) throw new Error(`complete mismatch ${row.review_id}`);
}
const out = "\uFEFF" + [headers.join(","), ...rows.map(r => headers.map(h => cell(r[h])).join(","))].join("\n") + "\n";
fs.writeFileSync(path.join(runDir, "blind_review_pass1.csv"), out);
fs.writeFileSync(path.join(runDir, "blind_pass1_manifest.json"), JSON.stringify({review_type:"masked_row_level_same_reviewer_pass1",completed_at:new Date().toISOString(),rows:rows.length,condition_and_case_id_hidden_during_row_scoring:true,limitation:"Reviewer had prior exposure to aggregate condition results and one identified C1 mismatch before row-level scoring; this is not a fully independent blind review."}, null, 2) + "\n");
console.log(`saved ${rows.length} pass-1 reviews`);
