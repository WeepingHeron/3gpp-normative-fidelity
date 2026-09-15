import fs from 'node:fs';
import crypto from 'node:crypto';

export const sha256 = value => crypto.createHash('sha256').update(value).digest('hex');
export function parseCsv(text) {
  const rows=[];let row=[],field='',quoted=false;
  for(let i=0;i<text.length;i++) {const c=text[i];
    if(quoted) {if(c==='"'&&text[i+1]==='"'){field+='"';i++;}else if(c==='"')quoted=false;else field+=c;}
    else if(c==='"')quoted=true;else if(c===','){row.push(field);field='';}
    else if(c==='\n'){row.push(field.replace(/\r$/,''));rows.push(row);row=[];field='';}else field+=c;
  }
  if(quoted)throw new Error('Unclosed CSV quote');
  if(field.length||row.length){row.push(field.replace(/\r$/,''));rows.push(row);}
  const [header,...body]=rows.filter(r=>r.some(Boolean));
  return body.map(r=>{if(r.length!==header.length)throw new Error('CSV width mismatch');return Object.fromEntries(header.map((h,i)=>[h.replace(/^\uFEFF/,''),r[i]]));});
}
export function projectCase(row) {
  return Object.fromEntries(['source_text_en','question_ko','spec_id','version','clause_id'].map(k=>{
    if(typeof row[k]!=='string'||!row[k].trim())throw new Error(`Missing source input: ${k}`);
    return [k,row[k]];
  }));
}
export function render(template, values) {
  return template.replace(/{{([a-z_]+)}}/g,(_,key)=>{
    if(!Object.hasOwn(values,key))throw new Error(`Missing prompt variable: ${key}`);
    return values[key];
  });
}
export function extractionInput(template, projected) {return render(template,{source_text_en:projected.source_text_en});}
export function generationInput(template, projected, extraction) {
  return render(template,{...projectCase(projected),...Object.fromEntries(['actor','condition','normative_type','polarity','action','exception'].map(k=>[k,extraction[k]]))});
}
export function validateObject(value,schema) {
  if(!value||typeof value!=='object'||Array.isArray(value))return false;
  if(Object.keys(value).length!==schema.required.length)return false;
  return schema.required.every(k=>typeof value[k]==='string'&&(!schema.properties[k].enum||schema.properties[k].enum.includes(value[k])));
}
export function extractionUsable(value,schema) {
  if(!validateObject(value,schema)||value.normative_type==='unclear'||!value.actor.trim()||!value.action.trim())return false;
  return value.polarity===(['prohibition','discouragement'].includes(value.normative_type)?'negative':'positive');
}
export function responseObject(response,schema) {
  if(response?.status!=='completed')return null;
  const parts=(response.output||[]).filter(x=>x.type==='message').flatMap(x=>x.content||[]);
  if(parts.some(x=>x.type==='refusal'))return null;
  try {const parsed=JSON.parse(parts.filter(x=>x.type==='output_text').map(x=>x.text).join(''));return validateObject(parsed,schema)?parsed:null;}catch{return null;}
}
export function tokenCost(usage) {
  if(!usage||!Number.isFinite(usage.input_tokens)||!Number.isFinite(usage.output_tokens))return null;
  const cached=usage.input_tokens_details?.cached_tokens||0;
  return ((usage.input_tokens-cached)*.75+cached*.075+usage.output_tokens*4.5)/1e6;
}
export function reserveCost(input,schema,maxOutput) {
  return ((Buffer.byteLength(input)+Buffer.byteLength(JSON.stringify(schema))+2048)*.75+maxOutput*4.5)/1e6;
}
export function writeCsv(file,rows,headers=Object.keys(rows[0]||{})) {
  const cell=v=>{const s=String(v??'');return /[",\n]/.test(s)?'"'+s.replaceAll('"','""')+'"':s;};
  fs.writeFileSync(file,'\uFEFF'+[headers.join(','),...rows.map(r=>headers.map(h=>cell(r[h])).join(','))].join('\n')+'\n');
}
