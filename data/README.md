# Data

## 예정 구조

```text
data/
├── README.md
├── cases_template.csv
├── source/
│   └── <pinned official specification.pdf>
├── source_manifest.json
├── pilot_cases.csv
├── main_cases.csv
└── exclusions.csv
```

PDF 원문을 저장소에 포함하거나 외부에 배포하기 전에는 배포 권한을 별도로 확인한다. 논문·공개 데이터셋에는 필요한 최소 인용과 공식 URL만 포함하고 원문 전체를 재배포하지 않는다.

## 현재 상태

- `source_manifest.json`: TS 23.501·TS 24.501 V18.12.0 원문과 SHA-256 고정
- `pilot_cases.csv`: 6개 modal class별 3건, 총 18건 완료
- source 균형: TS 23.501 9건·TS 24.501 9건
- `review_status`: 전 사례 `self_checked`; 아직 독립 2차 검토 전

검토용 workbook은 `outputs/01a041cb-a998-76f0-abd3-65e557043a7a/pilot_cases_review.xlsx`에 있다. 단, dry run에서 `PILOT-CAN-001`의 대안 통신 방식이 exception이 아니라 action의 선택지임이 확인되어 canonical CSV의 exception을 빈 값으로 수정했다. 따라서 현재 workbook은 이 한 셀에 대해 pre-refinement 상태이며 재생성이 필요하다. Canonical source는 `pilot_cases.csv`다.
