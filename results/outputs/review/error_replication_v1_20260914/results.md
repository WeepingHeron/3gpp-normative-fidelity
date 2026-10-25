# 추가 오류 재현 결과

기존 개발 원문 3개에 동일 A2 요청을 각 3회 계획했다. 9개 중 첫 SMF 슬롯은 통신 결과 미상이며 재시도하지 않았다. 승인 후 나머지 8개를 실행해 모두 정상 응답을 받았다. 결과 미상 1건은 의미 실패와 구분하며 9개 전체의 완수율을 산출하지 않는다. 완료 응답 8개는 완수 3개·미완수 5개·미확정 0개다. 동일 진행 AI의 수동 1차 판정으로 독립 전문가 검증이 아니다.

| 원문 | 계획 | 완료 | 완수 | 미완수 | 결과 미상 |
|---|---:|---:|---:|---:|---:|
| SMF | 3 | 2 | 2 | 0 | 1 |
| NSSAI | 3 | 3 | 1 | 2 | 0 |
| AMF | 3 | 3 | 0 | 3 | 0 |

AMF 3개 모두 규범 강도 변경과 망 검증 설정 조건 누락이 관찰됐다. NSSAI 3개 중 2개는 eCall 복합 예외의 일부가 누락됐다. 이것은 알려진 3개 원문 내 반복 관찰이며 일반 오류율이나 새 조항 검증이 아니다. temperature 0에서도 실제 문구가 달랐으며 독립 표본으로 간주하지 않는다. 프롬프트 수정·재시도·성공 결과 선별 없이 전체 완료 출력을 평가했다.

8개 정상 응답의 반환 usage 기준 비용은 $0.01865325다. 최초 결과 미상 요청의 비용은 확인되지 않아 전체 실제 청구액은 미확정이다.

## ERR-CTX-002-R1

출처: 3GPP TS 24.501 §4.6.2.2

원문: The allowed NSSAI(s) should be stored in a non-volatile memory in the ME as specified in annex C.

실제 설명: 출처 식별자 spec: 3GPP TS 24.501, version: 18.12.0, clause: 4.6.2.2에 따르면, SNPN access operation mode가 아닌 UE에서는 allowed NSSAI(s)를 USIM의 SUPI와 함께 ME의 비휘발성 메모리에 저장하는 것이 권고된다(should). 이 저장은 annex C에 지정된 방식에 따라 이루어지며, allowed NSSAI(s)는 SUPI가 USIM의 SUPI와 일치할 때만 사용할 수 있다. 일치하지 않으면 UE는 allowed NSSAI(s)를 삭제해야 하며, UE가 긴급 서비스에 등록된 경우에는 이 부속서의 5GMM 파라미터를 USIM이나 비휘발성 메모리에 저장하지 말고 ME에 임시로만 저장했다가 긴급 서비스 등록 해제 시 삭제해야 하고, eCall only 모드인 경우에도 같은 파라미터를 USIM이나 비휘발성 메모리에 저장하지 말고 ME에 임시 저장 후 5GMM-DEREGISTERED.eCALL-INACTIVE 상태 진입, 전원 차단, 또는 USIM 제거 시 삭제해야 한다.

판정: 1 / 비SNPN 저장 권고·SUPI 결합 및 불일치 삭제·긴급 등록과 eCall 각각의 비저장/임시 저장/삭제 사건을 설명에 보존했다. 저장 SUPI의 지시 대상은 앞 문장에서 복원 가능하다.

## ERR-CTX-003-R1

출처: 3GPP TS 23.501 §5.4.11.4

원문: The AMF should not reject the request or deregister the UE unless it has sufficiently accurate UE location information to determine that the UE is located in a geographical area where the PLMN is not allowed to operate.

실제 설명: [PDF page 133] 5.4.11.4에서, AMF는 충분히 정확한 UE 위치정보가 있어 UE가 PLMN이 운용할 수 없는 지리적 영역에 있다고 판단할 수 없는 한, UE의 요청을 거절하거나 UE를 등록해제해서는 안 된다. 이 규칙은 NR satellite access를 사용하는 UE에 대해, AMF가 NGAP 메시지의 User Location Information과 Selected PLMN ID를 바탕으로 위치를 검증하는 맥락에서 적용된다. 반대로, AMF가 그 정도로 정확한 위치정보를 가지고 해당 UE가 PLMN 운용 제한 지역에 있다고 판단할 수 있을 때에만 이 예외가 성립한다.

