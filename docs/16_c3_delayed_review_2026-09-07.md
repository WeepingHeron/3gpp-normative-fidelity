# C3 지연 재검토와 불일치 조정

2026-09-07. C1/C2/C3의 216개 설명을 새 D001–D216 순서로 원문·동결 gold와 다시 대조했다. 완전 보존 판정은 첫 평가와 216/216 일치했고, C1 61/72, C2 71/72, C3 65/72가 유지됐다. 이는 동일 Codex의 판단 안정성 점검이며 독립 통신 전문가 검증은 아니다.

## 절차와 증거

첫 평가 완료는 9월 6일 14:08:17 KST, 이번 시작 확인은 9월 7일 14:36 KST, 전수 판정 동결은 14:45:06 KST다. UTC 시각과 최소 24시간 경과를 코드로 확인했다. 점수·근거 216행을 직접 작성하고 동결한 뒤에만 대응 키와 첫 평가 행별 점수를 열었다. 기존 조건별 집계와 설계를 알고 있으므로 완전 맹검이 아니며, 시간차가 AI 평가자의 기억 효과를 제거한다고 주장하지 않는다. 모델 응답 재생성이나 API 호출은 하지 않았다.

적용 가능한 이진 판정은 1,131개 중 1,128개(99.735%)가 일치했다. 2개 응답의 세부 판정 3개가 달랐고 원문 대조 후 조정했다. 완전 보존 여부는 모두 일치하므로 집계 점수와 paired 차이는 바뀌지 않았다.

| 사례·조건 | 다른 세부 판정 | 조정 결과와 근거 |
|---|---|---|
| MAIN-CAN-008 · C3 | actor, action | 두 항목 실패 채택. 원문의 security 활성화 가능성에 걸린 주체·동작을 AMF/UE의 context 수립 능력으로 옮겼다. 실제 context 수립 전제와 능력 보유는 다르다. |
| MAIN-SDN-010 · C2 | exception | 실패 채택. 7종이라는 개수만 같아서는 충분하지 않다. mobile terminated를 이동 종료로 옮겨 착신 요청 대상 및 그 7종의 한정 범위가 달라졌다. |

TS 24.501의 PDF 53쪽에서 context 실제 수립 전제를, 133쪽에서 PLMN/SNPN 식별자·목록 문맥을, 197쪽에서 congestion과 paging/notification으로 시작되는 요청 범주를 재확인했다. TS 23.501 PDF 45쪽의 may have the capability 문맥도 대조했다. 모바일 착신 용례는 3GPP TS 51.010-1의 incoming call / mobile terminating 절 구성과도 일치한다([3GPP 원본](https://www.3gpp.org/ftp/tsg_geran/wg4_terminal_testing-radio_aspects/PDF_versions/51010-1-530.pdf)). 이 보조 용례는 연구의 고정 규격 버전을 교체하지 않는다.

이전 9월 3일 동결 main 판정과 새 첫 평가가 달랐던 9개 응답도 이번 전수 대조에 포함됐다. 9개 모두 새 첫 평가의 성공/실패 판정이 유지됐다. 이전 main 응답·점수·입력은 수정하지 않았고 `archived_main_discrepancies_rechecked.csv`에 두 이력과 근거를 함께 보존했다.

## 결과 해석

| 비교 | 표본 | 차이 | case bootstrap 95% 구간 | 양측 exact McNemar p |
|---|---:|---:|---:|---:|
| C3−C1 | 72 | +5.56%p | −2.78~+13.89%p | 0.34375 |
| C3−C1 · 원래 모호성 3건 제외 | 69 | +7.25%p | −1.45~+15.94%p | 0.17969 |
| C2−C3 | 72 | +8.33%p | +1.39~+16.67%p | 0.07031 |
| C2−C3 · 원래 모호성 3건 제외 | 69 | +5.80%p | 0.00~+13.04%p | 0.21875 |

C3−C1은 개선을 확정할 수 없다. 44개 조항 cluster bootstrap도 첫 평가와 완전 보존 벡터가 동일해 −2.53~+15.52%p로 유지된다. C2−C3의 bootstrap과 exact 검정은 작은 이산 표본에서 결론이 다를 수 있으므로 유의성을 단정하지 않는다.

새로 확인된 MAY-001과 SD-009 범위 모호성까지 포함해 총 5건을 제외한 사후 민감도에서도 C3−C1은 59/67 대 63/67, +5.97%p, p=0.28906이다. C2−C3는 +4.48%p, p=0.375다. 이 분석은 주 분석의 72개 분모를 대체하지 않으며 gold 자체를 수정하지 않는다.

## 현재 완료 경계

설명 216행의 지연 재검토·조정은 완료했다. 추출 구조 72행의 슬롯/슬롯 간 진단은 9월 6일 첫 검토에 근거한 탐색 분석으로 남는다. 단일 모델·두 규격 한 버전·선정된 72개 문장·동일 AI 평가자라는 범위와 생성 날짜 차이도 유지된다.

근거 디렉터리: `experiments/runs/c3_auto72_v1_2026-09-06T04-53-06-942Z/review/delayed_pass2/`.

- `pass2_decisions.tsv`, `pass2_freeze_manifest.json`: 키 복원 전 전수 판단과 동결
- `adjudication_decisions.tsv`, `adjudication_log.csv`: 명시적 조정 판단과 세부 차이
- `scores_adjudicated.csv`, `summary_adjudicated.json`, `adjudicated_freeze_manifest.json`: 최신 설명 평가와 해시
- 집계 코드: `tools/summarize_c3_delayed.py`. 기존 산출물 덮어쓰기를 막도록 구성했으므로 재집계는 별도 복사 환경에서 수행한다.

생성 시점의 `generation_complete_semantics_pending` 및 과거 준비 manifest의 `PREPARED_NOT_REVIEWED`는 당시의 동결 기록이다. 최신 의미 평가 상태는 위 조정 manifest를 따른다.
