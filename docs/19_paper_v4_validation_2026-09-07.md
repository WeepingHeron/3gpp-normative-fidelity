# 논문 v4 반영과 검증

2026-09-07. v3의 관련 단락·요약·표·그림만 수정해 v4 DOCX·PDF·Markdown을 작성했다. C1/C2/C3 지연 조정 결과와 C1M 첫 평가의 잠정 상태, 전체·제외 분석 및 해석 민감도를 구분했다. 기존 제목·저자·절 순서·참고문헌·KIPS 페이지 크기·여백·2단 설정은 유지했다.

번들 LibreOffice로 2쪽 전체를 렌더링하고 두 페이지 이미지를 확인했다. 한글·표·그림·캡션·참고문헌의 잘림이나 겹침은 없다. PDF에서 61/72, 71/72, 65/72, 68/72 및 p=0.34375, 0.06543, 0.22656을 확인했다. C1M은 표와 그림에 별표로 첫 평가임을 표시했다. DOCX의 기존 package part 중 본문과 본문 관계 파일만 변경됐고 새 그림이 추가됐다. 페이지·여백·단 XML은 v3와 같으며 tracked insertion/deletion은 없다. v2/v3 원본 해시도 유지됐다.

- 최신 파일: `outputs/paper/ACK2026_3GPP_normative_fidelity_draft_v4.docx`, 같은 이름의 PDF·Markdown
- DOCX SHA-256: `cf1a36a8a4deff6af047539d9c4e954c12d24011cce56011a86ad02a77dd6dc8`
- PDF SHA-256: `75ff995e24be23a2eb96e95ed3849efaac0a1a96119b7e994e30e5945933546f`
- 통계·평가 근거: `docs/16_c3_delayed_review_2026-09-07.md`, `docs/17_c1m_semantic_review_pass1_2026-09-07.md`

재현은 과학 그림 스크립트 `tools/generate_review_figure_v4.py`를 실행한 뒤 번들 Python으로 `tools/revise_paper_v4_20260907.py`를 실행하고 `sh tools/render_kips_paper.sh outputs/paper/ACK2026_3GPP_normative_fidelity_draft_v4.docx`로 렌더링한다. 그림에는 Matplotlib 환경이 필요하다. 문서 편집·렌더링에는 번들 문서 런타임을 사용한다.

이 버전은 C1M 지연 재검토 전의 연구 편집본이다. 독립 전문가 검증이나 새 조항 일반화 검증을 완료한 제출 확정본으로 표시하지 않는다.

최종 교차 검사는 14개 동결 manifest의 97개 파일 해시 항목, 판정 432행의 원응답 연결·완전보존 계산, C1M 지연 평가용 216행의 빈 점수를 확인했다. 기존 통계 함수와 별도로 불일치 쌍의 가능한 부호 조합을 전수 계산해 C3 대 C1의 p=0.34375와 C1M 대 C1의 p=0.0654296875를 재확인했다. 결과는 `outputs/analysis/review_resume_20260907_validation.json`, 이번 산출물 해시 목록은 `outputs/analysis/review_resume_20260907_manifest.json`에 저장했다. 이 검사는 자료 무결성과 산술 재현성에 대한 검사이며 독립적인 의미 판정은 아니다.
