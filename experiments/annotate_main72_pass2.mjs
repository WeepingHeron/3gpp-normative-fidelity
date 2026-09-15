import fs from "node:fs";
import path from "node:path";
import { assertArchivedMainReview } from './assert_archived_main_review.mjs';

function parseCsv(text) {
  const rows = []; let row = [], field = "", quoted = false;
  for (let i = 0; i < text.length; i++) { const c = text[i];
    if (quoted) { if (c === '"' && text[i + 1] === '"') { field += '"'; i++; } else if (c === '"') quoted = false; else field += c; }
    else if (c === '"') quoted = true; else if (c === ',') { row.push(field); field = ""; } else if (c === '\n') { row.push(field.replace(/\r$/, "")); rows.push(row); row = []; field = ""; } else field += c;
  }
  if (field.length || row.length) { row.push(field.replace(/\r$/, "")); rows.push(row); }
  const [header, ...body] = rows.filter(r => r.some(v => v !== ""));
  const clean = header.map(h => h.replace(/^\uFEFF/, ""));
  return body.map(r => Object.fromEntries(clean.map((h, i) => [h, r[i] ?? ""])));
}
function csvCell(v) { const s = String(v ?? ""); return /[",\n]/.test(s) ? `"${s.replaceAll('"', '""')}"` : s; }
function B(actor, polarity, condition, action, exception, unsupported, note) {
  const codes = [];
  if (actor === 0) codes.push("ACTOR_CHANGED");
  if (polarity === 0) codes.push("NORMATIVE_FORCE_CHANGED");
  if (condition === 0) codes.push("CONDITION_CHANGED");
  if (action === 0) codes.push("ACTION_CHANGED");
  if (exception === 0) codes.push("EXCEPTION_CHANGED");
  if (unsupported === 1) codes.push("UNSUPPORTED_ADDITION");
  return [actor, polarity, condition, action, exception, unsupported, codes.join(";"), note];
}

const runDir = path.resolve(process.argv[2] || "");
if (!process.argv[2]) throw new Error("Usage: node experiments/annotate_main72_pass2.mjs <run_directory>");
assertArchivedMainReview(runDir, 'pass2');
const inputPath = path.join(runDir, "blind_review_pass2_blank.csv");
const rows = parseCsv(fs.readFileSync(inputPath, "utf8"));
if (rows.length !== 216) throw new Error(`Expected 216 blind rows, got ${rows.length}`);

// Pass 2 was scored in S-order without opening either condition key or pass-1 row scores.
// Values: actor, polarity, condition, action, exception, unsupported addition, reviewer note.
// Unlisted rows passed all applicable semantic checks.
const bad = {
  S002:B(0,0,1,0,0,1,"새 KAMF 비유도를 유도 여부 표시 의무로 바꿈"),
  S003:B(1,0,"NA",0,"NA",1,"동일·상이 TAI 허용을 access별 TAI 의무로 바꿈"),
  S005:B(1,0,1,1,"NA",1,"5GSM 전송 가능성을 필수 캡슐화 의무로 강화함"),
  S009:B(1,0,1,0,0,1,"rejected NSSAI 제거 허용을 중단·대기·재시도 의무로 바꿈"),
  S013:B(1,0,1,1,"NA",1,"SMF의 선택적 indication을 의무로 강화함"),
  S014:B(1,1,0,0,"NA",1,"single/dual registration을 S1/N1 mode 선택으로 바꾸고 조건을 누락함"),
  S015:B(0,0,0,0,"NA",1,"default NSSAI 변경 허용을 UE의 NAS update 의무로 바꿈"),
  S016:B(0,0,1,0,"NA",1,"single AMF 의무를 두 AMF 사용 가능성으로 반전함"),
  S022:B(0,0,1,0,0,0,"DSCP에 따른 Paging Policy 선택 권고를 일반 marker capability로 축약함"),
  S023:B(1,1,1,0,"NA",1,"MICO 활성화 금지를 등록과 관련 동작 전반으로 확대함"),
  S026:B(1,0,1,0,0,1,"5G NAS context 사용 의무를 미사용·무효화 동작으로 반전함"),
  S033:B(0,0,0,0,0,1,"일부 event만 가능한 제약을 구성자의 직접 구독 허용으로 바꿈"),
  S034:B(0,0,0,0,"NA",1,"Any UE subscription 이동 금지를 AMF 이동 허용·의무로 반전함"),
  S039:B(1,0,0,0,0,1,"모든 관련 AMF 요청 조건을 target AMF 확인 의무로 바꿈"),
  S040:B(0,0,1,0,"NA",1,"Forbidden Area 사용 비권고를 사용 허용으로 반전함"),
  S041:B(0,0,1,0,1,1,"security 활성화 전제조건을 AMF와 UE의 복수 의무로 재구성함"),
  S042:B(1,0,1,0,"NA",1,"구현별 시간 대기 권고를 MICO 해제·미요청 의무로 바꿈"),
  S046:B(1,0,1,1,"NA",1,"PLMN 이동 비권고를 금지와 기존 네트워크 유지 의무로 강화함"),
  S048:B(1,0,1,0,"NA",1,"identity 기억 권고를 저장 금지로 반전함"),
  S049:B(1,0,"NA",0,"NA",1,"native/mapped 가능성을 일반 보안 context 설명으로 대체함"),
  S056:B(1,0,1,1,0,1,"SBI만 사용해야 한다는 요구를 원칙으로 약화하고 별도 권고를 추가함"),
  S057:B(0,0,1,0,0,1,"98%·2% 권고를 주체가 불명확한 의무 기준으로 바꿈"),
  S059:B(1,1,0,1,"NA",0,"서로 다른 TAC에 RAT가 배치되어야 하는 조건을 누락함"),
  S064:B(1,1,1,0,"NA",0,"5G-IA0·5G-EA0과 대상 IE를 일반적인 알고리즘으로 축약함"),
  S066:B(0,0,1,0,0,1,"보안 context 활성화 전제를 여러 준비 의무로 확대함"),
  S071:B(1,1,0,0,"NA",1,"handover 중 생성 가능성을 handover 후 생성으로 바꿈"),
  S072:B(1,0,"NA",1,0,1,"저장 권고를 의무로 강화하고 annex C 대신 PLMN별 재사용을 추가함"),
  S073:B(0,0,1,0,"NA",1,"RAT restriction 고려 권고를 지원 불가 target 금지로 바꿈"),
  S074:B(1,1,0,1,"NA",0,"관련 RAT의 서로 다른 TAC 배치 조건을 누락함"),
  S075:B(1,0,1,0,"NA",1,"AUTHENTICATION REJECT 종료 권고를 절차 계속 의무로 반전함"),
  S077:B(1,1,1,0,"NA",1,"ngKSI 삭제를 새 context에 맞춘 대체 처리로 바꿈"),
  S078:B(0,1,"NA",0,0,1,"서로 다른 VPLMN 경로와 inter-PLMN mobility를 누락함"),
  S083:B(1,0,0,0,0,1,"거절 비권고와 위치 예외를 위치정보 확보 의무로 바꿈"),
  S085:B(1,0,1,0,"NA",1,"Non-Allowed Area 정보를 사용하지 말라는 요구를 사용 허용으로 반전함"),
  S086:B(1,0,1,0,"NA",1,"lower layer NSSAI 제공 금지를 허용으로 반전함"),
  S092:B(0,0,1,0,1,1,"authorized NF의 접근 가능성을 UDSF 구현 의무로 바꿈"),
  S093:B(1,0,1,0,0,1,"첫 access 완료 전 등록 금지를 병행 등록 허용으로 반전함"),
  S095:B(0,1,1,0,0,1,"새 KAMF 비유도를 target AMF의 표시 동작으로 바꿈"),
  S098:B(1,0,1,0,0,1,"PLMN/SNPN identity 기억 권고를 일반 정보 기억 의무로 바꿈"),
  S099:B(1,0,0,1,"NA",1,"timer 설정 권고를 의무로 강화하고 duration/start 기준을 축약함"),
  S100:B(1,0,1,0,0,1,"authentication 생략 후 SMC 진행 허용을 두 절차 중단 권고로 바꿈"),
  S101:B(1,1,1,0,"NA",1,"key invalid 간주 요구를 연관 키 삭제로 바꿈"),
  S102:B(1,0,1,0,0,1,"sub-network 가능성을 단정하고 트래픽·시간 동기 역할을 추가함"),
  S107:B(0,1,0,0,"NA",1,"두 구체 조건과 secure exchange 목적을 일반 context 재사용으로 바꿈"),
  S108:B(1,0,1,0,"NA",1,"MBS join 비권고를 join 허용으로 반전함"),
  S111:B(0,1,"NA",0,0,1,"최대 7개를 최대 8개로 변경함"),
  S116:B(0,0,1,0,"NA",1,"SUCI 사용 의무를 5G-S-TMSI 사용 설명으로 바꿈"),
  S122:B(1,1,"NA",0,"NA",1,"필수 네 보안 항목을 일반 보안 정보로 축약함"),
  S127:B(0,0,1,0,"NA",1,"Paging Policy 선택 권고를 application의 DSCP 설정 의무로 바꿈"),
  S131:B(1,1,"NA",0,0,0,"지원 PLMN/SNPN과 connectivity type 대신 지원 여부만 광고함"),
  S134:B(0,0,0,1,"NA",1,"NSSAI 변경 허용을 UE의 수신 후 갱신 의무로 바꿈"),
  S135:B(1,0,1,0,0,1,"7개 요청 비거절 권고를 일부 요청 우선 처리 허용으로 축약함"),
  S141:B(1,0,1,1,1,0,"authorized data만 변경하는 의무를 단순 허용으로 약화함"),
  S142:B(1,0,1,1,"NA",1,"all-PLMN 표시 비권고를 금지로 강화함"),
  S144:B(0,0,0,0,"NA",1,"N1 기반 control-plane NAS 지원 의무를 일반 NAS 가능성으로 약화함"),
  S145:B(1,0,1,0,"NA",1,"all-PLMN 표시 비권고를 동일 적용 의무로 바꿈"),
  S148:B(1,1,1,0,"NA",1,"eKSI와 mapped type을 누락하고 ngKSI 연결 대상을 바꿈"),
  S149:B(1,0,1,0,"NA",1,"configured NSSAI 제공 금지를 제공 의무로 반전함"),
  S152:B(1,1,0,1,"NA",1,"선택적 dual-UPF 제어에 역할 분담과 경로 분할 주장을 추가함"),
  S158:B(0,1,"NA",0,"NA",1,"session 해제 금지에 종료·허용 조건 예외를 추가함"),
  S165:B(1,0,0,0,0,1,"capability 미전송 권고를 허용 범위 전송 의무로 바꿈"),
  S166:B(1,0,1,0,"NA",1,"mobility registration update 권고를 종료 보고 의무로 바꿈"),
  S173:B(1,0,1,1,1,0,"7개 요청 비거절 권고를 금지로 강화함"),
  S175:B(0,1,0,1,0,1,"비요구 한계를 누락하고 필요한 경우라는 조건과 배치 허용을 추가함"),
  S176:B(1,1,1,0,0,1,"Disaster Condition 영역 TAI를 재난 로밍 허용 TAI로 바꿈"),
  S177:B(0,0,1,0,"NA",1,"PGW 또는 SMF/UPF 선택 허용을 gNB·AMF 구성으로 대체함"),
  S178:B(1,0,1,0,"NA",1,"새 AUTHENTICATION REQUEST 권고를 추상적 재인증 의무로 바꿈"),
  S183:B(1,1,0,0,0,1,"N3IWF/TNGF와 trusted/untrusted 경로 대응을 누락함"),
  S184:B(1,0,1,0,"NA",1,"slice 기반 동작 금지를 일반 절차 수행 의무로 바꿈"),
  S185:B(1,0,1,1,"NA",1,"PLMN 이동 비권고를 금지로 강화함"),
  S186:B(0,0,1,0,0,1,"UE의 5GC 사용 비권고를 AMF의 cause 전달 의무로 바꿈"),
  S188:B(1,0,1,0,0,1,"무결성 검사 전 처리 금지를 일반 메시지 처리 의무로 바꿈"),
  S189:B(0,0,1,0,"NA",1,"AMF의 즉시 해제 비권고를 네트워크의 일반 처리 의무로 바꿈"),
  S190:B(0,0,1,0,0,1,"authorized NF 접근 가능성을 NF별 범위 사용 의무로 바꿈"),
  S196:B(1,0,1,0,"NA",0,"Non-Allowed Area 소속 TA 권고를 영역 포함 의무로 바꿈"),
  S198:B(1,0,1,0,"NA",1,"all-PLMN 비할당 권고를 제한적 registration area 설정 의무로 바꿈"),
  S202:B(1,0,1,0,"NA",1,"동시 등록 허용을 사전 등록 의무로 바꿈"),
  S209:B(1,0,1,0,"NA",1,"Registration Request 거절 비권고를 거절 의무로 반전함"),
  S212:B(0,0,1,0,0,1,"HPLMN의 단일 default NSSAI 구성 허용을 UE의 사용 권고로 바꿈"),
  S216:B(1,0,1,0,"NA",1,"REGISTRATION COMPLETE 제공 가능성을 Registration Request 포함 의무로 바꿈")
};

const allowed = new Set(["0", "1", "NA"]); const seen = new Set();
for (const row of rows) {
  if (seen.has(row.review_id)) throw new Error(`Duplicate review_id ${row.review_id}`); seen.add(row.review_id);
  const fallback = [1, 1, row.gold_condition ? 1 : "NA", 1, row.gold_exception ? 1 : "NA", 0, "", "의미 보존"];
  const values = bad[row.review_id] || fallback;
  if (values.length !== 8) throw new Error(`Invalid annotation length for ${row.review_id}`);
  [row.actor_preserved, row.polarity_preserved, row.condition_preserved, row.action_preserved,
    row.exception_preserved, row.unsupported_addition, row.error_codes, row.reviewer_note] = values.map(String);
  const applicable = [row.actor_preserved, row.polarity_preserved, row.condition_preserved, row.action_preserved, row.exception_preserved].filter(v => v !== "NA");
  for (const value of [...applicable, row.unsupported_addition]) if (!allowed.has(value) || value === "NA") throw new Error(`Invalid score for ${row.review_id}`);
  row.complete_preservation = String(Number(applicable.every(v => v === "1") && row.unsupported_addition === "0"));
}
for (const id of Object.keys(bad)) if (!seen.has(id)) throw new Error(`Unknown annotation ${id}`);

const headers = Object.keys(rows[0]);
const output = "\uFEFF" + [headers.join(","), ...rows.map(r => headers.map(h => csvCell(r[h])).join(","))].join("\n") + "\n";
fs.writeFileSync(path.join(runDir, "blind_review_pass2.csv"), output);
const manifestPath = path.join(runDir, "blind_pass2_completion_manifest.json");
const completedAt = fs.existsSync(manifestPath) ? JSON.parse(fs.readFileSync(manifestPath, "utf8")).completed_at : new Date().toISOString();
fs.writeFileSync(manifestPath, JSON.stringify({
  review_type: "delayed_masked_row_level_codex_single_reviewer_pass2",
  completed_at: completedAt,
  rows: rows.length,
  reviewed_range: "S001-S216",
  condition_keys_and_pass1_row_scores_not_consulted_during_row_scoring: true,
  semantic_source: "source_text_en and frozen gold fields compared against explanation_ko; JSON output fields used only as secondary context",
  limitation: "This is delayed same-reviewer agreement, not an independent human expert review. The reviewer had prior-day exposure to the experiment and pass-1 aggregate results.",
  failed_complete_preservation_rows: Object.keys(bad).length
}, null, 2) + "\n");
console.log(JSON.stringify({status:"PASS", rows:rows.length, complete_preservation:rows.filter(r=>r.complete_preservation==="1").length, failed_complete_preservation:rows.filter(r=>r.complete_preservation==="0").length}, null, 2));
