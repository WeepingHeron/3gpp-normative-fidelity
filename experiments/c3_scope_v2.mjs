import { render } from './c3_lib.mjs';

const TYPES = {shall:'obligation','shall not':'prohibition',should:'recommendation','should not':'discouragement',may:'permission',can:'capability'};
const FIELDS = ['normative_type','polarity','modal_cue','scope_quote','actor_quote','action_quote','conditions','limitations','references'];
const ARRAYS = ['conditions','limitations','references'];

export function sourceOnlyInput(template, row) {
  if(typeof row?.source_text_en!=='string'||!row.source_text_en.trim())throw new Error('SOURCE_REQUIRED');
  return render(template,{source_text_en:row.source_text_en});
}

export function protectedSourceMarkers(source) {
  return [...new Set((source.match(/\bnot all\b|\bonly\b|\bunless\b|\buntil\b|\bwithout\b|\bbefore\b|\bneed to\b|\bmake sure\b|\bboth\b|\bneither\b|\ball\b|\b\d+(?:\.\d+)?\s*(?:percent\b|%)|\bexceed\s+\d+(?:\.\d+)?\b/gi)||[]).map(s=>s.toLowerCase()))];
}

export function validateScopeExtraction(source, value) {
  const fail = (...reasons) => ({status:'HOLD',reasons,semantic_status:'NOT_EVALUATED',structure:null});
  if(typeof source!=='string'||!source.trim())return fail('SOURCE_REQUIRED');
  if(!value||typeof value!=='object'||Array.isArray(value)||Object.keys(value).length!==FIELDS.length||!FIELDS.every(f=>Object.hasOwn(value,f)))return fail('SCHEMA_INVALID');
  if(!FIELDS.filter(f=>!ARRAYS.includes(f)).every(f=>typeof value[f]==='string')||!ARRAYS.every(f=>Array.isArray(value[f])&&value[f].every(s=>typeof s==='string'&&s.trim())))return fail('SCHEMA_INVALID');
  if(value.normative_type==='unclear'||value.polarity==='unclear'||value.modal_cue==='unclear')return fail('AMBIGUOUS_SCOPE');
  if(!Object.hasOwn(TYPES,value.modal_cue)||TYPES[value.modal_cue]!==value.normative_type)return fail('CUE_TYPE_MISMATCH');
  const polarity=['prohibition','discouragement'].includes(value.normative_type)?'negative':'positive';
  if(value.polarity!==polarity)return fail('CUE_POLARITY_MISMATCH');
  const core=['actor_quote','scope_quote','action_quote'];
  if(core.some(f=>!value[f].trim()))return fail('CORE_QUOTE_REQUIRED');
  const quotes=[...core.map(f=>value[f]),...ARRAYS.flatMap(f=>value[f])];
  if(quotes.some(q=>!source.includes(q)))return fail('QUOTE_NOT_IN_SOURCE');
  if(value.scope_quote!==[value.actor_quote,value.modal_cue,value.action_quote].join(' '))return fail('SCOPE_LINK_MISMATCH');
  if(value.limitations.some(q=>/^\s*\(?\s*(?:see|refer to)\s+(?:subclause|clause|annex)\b/i.test(q)))return fail('REFERENCE_USED_AS_LIMITATION');
  const retained=[value.scope_quote,...value.conditions,...value.limitations].join('\n').toLowerCase();
  const missing=protectedSourceMarkers(source).filter(q=>!retained.includes(q));
  if(missing.length)return fail(...missing.map(q=>'PROTECTED_MARKER_MISSING:'+q));
  return {status:'PASS_EVIDENCE_LINKS_ONLY',reasons:[],semantic_status:'NOT_EVALUATED',
    structure:{actor:value.actor_quote,condition:value.conditions.join('; '),normative_type:value.normative_type,polarity:value.polarity,action:value.action_quote,exception:value.limitations.join('; ')}};
}
