import assert from 'node:assert/strict';
import fs from 'node:fs';
import { parseCsv } from './c3_lib.mjs';
import { sourceOnlyInput, validateScopeExtraction, protectedSourceMarkers } from './c3_scope_v2.mjs';

const template=fs.readFileSync(new URL('./prompts/c3_scope_extract_v2.md',import.meta.url),'utf8');
const cases=parseCsv(fs.readFileSync(new URL('../data/main_cases.csv',import.meta.url),'utf8'));
for(const r of cases){
  const mutated=Object.fromEntries(Object.entries(r).map(([k,v])=>[k,k==='source_text_en'?v:'UNTRUSTED_GOLD_SENTINEL']));
  assert.equal(sourceOnlyInput(template,r),sourceOnlyInput(template,mutated));
  assert(!sourceOnlyInput(template,mutated).includes('UNTRUSTED_GOLD_SENTINEL'));
}
assert.throws(()=>sourceOnlyInput(template,{question_ko:'source omitted'}),/SOURCE_REQUIRED/);
const source='The UE shall not transmit unless the AMF authorizes it.';
const good={normative_type:'prohibition',polarity:'negative',modal_cue:'shall not',scope_quote:'The UE shall not transmit',actor_quote:'The UE',action_quote:'transmit',conditions:[],limitations:['unless the AMF authorizes it.'],references:[]};
const validate=v=>validateScopeExtraction(source,v);
assert.equal(validate(good).status,'PASS_EVIDENCE_LINKS_ONLY');
assert.equal(validate(good).semantic_status,'NOT_EVALUATED');
assert.equal(validate({...good,actor_quote:'the AMF'}).reasons[0],'SCOPE_LINK_MISMATCH');
assert.equal(validate({...good,actor_quote:'The SMF'}).reasons[0],'QUOTE_NOT_IN_SOURCE');
assert.equal(validate({...good,normative_type:'permission'}).reasons[0],'CUE_TYPE_MISMATCH');
assert.equal(validate({...good,polarity:'positive'}).reasons[0],'CUE_POLARITY_MISMATCH');
assert.equal(validate({...good,limitations:[]}).reasons[0],'PROTECTED_MARKER_MISSING:unless');
assert.equal(validate({...good,conditions:['if the network is congested']}).reasons[0],'QUOTE_NOT_IN_SOURCE');
assert.equal(validate({...good,extra:'field'}).reasons[0],'SCHEMA_INVALID');
assert.equal(validate({...good,conditions:[null]}).reasons[0],'SCHEMA_INVALID');
assert.equal(validate({...good,normative_type:'unclear'}).status,'HOLD');
const refsource=source+' (see subclause 1.2).';
assert.equal(validateScopeExtraction(refsource,{...good,limitations:[...good.limitations,'see subclause 1.2']}).reasons[0],'REFERENCE_USED_AS_LIMITATION');
assert.equal(validateScopeExtraction(refsource,{...good,references:['see subclause 1.2']}).status,'PASS_EVIDENCE_LINKS_ONLY');
const numeric='In uncongested scenarios, 98 percent of packets should not experience a delay exceeding the PDB.';
const nr={...good,normative_type:'discouragement',modal_cue:'should not',scope_quote:'packets should not experience a delay exceeding the PDB.',actor_quote:'packets',action_quote:'experience a delay exceeding the PDB.',conditions:['In uncongested scenarios'],limitations:[]};
assert.equal(validateScopeExtraction(numeric,nr).reasons[0],'PROTECTED_MARKER_MISSING:98 percent');
assert.equal(validateScopeExtraction(numeric,{...nr,limitations:['98 percent of packets']}).status,'PASS_EVIDENCE_LINKS_ONLY');
const partial='Not all events can be subscribed to UPF directly.';
const pr={normative_type:'capability',polarity:'positive',modal_cue:'can',scope_quote:'events can be subscribed to UPF directly.',actor_quote:'events',action_quote:'be subscribed to UPF directly.',conditions:[],limitations:[],references:[]};
assert(validateScopeExtraction(partial,pr).reasons.includes('PROTECTED_MARKER_MISSING:not all'));
assert.equal(validateScopeExtraction(partial,{...pr,actor_quote:'Not all events',scope_quote:partial}).status,'PASS_EVIDENCE_LINKS_ONLY');
assert(protectedSourceMarkers('shall exceed 7 only if ready; 98% of packets').includes('exceed 7'));
// Deliberate boundary: exact source fragments do not prove a valid parse/relationship.
const ambiguous='The AMF indicates that the UE should not use 5GC.';
const plausible={...good,normative_type:'discouragement',modal_cue:'should not',actor_quote:'The AMF indicates that the UE',action_quote:'use 5GC.',scope_quote:ambiguous,limitations:[]};
assert.equal(validateScopeExtraction(ambiguous,plausible).status,'PASS_EVIDENCE_LINKS_ONLY');
assert.equal(validateScopeExtraction(ambiguous,plausible).semantic_status,'NOT_EVALUATED');
console.log(JSON.stringify({status:'PASS_OFFLINE_CONTRACT_ONLY',gold_projection_cases:cases.length,fixture_coverage:['source spans','cue/type/polarity','scope links','marker omission','reference role','schema','semantic boundary'],model_calls:0,semantic_evaluation:'NOT_EVALUATED'}));
