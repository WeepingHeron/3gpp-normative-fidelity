import {projectCase,render} from './c3_lib.mjs';
export const TYPES={shall:'obligation',shall_not:'prohibition',should:'recommendation',should_not:'discouragement',may:'permission',can:'capability'};
export const HINT='## 규범 유형 힌트\n\n- normative_type: {{normative_type}}\n- polarity: {{polarity}}\n\n';
export function modalProjection(row){
  if(!Object.hasOwn(TYPES,row.modal_class)||!['positive','negative'].includes(row.polarity))throw new Error('Invalid modal gold');
  return {...projectCase(row),normative_type:TYPES[row.modal_class],polarity:row.polarity};
}
export function modalTemplate(base){
  if(base.split('## 출처 식별자').length!==2)throw new Error('Expected exactly one citation block');
  return base.replace('## 출처 식별자',HINT+'## 출처 식별자');
}
export const modalInput=(base,row)=>render(modalTemplate(base),modalProjection(row));