판정: 0 / should not을 “등록해제해서는 안 된다”로 강제 금지화했다. 위성 접속 범위는 있으나 망이 검증하도록 설정된 경우라는 조건은 없다.

## ERR-CTX-001-R2

출처: 3GPP TS 23.501 §4.2.3

원문: However, each SMF may also have the capability to control both a local and a central UPF within a PDU Session.

실제 설명: [PDF page 45]의 문맥에서, 여러 PDU Session을 사용하는 경우에는 두 개의 서로 다른 PDU Session에 대해 두 개의 SMF가 선택되는 구성을 설명하고 있다. 그와 별개로, 각 SMF는 하나의 PDU Session 안에서 local UPF와 central UPF를 모두 제어할 수 있는 능력을 가질 수도 있다(may also have the capability). 이 문장은 그러한 능력이 선택적으로 존재할 수 있음을 말할 뿐, 각 SMF가 반드시 그 능력을 가져야 한다고 요구하지는 않는다.

판정: 1 / “능력을 가질 수도 있다”, “선택적으로 존재”가 능력 보유의 선택성을 보존하며 하나의 세션에서 두 UPF 모두를 명시한다. 메타데이터 capability만으로 설명을 실패 처리하지 않는다.

## ERR-CTX-002-R2

출처: 3GPP TS 24.501 §4.6.2.2

원문: The allowed NSSAI(s) should be stored in a non-volatile memory in the ME as specified in annex C.

실제 설명: 이 규칙은 Annex C의 규정에 따라, SNPN access operation mode가 아닌 UE에서 allowed NSSAI(s)를 USIM의 SUPI와 함께 ME의 비휘발성 메모리에 저장해야 한다는 권고를 뜻한다. 다만 allowed NSSAI(s)는 SUPI from the USIM이 ME의 비휘발성 메모리에 저장된 SUPI와 일치할 때만 사용할 수 있으며, 일치하지 않으면 UE는 이를 삭제해야 한다. 또한 UE가 긴급 서비스에 등록된 경우에는 이 부속서의 5GMM 파라미터를 USIM이나 비휘발성 메모리에 저장하지 말고 ME에 임시로만 저장해야 하며, 긴급 서비스 등록 해제 시 삭제해야 하고, eCall only 모드에서는 5GMM-DEREGISTERED.eCALL-INACTIVE 상태 진입, 전원 꺼짐, USIM 제거 시 삭제해야 한다.

판정: 0 / “저장해야 한다는 권고”는 권고임을 명시하므로 의무화로 단정하지 않는다. 긴급 등록의 비저장·임시 저장 뒤 eCall에는 삭제 사건만 기술하고 eCall 자체의 비저장 및 임시 저장 규칙은 보존하지 않았다.

## ERR-CTX-003-R2

출처: 3GPP TS 23.501 §5.4.11.4

원문: The AMF should not reject the request or deregister the UE unless it has sufficiently accurate UE location information to determine that the UE is located in a geographical area where the PLMN is not allowed to operate.

실제 설명: [PDF page 133] 5.4.11.4 Verification of UE location에 따르면, AMF는 UE의 위치가 PLMN의 운용이 허용되지 않는 지리적 영역에 있다고 판단할 수 있을 만큼 충분히 정확한 UE 위치정보를 가지고 있을 때에만 UE의 요청을 거절하거나 UE를 등록해제해야 한다. 반대로 그러한 충분히 정확한 위치정보가 없으면, AMF는 요청을 거절하거나 UE를 deregister해서는 안 된다고 권고된다. 이 규칙은 NR satellite access에서 UE 위치를 검증하는 맥락, 즉 AMF가 Selected PLMN ID와 ULI(셀 ID 포함) 및 UE의 network verified UE location over NR NTN 지원 능력을 고려해 위치 검증을 수행하는 경우에 적용된다.

판정: 0 / 첫 문장의 “있을 때에만 ... 등록해제해야 한다”는 원문의 비권고/예외를 처리 의무로 바꾼다. 뒤의 비권고 설명이 이 적극적 의무를 철회하지 않는다. 위성 범위는 있고 망 검증 설정 조건은 빠졌다.

## ERR-CTX-001-R3

