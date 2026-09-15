import fs from 'node:fs';
import assert from 'node:assert/strict';
import {parseCsv,projectCase,render} from './c3_lib.mjs';
import {modalInput,modalTemplate,HINT,modalProjection} from './c1m_lib.mjs';
const base=fs.readFileSync(new URL('./prompts/c1_v2.md',import.meta.url),'utf8');
const rows=parseCsv(fs.readFileSync(new URL('../data/main_cases.csv',import.meta.url),'utf8'));
assert.equal(modalTemplate(base).replace(HINT,''),base);
for(const r of rows){
 const altered={...r};for(const k of ['case_id','actor','condition','action','exception','gold_summary_ko','difficulty_tier'])altered[k]='PRIVATE_SENTINEL_'+k;
 assert.equal(modalInput(base,r),modalInput(base,altered));
 assert(!modalInput(base,altered).includes('PRIVATE_SENTINEL'));
 const projected=modalProjection(r);
 assert.deepEqual(Object.keys(projected).sort(),['source_text_en','question_ko','spec_id','version','clause_id','normative_type','polarity'].sort());
 assert.equal(modalInput(base,r).replace(render(HINT,projected),''),render(base,projectCase(r)));
 const changed={...r,modal_class:r.modal_class==='shall'?'may':'shall',polarity:'positive'};
 assert.notEqual(modalInput(base,r),modalInput(base,changed));
 assert.equal(modalInput(base,changed).replace(render(HINT,modalProjection(changed)),''),render(base,projectCase(r)));
}
console.log(`PASS ${rows.length} gold-field mutation, exact C1 base and hint-only changes; no API`);
