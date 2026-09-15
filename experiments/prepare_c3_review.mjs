import fs from 'node:fs';
import path from 'node:path';
import {sha256,parseCsv,writeCsv,tokenCost} from './c3_lib.mjs';
const ROOT=path.resolve(import.meta.dirname,'..');
if(!process.argv[2])throw new Error('Usage: node experiments/prepare_c3_review.mjs <c3_run>');
const dir=path.resolve(process.argv[2]);
const original=path.join(ROOT,'experiments/runs/main72_v3_2026-09-03T07-35-49-603Z');
const manifest=JSON.parse(fs.readFileSync(path.join(dir,'manifest.json')));
if(manifest.status!=='generation_complete_semantics_pending'||manifest.processed_cases!==72)throw new Error('Complete generation required; do not hide partial-run cases');
for(const [name,hash] of Object.entries(JSON.parse(fs.readFileSync(path.join(dir,'output_freeze_manifest.json'))).file_sha256))
  if(sha256(fs.readFileSync(path.join(dir,name)))!==hash)throw new Error(`Output changed: ${name}`);
const load=(base,name)=>fs.readFileSync(path.join(base,name),'utf8').trim().split('\n').filter(Boolean).map(JSON.parse);
const gold=new Map(parseCsv(fs.readFileSync(path.join(ROOT,'data/main_cases.csv'),'utf8')).map(r=>[r.case_id,r]));
const c3=load(dir,'parsed_responses.jsonl');const ex=load(dir,'extractions.jsonl');
const all=[...load(original,'parsed_responses.jsonl').filter(r=>['C1','C2'].includes(r.condition)),...c3];
if(all.length!==216||new Set(all.map(r=>`${r.case_id}:${r.condition}`)).size!==216)throw new Error('Invalid C1/C2/C3 matrix');
const key={};
const blank=all.map(r=>({r,order:sha256(`C3-fresh-review-v1:${r.case_id}:${r.condition}`)})).sort((a,b)=>a.order.localeCompare(b.order)).map(({r},i)=>{
  const id=`E${String(i+1).padStart(3,'0')}`;key[id]={case_id:r.case_id,condition:r.condition};const g=gold.get(r.case_id);
  return {review_id:id,source_text_en:g.source_text_en,question_ko:g.question_ko,gold_modal_class:g.modal_class,
    gold_actor:g.actor,gold_condition:g.condition,gold_action:g.action,gold_exception:g.exception,
    explanation_ko:r.parsed?.explanation_ko||'',actor_preserved:'',polarity_preserved:'',condition_preserved:'',
    action_preserved:'',exception_preserved:'',unsupported_addition:'',complete_preservation:'',error_codes:'',reviewer_note:''};
});
const out=path.join(dir,'review');fs.mkdirSync(out);
writeCsv(path.join(out,'blind_explanations_blank.csv'),blank);
fs.writeFileSync(path.join(out,'blind_key.json'),JSON.stringify(key,null,2)+'\n');
const types={shall:'obligation',shall_not:'prohibition',should:'recommendation',should_not:'discouragement',may:'permission',can:'capability'};
const comparisons=ex.map(r=>({case_id:r.case_id,extraction_parsed:Number(Boolean(r.parsed)),
  extraction_JSON_modal_correct:Number(r.parsed?.normative_type===types[gold.get(r.case_id).modal_class]),
  extraction_polarity_correct:Number(r.parsed?.polarity===gold.get(r.case_id).polarity),
  explanation_JSON_modal_correct:Number(c3.find(g=>g.case_id===r.case_id)?.parsed?.normative_type===types[gold.get(r.case_id).modal_class]),
  source_text_en:gold.get(r.case_id).source_text_en,...Object.fromEntries(['actor','condition','action','exception'].flatMap(f=>[[`gold_${f}`,gold.get(r.case_id)[f]],[`extracted_${f}`,r.parsed?.[f]||''],[`${f}_semantic_preserved`,'']]))}));
writeCsv(path.join(out,'extraction_review.csv'),comparisons);
const excluded=new Set(['MAIN-CAN-004','MAIN-SD-002','MAIN-CAN-008']);
function tally(list){return {n:list.length,...Object.fromEntries(['extraction_JSON_modal_correct','extraction_polarity_correct','explanation_JSON_modal_correct'].map(k=>[k,list.reduce((sum,r)=>sum+r[k],0)]))};}
const summary={status:'DETERMINISTIC_DIAGNOSTICS_ONLY_SEMANTICS_NOT_EVALUATED',all_72:tally(comparisons),excluding_scope_ambiguous:tally(comparisons.filter(r=>!excluded.has(r.case_id))),
  review_rows:blank.length,warning:'No semantic preservation rate until fresh review. JSON matches do not validate Korean meaning.'};
fs.writeFileSync(path.join(out,'diagnostics.json'),JSON.stringify(summary,null,2)+'\n');
fs.writeFileSync(path.join(out,'review_manifest.json'),JSON.stringify({created_at:new Date().toISOString(),score_status:'BLANK_NOT_REVIEWED',conditions:['C1','C2','C3'],rows:216,
  limitation:'Masking hides condition and ID, but the reviewing agent has prior experiment knowledge; independent human review is still absent.',
  file_sha256:Object.fromEntries(fs.readdirSync(out).sort().map(name=>[name,sha256(fs.readFileSync(path.join(out,name)))]))},null,2)+'\n');
console.log(JSON.stringify(summary,null,2));
