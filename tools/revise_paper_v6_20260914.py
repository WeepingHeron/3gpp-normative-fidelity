from pathlib import Path
from copy import deepcopy
from docx import Document
from revise_paper_template_20260906 import replace_text
R=Path(__file__).resolve().parents[1];B=R/'outputs/paper';d=Document(B/'ACK2026_3GPP_normative_fidelity_validated_v5.docx');out=B/'ACK2026_3GPP_normative_fidelity_validated_v6.docx'
p=d.paragraphs
replace_text(p[6], '원문은 ETSI 공식 배포본 TS 23.501 및 TS 24.501 V18.12.0 Release 18로 고정했다[8], [9]. 최초 72개 문장(규범 유형 6종별 12개, 44개 조항)은 7,727개 후보에서 선정했다. 사후 적격성 감사에서 일반 적격 50건, 조건부 예외 1건, 부적격 10건, 보류 11건을 확인했다. 부적격은 NOTE·목록 제외 위반이며, 보류는 문맥 범위·메타데이터·대응 관계·의미 중복 문제다. 사후 분석 처리 방침을 재평가 전에 동결하고, 일반 적격 중 C2 정답 입력 오염 사례(MAY-001)를 제외한 49건·33개 조항을 주 분석으로 삼았다. 기존 응답은 수정하지 않았다.')
replace_text(p[8],p[8].text.replace('51건×5조건의 255개 슬롯을','주 분석과 민감도 집합의 합집합 51건×5조건의 255개 슬롯을'))
replace_text(p[11],p[11].text.replace('주 분석의 U 7건과','주 분석의 조건별 응답 U 합계 7건과'))
replace_text(p[15],'C2−C1M은 주 분석에서 −2.04~+6.12%p이며 세 민감도 표본에서도 0을 포함해 순위나 동등성을 확정할 수 없다. 실제 오류로 TS 24.501 §4.4.4.2의 NAS 메시지 무결성 검사 조건을 “UE의 수신 5GMM 엔티티가 NAS에 의해 성공적으로 무결성 검사를 받은 경우”로 설명한 응답이 있었다. 금지 표현을 유지했어도 검사 대상이 메시지에서 엔티티로 바뀌어 실패로 판정했다.')
# Insert two scoped paragraphs before conclusion, keeping existing body style.
texts=[
 '개발 원문 SMF(§4.2.3)·AMF(§5.4.11.4)[8]·NSSAI(§4.6.2.2 및 Annex C)[9]에 문맥을 제공한 직접 설명을 9월 14일 각 3회 계획했다. 동결 입력·동일 모델·temperature 0·2~4문장·900토큰을 유지했다. 통신 결과 미상 1개는 재시도하지 않았다. 나머지 8개의 동일 AI 1차 평가는 완수 3개·미완수 5개였다(SMF 2/2, NSSAI 1/3, AMF 0/3 완수).',
'AMF 3개 모두 강도 변경과 망 검증 설정 조건 누락이 있었다. 첫 응답의 “등록해제해서는 안 된다”는 should not을 강제 금지화했다. NSSAI 3개 중 2개는 eCall 예외 일부를 누락했다. 마지막 응답은 비저장·삭제 사건을 설명했지만 ME 임시 저장은 action·exception 메타데이터에만 남겼다. 형식 필드가 설명의 누락을 복구하지 못한 사례다.' 
]
for text in texts:
 el=deepcopy(p[15]._p);p[16]._p.addprevious(el)
 from docx.text.paragraph import Paragraph
 replace_text(Paragraph(el,p[16]._parent),text)
replace_text(p[17],'정답 구조·자동 추출 구조·유형 힌트 조건의 C1 대비 차이는 확정 판정을 유지하는 범위에서 양수였으나, 전체 구조와 유형 힌트의 우열은 정해지지 않았다. 실제 오류는 규범 강도뿐 아니라 검사 대상·적용 조건·복합 예외의 연결에서 나타났다. 따라서 규범 유형 및 출처 필드와 자연어 설명의 명제 보존을 분리해 평가해야 한다.')
replace_text(p[18],'본 연구는 단일 모델·고정 규격 버전·동일 AI의 정답과 평가에 한정된다. 사후 표본 처리, 조항 내 의존성, 미확정 판정 때문에 통계적 유의성이나 일반화를 주장하지 않는다. 조건별 지시문과 생성일 차이로 순수한 구조 효과를 분리하지 못한다. 추가 8개는 알려진 원문의 반복·1차 평가이며 독립 표본이나 주 분석에 합산하지 않았다. 통신 미상은 의미 오류와 구분했다. 독립 전문가 판정과 개발에 쓰지 않은 새 조항 검증이 필요하다.')
a=d.tables[0].cell(8,0).paragraphs[1]
replace_text(a,'3GPP 영문 규격의 한국어 설명에서 규범 강도·행위자·조건·행동·예외의 보존을 평가했다. 동결 응답의 사후 적격성 감사와 동일 AI의 지연 재검토 후, 주 분석 49건의 완전 보존 범위는 원문 단독 77.55~79.59%, 정답 구조 89.80~93.88%, 자동 추출 구조 83.67~87.76%, 정답 유형·부정 힌트 87.76~91.84%였다. 이는 미확정에 따른 논리적 범위이며 신뢰구간이 아니다. 별도 개발 원문 3개에서 추가 생성된 8개 설명의 1차 평가로 규범 강도 변경과 조건·예외 누락을 확인했다. 메타데이터가 맞아도 설명의 명제 연결이 달라질 수 있어 두 평가를 구분해야 한다. 사후 표본 처리와 단일 AI 평가의 한계가 있으며 통계적 우월성이나 일반화를 주장하지 않는다.')
replace_text(p[4],'원문 단독(C1)에 정답 구조(C2), 자동 추출 구조(C3), 정답 규범 유형·부정 힌트(C1M)를 추가할 때 완전 의미 보존율이 어떻게 달라지는지 비교한다. 동결 응답의 사후 재평가이며 실제 검색 정확도나 3GPP 전체 일반화는 다루지 않는다.')
replace_text(p[11],'표 1의 범위는 미확정 판정에 따른 논리적 상·하한이다. C2−C1은 +10.20~+16.33%p, C3−C1은 +4.08~+10.20%p, C1M−C1은 +8.16~+14.29%p다. 조건별 응답 U 합계 7건과 C3 미생성 1건은 분모에 남겼다. C0의 0/49는 원문 없는 조건에서 이 완전 보존 기준을 충족하지 못한 결과다.')
d.save(out)
lines=['# '+d.tables[0].cell(0,0).text,'',d.tables[0].cell(4,0).text,'',d.tables[0].cell(2,0).text,'',d.tables[0].cell(6,0).text,'','## 요약','',a.text,'']
for para in d.paragraphs:
 if not para.text.strip():continue
 lines += [('## ' if para.style.name=='논문 내용 제목' else '')+para.text,'']
 if para.text.startswith('<표 1>'):
  for i,row in enumerate(d.tables[1].rows):
   lines.append('| '+' | '.join(c.text.replace('\n',' ') for c in row.cells)+' |')
   if i==0:lines.append('|---|---:|---:|---:|---:|')
 if para.text.startswith('(그림 1)'):lines+=['![C2−C1 논리적 범위](cohort_bounds_paper_v5.png)','']
out.with_suffix('.md').write_text('\n'.join(lines));print(out)
