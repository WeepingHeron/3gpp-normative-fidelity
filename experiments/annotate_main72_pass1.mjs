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
  return body.map(r => Object.fromEntries(header.map((h, i) => [h.replace(/^\uFEFF/, ""), r[i] ?? ""])));
}
function csvCell(v) { const s = v == null ? "" : String(v); return /[",\n]/.test(s) ? `"${s.replaceAll('"', '""')}"` : s; }

const runDir = path.resolve(process.argv[2] || "");
if (!process.argv[2]) throw new Error("Usage: node experiments/annotate_main72_pass1.mjs <run_directory>");
const inputPath = path.join(runDir, "blind_review.csv");
const rows = parseCsv(fs.readFileSync(inputPath, "utf8"));
if (rows.length !== 216) throw new Error(`Expected 216 blind rows, got ${rows.length}`);

// Values: actor, polarity, condition, action, exception, unsupported addition, codes, note.
// Unlisted rows passed all applicable semantic checks during the masked row-level review.
const bad = {
  R003:[0,0,0,0,0,1,"MODAL_STRENGTHENED;ACTOR_CHANGED;CONDITION_DROPPED;ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","일부 event만 가능한 제약을 버리고 구성자의 직접 구독 허용으로 변경함"],
  R009:[0,0,1,0,0,1,"MODAL_STRENGTHENED;ACTOR_CHANGED;ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","98% 권고를 네트워크 의무와 불명확한 기준으로 바꾸고 2% 한계를 누락함"],
  R014:[1,0,1,0,"NA",1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","가능성을 의무로 강화하고 REGISTRATION COMPLETE를 등록 요청으로 변경함"],
  R015:[1,0,1,0,"NA",1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","PGW 또는 SMF/UPF 선택을 gNB와 AMF 구성으로 대체함"],
  R017:[1,1,"NA",0,"NA",0,"ACTION_CHANGED","필수 네 항목을 일반적인 보안 정보로 축약함"],
  R018:[1,0,0,0,0,1,"MODAL_STRENGTHENED;CONDITION_DROPPED;ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","거절 비권고와 위치정보 예외를 위치정보 확보 의무로 변경함"],
  R019:[1,1,1,0,"NA",1,"ACTION_CHANGED;UNSUPPORTED_ADDITION","eKSI 값과 mapped type 설정을 누락하고 ngKSI 연결 대상을 바꿈"],
  R026:[0,0,1,0,"NA",1,"MODAL_STRENGTHENED;ACTOR_CHANGED;ACTION_CHANGED;UNSUPPORTED_ADDITION","AMF의 연결 즉시 해제 비권고를 네트워크의 일반 처리 의무로 바꿈"],
  R031:[0,0,1,0,"NA",1,"POLARITY_FLIPPED;ACTOR_CHANGED;ACTION_CHANGED;UNSUPPORTED_ADDITION","Forbidden Area 사용 비권고를 사용 허용으로 반전함"],
  R037:[1,1,1,0,"NA",0,"ACTION_CHANGED","5G-IA0와 5G-EA0 및 대상 IE를 적절한 알고리즘으로 축약함"],
  R038:[1,1,0,0,0,0,"CONDITION_DROPPED;ACTION_CHANGED;EXCEPTION_DROPPED","N3IWF/TNGF와 trusted/untrusted 경로 대응을 누락함"],
  R039:[1,0,1,0,"NA",1,"MODAL_WEAKENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","N1 기반 control-plane NAS 지원 의무를 일반 NAS 가능성으로 약화함"],
  R040:[1,0,1,0,"NA",1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","mobility registration update 권고를 종료 보고 의무로 바꿈"],
  R042:[1,0,1,1,"NA",1,"MODAL_STRENGTHENED;UNSUPPORTED_ADDITION","이동 비권고를 금지와 기존 네트워크 유지 의무로 강화함"],
  R043:[0,0,0,0,"NA",1,"POLARITY_FLIPPED;ACTOR_CHANGED;CONDITION_DROPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","subscription 이동 금지를 AMF의 이전 의무로 반전함"],
  R044:[1,0,1,0,"NA",1,"POLARITY_FLIPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","lower layer NSSAI 제공 금지를 허용으로 반전함"],
  R046:[1,1,1,0,"NA",1,"ACTION_CHANGED;UNSUPPORTED_ADDITION","MICO 활성화 금지를 등록과 모든 MICO 관련 동작으로 확대함"],
  R048:[0,0,1,0,1,1,"MODAL_STRENGTHENED;ACTOR_CHANGED;ACTION_CHANGED;UNSUPPORTED_ADDITION","security 활성화의 전제조건을 AMF와 UE의 의무로 재구성함"],
  R055:[1,0,1,0,0,1,"MODAL_STRENGTHENED;ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","sub-network 가능성을 단정하고 트래픽·시간 동기 역할을 추가함"],
  R057:[1,0,1,1,"NA",1,"MODAL_STRENGTHENED;UNSUPPORTED_ADDITION","SMF의 선택적 indication을 의무로 강화함"],
  R058:[1,1,1,0,"NA",1,"ACTION_CHANGED;UNSUPPORTED_ADDITION","키를 invalid로 간주하는 요구를 키 자료 삭제로 변경함"],
  R061:[0,0,1,0,"NA",1,"MODAL_WEAKENED;ACTOR_CHANGED;ACTION_CHANGED;UNSUPPORTED_ADDITION","single AMF 의무를 두 AMF 구성 가능성으로 반전함"],
  R065:[1,0,1,0,0,1,"POLARITY_FLIPPED;MODAL_STRENGTHENED;ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","authentication 생략 후 SMC 진행 허용을 두 절차 중단 권고로 바꿈"],
  R066:[0,1,0,0,"NA",1,"ACTOR_CHANGED;CONDITION_DROPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","보안 컨텍스트 사용 조건과 secure exchange 목적을 일반 재사용으로 바꿈"],
  R067:[0,0,1,1,"NA",1,"MODAL_STRENGTHENED;ACTOR_CHANGED;UNSUPPORTED_ADDITION","5GSM 전송 가능성을 UE와 네트워크의 의무로 강화함"],
  R068:[1,0,1,1,1,1,"MODAL_STRENGTHENED;UNSUPPORTED_ADDITION","거절 비권고를 예외 외에는 불가능한 금지로 강화함"],
  R076:[0,0,0,0,"NA",1,"MODAL_STRENGTHENED;ACTOR_CHANGED;CONDITION_DROPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","NSSAI 변경 허용을 UE의 수신 후 갱신 의무로 바꿈"],
  R079:[1,0,1,0,"NA",1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","동시 등록 가능성을 사전 등록 의무로 변경함"],
  R082:[1,0,1,0,"NA",1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","all-PLMN 표시 비권고를 동일 적용 의무로 변경함"],
  R083:[1,1,1,1,"NA",1,"UNSUPPORTED_ADDITION","local·central UPF의 역할과 경로 분할 주장을 추가함"],
  R087:[1,0,1,0,"NA",1,"POLARITY_FLIPPED;MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","AUTHENTICATION REJECT로 종료 권고를 인증 계속 의무로 반전함"],
  R090:[1,1,"NA",0,0,1,"ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","최대 7을 최대 8로 변경함"],
  R091:[1,0,1,0,"NA",1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","구현별 시간 대기 권고를 MICO 해제·미요청 의무로 바꿈"],
  R093:[0,1,"NA",1,0,1,"ACTOR_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","예외 없는 session 해제 금지에 종료·허용 조건 예외를 추가함"],
  R094:[0,0,1,0,0,1,"MODAL_STRENGTHENED;ACTOR_CHANGED;ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","HPLMN의 단일 NSSAI 구성 허용을 UE의 사용 권고로 바꿈"],
  R095:[1,0,1,0,"NA",1,"POLARITY_FLIPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","MBS join 비권고를 join 허용으로 반전함"],
  R103:[0,0,1,0,0,1,"MODAL_STRENGTHENED;ACTOR_CHANGED;ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","security 활성화 전제조건을 여러 보안 준비 의무로 확대함"],
  R107:[1,1,0,1,"NA",0,"CONDITION_DROPPED","관련 RAT가 서로 다른 TAC에 배치되어야 하는 조건을 누락함"],
  R108:[0,0,1,0,0,1,"MODAL_STRENGTHENED;ACTOR_CHANGED;ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","UE의 5GC 사용 비권고를 AMF의 cause 전달 의무로 바꿈"],
  R114:[0,1,0,1,0,1,"ACTOR_CHANGED;CONDITION_DROPPED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","비요구 한계를 누락하고 필요한 경우라는 조건과 배치 허용을 추가함"],
  R115:[1,1,1,0,0,1,"ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","Disaster Condition 영역 TAI를 재난 로밍 허용 TAI로 바꿈"],
  R120:[0,0,1,1,1,1,"MODAL_STRENGTHENED;ACTOR_CHANGED;UNSUPPORTED_ADDITION","authorized NF의 접근 가능성을 구현·배포 의무로 바꿈"],
  R122:[1,0,0,0,0,1,"MODAL_STRENGTHENED;CONDITION_DROPPED;ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","모든 관련 AMF의 load 제한 요청 조건을 대상 AMF 확인 의무로 바꿈"],
  R125:[1,0,1,0,0,1,"MODAL_WEAKENED;ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","7개 요청 비거절 권고를 일부 요청 수용 가능성으로 축약함"],
  R126:[1,0,1,1,0,1,"MODAL_WEAKENED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","SBI만 사용해야 함을 원칙으로 약화하고 별도 설계 권고를 추가함"],
  R129:[0,0,1,0,0,1,"POLARITY_FLIPPED;ACTOR_CHANGED;ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","새 KAMF 비유도를 유도 여부 표시 의무로 변경함"],
  R134:[1,0,"NA",0,"NA",1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","같거나 다른 TAI 허용을 access별 TAI 의무로 바꿈"],
  R138:[1,0,1,1,1,1,"MODAL_STRENGTHENED;UNSUPPORTED_ADDITION","7개 요청 비거절 권고를 금지로 강화함"],
  R140:[1,0,1,0,0,1,"MODAL_STRENGTHENED;ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","PLMN/SNPN별 identity 또는 list 기억 권고를 일반 정보 기억 의무로 바꿈"],
  R141:[1,0,1,0,"NA",1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","새 AUTHENTICATION REQUEST 전송 권고를 추상적 재인증 의무로 바꿈"],
  R143:[0,0,1,0,0,1,"MODAL_STRENGTHENED;ACTOR_CHANGED;ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","authorized NF 접근과 구현 책임을 NF별 범위 사용 의무로 바꿈"],
  R145:[1,0,1,0,"NA",1,"POLARITY_FLIPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","5G NAS context 사용 의무를 미사용·무효화 의무로 반전함"],
  R146:[1,0,"NA",1,0,1,"MODAL_STRENGTHENED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","저장 권고를 의무로 강화하고 annex C 대신 PLMN별 보관·재사용을 추가함"],
  R148:[1,0,1,1,"NA",1,"MODAL_STRENGTHENED;UNSUPPORTED_ADDITION","PLMN 이동 비권고를 금지로 강화함"],
  R149:[1,1,0,0,"NA",1,"CONDITION_DROPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","handover 중 생성 가능성을 handover 후 생성으로 변경함"],
  R150:[1,0,1,0,0,1,"POLARITY_FLIPPED;MODAL_STRENGTHENED;ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","capability 미전송 권고를 허용 범위 전송 의무로 바꿈"],
  R153:[0,0,1,0,"NA",1,"MODAL_STRENGTHENED;ACTOR_CHANGED;ACTION_CHANGED;UNSUPPORTED_ADDITION","per-PLMN RAT restriction 고려 권고를 지원 불가 target 금지로 바꿈"],
  R158:[0,0,1,0,"NA",1,"MODAL_WEAKENED;ACTOR_CHANGED;ACTION_CHANGED;UNSUPPORTED_ADDITION","SUCI 사용 의무를 5G-S-TMSI 사용 설명으로 바꿈"],
  R160:[1,0,1,0,0,1,"MODAL_STRENGTHENED;ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","rejected NSSAI 제거 허용을 절차 중단·재시도 의무로 바꿈"],
  R163:[1,1,0,0,"NA",1,"CONDITION_DROPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","single/dual registration을 S1/N1 mode 선택으로 바꾸고 EPC interworking 조건을 누락함"],
  R168:[1,0,1,0,0,1,"POLARITY_FLIPPED;ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","첫 access 완료 전 금지를 병행 등록 허용으로 반전함"],
  R169:[1,0,1,0,"NA",1,"POLARITY_FLIPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","Non-Allowed Area 진입 정보 사용 금지를 정책 사용 허용으로 반전함"],
  R173:[1,0,1,0,0,1,"POLARITY_FLIPPED;ACTION_CHANGED;EXCEPTION_DROPPED;UNSUPPORTED_ADDITION","무결성 검사 전 처리 금지를 일반 메시지 처리 의무로 바꿈"],
  R174:[1,0,1,1,"NA",1,"MODAL_STRENGTHENED;UNSUPPORTED_ADDITION","all-PLMN 표시 비권고를 금지로 강화함"],
  R177:[1,0,0,0,"NA",1,"POLARITY_FLIPPED;CONDITION_DROPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","UE의 slice 기반 동작 금지를 일반 절차 수행 의무로 바꿈"],
  R178:[1,0,1,0,"NA",1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","TA가 Non-Allowed Area에 속해야 한다는 권고를 영역 포함 의무로 바꿈"],
  R181:[1,0,"NA",0,"NA",1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","native 또는 mapped 유형 가능성을 현재 보안 기능 설명으로 대체함"],
  R187:[1,1,1,0,"NA",1,"ACTION_CHANGED;UNSUPPORTED_ADDITION","ngKSI 삭제를 미사용과 새 context에 맞춘 처리로 바꿈"],
  R189:[1,1,"NA",0,0,0,"ACTION_CHANGED;EXCEPTION_DROPPED","지원 PLMN/SNPN과 connectivity type 대신 지원 여부만 광고함"],
  R190:[1,0,1,0,"NA",1,"POLARITY_FLIPPED;MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","Registration Request 거절 비권고를 거절 의무로 반전함"],
  R192:[0,0,1,0,"NA",1,"MODAL_STRENGTHENED;ACTOR_CHANGED;ACTION_CHANGED;UNSUPPORTED_ADDITION","Paging Policy 적용 권고를 application의 DSCP 설정 의무로 바꿈"],
  R197:[0,0,1,0,"NA",0,"MODAL_WEAKENED;ACTOR_CHANGED;ACTION_CHANGED","application DSCP에 따른 Paging Policy 적용 권고를 5GS의 일반 표시 가능성으로 축약함"],
  R201:[0,0,0,0,"NA",1,"MODAL_STRENGTHENED;ACTOR_CHANGED;CONDITION_DROPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","container를 UE에 보내는 변경 허용을 UE의 네트워크 전송 의무로 반전함"],
  R205:[1,0,1,1,1,0,"MODAL_WEAKENED","authorized data만 변경할 수 있어야 하는 의무를 단순 허용으로 약화함"],
  R206:[1,0,1,0,"NA",1,"POLARITY_FLIPPED;MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","identity 기억 권고를 저장 금지로 반전함"],
  R207:[1,0,1,0,"NA",1,"MODAL_STRENGTHENED;ACTION_CHANGED;UNSUPPORTED_ADDITION","all-PLMN area 비할당 권고를 제한적 area 설정 의무로 바꿈"],
  R211:[0,1,"NA",0,0,0,"ACTOR_CHANGED;ACTION_CHANGED;EXCEPTION_DROPPED","서로 다른 VPLMN 간 N38과 inter-PLMN mobility를 누락함"],
  R212:[1,0,1,0,"NA",1,"POLARITY_FLIPPED;ACTION_CHANGED;UNSUPPORTED_ADDITION","configured NSSAI 제공 금지를 제공 의무로 반전함"],
  R213:[1,0,0,1,"NA",1,"MODAL_STRENGTHENED;CONDITION_DROPPED;UNSUPPORTED_ADDITION","두 timer 설정 권고를 의무로 강화하고 정확한 duration/start 기준을 축약함"]
};

const allowed = new Set(["0", "1", "NA"]);
const seen = new Set();
for (const row of rows) {
  if (seen.has(row.review_id)) throw new Error(`Duplicate review_id ${row.review_id}`);
  seen.add(row.review_id);
  const fallback = [1, 1, row.gold_condition ? 1 : "NA", 1, row.gold_exception ? 1 : "NA", 0, "", "의미 보존"];
  const values = bad[row.review_id] || fallback;
  if (values.length !== 8) throw new Error(`Invalid annotation length for ${row.review_id}`);
  [row.actor_preserved, row.polarity_preserved, row.condition_preserved, row.action_preserved,
    row.exception_preserved, row.unsupported_addition, row.error_codes, row.reviewer_note] = values.map(String);
  const applicable = [row.actor_preserved, row.polarity_preserved, row.condition_preserved, row.action_preserved, row.exception_preserved].filter(v => v !== "NA");
  for (const value of [...applicable, row.unsupported_addition]) if (!allowed.has(value) || value === "NA") throw new Error(`Invalid score for ${row.review_id}`);
  row.complete_preservation = String(Number(applicable.every(v => v === "1") && row.unsupported_addition === "0"));
}
for (const reviewId of Object.keys(bad)) if (!seen.has(reviewId)) throw new Error(`Unknown annotation ${reviewId}`);

const headers = Object.keys(rows[0]);
const output = "\uFEFF" + [headers.join(","), ...rows.map(r => headers.map(h => csvCell(r[h])).join(","))].join("\n") + "\n";
fs.writeFileSync(path.join(runDir, "blind_review_pass1.csv"), output);
const pass1ManifestPath = path.join(runDir, "blind_pass1_manifest.json");
const completedAt = fs.existsSync(pass1ManifestPath)
  ? JSON.parse(fs.readFileSync(pass1ManifestPath, "utf8")).completed_at
  : new Date().toISOString();
fs.writeFileSync(pass1ManifestPath, JSON.stringify({
  review_type: "masked_row_level_codex_single_reviewer_pass1",
  completed_at: completedAt,
  rows: rows.length,
  reviewed_range: "R001-R216",
  condition_and_case_id_hidden_during_row_scoring: true,
  semantic_source: "source_text_en and frozen gold fields compared against explanation_ko; JSON output fields used only as secondary context",
  limitation: "This is a Codex single-reviewer masked semantic pass, not an independent human expert review. The reviewer had already seen aggregate deterministic condition results before row-level scoring.",
  failed_complete_preservation_rows: Object.keys(bad).length
}, null, 2) + "\n");
console.log(JSON.stringify({ status: "PASS", rows: rows.length, complete_preservation: rows.filter(r => r.complete_preservation === "1").length, failed_complete_preservation: rows.filter(r => r.complete_preservation === "0").length }, null, 2));
