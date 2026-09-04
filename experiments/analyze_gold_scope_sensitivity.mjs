import fs from "node:fs";
import path from "node:path";

function parseCsv(text){const rows=[];let row=[],field="",quoted=false;for(let i=0;i<text.length;i++){const c=text[i];if(quoted){if(c==='"'&&text[i+1]==='"'){field+='"';i++;}else if(c==='"')quoted=false;else field+=c;}else if(c==='"')quoted=true;else if(c===','){row.push(field);field="";}else if(c==='\n'){row.push(field.replace(/\r$/, ""));rows.push(row);row=[];field="";}else field+=c;}const [header,...body]=rows.filter(r=>r.some(v=>v!==""));const clean=header.map(h=>h.replace(/^\uFEFF/,""));return body.map(r=>Object.fromEntries(clean.map((h,i)=>[h,r[i]??""])));}
const runDir=path.resolve(process.argv[2]||"");if(!process.argv[2])throw new Error("Usage: node experiments/analyze_gold_scope_sensitivity.mjs <run_directory>");
const rows=parseCsv(fs.readFileSync(path.join(runDir,"human_scores_adjudicated.csv"),"utf8"));
const excluded=new Set(["MAIN-CAN-004","MAIN-SD-002","MAIN-CAN-008"]);
const summarize=source=>Object.fromEntries(["C0","C1","C2"].map(condition=>{const x=source.filter(r=>r.condition===condition);return[condition,{complete_preservation:{successes:x.filter(r=>r.complete_preservation==="1").length,n:x.length,rate:x.filter(r=>r.complete_preservation==="1").length/x.length},unsupported_addition:{successes:x.filter(r=>r.unsupported_addition==="1").length,n:x.length,rate:x.filter(r=>r.unsupported_addition==="1").length/x.length}}];}));
const result={status:"SENSITIVITY_ONLY_NOT_REPLACEMENT_GOLD",excluded_case_ids:[...excluded],primary_frozen:summarize(rows),excluding_predeclared_ambiguous_cases:summarize(rows.filter(r=>!excluded.has(r.case_id))),interpretation:"The frozen labels remain primary. Exclusion is reported only to show dependence on the three predeclared scope-ambiguous sentences."};
fs.writeFileSync(path.join(runDir,"gold_scope_sensitivity.json"),JSON.stringify(result,null,2)+"\n");
console.log(JSON.stringify(result,null,2));
