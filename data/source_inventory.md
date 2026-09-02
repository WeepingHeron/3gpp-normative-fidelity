# 공식 PDF 선정 및 점검 결과

점검일: 2026-09-01

## 결론

- **주 원문:** 3GPP TS 23.501 V18.12.0 Release 18
- **적격 보조 원문:** 3GPP TS 24.501 V18.12.0 Release 18
- 두 문서는 ETSI 공식 PDF이며 암호화되지 않았고 텍스트 추출이 가능하다.
- `should not` 원시 occurrence 35건을 전수 검토한 결과 `eligible` 18건, `reserve` 8건, `exclude` 9건으로 판정했다.
- 명확한 적격 후보는 TS 23.501 10건, TS 24.501 8건이다. 따라서 pilot 3개와 main 12개를 만들 수 있지만 단일 규격 설계에는 여유 표본이 부족하다.
- 특정 modal 범주만 보조 문서에서 가져오면 문서 특성과 modal 효과가 섞이므로, main은 모든 modal 범주에서 두 규격을 6개씩 균형화한다.
- 상세 판정은 `../outputs/01a041cb-a998-76f0-abd3-65e557043a7a/should_not_candidate_audit.xlsx`에 기록했다.

## 파일 검증

| 구분 | TS 23.501 | TS 24.501 |
|---|---:|---:|
| ETSI 표기 | TS 123 501 V18.12.0 | TS 124 501 V18.12.0 |
| 3GPP 표기 | TS 23.501 Release 18 | TS 24.501 Release 18 |
| 발행월 | 2026-01 | 2025-10 |
| 전체 페이지 | 723 | 1,204 |
| 파일 크기 | 6,643,370 bytes | 7,896,856 bytes |
| 암호화 | 없음 | 없음 |
| SHA-256 | `2ef71f81a87c86967dc623741b5a3479338844661067a3bb13089fffe6fed2ac` | `fef06d660506abf6885d593e4129095c17140be4f2317e802daa8599233f1b06` |

## Modal 원시 출현 수

아래 값은 대소문자를 무시한 정규식 검색 결과다. `shall not`은 `shall`에서, `should not`은 `should`에서, `cannot/can not`은 `can`에서 중복 집계하지 않았다.

| 범주 | TS 23.501 조항 4-8 | TS 24.501 조항 4-6 |
|---|---:|---:|
| `shall` | 1,238 | 5,496 |
| `shall not` | 155 | 567 |
| `should` | 227 | 125 |
| `should not` | 17 | 18 |
| `may` | 1,966 | 729 |
| `can` | 1,042 | 568 |
| `cannot` / `can not` | 101 | 109 |

이 수치는 **채택 가능한 사례 수가 아니다.** NOTE, 표 설명, 외부 인용, 중복 문장, 파서 단편, 행위자가 불명확한 문장을 제거해야 한다. 특히 `may`와 `can`은 일반 가능성 서술이 많으므로 허용·능력 의미인지 사람이 판정해야 한다.

## 확정된 수집 순서

1. Main 72개는 각 modal 범주마다 TS 23.501 6개와 TS 24.501 6개를 선택한다.
2. Pilot 18개는 두 규격에서 총 9개씩 뽑는다. `should_not`은 TS 23.501 2개와 TS 24.501 1개를 사용하고, 다른 범주에서 반대로 배분해 전체 균형을 맞춘다.
3. exact duplicate와 near-duplicate는 pilot과 main에 나누어 넣지 않는다. 하나만 선택하거나 같은 split에 묶는다.
4. `eligible`부터 사용하고 `reserve`는 2차 검토에서 적격 후보가 탈락할 때만 승격한다.
5. 최종 case 작성 시 공식 PDF에서 문장 전체, 조항 번호, 조건과 예외를 다시 대조한다.

## 공식 출처

- [ETSI TS 123 501 V18.12.0 PDF](https://www.etsi.org/deliver/etsi_ts/123500_123599/123501/18.12.00_60/ts_123501v181200p.pdf)
- [3GPP TS 23.501 규격 페이지](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3144)
- [ETSI TS 124 501 V18.12.0 PDF](https://www.etsi.org/deliver/etsi_ts/124500_124599/124501/18.12.00_60/ts_124501v181200p.pdf)
- [3GPP TS 24.501 규격 페이지](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3370)
