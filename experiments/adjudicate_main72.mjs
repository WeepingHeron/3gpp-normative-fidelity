import fs from "node:fs";
import path from "node:path";

function parseCsv(text) {
  const rows=[]; let row=[],field="",quoted=false;
  for(let i=0;i<text.length;i++){const c=text[i];if(quoted){if(c==='"'&&text[i+1]==='"'){field+='"';i++;}else if(c==='"')quoted=false;else field+=c;}else if(c==='"')quoted=true;else if(c===','){row.push(field);field="";}else if(c==='\n'){row.push(field.replace(/\r$/, ""));rows.push(row);row=[];field="";}else field+=c;}
  if(field.length||row.length){row.push(field.replace(/\r$/, ""));rows.push(row);}
  const [header,...body]=rows.filter(r=>r.some(v=>v!==""));const clean=header.map(h=>h.replace(/^\uFEFF/,""));
  return body.map(r=>Object.fromEntries(clean.map((h,i)=>[h,r[i]??""])));
}
function cell(v){const s=String(v??"");return /[",\n]/.test(s)?`"${s.replaceAll('"','""')}"`:s;}
function writeCsv(file,rows,headers){fs.writeFileSync(file,"\uFEFF"+[headers.join(","),...rows.map(r=>headers.map(h=>cell(r[h])).join(","))].join("\n")+"\n");}

const runDir=path.resolve(process.argv[2]||"");if(!process.argv[2])throw new Error("Usage: node experiments/adjudicate_main72.mjs <run_directory>");
const disagreements=parseCsv(fs.readFileSync(path.join(runDir,"adjudication.csv"),"utf8"));
const pass1=parseCsv(fs.readFileSync(path.join(runDir,"blind_review_pass1.csv"),"utf8"));
const key1=JSON.parse(fs.readFileSync(path.join(runDir,"blind_key.json"),"utf8"));

// Each entry is [adjudicated value, concise rationale]. Only pass-1/pass-2 score disagreements are adjudicated.
const D={
  "MAIN-CAN-001:C0:unsupported_addition":["0","인터페이스가 연동을 지원한다는 표현은 원문의 reference point 관계를 벗어난 새 규칙으로 보지 않음"],
  "MAIN-CAN-004:C1:action_preserved":["0","동결 gold의 actor-action scope 기준으로 authorized NF의 access action을 구현 주체의 보장 action으로 바꿈"],
  "MAIN-CAN-005:C0:unsupported_addition":["1","직접 접속이 아니라 RG를 경유한다는 배타적 설명을 원문보다 추가함"],
  "MAIN-CAN-007:C0:actor_preserved":["1","한국어 설명의 문법적 주체는 5GSM message이며 JSON actor는 보조 근거로만 사용함"],
  "MAIN-MAY-001:C0:condition_preserved":["0","within a PDU Session을 local/central UPF를 함께 쓰는 구성이라는 순환 조건으로 바꿈"],
  "MAIN-MAY-005:C0:actor_preserved":["1","UEs와 UE는 의미상 같은 주체임"],
  "MAIN-MAY-012:C0:action_preserved":["1","configured/rejected NSSAI 갱신은 원문의 changed action 범위 안에 있음"],
  "MAIN-SD-001:C0:unsupported_addition":["0","영역 포함 표현은 부정확하지만 별도의 새 규칙을 추가한 것은 아님"],
  "MAIN-SD-002:C0:exception_preserved":["NA","동결 gold에 별도 exception이 없어 적용 불가"],
  "MAIN-SDN-003:C1:polarity_preserved":["0","should not 권고를 예외 외에는 불가능하다는 강한 금지로 표현함"],
  "MAIN-SDN-003:C1:complete_preservation":["0","규범 강도 강화 때문에 완전 보존 실패"],
  "MAIN-SDN-003:C1:unsupported_addition":["1","원문보다 강한 금지 의미를 추가함"],
  "MAIN-SDN-004:C0:condition_preserved":["0","connected 상태를 capability 전송 상황으로 재정의함"],
  "MAIN-SDN-010:C1:unsupported_addition":["1","should not을 예외 없는 금지처럼 서술함"],
  "MAIN-SH-002:C0:actor_preserved":["1","한국어 설명에서 non-3GPP access UE 주체를 보존함"],
  "MAIN-SH-002:C0:condition_preserved":["1","등록 후 조건을 설명에 명시함"],
  "MAIN-SH-007:C0:unsupported_addition":["1","새 AMF 보안 연속성과 복원 목적을 원문보다 추가함"],
  "MAIN-SH-009:C0:exception_preserved":["NA","동결 gold에 별도 exception이 없어 적용 불가"],
  "MAIN-SN-001:C1:condition_preserved":["1","한국어 설명이 related RAT의 서로 다른 TAC 배치 조건을 명시함"],
  "MAIN-SN-001:C1:complete_preservation":["1","설명 기준으로 actor, force, condition, action을 모두 보존하고 추가 주장 없음"],
  "MAIN-SN-005:C0:condition_preserved":["0","UE가 정보를 받지 못한 조건을 AMF가 정보를 받지 못한 조건으로 바꿈"],
  "MAIN-SN-007:C0:action_preserved":["0","예외 없는 release 금지를 임의 release 금지로 약화함"],
  "MAIN-SN-007:C0:exception_preserved":["NA","동결 gold에 별도 exception이 없어 적용 불가"],
  "MAIN-SN-008:C0:actor_preserved":["0","S-NSSAI 개수라는 주체를 네트워크 또는 목록으로 바꿈"],
  "MAIN-SN-009:C1:actor_preserved":["1","전체 한국어 설명이 target AMF와 new KAMF의 관계를 함께 보존함"],
  "MAIN-SN-009:C1:action_preserved":["1","8 LSB 포함과 new KAMF 비유도 표시를 설명에서 모두 보존함"],
  "MAIN-SN-009:C1:exception_preserved":["1","target AMF의 container 표시 맥락을 설명에서 보존함"],
  "MAIN-SN-009:C1:complete_preservation":["1","전체 설명 기준으로 동결 gold 의미를 보존함"],
  "MAIN-SN-009:C1:unsupported_addition":["0","금지 의미 설명은 shall not의 해석이며 새 규칙이 아님"]
};

for(const row of disagreements){const id=`${row.case_id}:${row.condition}:${row.field}`;const d=D[id];if(!d)throw new Error(`Missing adjudication ${id}`);[row.adjudicated,row.rationale]=d;}
for(const id of Object.keys(D))if(!disagreements.some(r=>`${r.case_id}:${r.condition}:${r.field}`===id))throw new Error(`Stale adjudication ${id}`);
writeCsv(path.join(runDir,"adjudication.csv"),disagreements,["case_id","condition","field","pass1","pass2","adjudicated","rationale"]);

const adjudicated=pass1.map(r=>({...r}));const index=new Map(adjudicated.map(r=>{const k=key1[r.review_id];return[`${k.case_id}:${k.condition}`,r];}));
for(const d of disagreements)index.get(`${d.case_id}:${d.condition}`)[d.field]=d.adjudicated;
for(const r of adjudicated){const applicable=[r.actor_preserved,r.polarity_preserved,r.condition_preserved,r.action_preserved,r.exception_preserved].filter(v=>v!=="NA");const derived=String(Number(applicable.every(v=>v==="1")&&r.unsupported_addition==="0"));if(derived!==r.complete_preservation)throw new Error(`Derived complete mismatch after adjudication: ${r.review_id}`);}
writeCsv(path.join(runDir,"blind_review_adjudicated.csv"),adjudicated,Object.keys(adjudicated[0]));

const auto=parseCsv(fs.readFileSync(path.join(runDir,"scores.csv"),"utf8"));const byIdentity=new Map(adjudicated.map(r=>{const k=key1[r.review_id];return[`${k.case_id}:${k.condition}`,r];}));
const merged=auto.map(r=>({...r,...Object.fromEntries(Object.entries(byIdentity.get(`${r.case_id}:${r.condition}`)).filter(([k])=>k!=="review_id"))}));
writeCsv(path.join(runDir,"human_scores_adjudicated.csv"),merged,Object.keys(merged[0]));
fs.writeFileSync(path.join(runDir,"adjudication_manifest.json"),JSON.stringify({status:"ADJUDICATED_SAME_CODEX_REVIEWER",rows:216,score_disagreements:disagreements.length,complete_preservation_pass1:pass1.filter(r=>r.complete_preservation==="1").length,complete_preservation_pass2:parseCsv(fs.readFileSync(path.join(runDir,"blind_review_pass2.csv"),"utf8")).filter(r=>r.complete_preservation==="1").length,complete_preservation_adjudicated:adjudicated.filter(r=>r.complete_preservation==="1").length,limitation:"Adjudication was performed by the same Codex reviewer. It is not independent human expert validation."},null,2)+"\n");
console.log(JSON.stringify({status:"PASS",score_disagreements:disagreements.length,complete_preservation_adjudicated:adjudicated.filter(r=>r.complete_preservation==="1").length},null,2));