출처: 3GPP TS 23.501 §4.2.3

원문: However, each SMF may also have the capability to control both a local and a central UPF within a PDU Session.

실제 설명: [PDF page 45]의 문맥에서, 두 개의 서로 다른 PDU Session을 사용해 로컬 및 중앙 데이터 네트워크에 동시에 접근하는 비로밍 구조를 설명하면서, 각 SMF는 하나의 PDU Session 안에서 local UPF와 central UPF를 모두 제어할 수 있는 능력을 가질 수도 있다고 말한다. 여기서 대상 규칙의 행위자는 각 SMF이며, 규범 표현 may have the capability는 그 능력을 보유하는 것이 선택적임을 뜻한다. 이 문장은 반드시 그렇게 해야 한다는 의무나 허용을 부여하는 것이 아니라, 하나의 PDU Session에서 두 UPF를 함께 제어하는 구성이 가능함을 나타낸다.

판정: 1 / 능력을 가질 수도 있고 보유가 선택적이라고 명시하며 하나의 세션에서 양 UPF를 보존한다. 마지막 허용 부정은 제어 행동 허가와 능력 보유를 구분하는 문맥으로, 앞의 선택성을 철회하지 않는다.

## ERR-CTX-002-R3

출처: 3GPP TS 24.501 §4.6.2.2

원문: The allowed NSSAI(s) should be stored in a non-volatile memory in the ME as specified in annex C.

실제 설명: 이 규칙은 Annex C의 규정에 따라, SNPN access operation mode가 아닌 UE에 대해 allowed NSSAI(s)를 USIM의 SUPI와 함께 ME의 비휘발성 메모리에 저장하는 것을 다룬다. 대상 문장의 should는 권고이므로, allowed NSSAI(s)는 비휘발성 메모리에 저장되어야 하는 권고 사항이며, 문맥상 allowed NSSAI(s)는 SUPI가 USIM의 SUPI와 일치할 때만 사용할 수 있다. 일치하지 않으면 UE는 allowed NSSAI(s)를 삭제해야 하며, UE가 긴급 서비스에 등록된 경우에는 이 부속서의 5GMM 파라미터를 USIM이나 비휘발성 메모리에 저장하지 말고 ME에 임시로만 저장했다가 긴급 서비스 등록 해제 시 삭제해야 하고, eCall only 모드에서는 USIM이나 비휘발성 메모리에 저장하지 말고 5GMM-DEREGISTERED.eCALL-INACTIVE 상태 진입, 전원 차단, 또는 USIM 제거 시 삭제해야 한다.

판정: 0 / should 권고와 SUPI 조건, 긴급 등록 예외를 보존한다. eCall 비저장·삭제 사건은 있으나 eCall 시 ME 임시 저장이 설명에서 빠졌다. action/exception 메타데이터의 임시 저장 표현으로 설명의 누락을 복구하지 않는다.

## ERR-CTX-003-R3

출처: 3GPP TS 23.501 §5.4.11.4

원문: The AMF should not reject the request or deregister the UE unless it has sufficiently accurate UE location information to determine that the UE is located in a geographical area where the PLMN is not allowed to operate.

실제 설명: [PDF page 133] 5.4.11.4 Verification of UE location에 따르면, AMF는 UE의 위치가 PLMN의 운용이 허용되지 않는 지역인지 판단할 수 있을 만큼 충분히 정확한 UE 위치정보를 가지고 있지 않다면 UE 요청을 거절하거나 UE를 등록해제해서는 안 된다. 이 규칙은 NR satellite access를 사용하는 UE에 대해, gNB로부터 받은 Selected PLMN ID와 ULI(셀 ID 포함) 또는 다른 충분히 정확한 위치정보를 바탕으로 AMF가 현재 UE 위치에서 해당 PLMN의 운용 가능 여부를 판단하는 경우에 적용된다. 반대로 AMF가 그 정도로 정확한 위치정보를 확보해 해당 UE가 PLMN 운용이 허용되지 않는 지리적 영역에 있다고 판단할 수 있을 때에만, 요청 거절 또는 등록해제 여부를 고려할 수 있다.

판정: 0 / “등록해제해서는 안 된다”가 should not을 강제 금지로 바꾼다. 위성 접속 범위는 있으나 망 검증 설정이라는 적용 조건은 없다.
