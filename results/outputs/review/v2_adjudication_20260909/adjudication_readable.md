# v2 불일치 조정 근거

동일 평가자의 공개된 사후 조정 기록이다. 기존 두 차수의 봉인 자료는 그대로 보존한다. 조건별 결과를 보고 상태를 선택하지 않았으며 독립 검증으로 주장하지 않는다.

## V2-P2-019 · G031 · PASS

1차 PASS → 2차 FAIL → 조정 PASS; 적용: R3, R4, R8.

원문: To avoid paging in the entire PLMN, when the AMF allocates the Active Time the AMF should not allocate "all PLMN" registration area to the UE.

응답: 전체 PLMN paging을 피하기 위해 AMF가 Active Time을 할당할 때, AMF는 UE에 "all PLMN" registration area를 할당하지 않는 것이 권고된다. 이는 전체 PLMN paging을 피하려는 조건에서 적용된다.

1차 근거: Active Time 할당 시 all-PLMN 영역을 배정하지 않는 권고와 전체 PLMN paging 회피 목적을 모두 보존한다. 마지막 조건이라는 표현은 앞의 목적을 재언급하며 다른 경우의 허용을 추가하지 않는다.

2차 근거: Active Time 할당 시 비권고는 맞지만 paging 회피 목적을 추가 적용 조건으로 명시해 범위를 좁힌다.

조정 근거: 첫 문장이 Active Time 할당 조건과 all PLMN 비권고를 완결한다. 뒤의 목적 재언급은 only-if나 다른 경우 허용을 명시하지 않으므로 조건이라는 단어만으로 범위 축소를 확정하지 않는다.

출처: 3GPP TS 23.501 v18.12.0 §5.31.7.4, PDF p.436. 기록 시각: 2026-09-09T05:06:06.794748+00:00.

## V2-P2-070 · G010 · PASS

1차 PASS → 2차 FAIL → 조정 PASS; 적용: R1, R3, R4.

원문: However, each SMF may also have the capability to control both a local and a central UPF within a PDU Session.

응답: 각 SMF는 하나의 PDU Session 안에서 로컬 UPF와 중앙 UPF를 모두 제어할 수 있는 능력이 있을 수 있다. 이는 의무나 금지가 아니라 기술적 가능성을 나타낸다.

1차 근거: 하나의 session에서 local과 central UPF 모두를 제어할 능력이 있을 수 있다고 하여 능력 보유의 선택성을 남겼다. 기술적 가능성이라는 부연도 모든 SMF의 능력 보유나 제어 행동 자체의 허가를 확정하지 않는다.

2차 근거: 능력의 대상과 보유 가능성은 남지만 may의 선택적 능력 보유를 기술적 가능성으로 단정해 유형을 바꾼다.

조정 근거: 능력이 있을 수 있다는 표현이 보유 여부의 선택성과 두 UPF의 제어 대상을 남긴다. 기술적 가능성이라는 부연은 그 능력을 설명할 수 있고 보유를 확정하거나 행동 허가로 바꾸지 않으므로 유형 명칭 하나로 FAIL하지 않는다.

출처: 3GPP TS 23.501 v18.12.0 §4.2.3, PDF p.45. 기록 시각: 2026-09-09T05:06:06.794748+00:00.

## V2-P2-099 · G050 · FAIL

1차 PASS → 2차 FAIL → 조정 FAIL; 적용: R3, R4, R8.

원문: Once the secure exchange of NAS messages has been established, the receiving 5GMM entity in the UE shall not process any NAS signalling messages unless they have been successfully integrity checked by the NAS.

응답: secure NAS 메시지 교환이 설정된 뒤에는 UE의 수신 5GMM 엔티티가 NAS에 의해 성공적으로 무결성 검사를 받은 경우를 제외하고 어떤 NAS 시그널링 메시지도 처리해서는 안 된다.

1차 근거: secure 교환 이후 성공적인 NAS integrity 검사 없이는 어떤 NAS signalling message도 처리해서는 안 된다는 금지와 예외 필요조건을 보존한다.

2차 근거: 무결성 검사의 대상을 NAS 메시지에서 UE의 수신 5GMM 엔티티로 바꾸었다.

조정 근거: 엔티티가 NAS에 의해 무결성 검사를 받았다는 문법적 주어와 피검사자의 연결이 명시된다. 메시지가 아니라 엔티티를 검사 대상으로 둔 오류를 고쳐 읽어야 하므로 단순 문체 차이로 인정하지 않는다.

출처: 3GPP TS 24.501 v18.12.0 §4.4.4.2, PDF p.65. 기록 시각: 2026-09-09T05:06:06.794748+00:00.

## V2-P2-106 · G010 · UNRESOLVED

1차 FAIL → 2차 UNRESOLVED → 조정 UNRESOLVED; 적용: R1, R3.

원문: However, each SMF may also have the capability to control both a local and a central UPF within a PDU Session.

응답: 그러나 각 SMF는 하나의 PDU Session 내에서 local UPF와 central UPF를 모두 제어할 수 있는 능력이 있다. 이는 허용 또는 선택 가능을 나타내며, 반드시 해야 한다는 의미는 아니다.

1차 근거: 첫 문장에서 각 SMF의 제어 능력 보유를 확정한다. 뒤의 허용·선택 가능 부연은 무엇이 선택적인지 불명확하며 능력이 없을 수도 있다는 명시적 정정이 아니므로 선택적 능력 보유를 분명하게 보존하지 못한다.

2차 근거: 첫 문장은 모든 SMF의 능력 보유를 확정하고 둘째는 선택 가능이라 하나 지시 대상이 보유인지 제어인지 불명확하다.

조정 근거: 능력이 있다는 첫 문장과 선택 가능이라는 뒤 문장 사이에서 이는의 대상이 보유인지 행동인지 확정되지 않는다. R3의 지시 대상 불명확 규칙을 적용하고 명백한 보유 확정만 있는 158과 구분한다.

출처: 3GPP TS 23.501 v18.12.0 §4.2.3, PDF p.45. 기록 시각: 2026-09-09T05:06:06.794748+00:00.

## V2-P2-151 · G050 · FAIL

1차 PASS → 2차 FAIL → 조정 FAIL; 적용: R3, R4, R8.

원문: Once the secure exchange of NAS messages has been established, the receiving 5GMM entity in the UE shall not process any NAS signalling messages unless they have been successfully integrity checked by the NAS.

응답: secure NAS message exchange가 설정된 뒤에는 UE의 수신 5GMM entity가 NAS에 의해 성공적으로 무결성 검사를 받은 경우가 아니면 어떤 NAS signalling message도 처리해서는 안 된다. 즉, NAS 무결성 검사가 성공한 경우에만 처리할 수 있다.

1차 근거: secure 교환 수립 후 NAS integrity 검사 성공을 메시지 처리의 필요조건으로 보존한다. 성공했으면 반드시 처리한다는 충분조건 주장은 없다.

2차 근거: 첫 문장이 integrity 검사의 대상을 entity로 명시하며 뒤 문장은 검사 대상 오류를 분명히 정정하지 않는다.

조정 근거: 첫 문장에서 엔티티가 검사를 받은 것으로 명시한다. 뒤 문장도 검사 성공만 말하며 검사 대상을 메시지로 바로잡지 않아 첫 오류가 남는다. 실제 필요한 행위를 명시해 복원한 137과 다르다.

출처: 3GPP TS 24.501 v18.12.0 §4.4.4.2, PDF p.65. 기록 시각: 2026-09-09T05:06:06.794748+00:00.

