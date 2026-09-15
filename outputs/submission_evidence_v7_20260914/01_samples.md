# 표본 구성

기존 72건은 일반 적격 50·조건부 예외 1·부적격 10·보류 11로 재감사됐다. 일반 적격에서 C2 입력 오염 MAY-001을 제외해 주 분석 49건이다. Gold 50은 MAY-001, Exception 50은 SDN-011, Both 51은 둘 다 복원한다. 제외 기준의 기존 규약과 사후 분석 처리 동결을 구분한다.

아래 규범 유형·난도는 최초 표본의 층화 라벨이며 수정 정답의 규범 판정 분포를 뜻하지 않는다. 네 분석 집합은 겹친다. 사례 수를 더하거나 반복을 독립 표본으로 세지 않는다.

## spec_id

| 집합 | 3GPP TS 23.501 | 3GPP TS 24.501 | 합계 |
|---|---:|---:|---:|
| ORIGINAL_72 | 36 | 36 | 72 |
| PRIMARY_STRICT_49 | 23 | 26 | 49 |
| SENS_GOLD_50 | 24 | 26 | 50 |
| SENS_EXCEPTION_50 | 23 | 27 | 50 |
| SENS_GOLD_EXCEPTION_51 | 24 | 27 | 51 |

## modal_class

| 집합 | can | may | shall | shall_not | should | should_not | 합계 |
|---|---:|---:|---:|---:|---:|---:|---:|
| ORIGINAL_72 | 12 | 12 | 12 | 12 | 12 | 12 | 72 |
| PRIMARY_STRICT_49 | 9 | 9 | 8 | 9 | 8 | 6 | 49 |
| SENS_GOLD_50 | 9 | 10 | 8 | 9 | 8 | 6 | 50 |
| SENS_EXCEPTION_50 | 9 | 9 | 8 | 9 | 8 | 7 | 50 |
| SENS_GOLD_EXCEPTION_51 | 9 | 10 | 8 | 9 | 8 | 7 | 51 |

## difficulty_tier

| 집합 | compound | conditional | simple | 합계 |
|---|---:|---:|---:|---:|
| ORIGINAL_72 | 42 | 22 | 8 | 72 |
| PRIMARY_STRICT_49 | 28 | 15 | 6 | 49 |
| SENS_GOLD_50 | 28 | 15 | 7 | 50 |
| SENS_EXCEPTION_50 | 29 | 15 | 6 | 50 |
| SENS_GOLD_EXCEPTION_51 | 29 | 15 | 7 | 51 |

주 분석은 33개 규격·조항 군집이며 민감도 집합은 각각 34·34·35개다. 최초 규격별 36건·규범 유형별 12건의 균형은 49건에 자동 유지되지 않는다.

72건의 개별 포함/제외 이유: [case_membership_72.csv](case_membership_72.csv).