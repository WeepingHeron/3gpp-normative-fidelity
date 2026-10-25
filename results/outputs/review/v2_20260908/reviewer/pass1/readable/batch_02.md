# pass1 검토 자료 44–86

원문·정답 참고 자료이며 판정은 별도 JSONL 사본에 기록한다.

## V2-P1-044
기준 G014 · 3GPP TS 23.501 V18.12.0 · 5.3.2.3 · PDF 98쪽(인쇄 97쪽)

원문: Each N3IWF, TNGF, TWIF and W-AGF may be configured with a different TAI value or with the same TAI value as other N3IWFs, TNGFs, TWIFs and/or W-AGFs.

질문: N3IWF, TNGF, TWIF, W-AGF 사이의 TAI value 구성 관계를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "may",
  "polarity": "positive",
  "actor": "each N3IWF, TNGF, TWIF, and W-AGF",
  "condition": "",
  "action": "be configured with a TAI value different from or the same as the value of the other listed access functions",
  "exception": "",
  "gold_summary_ko": "각 기능에는 다른 기능과 서로 다른 TAI value 또는 동일한 TAI value를 구성할 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

각 N3IWF, TNGF, TWIF 및 W-AGF는 다른 TAI 값으로 구성되거나, 다른 N3IWF, TNGF, TWIF 및/또는 W-AGF와 동일한 TAI 값으로 구성되도록 허용된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 123 501 V18.12.0 (2026-01)973GPP TS 23.501 version 18.12.0 Release 18
TAI used for non-3GPP access shall be dedicated to non-3GPP access. TAI(s) dedicated to Non-3GPP access may be 
defined in a PLMN and apply within this PLMN. Each N3IWF, TNGF, TWIF and W-AGF is locally configured with 
one TAI value. 
[대상 문장]
. The TAI is provided to the AMF during N2 
interface setup and as part of the User Location Information in UE associated messages as described in TS 38.413 [34]. 
When a UE registers with the network over a Non-3GPP access, the AMF allocates to the UE a registration area that 
only includes the TAI received from the serving N3IWF, TNGF, TWIF or W-AGF. 
NOTE 1: For example, two W-AGFs can each correspond to a different TAI (one TAI per W-AGF) and thus 
support different sets of S-NSSAI(s). 
When generating the TAI list, the AMF shall include only TAIs that are applicable on the access type (i.e. 3GPP access 
or Non-3GPP access) where the TAI list is sent. 
NOTE 2: To prevent extra signalling load resulting from Mobility Registration Update occurring at every RAT 
change, it is preferable to avoid generating a RAT-specific TAI list for a UE supporting more than one 
RAT. 
NOTE 3: For a UE registered on N3GPP access the TAI(s) prov ided t
```

</details>

## V2-P1-045
기준 G050 · 3GPP TS 24.501 V18.12.0 · 4.4.4.2 · PDF 65쪽(인쇄 64쪽)

원문: Once the secure exchange of NAS messages has been established, the receiving 5GMM entity in the UE shall not process any NAS signalling messages unless they have been successfully integrity checked by the NAS.

질문: secure NAS message exchange가 설정된 뒤 UE receiving 5GMM entity의 NAS signalling message 처리 조건을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall_not",
  "polarity": "negative",
  "actor": "receiving 5GMM entity in the UE",
  "condition": "once secure NAS-message exchange has been established",
  "action": "process NAS signalling messages",
  "exception": "unless the messages have been successfully integrity checked by NAS",
  "gold_summary_ko": "secure exchange 설정 후 UE의 receiving 5GMM entity는 NAS 무결성 검사를 성공한 message가 아니면 처리해서는 안 된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

secure NAS 메시지 교환이 설정된 뒤에는 UE의 수신 5GMM 엔티티가 NAS에 의해 성공적으로 무결성 검사를 받은 경우를 제외하고 어떤 NAS 시그널링 메시지도 처리해서는 안 된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 124 501 V18.12.0 (2025-10)643GPP TS 24.501 version 18.12.0 Release 18
Integrity protection is never applied directly to 5GSM messages, but to the 5GMM message in which the 5GSM 
message is included. 

[대상 문장]
. If NAS 
signalling messages, having not successfully passed the integrity check, are received, then the NAS in the UE shall 
discard that message. The processing of the SECURITY MODE COMMAND message that has not successfully passed 
the integrity check is specified in subclause 5.4.2.5. If any NAS signalling message is received as not integrity protected 
even though the secure exchange of NAS messages has been established by the network, then the NAS shall discard this 
message. 
4.4.4.3 Integrity checking of NAS signalling messages in the AMF 
Except the messages listed below, no NAS signalling messages shall be processed by the receiving 5GMM entity in the 
AMF or forwarded to the 5GSM entity, unless the secure exchange of NAS messages has been established for the NAS 
signalling connection: 
a) REGISTRATION REQUEST; 
b) IDENTITY RESPONSE (if requested identification parameter is SUCI); 
c) AUTHENTICATION RESPONSE; 
d) AUTHENTICATI
```

</details>

## V2-P1-046
기준 G005 · 3GPP TS 24.501 V18.12.0 · 4.4.2.1.1 · PDF 53쪽(인쇄 52쪽)

원문: Before security can be activated, the AMF and the UE need to establish a 5G NAS security context.

질문: 5G NAS security를 활성화하기 전에 AMF와 UE가 충족해야 하는 전제조건을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "can",
  "polarity": "positive",
  "actor": "security",
  "condition": "after the AMF and UE establish a 5G NAS security context",
  "action": "be activated",
  "exception": "security cannot be activated before that context is established",
  "gold_summary_ko": "AMF와 UE가 5G NAS security context를 먼저 설정해야 하며, 그 전에는 security를 활성화할 수 없다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

5G NAS security는 기술적으로 활성화되기 전에 AMF와 UE가 5G NAS security context를 반드시 확립해야 한다. 즉, 해당 context가 확립된 후에만 security가 활성화될 수 있다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
ection of NAS IEs between the UE and the UDM. Security protection involves integrity protection and 
ciphering of the 5GMM messages. 5GSM messages are security protected indirectly by being piggybacked by the 
security protected 5GMM messages (i.e. UL NAS TRANSPORT message and the DL NAS TRANSPORT message). 
The signalling procedures for the control of NAS security are part of the 5GMM protocol and are described in detail in 
clause 5. 
NOTE: The use of ciphering in a network is an operator optio n. In this subclause, for the ease of description, it is 
assumed that ciphering is used, unless explicitly indicated otherwise. Operation of a network without 
ciphering is achieved by configuring the AMF so that it always selects the "null ciphering algorithm", 5G-
EA0. 
4.4.2 Handling of 5G NAS security contexts 
4.4.2.1 General 
4.4.2.1.1 Establishment of 5G NAS security context 
The security parameters for authentication, integrity protection and ciphering are tied together in a 5G NAS security 
context and identified by a key set identifier (ngKSI). The relationship between the security parameters is defined in 
3GPP TS 33.501 [24]. 

[대상 문장]
. Usually, the 5G 
NAS security context is created as the result of a primary authentication and key agreement procedure between the 
AMF and the UE. A new 5G NAS security context may also be created during an N1 mode to N1 mode handover. 
Alternatively, during inter-system change from S1 mode to N1 mode, the AMF not supporting interworking without 
```

</details>

## V2-P1-047
기준 G012 · 3GPP TS 23.501 V18.12.0 · 4.4.8.3 · PDF 92쪽(인쇄 91쪽)

원문: The network instance for the N6 interface (clause 5.6.12) may be indicated by the SMF to the UPF for a given PDU Session during PDU Session establishment procedure.

질문: PDU Session establishment 중 N6 interface의 network instance를 UPF에 전달하는 방식을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "may",
  "polarity": "positive",
  "actor": "SMF",
  "condition": "for a given PDU Session during PDU Session establishment",
  "action": "indicate the N6-interface network instance to the UPF",
  "exception": "",
  "gold_summary_ko": "SMF는 해당 PDU Session의 N6-interface network instance를 UPF에 표시할 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

SMF는 PDU Session establishment procedure 동안 특정 PDU Session에 대해 N6 interface의 network instance를 UPF에 표시하도록 허용된다. 이는 반드시 해야 하는 의무가 아니라 선택적으로 수행할 수 있는 동작이다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
clause 5.27. The NEF exposes 5GS capability to support Time Synchronization 
service as described in clause 5.27.1.8. TSCTSF controls the DS-TT(s) and NW-TT for the (g)PTP based time 
synchronization service. In addition, TSCTSF supports TSC assistance container related functionalities. 
 
 
AMF PCF 
Device side 
 
(R)AN UPF
N7
N3
N2 N4
N1 
AF
SMFN11
N9 
N8
UDM
N10
UE DS -TTEnd Station
Device
TSCTSF N 33 
U -plane
NW -TT
N84
N52 
DN 
NEF 
N30
N85N87
 
Figure 4.4.8.3-1: Architecture to enable Time Sensitive Communication and Time Synchronization 
services 
NOTE 1: If the AF is considered to be trusted by the operator, the AF could interact directly with TSCTSF, the 
connection between AF and TSCTSF is not depicted in the architecture diagram for brevity. 
UPF/NW-TT distributes the (g)PTP messages as described in clause 5.27.1. 
When the UPF supports one or more NW-TT(s), there is one-to-one association between an NW-TT and the network 
instance or between an NW-TT and network instance together with DNN/S-NSSAI in the UPF. When there are multiple 
network instances within a UPF, each network instance is considered logically separate. 
[대상 문장]
. UPF allocates resources based on the Network Instance and S-NSSAI and it is supported 
according to TS 29.244 [65]. DNN/S-NSSAI may be indicated by the SMF together with the network instance to the 
UPF for a given PDU Session during PDU Session establishment procedure. 
NOTE 2: The same NW-TT is used for all PDU Sessions in the UPF for the given DNN/S-NSSAI; the NW-TT is 
unique per DNN/S-NSSAI. This ensures that the UPF selects an N4 session associated with the correct 
TSCTSF when the NW-TT initiates an UMIC or PMIC. At any given time, the NW-TT is associated with 
a single TSCTSF. 
4.4.8.4 Architecture to support IETF Deterministic Networking 
The 5G System is integrated with the Deterministic Network as defined in IETF RFC 8655 [150] as a logical DetNet 
transit router, see Figure 4.4.8.4-1. The TSCTSF performs mapping in the control plane between the 5GS internal 
functions and the DetNet controller. 5G System specific procedure
```

</details>

## V2-P1-048
기준 G030 · 3GPP TS 23.501 V18.12.0 · 5.31.3 · PDF 428쪽(인쇄 427쪽)

원문: To redirect a UE from 5GC to EPC, when the UE sends a Registration Request or Service Request, the AMF sends a Registration Reject or Service Reject with an EMM cause value indicating that the UE should not use 5GC.

질문: UE를 5GC에서 EPC로 redirect할 때 AMF가 reject message의 EMM cause로 전달하는 5GC 사용 지침을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should_not",
  "polarity": "negative",
  "actor": "UE",
  "condition": "when redirecting the UE from 5GC to EPC after a Registration Request or Service Request",
  "action": "use 5GC",
  "exception": "the AMF conveys this in the EMM cause of a Registration Reject or Service Reject",
  "gold_summary_ko": "AMF는 reject message의 EMM cause를 통해 UE가 5GC를 사용하지 않는 것이 권고된다는 뜻을 전달한다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

UE를 5GC에서 EPC로 redirect할 때 AMF는 reject message의 EMM cause로 5GC 사용 지침을 전달해야 한다. 이 지침은 UE가 5GC 대신 EPC를 사용하도록 유도하는 용도이다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
UE selects the core network type (EPC or 5GC) based on the broadcast indications for both EPC and 5GC and the 
UE's EPC and 5GC Preferred Network Behaviour. Networks that support NB-IoT shall broadcast an indication whether 
N3 data transfer is supported or not in system information. 
When the UE performs the registration procedure it includes its Preferred Network Behaviour (for 5G and EPC) in the 
Registration Request message and the AMF replies with the 5G Supported Network Behaviour in the Registration 
Accept message. 
If the UE supports any of the CIoT 5GS Optimisations included in 5GC Preferred Network Behaviour, then when the 
UE performs an Attach or TAU procedure and the UE includes its EPC Preferred Network Behaviour then the UE shall 
also include its 5GC Preferred Network Behaviour. 
In networks that support CIoT features in both EPC and 5GC, the operator may steer UEs from a specific CN type due 
to operator policy, e.g. due to roaming agreements, Preferred and Supported Network Behaviour, load redistribution, 
etc. Operator policies in EPC and 5GC are assumed to avoid steering UEs back and forth between EPC and 5GC. 

[대상 문장]
. The UE 
disables N1 mode and re-enables S1 mode, if it was disabled. The UE then performs either an Attach or TAU in EPC as 
described in clause 5.17.2. 
To redirect a UE from EPC to 5GC, when the UE requests an Attach or TAU procedure or Service Reject, the MME 
sends a reject message with an EMM cause indicating the UE should not use EPC. The UE disables S1 mode and re-
enables N1 mode, if it was disabled. The UE then registers with 5GC as described in clause 5.17.2. 
When determining whether to redirect the UE, the AMF/MME takes into account the UE support of S1/N1 mode, 
respectively and the UE's Preferred Network Behaviour and the Supported Network Behaviour of the network the UE is 
being redirected towards. 
```

</details>

## V2-P1-049
기준 G011 · 3GPP TS 23.501 V18.12.0 · 4.2.8.5.1 · PDF 67쪽(인쇄 66쪽)

원문: When a N5CW device performs an EAP-based access authentication procedure to connect to a trusted WLAN access network, the N5CW device may simultaneously be registered to a 5GC of a PLMN or SNPN.

질문: N5CW device가 trusted WLAN 연결을 위해 EAP 기반 access authentication을 수행할 때 5GC 등록 상태를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "may",
  "polarity": "positive",
  "actor": "N5CW device",
  "condition": "when performing EAP-based access authentication to connect to a trusted WLAN access network",
  "action": "simultaneously be registered to a 5GC of a PLMN or SNPN",
  "exception": "",
  "gold_summary_ko": "그 과정에서 N5CW device는 PLMN 또는 SNPN의 5GC에 동시에 등록되어 있을 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

N5CW device가 trusted WLAN access network에 연결하기 위해 EAP-based access authentication procedure를 수행하는 경우, N5CW device는 PLMN 또는 SNPN의 5GC에 동시에 등록될 수 있도록 허용된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
are the same as 
defined in clause 4.2. 
NOTE 6: The reference architecture in figure 4.2.8.4-1 supports service based interfaces for AMF, SMF and other 
NFs not represented in the figure. 
4.2.8.5 Access to 5GC from devices that do not support 5GC NAS over WLAN 
access 
4.2.8.5.1 General 
The devices that do not support 5GC NAS signalling over WLAN access are referred to as "Non-5G-Capable over 
WLAN" devices, or N5CW devices for short. A N5CW device is not capable to operate as a 5G UE that supports 5GC 
NAS signalling over a WLAN access network, however, it may be capable to operate as a 5G UE over NG-RAN. 
Clause 4.2.8.5 specifies the 5GC architectural enhancements that enable N5CW devices to access 5GC via trusted 
WLAN access networks. A trusted WLAN access network is a particular type of a Trusted Non-3GPP Access Network 
(TNAN) that supports a WLAN access technology, e.g. IEEE 802.11. Not all trusted WLAN access networks support 
5GC access from N5CW devices. To support 5GC access from N5CW devices, a trusted WLAN access network must 
support the special functionality specified below (e.g. it must support a TWIF function). 

[대상 문장]
. The 5GC registration is 
performed by the TWIF function (see next clause) in the trusted WLAN access network, on behalf of the N5CW device. 
The type of EAP authentication procedure, which is used during the 5GC registration to authenticate the N5CW device, 
is specified in TS 33.501 [29]. In this Release of the specification, Trusted WLAN Access for N5CW Device only 
supports IP PDU Session type. 
```

</details>

## V2-P1-050
기준 G001 · 3GPP TS 23.501 V18.12.0 · 4.2.4 · PDF 50쪽(인쇄 49쪽)

원문: The N38 references point can be between V-SMFs in the same VPLMN, or between V-SMFs in different VPLMNs (to enable inter-PLMN mobility).

질문: V-SMF 사이 N38 reference point의 VPLMN 배치 관계를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "can",
  "polarity": "positive",
  "actor": "N38 reference point",
  "condition": "",
  "action": "exist between V-SMFs in the same VPLMN or in different VPLMNs",
  "exception": "the inter-VPLMN case enables inter-PLMN mobility",
  "gold_summary_ko": "N38 reference point는 같은 VPLMN의 V-SMF 사이 또는 서로 다른 VPLMN의 V-SMF 사이에 존재할 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

N38 reference point는 V-SMF 사이의 인터페이스로, VPLMN 내에서 서로 다른 V-SMF 배치 간의 연동을 지원하도록 정의된다. 즉, V-SMF가 VPLMN에 배치되는 관계에서 N38을 통해 상호 연결될 수 있다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 123 501 V18.12.0 (2026-01)493GPP TS 23.501 version 18.12.0 Release 18

[대상 문장]
). 
NOTE 10: For clarity, the NWDAF(s) with roaming exchange capability (RE-NWDAF) and their connections with 
other NFs, are not depicted in the reference point architecture figure. For more information on network 
data analytics architecture refer to TS 23.288 [86]. 
For the roaming scenarios described above each PLMN implements proxy functionality to secure interconnection and 
hide topology on the inter-PLMN interfaces. 
vNRFVPLMN
NF
VPLMN HPLMN
hNRFN27
 
Figure 4.2.4-7: NRF Roaming architecture in reference point representation 
NOTE 11: For the sake of clarity, SEPPs on both sides of PLMN borders are not depicted in figure 4.2.4-7. 
Figure 4.2.4-8: Void 
Operators can deploy UPFs supporting the Inter PLMN UP Security (IPUPS) functionality at the border of their 
network to protect their network from invalid inter PLMN N9 traffic in home routed roaming scenarios. The UPFs 
supporting the IPUPS functionality in VPLMN and HPLMN are c
```

</details>

## V2-P1-051
기준 G042 · 3GPP TS 24.501 V18.12.0 · 4.4.2.2 · PDF 56쪽(인쇄 55쪽)

원문: When the UE operating in single-registration mode in a network supporting N26 interface has a PDN connection for emergency bearer services and has no current EPS security context, the AMF shall set 5G-IA0 and 5G-EA0 as the selected 5G NAS security algorithms in the S1 mode to N1 mode NAS transparent container IE.

질문: N26 지원망의 single-registration mode UE가 emergency bearer PDN connection은 있지만 현재 EPS security context가 없을 때 AMF의 알고리즘 설정을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall",
  "polarity": "positive",
  "actor": "AMF",
  "condition": "when a single-registration-mode UE in a network supporting N26 has an emergency-bearer PDN connection and no current EPS security context",
  "action": "set 5G-IA0 and 5G-EA0 as the selected 5G NAS security algorithms in the S1 mode to N1 mode NAS transparent container IE",
  "exception": "",
  "gold_summary_ko": "그 조건에서 AMF는 해당 IE의 선택된 5G NAS security algorithm을 5G-IA0과 5G-EA0으로 반드시 설정해야 한다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

UE가 N26 인터페이스를 지원하는 망에서 single-registration mode로 동작하고, emergency bearer services용 PDN connection은 있지만 현재 EPS security context가 없는 경우, AMF는 S1 mode to N1 mode NAS transparent container IE에서 5G-IA0와 5G-EA0를 선택된 5G NAS 보안 알고리즘으로 설정해야 한다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
SI with the newly created mapped 5G NAS security context. The AMF shall then include the message 
authentication code, selected NAS algorithms, NCC and generated ngKSI in the S1 mode to N1 mode NAS transparent 
container IE (see subclause 9.11.2.9). 
When the UE operating in single-registration mode in a network supporting N26 interface receives the command to 
perform inter-system change to N1 mode in 5GMM-CONNECTED mode, the UE shall derive a mapped K' AMF, as 
indicated in 3GPP TS 33.501 [24], using the KASME from the EPS security context. Furthermore, the UE shall also 
derive the 5G NAS keys from the mapped K'AMF using the selected NAS algorithm identifiers included in the S1 mode 
to N1 mode NAS transparent container IE and associate this mapped 5G NAS security context with the ngKSI value 
received. The UE shall then verify the received NAS MAC. In case the received NAS MAC is not verified successfully 
(see subclause 4.4.3.3) the UE shall discard the content of the received S1 mode to N1 mode NAS transparent container 
IE and inform the lower layers that the received S1 mode to N1 mode NAS transparent container is invalid. 

[대상 문장]
. The AMF shall create a 
locally generated K'
AMF. The AMF shall set the ngKSI value of the associated security context to "000" and the type of 
security context flag to "mapped security context" in the S1 mode to N1 mode NAS transparent container IE. 
When the UE operating in single-registration mode in a network supporting N26 interface receives the command to 
perform inter-system change to N1 mode in 5GMM-CONNECTED mode (see 3GPP TS 38.331 [30]) and has a PDN 
connection for emergency bearer services, if 5G-IA0 and 5G-EA0 as the selected 5G NAS security algorithms are 
included in the S1 mode to N1 mode NAS transparent container IE, the UE shall create a locally generated K'
AMF. 
Furthermore, the UE shall set the ngKSI value of the associated security context to the KSI value received. 
```

</details>

## V2-P1-052
기준 G009 · 3GPP TS 24.501 V18.12.0 · 4.4.2.1.1 · PDF 54쪽(인쇄 53쪽)

원문: As described in subclause 4.8 in order to interwork with E-UTRAN connected to EPC, the UE supporting both S1 mode and N1 mode can operate in either single-registration mode or dual-registration mode.

질문: S1 mode와 N1 mode를 모두 지원하는 UE의 registration mode 운용 선택지를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "can",
  "polarity": "positive",
  "actor": "UE supporting both S1 mode and N1 mode",
  "condition": "for interworking with E-UTRAN connected to EPC",
  "action": "operate in either single-registration mode or dual-registration mode",
  "exception": "",
  "gold_summary_ko": "해당 UE는 EPC 연결 E-UTRAN과 interwork하기 위해 single-registration mode 또는 dual-registration mode로 동작할 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

S1 mode와 N1 mode를 모두 지원하는 UE는 EPC에 연결된 E-UTRAN과 상호동작하기 위해 단일 등록 모드 또는 이중 등록 모드로 동작할 수 있다. 이는 선택 가능한 운용 옵션을 뜻한다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
e taken into use to establish the secure exchange of 
NAS messages when a new N1 NAS signalling connection is established without executing a new primary 
authentication and key agreement procedure (see subclause 5.4.1) or when the AMF initiates a security mode control 
procedure. For this purpose, the initial NAS messages (i.e. REGISTRATION REQUEST, DEREGISTRATION 
REQUEST, SERVICE REQUEST and CONTROL PLANE SERVICE REQUEST) and the SECURITY MODE 
COMMAND message contain an ngKSI in the ngKSI IE indicating the current 5G NAS security context used to 
integrity protect the NAS message. 
In the present document, when the UE is required to delete an ngKSI, the UE shall set the ngKSI to the value "no key is 
available" and consider also the associated keys K
AMF or K'AMF, 5G NAS ciphering key and 5G NAS integrity key 
invalid (i.e. the 5G NAS security context associated with the ngKSI as no longer valid). In the initial registration 
procedure, when the key K
AUSF, is invalid, the UE shall delete the ngKSI. 
NOTE: In some specifications the term ciphering key sequence number might be used instead of the term key set 
identifier (KSI). 

[대상 문장]
. A UE operating in dual-
registration mode shall independently maintain and use both EPS security context (see 3GPP TS 24.301 [15]) and 5G 
NAS security context. When the UE operating in dual-registration mode performs an EPS attach procedure, it shall take 
into use an EPS security context and follow the handling of this security context as specified in 3GPP TS 24.301 [15]. 
However, when the UE operating in dual-registration mode performs an initial registration procedure, it shall take into 
use a 5G NAS security context and follow the handling of this security context as described in the present specification. 
The UE and the AMF need to be able to maintain two 5G NAS security contexts simultaneously, i.e. a current 5G NAS 
security context and a non-current 5G NAS security context, since: 
a) after a 5G re-authentication, the UE and the AMF can have both a current 5G NAS security context and a non-
current 5G NAS security context 
```

</details>

## V2-P1-053
기준 G039 · 3GPP TS 24.501 V18.12.0 · 4.4.2.1.1 · PDF 54쪽(인쇄 53쪽)

원문: In the initial registration procedure, when the key K AUSF, is invalid, the UE shall delete the ngKSI.

질문: initial registration 중 K_AUSF가 유효하지 않을 때 UE의 ngKSI 처리를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall",
  "polarity": "positive",
  "actor": "UE",
  "condition": "during the initial registration procedure when K_AUSF is invalid",
  "action": "delete the ngKSI",
  "exception": "",
  "gold_summary_ko": "initial registration 중 K_AUSF가 유효하지 않으면 UE는 ngKSI를 반드시 삭제해야 한다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

초기 등록 절차에서 K_AUSF가 유효하지 않을 때 UE는 ngKSI를 반드시 삭제해야 한다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
native 5G NAS security context, 
the ngKSI has the value of KSI
AMF, and when the current 5G NAS security context is of type mapped, the ngKSI has the 
value of KSIASME. 
The 5G NAS security context which is indicated by an ngKSI can be taken into use to establish the secure exchange of 
NAS messages when a new N1 NAS signalling connection is established without executing a new primary 
authentication and key agreement procedure (see subclause 5.4.1) or when the AMF initiates a security mode control 
procedure. For this purpose, the initial NAS messages (i.e. REGISTRATION REQUEST, DEREGISTRATION 
REQUEST, SERVICE REQUEST and CONTROL PLANE SERVICE REQUEST) and the SECURITY MODE 
COMMAND message contain an ngKSI in the ngKSI IE indicating the current 5G NAS security context used to 
integrity protect the NAS message. 
In the present document, when the UE is required to delete an ngKSI, the UE shall set the ngKSI to the value "no key is 
available" and consider also the associated keys K
AMF or K'AMF, 5G NAS ciphering key and 5G NAS integrity key 
invalid (i.e. the 5G NAS security context associated with the ngKSI as no longer valid). 
[대상 문장]
. 
NOTE: In some specifications the term ciphering key sequence number might be used instead of the term key set 
identifier (KSI). 
As described in subclause 4.8 in order to interwork with E-UTRAN connected to EPC, the UE supporting both S1 mode 
and N1 mode can operate in either single-registration mode or dual-registration mode. A UE operating in dual-
registration mode shall independently maintain and use both EPS security context (see 3GPP TS 24.301 [15]) and 5G 
NAS security context. When the UE operating in dual-registration mode performs an EPS attach procedure, it shall take 
into use an EPS security context and follow the handling of this security context as specified in 3GPP TS 24.301 [15]. 
However, when the UE operating in dual-registration mode performs an initial registration procedure, it shall take into 
use a 5G NAS security context and follow the handling of this security context as described in the present specificat
```

</details>

## V2-P1-054
기준 G013 · 3GPP TS 23.501 V18.12.0 · 4.2.8.1 · PDF 57쪽(인쇄 56쪽)

원문: A non-3GPP access network may advertise the PLMNs or SNPNs for which it supports trusted connectivity and the type of supported trusted connectivity (e.g. "5G connectivity").

질문: non-3GPP access network가 trusted connectivity 지원 정보를 광고하는 범위를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "may",
  "polarity": "positive",
  "actor": "non-3GPP access network",
  "condition": "",
  "action": "advertise supported PLMNs or SNPNs and the supported trusted-connectivity type",
  "exception": "only PLMNs or SNPNs for which trusted connectivity is supported",
  "gold_summary_ko": "non-3GPP access network는 trusted connectivity를 지원하는 PLMN 또는 SNPN과 그 connectivity 유형을 광고할 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

non-3GPP access network는 trusted connectivity를 지원하는 PLMN 또는 SNPN과, 지원되는 trusted connectivity의 유형을 광고하도록 허용된다. 이 광고 범위는 trusted connectivity가 지원되는 PLMN 또는 SNPN에 한정된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
n-3GPP access networks are defined: 
- Untrusted non-3GPP access networks; 
- Trusted non-3GPP access networks; and 
- Wireline access networks. 
The architecture to support Untrusted and Trusted non-3GPP access networks is defined in clause 4.2.8.2. The 
architecture to support Wireline access networks is defined in clause 4.2.8.2.4 and in TS 23.316 [84]. 
4.2.8.1 General Concepts to Support Trusted and Untrusted Non-3GPP Access 
The 5G Core Network supports connectivity of UEs via non-3GPP access networks, e.g. WLAN access networks. 
Only the support of non-3GPP access networks deployed outside the NG-RAN is described in this clause. 
The 5G Core Network supports both untrusted non-3GPP access networks and trusted non-3GPP access networks 
(TNANs). 
An untrusted non-3GPP access network shall be connected to the 5G Core Network via a Non-3GPP InterWorking 
Function (N3IWF), whereas a trusted non-3GPP access network shall be connected to the 5G Core Network via a 
Trusted Non-3GPP Gateway Function (TNGF). Both the N3IWF and the TNGF interface with the 5G Core Network 
CP and UP functions via the N2 and N3 interfaces, respectively. 

[대상 문장]
"). Therefore, the UEs can discover the non-3GPP access 
networks that can provide trusted connectivity to one or more PLMNs or SNPNs. This is further specified in 
clause 6.3.12 (Trusted Non-3GPP Access Network selection). 
The UE decides to use trusted or untrusted non-3GPP access for connecting to a 5G PLMN or SNPNs by using 
procedures not specified in this document. Examples of such procedures are defined in clause 6.3.12.1. 
When the UE decides to use untrusted non-3GPP access to connect to a 5G Core Network in a PLMN: 
- the UE first selects and connects with a non-3GPP access network; and then 
```

</details>

## V2-P1-055
기준 G032 · 3GPP TS 24.501 V18.12.0 · 5.3.6 · PDF 193쪽(인쇄 192쪽)

원문: If the AMF indicates active time value to the UE, AMF should not indicate "all PLMN registration area allocated" indication in the MICO indication IE to the UE.

질문: AMF가 UE에 active time value를 알릴 때 MICO indication IE의 all-PLMN 표시에 관한 정책을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should_not",
  "polarity": "negative",
  "actor": "AMF",
  "condition": "if the AMF indicates an active-time value to the UE",
  "action": "indicate 'all PLMN registration area allocated' in the MICO indication IE",
  "exception": "",
  "gold_summary_ko": "그 경우 AMF는 MICO indication IE에 'all PLMN registration area allocated'를 표시하지 않는 것이 권고된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

AMF가 UE에 active time value를 알릴 때, AMF는 MICO indication IE에서 UE에 "all PLMN registration area allocated" 표시를 하지 않는 것이 권고된다. 이는 금지라기보다 하지 않는 것이 권고되는 경우이다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 124 501 V18.12.0 (2025-10)1923GPP TS 24.501 version 18.12.0 Release 18
If the UE requested the use of active time by including an active time value and the network accepts the use of MICO 
mode and the use of active time, the AMF shall include an active time value in the T3324 IE to the UE. 
[대상 문장]
. Upon entering 5GMM-IDLE mode, AMF shall start the active timer with the active time 
value indicated to the UE and shall consider the UE is reachable for paging as long as the timer is running. If the UE 
enters 5GMM-CONNECTED mode over 3GPP access when the active timer is running, the AMF shall stop the active 
timer. 
NOTE 1: The active time value assigned by AMF can be different from the active time value requested by the UE. 
AMF assigns the active time value based on several factors, e.g. local configuration, expected UE 
behaviour, UE requested active time value, UE subscription information, network policies etc. 
If the UE requested an active time and a requested T3512 value and the network accepts the use of MICO mode, the 
AMF shall take the UE requested T3512 value into consideration when assigning a value of timer T3512 to the UE. 
If the network accepts the use of MICO mode, the UE may deactivate the AS layer and activate 
```

</details>

## V2-P1-056
기준 G003 · 3GPP TS 23.501 V18.12.0 · 4.4.8.4 · PDF 93쪽(인쇄 92쪽)

원문: A special case where the 5GS can act as a sub-network is when the 5GS acts as a TSN network, which is supported by the 3GPP specifications based on the architecture in clause 4.4.8.2.

질문: 5GS가 TSN network로 동작할 때의 sub-network 역할을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "can",
  "polarity": "positive",
  "actor": "5GS",
  "condition": "when the 5GS acts as a TSN network",
  "action": "act as a sub-network",
  "exception": "this is a special case based on the referenced TSN architecture",
  "gold_summary_ko": "5GS가 TSN network로 동작하는 특수한 경우에는 sub-network로 동작할 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

5GS가 TSN network로 동작할 때는 TSN 서브네트워크의 일부로서 동작하며, TSN 도메인과 5GS 사이의 트래픽 전달과 시간 동기 지원을 담당한다. 즉, 5GS는 TSN 장치와 외부 TSN 네트워크 사이에서 TSN 서비스가 유지되도록 연결 역할을 수행한다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
Release 18
UE (R)AN
UPF
SMFAMF PCF
TSCTSF CPF: DetNet
controller
DetNet network
5GS logical DetNet Router
DetNet 
system
NW-TT
N1
N3
N11
N2 N4
N7
N84
UDM
N8 N10
N9
U-plane
 
Figure 4.4.8.4-1: 5GS Architecture to support IETF Deterministic Networking 
On the device side, the UE is connected with a DetNet system, which may be a DetNet End System or a DetNet Node. 
The architecture does not require the DS-TT functionality to be supported in the device nor require the user plane NW-
TT functionality to be supported in the UPF, however, it can co-exist with such functions. For the reporting of 
information of the network side ports, NW-TT control plane function is used. The architecture can be combined with 
architecture in clause 4.4.8.3 to support time synchronization and TSC. 
DetNet may be used in combination with time synchronization mechanisms as defined in clause 5.27, but it does not 
require usage of these mechanisms. 
5GS acts as a DetNet router in the DetNet domain. Use cases where the 5GS acts as a sub-network (see clause 4.1.2 of 
IETF RFC 8655 [150]) are also possible but do not require any additional 3GPP standardization. 
[대상 문장]
. 
NOTE: For DetNet interworking, it is assumed that there is a business agreement to support the use of the DetNet 
controller so that it can be regarded trusted for the operator. Depending on the needs of a given 
deployment, functions such as the authentication, authorization and potential throttling of signalling from 
the DetNet controller can be achieved by including such functionalities in the TSCTSF. 
The routing of the downlink packets is achieved using the existing 3GPP functions. 
5 High level features 
5.1 General 
Clause 5 specifies the high level functionality and features of the 5G System for both 3GPP and Non-3GPP access and 
for the interoperability with the EPC defined in TS 23.401 [26]. 
```

</details>

## V2-P1-057
기준 G011 · 3GPP TS 23.501 V18.12.0 · 4.2.8.5.1 · PDF 67쪽(인쇄 66쪽)

원문: When a N5CW device performs an EAP-based access authentication procedure to connect to a trusted WLAN access network, the N5CW device may simultaneously be registered to a 5GC of a PLMN or SNPN.

질문: N5CW device가 trusted WLAN 연결을 위해 EAP 기반 access authentication을 수행할 때 5GC 등록 상태를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "may",
  "polarity": "positive",
  "actor": "N5CW device",
  "condition": "when performing EAP-based access authentication to connect to a trusted WLAN access network",
  "action": "simultaneously be registered to a 5GC of a PLMN or SNPN",
  "exception": "",
  "gold_summary_ko": "그 과정에서 N5CW device는 PLMN 또는 SNPN의 5GC에 동시에 등록되어 있을 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

N5CW device가 trusted WLAN access network에 연결하기 위해 EAP 기반 access authentication 절차를 수행할 때, 그 N5CW device는 PLMN 또는 SNPN의 5GC에 동시에 등록되어 있을 수 있다. 이는 허용 또는 가능한 상태를 나타내며, 반드시 그렇게 되어야 한다는 의미는 아니다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
are the same as 
defined in clause 4.2. 
NOTE 6: The reference architecture in figure 4.2.8.4-1 supports service based interfaces for AMF, SMF and other 
NFs not represented in the figure. 
4.2.8.5 Access to 5GC from devices that do not support 5GC NAS over WLAN 
access 
4.2.8.5.1 General 
The devices that do not support 5GC NAS signalling over WLAN access are referred to as "Non-5G-Capable over 
WLAN" devices, or N5CW devices for short. A N5CW device is not capable to operate as a 5G UE that supports 5GC 
NAS signalling over a WLAN access network, however, it may be capable to operate as a 5G UE over NG-RAN. 
Clause 4.2.8.5 specifies the 5GC architectural enhancements that enable N5CW devices to access 5GC via trusted 
WLAN access networks. A trusted WLAN access network is a particular type of a Trusted Non-3GPP Access Network 
(TNAN) that supports a WLAN access technology, e.g. IEEE 802.11. Not all trusted WLAN access networks support 
5GC access from N5CW devices. To support 5GC access from N5CW devices, a trusted WLAN access network must 
support the special functionality specified below (e.g. it must support a TWIF function). 

[대상 문장]
. The 5GC registration is 
performed by the TWIF function (see next clause) in the trusted WLAN access network, on behalf of the N5CW device. 
The type of EAP authentication procedure, which is used during the 5GC registration to authenticate the N5CW device, 
is specified in TS 33.501 [29]. In this Release of the specification, Trusted WLAN Access for N5CW Device only 
supports IP PDU Session type. 
```

</details>

## V2-P1-058
기준 G047 · 3GPP TS 23.501 V18.12.0 · 5.4.1.3 · PDF 116쪽(인쇄 115쪽)

원문: If the UE does not indicate preference for MICO mode during Registration procedure, the AMF shall not activate MICO mode for this UE.

질문: registration 중 UE가 MICO mode 선호를 표시하지 않았을 때 AMF의 MICO mode 처리를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall_not",
  "polarity": "negative",
  "actor": "AMF",
  "condition": "if the UE does not indicate a preference for MICO mode during registration",
  "action": "activate MICO mode for that UE",
  "exception": "",
  "gold_summary_ko": "UE가 MICO mode 선호를 표시하지 않으면 AMF는 그 UE에 MICO mode를 활성화해서는 안 된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

UE가 Registration 절차 동안 MICO mode 선호를 표시하지 않으면, AMF는 이 UE에 대해 MICO mode를 활성화해서는 안 된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
he UE. 
As part of deregistration for a particular access (3GPP or non-3GPP), the AMF shall request the UE's related SMF to 
release the PDU Sessions established on that access. 
5.4.1.2 UE reachability allowing mobile terminated data while the UE is CM-IDLE 
The AMF considers a UE in RM-REGISTERED state to be reachable by CN paging if the UE CM state in the AMF is 
CM-IDLE state unless the UE applies MICO mode or the UE has indicated Unavailability Period Duration. 
5.4.1.3 Mobile Initiated Connection Only (MICO) mode 
A UE may indicate preference for MICO mode during Initial Registration or Mobility Registration Update procedure. 
The AMF, based on local configuration, Expected UE Behaviour and/or Network Configuration parameters if available 
from the UDM, UE indicated preferences, UE subscription information and network policies, or any combination of 
them, determines whether MICO mode is allowed for the UE and indicates it to the UE during Registration procedure. 
If NWDAF is deployed, the AMF may also use analytics on UE mobility and/or UE communication generated by 
NWDAF (see TS 23.288 [86]) to decide MICO mode parameters. 
[대상 문장]
. 
The UE and the AMF re- negotiate the MICO mode at every subsequent Registration procedure. When the UE is in 
CM-CONNECTED, the AMF may deactivate MICO mode by triggering Mobility Registration Update procedure 
through UE Configuration Update procedure as described in clause 4.2.4 of TS 23.502 [3]. 
The AMF assigns a registration area to the UE during the Registration procedure. When the AMF indicates MICO 
mode to a UE, the registration area is not constrained by paging area size. If the AMF serving area is the whole PLMN, 
based on local policy and subscription information, may decide to provide an "all PLMN" registration area to the UE. In 
that case, re-registration to the same PLMN due to mobility does not apply. 
If Mobility Restrictions are applied to a UE in MICO mode, the AMF needs to allocate an Allowed Area/Non-Allowed 
Area to the UE as specified in clause 5.3.4.1. 
When the AMF indicates MICO mode to a UE, the AMF consid
```

</details>

## V2-P1-059
기준 G005 · 3GPP TS 24.501 V18.12.0 · 4.4.2.1.1 · PDF 53쪽(인쇄 52쪽)

원문: Before security can be activated, the AMF and the UE need to establish a 5G NAS security context.

질문: 5G NAS security를 활성화하기 전에 AMF와 UE가 충족해야 하는 전제조건을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "can",
  "polarity": "positive",
  "actor": "security",
  "condition": "after the AMF and UE establish a 5G NAS security context",
  "action": "be activated",
  "exception": "security cannot be activated before that context is established",
  "gold_summary_ko": "AMF와 UE가 5G NAS security context를 먼저 설정해야 하며, 그 전에는 security를 활성화할 수 없다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

5G NAS 보안을 활성화하기 전에 AMF와 UE는 서로에 대해 NAS 보안 절차를 수행할 수 있는 상태여야 하며, 보안에 사용할 공통의 보안 컨텍스트와 관련 키 자료가 준비되어 있어야 한다. 또한 해당 보안 컨텍스트는 유효해야 하고, 양측이 같은 보안 알고리즘과 절차를 적용할 수 있어야 한다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
ection of NAS IEs between the UE and the UDM. Security protection involves integrity protection and 
ciphering of the 5GMM messages. 5GSM messages are security protected indirectly by being piggybacked by the 
security protected 5GMM messages (i.e. UL NAS TRANSPORT message and the DL NAS TRANSPORT message). 
The signalling procedures for the control of NAS security are part of the 5GMM protocol and are described in detail in 
clause 5. 
NOTE: The use of ciphering in a network is an operator optio n. In this subclause, for the ease of description, it is 
assumed that ciphering is used, unless explicitly indicated otherwise. Operation of a network without 
ciphering is achieved by configuring the AMF so that it always selects the "null ciphering algorithm", 5G-
EA0. 
4.4.2 Handling of 5G NAS security contexts 
4.4.2.1 General 
4.4.2.1.1 Establishment of 5G NAS security context 
The security parameters for authentication, integrity protection and ciphering are tied together in a 5G NAS security 
context and identified by a key set identifier (ngKSI). The relationship between the security parameters is defined in 
3GPP TS 33.501 [24]. 

[대상 문장]
. Usually, the 5G 
NAS security context is created as the result of a primary authentication and key agreement procedure between the 
AMF and the UE. A new 5G NAS security context may also be created during an N1 mode to N1 mode handover. 
Alternatively, during inter-system change from S1 mode to N1 mode, the AMF not supporting interworking without 
```

</details>

## V2-P1-060
기준 G001 · 3GPP TS 23.501 V18.12.0 · 4.2.4 · PDF 50쪽(인쇄 49쪽)

원문: The N38 references point can be between V-SMFs in the same VPLMN, or between V-SMFs in different VPLMNs (to enable inter-PLMN mobility).

질문: V-SMF 사이 N38 reference point의 VPLMN 배치 관계를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "can",
  "polarity": "positive",
  "actor": "N38 reference point",
  "condition": "",
  "action": "exist between V-SMFs in the same VPLMN or in different VPLMNs",
  "exception": "the inter-VPLMN case enables inter-PLMN mobility",
  "gold_summary_ko": "N38 reference point는 같은 VPLMN의 V-SMF 사이 또는 서로 다른 VPLMN의 V-SMF 사이에 존재할 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

N38 reference point는 같은 VPLMN에 있는 V-SMF들 사이에 있을 수 있고, 서로 다른 VPLMN에 있는 V-SMF들 사이에도 있을 수 있다. 후자의 경우는 inter-PLMN mobility를 가능하게 하기 위한 것이다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 123 501 V18.12.0 (2026-01)493GPP TS 23.501 version 18.12.0 Release 18

[대상 문장]
). 
NOTE 10: For clarity, the NWDAF(s) with roaming exchange capability (RE-NWDAF) and their connections with 
other NFs, are not depicted in the reference point architecture figure. For more information on network 
data analytics architecture refer to TS 23.288 [86]. 
For the roaming scenarios described above each PLMN implements proxy functionality to secure interconnection and 
hide topology on the inter-PLMN interfaces. 
vNRFVPLMN
NF
VPLMN HPLMN
hNRFN27
 
Figure 4.2.4-7: NRF Roaming architecture in reference point representation 
NOTE 11: For the sake of clarity, SEPPs on both sides of PLMN borders are not depicted in figure 4.2.4-7. 
Figure 4.2.4-8: Void 
Operators can deploy UPFs supporting the Inter PLMN UP Security (IPUPS) functionality at the border of their 
network to protect their network from invalid inter PLMN N9 traffic in home routed roaming scenarios. The UPFs 
supporting the IPUPS functionality in VPLMN and HPLMN are c
```

</details>

## V2-P1-061
기준 G026 · 3GPP TS 24.501 V18.12.0 · 5.3.26 · PDF 222쪽(인쇄 221쪽)

원문: The AMF should set the value of the mobile reachable timer and implicit deregistration timer based on the unavailability period duration and the start of the unavailability period.

질문: AMF가 unavailability period 정보를 이용해 mobile reachable timer와 implicit deregistration timer를 설정하는 방식을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should",
  "polarity": "positive",
  "actor": "AMF",
  "condition": "based on the unavailability-period duration and its start",
  "action": "set the mobile reachable timer and implicit deregistration timer values",
  "exception": "",
  "gold_summary_ko": "AMF는 unavailability period의 duration과 시작 시점을 바탕으로 두 timer 값을 설정하는 것이 권고된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

AMF는 unavailability period의 지속 시간과 시작 시점을 바탕으로 mobile reachable timer와 implicit deregistration timer의 값을 설정하는 것이 권고된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
ermine the unavailability period duration of the UE as described 
in subclause 5.5.1.2.4 and 5.5.1.3.4. The AMF may also consider the start of the unavailability period provided by the 
UE, if available, and determine the start of the unavailability period of the UE as described in subclause 5.5.1.3.4. 
If the UE provided unavailability information in the last registration procedure for mobility registration or the de-
registration procedure, the AMF considers the UE unreachable until the UE registers for a normal service. If the UE did 
not include a start of the unavailability period, the AMF shall consider the start of the unavailability period to be the 
time at which AMF received the REGISTRATION REQUEST message or the DEREGISTRATION REQUEST 
message from the UE. During the registration procedure, the AMF may determine the values of the negotiated extended 
DRX parameters, the timer T3324, and the periodic registration update timer (T3512) to be provided to the UE based on 
the discontinuous coverage maximum time offset, the unavailability period duration and the start of the unavailability 
period based on their availability. 
[대상 문장]
. The AMF 
releases the N1 signalling connection after the completion of the registration procedure in which the UE provided 
unavailability information without providing the start of the unavailability period. 
NOTE 2:  If the UE supports MUSIM and the UE is registered with the support of unavailability period, then the UE 
can indicate a different unavailability periods to each registered network. 
If for discontinuous coverage the UE has stored a discontinuous coverage maximum time offset as described in 
subclause 5.4.4.3, 5.5.1.2.4, and 5.5.1.3.4, the UE shall set the discontinuous coverage maximum time offset value to a 
random value up to and including the stored discontinuous coverage maximum time offset for this PLMN and satellite 
NG-RAN RAT Type, determine a time point equal to the time when the UE is about to lose satellite coverage minus the 
discontinuous coverage maximum time offset value, and send the REGISTRATION REQUES
```

</details>

## V2-P1-062
기준 G022 · 3GPP TS 23.501 V18.12.0 · 5.2.5 · PDF 95쪽(인쇄 94쪽)

원문: If the NG-RAN node takes a decision to initiate UAC because of the reception of the N2 interface OVERLOAD START messages, the NG-RAN should only initiate such procedure if all the AMFs relevant to the request contained in the OVERLOAD START message and connected to this NG-RAN node request to restrict the load for UEs that access the network.

질문: N2 OVERLOAD START 수신으로 UAC를 시작하려는 NG-RAN node가 확인할 AMF 조건을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should",
  "polarity": "positive",
  "actor": "NG-RAN node",
  "condition": "if it decides to initiate UAC after receiving N2 OVERLOAD START messages",
  "action": "initiate UAC",
  "exception": "only if all relevant connected AMFs named by the request ask to restrict load for accessing UEs",
  "gold_summary_ko": "NG-RAN node는 요청과 관련된 모든 연결 AMF가 UE load 제한을 요구할 때에만 UAC를 시작하는 것이 권고된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

NG-RAN 노드는 N2 OVERLOAD START를 수신해 UAC를 시작하려는 경우, 해당 AMF가 이 절차를 지원하고 현재 N2 과부하 상태를 관리할 수 있는 대상인지 확인해야 한다. 또한 UAC를 시작할 수 있는 조건이 충족되지 않으면 그 AMF에 대해 UAC를 시작해서는 안 된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 123 501 V18.12.0 (2026-01)943GPP TS 23.501 version 18.12.0 Release 18
- AMFs request to restrict the load for UEs that access the network by sending OVERLOAD START message 
containing conditions defined in clause 5.19.5.2, or 
- requested by OAM, or 
- triggered by NG-RAN itself. 

[대상 문장]
. 
If the UE supports both N1 and S1 modes NAS and, as defined in TS 23.401 [26], the UE is configured for Extended 
Access Barring (EAB) but is not configured with a permission for overriding Extended Access Barring (EAB), when 
the UE wants to access the 5GS it shall perform Unified Access Control checks for Access Category 1 on receiving an 
indication from the upper layers as defined in TS 24.501 [47], TS 38.331 [28], TS 36.331 [51]. 
If the UE supports both N1 and S1 modes NAS and, as defined in TS 23.401 [26], the UE is configured with a 
permission for overriding Extended Access Barring (EAB), when the UE wants to access the 5GS it shall ignore 
Unified Access Control checks for Access Category 1 on receiving an indication from the upper layers, as defined in 
TS 24.501 [47]. 
NOTE: UE signalling of Low Access Priority indication over N1 in 5GS is not supported in this release of the 
specification. 
Operator may provide one or m
```

</details>

## V2-P1-063
기준 G049 · 3GPP TS 24.501 V18.12.0 · 4.4.2.3 · PDF 57쪽(인쇄 56쪽)

원문: When a new 5G NAS security context is derived using the same K AMF, the target AMF includes the 8 least significant bits of the downlink NAS COUNT in the Intra N1 mode NAS transparent container IE, and indicates that a new KAMF shall not be derived (see subclause 9.11.2.6).

질문: 동일한 K_AMF로 새 5G NAS security context를 유도할 때 target AMF가 새 K_AMF 유도 여부를 어떻게 표시하는지 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall_not",
  "polarity": "negative",
  "actor": "new K_AMF",
  "condition": "when a new 5G NAS security context is derived using the same K_AMF",
  "action": "be derived",
  "exception": "the target AMF indicates this in the Intra N1 mode NAS transparent container IE",
  "gold_summary_ko": "그 경우 새로운 K_AMF는 유도되어서는 안 되며, target AMF는 그 사실을 container IE에 표시한다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

동일한 K_AMF로 새 5G NAS security context를 유도하는 경우, target AMF는 새 K_AMF를 유도했는지 여부를 표시해야 한다. 이 표시는 이후 보안 컨텍스트 처리에서 새로 유도된 K_AMF를 사용할지 판단할 수 있게 한다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
ontext active on the 3GPP access for the non-3GPP access as described in 
3GPP TS 33.501 [24] after the AMF sends or the UE receives the REGISTRATION ACCEPT message 
respectively; or 
2) the UE is in 5GMM-CONNECTED mode over non-3GPP access, in order to activate the same mapped 5G 
NAS security context over one access that is used on the other access the AMF shall send the SECURITY 
MODE COMMAND message over one-access as described in 3GPP TS 33.501 [24]. The SECURITY 
MODE COMMAND message shall include the same ngKSI to identify the mapped 5G NAS security context 
that is used over the other access. 
If the inter-system change from S1 mode to N1 mode in 5GMM-CONNECTED mode is not completed successfully, 
the AMF and the UE operating in single-registration mode in a network supporting N26 interface shall delete the new 
mapped 5G NAS security context. 
4.4.2.3 Establishment of a 5G NAS security context during N1 mode to N1 mode 
handover 
During an N1 mode to N1 mode handover, the target AMF may derive a new 5G NAS security context for which the 
target AMF creates a new 5G NAS security context as indicated in 3GPP TS 33.501 [24]. 

[대상 문장]
). The AMF shall increment the downlink NAS COUNT by one after 
creating the Intra N1 mode NAS transparent container IE. 
When a new 5G NAS security context is created from a new K
AMF, the target AMF includes the 8 least significant bits 
of the downlink NAS COUNT in the Intra N1 mode NAS transparent container IE and indicates that a new K AMF shall 
be derived (see subclause 9.11.2.6). The AMF shall then set both the uplink and downlink NAS COUNT counters of 
this 5G NAS security context to zero. The AMF shall increment the downlink NAS COUNT by one after creating the 
Intra N1 mode NAS transparent container IE. 
The target AMF also includes the ngKSI with the same value as the ngKSI currently being used with the UE, the 
message authentication code, and the selected NAS algorithms in the Intra N1 mode NAS transparent container IE. 
When the UE receives a command to perform handover to NG-RAN including an Intra N1 mode NAS transparent
```

</details>

## V2-P1-064
기준 G008 · 3GPP TS 24.501 V18.12.0 · 4.4.2.1.1 · PDF 54쪽(인쇄 53쪽)

원문: The 5G NAS security context which is indicated by an ngKSI can be taken into use to establish the secure exchange of NAS messages when a new N1 NAS signalling connection is established without executing a new primary authentication and key agreement procedure (see subclause 5.4.1) or when the AMF initiates a security mode control procedure.

질문: ngKSI가 가리키는 5G NAS security context를 새 인증 없이 사용하는 상황을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "can",
  "polarity": "positive",
  "actor": "5G NAS security context indicated by an ngKSI",
  "condition": "when a new N1 NAS signalling connection is established without new primary authentication and key agreement, or when the AMF initiates security mode control",
  "action": "be taken into use to establish secure NAS-message exchange",
  "exception": "",
  "gold_summary_ko": "새 N1 NAS signalling connection을 새 primary authentication 없이 설정하거나 AMF가 security mode control을 시작할 때, 해당 context를 secure NAS exchange 설정에 사용할 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

ngKSI가 가리키는 5G NAS security context는 새 N1 NAS signalling connection이 새 primary authentication and key agreement 절차를 수행하지 않고 설정될 때, 또는 AMF가 security mode control 절차를 시작할 때 NAS 메시지의 안전한 교환을 확립하는 데 사용될 수 있다. 이는 허용을 나타내며, 반드시 사용해야 한다는 뜻은 아니다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
e UE was in S1 mode. 
The 5G NAS security context is taken into use by the UE and the AMF, when the AMF initiates a security mode control 
procedure, during an N1 mode to N1 mode handover, or during the inter-system change procedure from S1 mode to N1 
mode. The 5G NAS security context which has been taken into use by the network most recently is called current 5G 
NAS security context. This current 5G NAS security context can be of type native or mapped, i.e. originating from a 
native 5G NAS security context or mapped 5G NAS security context. 
The key set identifier ngKSI is assigned by the AMF either during the primary authentication and key agreement 
procedure or, for the mapped 5G NAS security context, during the inter-system change. The ngKSI consists of a value 
and a type of security context parameter indicating whether a 5G NAS security context is a native 5G NAS security 
context or a mapped 5G NAS security context. When the 5G NAS security context is a native 5G NAS security context, 
the ngKSI has the value of KSI
AMF, and when the current 5G NAS security context is of type mapped, the ngKSI has the 
value of KSIASME. 

[대상 문장]
. For this purpose, the initial NAS messages (i.e. REGISTRATION REQUEST, DEREGISTRATION 
REQUEST, SERVICE REQUEST and CONTROL PLANE SERVICE REQUEST) and the SECURITY MODE 
COMMAND message contain an ngKSI in the ngKSI IE indicating the current 5G NAS security context used to 
integrity protect the NAS message. 
In the present document, when the UE is required to delete an ngKSI, the UE shall set the ngKSI to the value "no key is 
available" and consider also the associated keys K
AMF or K'AMF, 5G NAS ciphering key and 5G NAS integrity key 
invalid (i.e. the 5G NAS security context associated with the ngKSI as no longer valid). In the initial registration 
procedure, when the key K
AUSF, is invalid, the UE shall delete the ngKSI. 
NOTE: In some specifications the term ciphering key sequence number might be used instead of the term key set 
identifier (KSI). 
As described in subclause 4.8 in order to interwork with E-UTRAN connected to EP
```

</details>

## V2-P1-065
기준 G031 · 3GPP TS 23.501 V18.12.0 · 5.31.7.4 · PDF 436쪽(인쇄 435쪽)

원문: To avoid paging in the entire PLMN, when the AMF allocates the Active Time the AMF should not allocate "all PLMN" registration area to the UE.

질문: 전체 PLMN paging을 피하기 위해 AMF가 Active Time을 할당할 때 registration area를 정하는 정책을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should_not",
  "polarity": "negative",
  "actor": "AMF",
  "condition": "when allocating Active Time, to avoid paging across the entire PLMN",
  "action": "allocate an 'all PLMN' registration area to the UE",
  "exception": "",
  "gold_summary_ko": "AMF는 Active Time 할당 시 UE에 'all PLMN' registration area를 할당하지 않는 것이 권고된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

전체 PLMN에서 paging이 발생하는 것을 피하기 위해, AMF가 Active Time을 할당할 때 UE에 "all PLMN" registration area를 할당하지 않는 것이 권고된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
ter-RAN node handovers, if some signalling or data are still pending, the target AMF may send the Extended 
Connected Time value to the target RAN node. 
5.31.7.4 MICO mode with Active Time 
During a Registration procedure the UE may optionally request an Active Time value from the AMF as part of MICO 
Mode negotiation. In response, if the AMF receives an Active Time value from the UE and determines that the MICO 
mode is allowed for the UE, the AMF may assign an Active Time value for the UE, e.g. based on local configuration, 
Expected UE Behaviour if available, UE requested Active Time value, UE subscription information and network 
policies and indicates it to the UE during Registration procedure. When an Active Time value is assigned to the UE the 
AMF shall consider the UE reachable for paging after the transition from CM-CONNECTED to CM-IDLE for the 
duration of the Active Time. Together with the Active Time value, the UE may request a periodic registration time 
value as specified in clause 5.31.7.45. 
When the AMF indicates MICO mode with an Active Time to a UE, the registration area may be constrained by paging 
area size. 
[대상 문장]
. 
The UE and AMF shall set a timer corresponding to the Active Time value negotiated during the most recent 
Registration procedure. The UE and AMF shall start the timer upon entering CM-IDLE state from CM-CONNECTED. 
When the timer expires (i.e. reaches the Active Time) the UE enters MICO mode and the AMF can deduce that the UE 
has entered MICO mode and is not available for paging. If the UE enters CM-CONNECTED state before the timer 
expires, the UE and AMF shall stop and reset the timer. 
If no Active Time value was negotiated during the most recent Registration procedure the UE shall not start the timer 
and it shall instead enter MICO mode directly upon entering CM-IDLE state. 
Active Time is not transferred between AMF and MME. 
5.31.7.5 MICO mode and Periodic Registration Timer Control 
If the Expected UE Behaviour indicates the absence of DL communication, the AMF may allow MICO mode for the 
UE and allocate a large periodic r
```

</details>

## V2-P1-066
기준 G041 · 3GPP TS 24.501 V18.12.0 · 4.4.2.1.1 · PDF 54쪽(인쇄 53쪽)

원문: In the present document, when the UE is required to delete an ngKSI, the UE shall set the ngKSI to the value "no key is available" and consider also the associated keys K AMF or K'AMF, 5G NAS ciphering key and 5G NAS integrity key invalid (i.e. the 5G NAS security context associated with the ngKSI as no longer valid).

질문: UE의 ngKSI 삭제 상황에서 ngKSI와 연관 키를 어떻게 처리하는지 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall",
  "polarity": "positive",
  "actor": "UE",
  "condition": "when the UE is required to delete an ngKSI",
  "action": "set the ngKSI to 'no key is available' and consider the associated K_AMF or K'_AMF, NAS ciphering key, and NAS integrity key invalid",
  "exception": "",
  "gold_summary_ko": "UE는 ngKSI를 'no key is available'로 반드시 설정하고 연관된 K_AMF 또는 K'_AMF와 NAS 암호화·무결성 키를 무효로 간주해야 한다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

UE가 ngKSI를 삭제해야 하는 경우, UE는 ngKSI를 "no key is available" 값으로 설정해야 하며, 연관된 키 K AMF 또는 K'AMF, 5G NAS ciphering key, 5G NAS integrity key도 무효로 간주해야 한다. 즉, ngKSI와 그에 연결된 5G NAS 보안 컨텍스트는 더 이상 유효하지 않은 것으로 처리해야 한다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
ement 
procedure or, for the mapped 5G NAS security context, during the inter-system change. The ngKSI consists of a value 
and a type of security context parameter indicating whether a 5G NAS security context is a native 5G NAS security 
context or a mapped 5G NAS security context. When the 5G NAS security context is a native 5G NAS security context, 
the ngKSI has the value of KSI
AMF, and when the current 5G NAS security context is of type mapped, the ngKSI has the 
value of KSIASME. 
The 5G NAS security context which is indicated by an ngKSI can be taken into use to establish the secure exchange of 
NAS messages when a new N1 NAS signalling connection is established without executing a new primary 
authentication and key agreement procedure (see subclause 5.4.1) or when the AMF initiates a security mode control 
procedure. For this purpose, the initial NAS messages (i.e. REGISTRATION REQUEST, DEREGISTRATION 
REQUEST, SERVICE REQUEST and CONTROL PLANE SERVICE REQUEST) and the SECURITY MODE 
COMMAND message contain an ngKSI in the ngKSI IE indicating the current 5G NAS security context used to 
integrity protect the NAS message. 

[대상 문장]
). In the initial registration 
procedure, when the key K
AUSF, is invalid, the UE shall delete the ngKSI. 
NOTE: In some specifications the term ciphering key sequence number might be used instead of the term key set 
identifier (KSI). 
As described in subclause 4.8 in order to interwork with E-UTRAN connected to EPC, the UE supporting both S1 mode 
and N1 mode can operate in either single-registration mode or dual-registration mode. A UE operating in dual-
registration mode shall independently maintain and use both EPS security context (see 3GPP TS 24.301 [15]) and 5G 
NAS security context. When the UE operating in dual-registration mode performs an EPS attach procedure, it shall take 
into use an EPS security context and follow the handling of this security context as specified in 3GPP TS 24.301 [15]. 
However, when the UE operating in dual-registration mode performs an initial registration procedure, it shall take into 
use a 5G NAS
```

</details>

## V2-P1-067
기준 G005 · 3GPP TS 24.501 V18.12.0 · 4.4.2.1.1 · PDF 53쪽(인쇄 52쪽)

원문: Before security can be activated, the AMF and the UE need to establish a 5G NAS security context.

질문: 5G NAS security를 활성화하기 전에 AMF와 UE가 충족해야 하는 전제조건을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "can",
  "polarity": "positive",
  "actor": "security",
  "condition": "after the AMF and UE establish a 5G NAS security context",
  "action": "be activated",
  "exception": "security cannot be activated before that context is established",
  "gold_summary_ko": "AMF와 UE가 5G NAS security context를 먼저 설정해야 하며, 그 전에는 security를 활성화할 수 없다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

5G NAS security를 활성화하기 전에 AMF와 UE는 5G NAS security context를 수립해야 한다. 이는 보안이 활성화되기 위한 전제조건이다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
ection of NAS IEs between the UE and the UDM. Security protection involves integrity protection and 
ciphering of the 5GMM messages. 5GSM messages are security protected indirectly by being piggybacked by the 
security protected 5GMM messages (i.e. UL NAS TRANSPORT message and the DL NAS TRANSPORT message). 
The signalling procedures for the control of NAS security are part of the 5GMM protocol and are described in detail in 
clause 5. 
NOTE: The use of ciphering in a network is an operator optio n. In this subclause, for the ease of description, it is 
assumed that ciphering is used, unless explicitly indicated otherwise. Operation of a network without 
ciphering is achieved by configuring the AMF so that it always selects the "null ciphering algorithm", 5G-
EA0. 
4.4.2 Handling of 5G NAS security contexts 
4.4.2.1 General 
4.4.2.1.1 Establishment of 5G NAS security context 
The security parameters for authentication, integrity protection and ciphering are tied together in a 5G NAS security 
context and identified by a key set identifier (ngKSI). The relationship between the security parameters is defined in 
3GPP TS 33.501 [24]. 

[대상 문장]
. Usually, the 5G 
NAS security context is created as the result of a primary authentication and key agreement procedure between the 
AMF and the UE. A new 5G NAS security context may also be created during an N1 mode to N1 mode handover. 
Alternatively, during inter-system change from S1 mode to N1 mode, the AMF not supporting interworking without 
```

</details>

## V2-P1-068
기준 G051 · 3GPP TS 24.501 V18.12.0 · 4.6.1 · PDF 95쪽(인쇄 94쪽)

원문: If the UE is registering or registered for onboarding services in SNPN, the serving SNPN shall not provide a configured NSSAI to the UE.

질문: UE가 SNPN onboarding service에 등록 중이거나 등록된 경우 serving SNPN의 configured NSSAI 제공 정책을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall_not",
  "polarity": "negative",
  "actor": "serving SNPN",
  "condition": "if the UE is registering or registered for onboarding services in the SNPN",
  "action": "provide a configured NSSAI to the UE",
  "exception": "",
  "gold_summary_ko": "그 경우 serving SNPN은 UE에 configured NSSAI를 제공해서는 안 된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

UE가 SNPN에서 onboarding services에 대해 등록 중이거나 등록된 경우, serving SNPN은 UE에게 configured NSSAI를 제공해서는 안 된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 1: The value(s) used in the default configured NSSAI are expected to be commonly decided by all roaming 
partners, e.g., values standardized by 3GPP or other bodies. 
In case of an SNPN, the SNPN may configure a UE which is neither registering nor registered for onboarding services 
in SNPN with: 
a) a configured NSSAI applicable to the SNPN; 
b) NSSRG information if the UE has indicated that it supports the subscription-based restrictions to simultaneous 
registration of network slices feature; 
c) S-NSSAI time validity information if the UE has indicated that it supports S-NSSAI time validity information; 
d) on-demand NSSAI if the UE has indicated it supports the network slice usage control feature; and 
e) S-NSSAI location validity information if the UE has indicated that it supports S-NSSAI location validity 
information. 
In addition, the credential holder may configure a single default configured NSSAI associated with the selected entry of 
the "list of subscriber data" or the PLMN subscription and consider the default configured NSSAI as valid in a SNPN 
for which the UE has neither a configured NSSAI nor an allowed NSSAI. 
[대상 문장]
. The support for 
NSSRG information by the UE and the network, respectively, is optional. 
The allowed NSSAI and the rejected NSSAI for the current registration area are managed per access type 
independently, i.e. 3GPP access or non-3GPP access, and is applicable for the registration area. If the UE does not have 
a valid registration area, the rejected NSSAI for the current registration area is applicable to the tracking area on which 
it was received. If the registration area contains TAIs belonging to different PLMNs, which are equivalent PLMNs, the 
allowed NSSAI, the rejected NSSAI for the current registration area, rejected NSSAI for the failed or revoked NSSAA 
and rejected NSSAI for the maximum number of UEs reached are applicable to these PLMNs in this registration area. 
The allowed NSSAI that is associated with a registration area containing TAIs belonging to different PLMNs, which are 
equivalent PLMNs, can be used to form
```

</details>

## V2-P1-069
기준 G045 · 3GPP TS 23.501 V18.12.0 · 5.3.2.4 · PDF 100쪽(인쇄 99쪽)

원문: If the UE is performing registration over one access and intends to perform registration over the other access in the same PLMN (e.g. the 3GPP access and the selected N3IWF, TNGF or W-AGF are located in the same PLMN), the UE shall not initiate the registration over the other access until the Registration procedure over first access is completed.

질문: UE가 같은 PLMN의 한 access에서 등록 중 다른 access 등록도 하려는 경우 시작 시점을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall_not",
  "polarity": "negative",
  "actor": "UE",
  "condition": "when already registering over one access and intending to register over the other access in the same PLMN",
  "action": "initiate registration over the other access",
  "exception": "not until registration over the first access is complete",
  "gold_summary_ko": "UE는 첫 access의 registration procedure가 완료되기 전에는 다른 access의 등록을 시작해서는 안 된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

UE가 같은 PLMN의 한 access에서 이미 등록 절차를 진행 중인 상태에서 다른 access에 대해서도 등록을 시도하려면, 기존 등록 절차가 시작된 뒤에 그 시도를 시작할 수 있다. 즉, 한 access의 등록이 진행 중이어도 다른 access 등록은 병행하여 시작할 수 있다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 123 501 V18.12.0 (2026-01)993GPP TS 23.501 version 18.12.0 Release 18

[대상 문장]
. 
NOTE: To which access the UE performs registration first is up to UE implementation. 
When the UE is successfully registered to an access (3GPP access or Non-3GPP access respectively) and the UE 
registers via the other access: 
- if the second access is located in the same PLMN (e.g. the UE is registered via a 3GPP access and selects a 
N3IWF, TNGF or W-AGF located in the same PLMN), the UE shall use for the registration to the PLMN 
associated with the new access the 5G-GUTI that the UE has been provided with at the previous registration or 
UE configuration update procedure for the first access in the same PLMN. Upon successful completion of the 
registration to the second access, if the network included a 5G-GUTI in the Registration Accept, the UE shall use 
the 5G-GUTI received in the Registration Accept for both registrations. If no 5G-GUTI is included in the 
Registration Accept, then the UE uses the 5G-GUTI assigned for the e
```

</details>

## V2-P1-070
기준 G034 · 3GPP TS 24.501 V18.12.0 · 6.4.1.2 · PDF 644쪽(인쇄 643쪽)

원문: The UE should not request to join a multicast MBS session for local MBS service if neither current TAI nor CGI of the current cell is part of the MBS service area(s) of the multicast MBS session, if the UE has valid information of the MBS service area(s) of the multicast MBS session.

질문: 현재 TAI와 cell CGI가 multicast MBS session service area에 없고 UE가 유효한 area 정보를 가진 경우 join request 정책을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should_not",
  "polarity": "negative",
  "actor": "UE",
  "condition": "if the UE has valid MBS service-area information and neither the current TAI nor current-cell CGI is in the multicast session service area",
  "action": "request to join the multicast MBS session for local MBS service",
  "exception": "",
  "gold_summary_ko": "그 조건에서 UE는 local MBS service의 multicast MBS session 참가를 요청하지 않는 것이 권고된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

UE가 multicast MBS session의 MBS service area에 대한 유효한 정보를 가지고 있고, 현재 TAI와 현재 셀의 CGI가 그 service area에 속하지 않는 경우, UE는 local MBS service를 위한 multicast MBS session join request를 하지 않는 것이 권고된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 124 501 V18.12.0 (2025-10)6433GPP TS 24.501 version 18.12.0 Release 18
b) if the Type of multicast MBS session ID is set to "Source specific IP multicast address for IPv4" or " Source 
specific IP multicast address for IPv6", the UE shall set the Source IP address information and the Destination IP 
address information to the corresponding values. 

[대상 문장]
. 
NOTE 4: The UE obtains the details of the MBS session ID(s) e.g., TMGI, Source IP address information and 
Destination IP address information as a pre-configuration in the UE or during the MBS service 
announcement, which is out of scope of this specification. Pre-configuration can be provided in one or 
more of the following ways: 
a) in a UE implementation-specific way (e.g. factory configuration); 
b) in the USIM (see EF
5MBSUECONFIG file in 3GPP TS 31.102 [22]); or 
c) in the UE pre-configuration MO for MBS (see 3GPP TS 24.575 [65). 
The UE should set the RQoS bit to "Reflective QoS supported" in the 5GSM capability IE of the PDU SESSION 
ESTABLISHMENT REQUEST message if the UE supports reflective QoS and: 
a) the UE requests to establish a new PDU session of "IPv4", "IPv6", "IPv4v6" or "Ethernet" PDU session type; 
b) the UE requests to transfer an existing PDN connectio n in the EPS of "IPv4", "IPv6", "IPv4v6" or "Ethernet" 
PD
```

</details>

## V2-P1-071
기준 G021 · 3GPP TS 23.501 V18.12.0 · 5.4.3.2 · PDF 119쪽(인쇄 118쪽)

원문: When the 5GS supports the Paging Policy Differentiation (PPD) feature, the DSCP value (TOS in IPv4 / TC in IPv6) is set by the application to indicate to the 5GS which Paging Policy should be applied for a certain IP packet.

질문: 5GS가 Paging Policy Differentiation을 지원할 때 특정 IP packet에 적용할 Paging Policy를 표시하는 방식을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should",
  "polarity": "positive",
  "actor": "Paging Policy",
  "condition": "when the 5GS supports Paging Policy Differentiation, for a particular IP packet",
  "action": "be selected for application according to the DSCP value set by the application",
  "exception": "",
  "gold_summary_ko": "application이 설정한 DSCP value는 특정 IP packet에 어떤 Paging Policy를 적용하는 것이 권고되는지를 5GS에 나타낸다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

5GS가 Paging Policy Differentiation(PPD) 기능을 지원할 때, 애플리케이션은 특정 IP packet에 적용할 Paging Policy를 5GS에 알리기 위해 DSCP 값(TOS in IPv4 / TC in IPv6)을 설정하는 것이 권고된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
CTIVE state, the NG-RAN performs paging and determines 
the paging strategy based on e.g. local configuration and information received from AMF as described in clause 5.4.6.3 
and SMF as described in clause 5.4.3.2. 
In the case of Network Triggered Service Request from SMF, the SMF determines the 5QI and ARP based on the 
downlink packet (if the SMF performs buffering) or the Downlink Data Report received from UPF (if the UPF performs 
buffering). The SMF includes the 5QI and ARP corresponding to the QoS Flow of the received downlink PDU in the 
request sent to the AMF. If the UE is in CM IDLE, the AMF uses e.g. the 5QI and ARP to derive different paging 
strategies as described in clause 4.2.3.3 of TS 23.502 [3]. 
NOTE: The 5QI is used by AMF to determine suitable paging strategies. 
5.4.3.2 Paging Policy Differentiation 
Paging policy differentiation is an optional feature that allows the AMF, based on operator configuration, to apply 
different paging strategies for different traffic or service types provided within the same PDU Session. In this Release of 
the specification this feature applies only to PDU Session of IP type. 

[대상 문장]
. For example, 
as defined in TS 23.228 [15], the P-CSCF may support Paging Policy Differentiation by marking packet(s) to be sent 
towards the UE that relate to a specific IMS services (e.g. conversational voice as defined in IMS multimedia telephony 
service). 
NOTE 1: This PPD feature may be used to determine the Paging Cause Indication for Voice Service, as described 
in clause 5.38.3. 
```

</details>

## V2-P1-072
기준 G041 · 3GPP TS 24.501 V18.12.0 · 4.4.2.1.1 · PDF 54쪽(인쇄 53쪽)

원문: In the present document, when the UE is required to delete an ngKSI, the UE shall set the ngKSI to the value "no key is available" and consider also the associated keys K AMF or K'AMF, 5G NAS ciphering key and 5G NAS integrity key invalid (i.e. the 5G NAS security context associated with the ngKSI as no longer valid).

질문: UE의 ngKSI 삭제 상황에서 ngKSI와 연관 키를 어떻게 처리하는지 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall",
  "polarity": "positive",
  "actor": "UE",
  "condition": "when the UE is required to delete an ngKSI",
  "action": "set the ngKSI to 'no key is available' and consider the associated K_AMF or K'_AMF, NAS ciphering key, and NAS integrity key invalid",
  "exception": "",
  "gold_summary_ko": "UE는 ngKSI를 'no key is available'로 반드시 설정하고 연관된 K_AMF 또는 K'_AMF와 NAS 암호화·무결성 키를 무효로 간주해야 한다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

UE에서 ngKSI를 삭제하는 상황에서는 해당 ngKSI와 연관된 키 자료도 함께 제거해야 한다. 즉, ngKSI만 따로 남겨 두지 않고 그와 연결된 보안 컨텍스트 정보를 함께 정리해야 한다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
ement 
procedure or, for the mapped 5G NAS security context, during the inter-system change. The ngKSI consists of a value 
and a type of security context parameter indicating whether a 5G NAS security context is a native 5G NAS security 
context or a mapped 5G NAS security context. When the 5G NAS security context is a native 5G NAS security context, 
the ngKSI has the value of KSI
AMF, and when the current 5G NAS security context is of type mapped, the ngKSI has the 
value of KSIASME. 
The 5G NAS security context which is indicated by an ngKSI can be taken into use to establish the secure exchange of 
NAS messages when a new N1 NAS signalling connection is established without executing a new primary 
authentication and key agreement procedure (see subclause 5.4.1) or when the AMF initiates a security mode control 
procedure. For this purpose, the initial NAS messages (i.e. REGISTRATION REQUEST, DEREGISTRATION 
REQUEST, SERVICE REQUEST and CONTROL PLANE SERVICE REQUEST) and the SECURITY MODE 
COMMAND message contain an ngKSI in the ngKSI IE indicating the current 5G NAS security context used to 
integrity protect the NAS message. 

[대상 문장]
). In the initial registration 
procedure, when the key K
AUSF, is invalid, the UE shall delete the ngKSI. 
NOTE: In some specifications the term ciphering key sequence number might be used instead of the term key set 
identifier (KSI). 
As described in subclause 4.8 in order to interwork with E-UTRAN connected to EPC, the UE supporting both S1 mode 
and N1 mode can operate in either single-registration mode or dual-registration mode. A UE operating in dual-
registration mode shall independently maintain and use both EPS security context (see 3GPP TS 24.301 [15]) and 5G 
NAS security context. When the UE operating in dual-registration mode performs an EPS attach procedure, it shall take 
into use an EPS security context and follow the handling of this security context as specified in 3GPP TS 24.301 [15]. 
However, when the UE operating in dual-registration mode performs an initial registration procedure, it shall take into 
use a 5G NAS
```

</details>

## V2-P1-073
기준 G011 · 3GPP TS 23.501 V18.12.0 · 4.2.8.5.1 · PDF 67쪽(인쇄 66쪽)

원문: When a N5CW device performs an EAP-based access authentication procedure to connect to a trusted WLAN access network, the N5CW device may simultaneously be registered to a 5GC of a PLMN or SNPN.

질문: N5CW device가 trusted WLAN 연결을 위해 EAP 기반 access authentication을 수행할 때 5GC 등록 상태를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "may",
  "polarity": "positive",
  "actor": "N5CW device",
  "condition": "when performing EAP-based access authentication to connect to a trusted WLAN access network",
  "action": "simultaneously be registered to a 5GC of a PLMN or SNPN",
  "exception": "",
  "gold_summary_ko": "그 과정에서 N5CW device는 PLMN 또는 SNPN의 5GC에 동시에 등록되어 있을 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

N5CW 디바이스가 trusted WLAN 연결을 위해 EAP 기반 access authentication을 수행하는 경우, 해당 디바이스는 5GC에 등록된 상태여야 한다. 즉, 이 절차는 5GC 등록이 완료된 디바이스를 전제로 한다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
are the same as 
defined in clause 4.2. 
NOTE 6: The reference architecture in figure 4.2.8.4-1 supports service based interfaces for AMF, SMF and other 
NFs not represented in the figure. 
4.2.8.5 Access to 5GC from devices that do not support 5GC NAS over WLAN 
access 
4.2.8.5.1 General 
The devices that do not support 5GC NAS signalling over WLAN access are referred to as "Non-5G-Capable over 
WLAN" devices, or N5CW devices for short. A N5CW device is not capable to operate as a 5G UE that supports 5GC 
NAS signalling over a WLAN access network, however, it may be capable to operate as a 5G UE over NG-RAN. 
Clause 4.2.8.5 specifies the 5GC architectural enhancements that enable N5CW devices to access 5GC via trusted 
WLAN access networks. A trusted WLAN access network is a particular type of a Trusted Non-3GPP Access Network 
(TNAN) that supports a WLAN access technology, e.g. IEEE 802.11. Not all trusted WLAN access networks support 
5GC access from N5CW devices. To support 5GC access from N5CW devices, a trusted WLAN access network must 
support the special functionality specified below (e.g. it must support a TWIF function). 

[대상 문장]
. The 5GC registration is 
performed by the TWIF function (see next clause) in the trusted WLAN access network, on behalf of the N5CW device. 
The type of EAP authentication procedure, which is used during the 5GC registration to authenticate the N5CW device, 
is specified in TS 33.501 [29]. In this Release of the specification, Trusted WLAN Access for N5CW Device only 
supports IP PDU Session type. 
```

</details>

## V2-P1-074
기준 G020 · 3GPP TS 23.501 V18.12.0 · 5.3.4.1.2 · PDF 109쪽(인쇄 108쪽)

원문: The Registration Area of a UE in the Non-Allowed Area should consist of a set of TAs which belongs to a NonAllowed Area of the UE.

질문: Non-Allowed Area에 있는 UE의 Registration Area를 구성하는 TA 범위를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should",
  "polarity": "positive",
  "actor": "Registration Area of a UE in a Non-Allowed Area",
  "condition": "when the UE is in a Non-Allowed Area",
  "action": "consist of a set of TAs belonging to a Non-Allowed Area of the UE",
  "exception": "",
  "gold_summary_ko": "해당 Registration Area는 UE의 Non-Allowed Area에 속하는 TA 집합으로 구성하는 것이 권고된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

Non-Allowed Area에 있는 UE의 Registration Area는 UE의 Non-Allowed Area에 속하는 TA들의 집합으로 구성되는 것이 권고된다. 즉, 해당 TA 범위는 UE의 Non-Allowed Area에 속한 TA들로 이루어져야 한다는 권고이다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
ing wireline 
access, see TS 23.316 [84]. 
A Service Area Restriction may contain one or more (e.g. up to 16) entire Tracking Areas each or the Service Area 
Restriction may be set as unlimited (i.e. contain all Tracking Areas of the PLMN). The UE's subscription data in the 
UDM includes a Service Area Restriction which may contain either Allowed or Non-Allowed Areas–specified by using 
explicit Tracking Area identities and/or other geographical information (e.g. longitude/latitude, zip code, etc). The 
geographical information used to specify Allowed or Non-Allowed Area is only managed in the network and the 
network will map it to a list of TAs before sending Service Area Restriction information to the PCF, NG-RAN and UE. 
When the AMF assigns a limited allowed area to the UE, the AMF shall provide the UE with Service Area Restrictions 
which consist of either Allowed Areas or Non-Allowed Areas. The Allowed Areas included in the Service Area 
Restrictions can be pre-configured and/or dynamically assigned by the AMF. 
The Allowed Area may alternatively be configured as unlimited i.e. it may contain all Tracking Areas of the PLMN. 

[대상 문장]
. The Registration Area of a UE in the Allowed Area should consist of a set of TAs which 
belongs to an Allowed Area of the UE. The AMF provides the Service Area Restriction in the form of TA(s), which 
may be a subset of full list stored in UE's subscription data or provided by the PCF, to the UE during the Registration 
procedure. 
NOTE: As the finest granularity for Service Area Restri ctions are at TA level, subscriptions with limited 
geographical extent, like subscriptions for Fixed Wireless Access, will be allocated one or a few TAs and 
will consequently be allowed to access services in a larger area than in e.g. a FWA system. 
The limited allowed area may also be limited by the AMF by a maximum allowed number of Tracking Areas, even 
though this limitation is not sent to the UE. If maximum allowed number of Tracking Areas is used in combination with 
Allowed Area, the maximum allowed number of Tracking Areas indicates (to the A
```

</details>

## V2-P1-075
기준 G009 · 3GPP TS 24.501 V18.12.0 · 4.4.2.1.1 · PDF 54쪽(인쇄 53쪽)

원문: As described in subclause 4.8 in order to interwork with E-UTRAN connected to EPC, the UE supporting both S1 mode and N1 mode can operate in either single-registration mode or dual-registration mode.

질문: S1 mode와 N1 mode를 모두 지원하는 UE의 registration mode 운용 선택지를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "can",
  "polarity": "positive",
  "actor": "UE supporting both S1 mode and N1 mode",
  "condition": "for interworking with E-UTRAN connected to EPC",
  "action": "operate in either single-registration mode or dual-registration mode",
  "exception": "",
  "gold_summary_ko": "해당 UE는 EPC 연결 E-UTRAN과 interwork하기 위해 single-registration mode 또는 dual-registration mode로 동작할 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

S1 mode와 N1 mode를 모두 지원하는 UE는 등록 모드를 S1 mode, N1 mode 또는 두 모드를 함께 사용하는 방식으로 운용할 수 있다. 즉, UE는 네트워크와의 등록 절차에서 두 모드 중 하나만 선택하거나 둘 다 지원하는 형태로 동작할 수 있다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
e taken into use to establish the secure exchange of 
NAS messages when a new N1 NAS signalling connection is established without executing a new primary 
authentication and key agreement procedure (see subclause 5.4.1) or when the AMF initiates a security mode control 
procedure. For this purpose, the initial NAS messages (i.e. REGISTRATION REQUEST, DEREGISTRATION 
REQUEST, SERVICE REQUEST and CONTROL PLANE SERVICE REQUEST) and the SECURITY MODE 
COMMAND message contain an ngKSI in the ngKSI IE indicating the current 5G NAS security context used to 
integrity protect the NAS message. 
In the present document, when the UE is required to delete an ngKSI, the UE shall set the ngKSI to the value "no key is 
available" and consider also the associated keys K
AMF or K'AMF, 5G NAS ciphering key and 5G NAS integrity key 
invalid (i.e. the 5G NAS security context associated with the ngKSI as no longer valid). In the initial registration 
procedure, when the key K
AUSF, is invalid, the UE shall delete the ngKSI. 
NOTE: In some specifications the term ciphering key sequence number might be used instead of the term key set 
identifier (KSI). 

[대상 문장]
. A UE operating in dual-
registration mode shall independently maintain and use both EPS security context (see 3GPP TS 24.301 [15]) and 5G 
NAS security context. When the UE operating in dual-registration mode performs an EPS attach procedure, it shall take 
into use an EPS security context and follow the handling of this security context as specified in 3GPP TS 24.301 [15]. 
However, when the UE operating in dual-registration mode performs an initial registration procedure, it shall take into 
use a 5G NAS security context and follow the handling of this security context as described in the present specification. 
The UE and the AMF need to be able to maintain two 5G NAS security contexts simultaneously, i.e. a current 5G NAS 
security context and a non-current 5G NAS security context, since: 
a) after a 5G re-authentication, the UE and the AMF can have both a current 5G NAS security context and a non-
current 5G NAS security context 
```

</details>

## V2-P1-076
기준 G046 · 3GPP TS 23.501 V18.12.0 · 5.3.4.3.4 · PDF 113쪽(인쇄 112쪽)

원문: If the UE has not received any NSAG Information from the AMF, the UE shall not use Network Slice based cell reselection and Random Access at all.

질문: AMF에서 NSAG Information을 받지 못한 UE의 Network Slice 기반 cell reselection과 Random Access 처리를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall_not",
  "polarity": "negative",
  "actor": "UE",
  "condition": "if the UE has not received NSAG Information from the AMF",
  "action": "use Network Slice based cell reselection and Random Access",
  "exception": "",
  "gold_summary_ko": "UE는 NSAG Information을 받지 못하면 Network Slice 기반 cell reselection과 Random Access를 전혀 사용해서는 안 된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

UE가 AMF로부터 NSAG Information을 받지 못한 경우, UE는 Network Slice 기반 cell reselection과 Random Access를 전혀 사용해서는 안 된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 123 501 V18.12.0 (2026-01)1123GPP TS 23.501 version 18.12.0 Release 18
NOTE 2: The AMF can assign same priority value for NSAGs provided in the NSAG Information. 
If the UE has received NSAG Information from the AMF, the UE shall use the NSAG Information provided by the 
AMF for cell reselection and Random Access as described below. 
[대상 문장]
. 
The UE NAS provides to the UE AS the NSAG Information as received from the AMF and the S-NSSAIs in the 
Allowed NSSAI and any Partially Allowed NSSAI as input to cell reselection, except when the UE intends to register 
with a new (including any S-NSSAIs rejected partially in the RA) set of S-NSSAIs with a Requested NSSAI different 
from the current Allowed NSSAI and any Partially Allowed NSSAI, in which case the UE NAS provides to the UE AS 
layer the NSAG Information as received from the AMF and the S-NSSAIs in the Requested NSSAI and this may trigger 
a cell reselection, before sending the Registration Request including the new Requested NSSAI. 
For Network Slice based Random Access, different Random Access resources may be assigned to different NSAG(s). 
The UE determines Random Access configuration among NSAGs that are published in SIB for Random Access and 
that are associated to the S-NSSAIs triggering the access. If the signa
```

</details>

## V2-P1-077
기준 G033 · 3GPP TS 24.501 V18.12.0 · 5.5.1.2.4 · PDF 359쪽(인쇄 358쪽)

원문: If the UE is authorized to use V2X communication over PC5 reference point based on: a) at least one of the following bits in the 5GMM capability IE of the REGISTRATION REQUEST message set by the UE, or already stored in the 5GMM context in the AMF during the previous registration procedure as follows: 1) the V2XCEPC5 bit to "V2X communication over E-UTRA-PC5 supported"; or 2) the V2XCNPC5 bit to "V2X communication over NR-PC5 supported"; and b) the user's subscription context obtained from the UDM as defined in 3GPP TS 23.287 [6C]; the AMF should not immediately release the NAS signalling connection after the completion of the registration procedure.

질문: UE가 capability bit와 subscription context에 따라 PC5 기반 V2X communication 권한을 가진 경우 registration 완료 후 NAS signalling connection 처리 정책을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should_not",
  "polarity": "negative",
  "actor": "AMF",
  "condition": "if the UE is authorized for V2X communication over PC5 by the stated capability bits and subscription context",
  "action": "immediately release the NAS signalling connection after registration completes",
  "exception": "",
  "gold_summary_ko": "그 조건에서 AMF는 registration 완료 직후 NAS signalling connection을 해제하지 않는 것이 권고된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

UE가 명시된 capability bit와 가입자 subscription context에 따라 PC5 기반 V2X communication 사용 권한이 있는 경우, AMF는 등록 절차 완료 후 NAS signalling connection을 즉시 해제하지 않는 것이 권고된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 124 501 V18.12.0 (2025-10)3583GPP TS 24.501 version 18.12.0 Release 18

[대상 문장]
. 
If the UE is authorized to use A2X communication over PC5 reference point based on: 
a) at least one of the following bits in the 5GMM capability IE of the REGISTRATION REQUEST message set by 
the UE, or already stored in the 5GMM context in the AMF during the previous registration procedure as 
follows: 
1) the A2XEPC5 bit to "A2X over E-UTRA-PC5 supported"; or 
2) the A2XNPC5 bit to "A2X over NR-PC5 supported"; and 
b) the user's subscription context obtained from the UDM as defined in 3GPP TS 23.256 [6C]; 
the AMF should not immediately release the NAS signalling connection after the completion of the registration 
procedure. 
If the UE is authorized to use 5G ProSe services based on: 
a) at least one of the following bits in the 5GMM capability IE of the REGISTRATION REQUEST message set by 
the UE, or already stored in the 5GMM context in the AMF during the previous registration procedure as 
follows: 
1) the 5G ProSe direct disc
```

</details>

## V2-P1-078
기준 G017 · 3GPP TS 24.501 V18.12.0 · 4.6.2.1 · PDF 98쪽(인쇄 97쪽)

원문: The default configured NSSAI may be changed by sending a UE parameters update transparent container to the UE during the NAS transport procedure.

질문: NAS transport procedure 중 default configured NSSAI를 변경하는 방법을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "may",
  "polarity": "positive",
  "actor": "default configured NSSAI",
  "condition": "during the NAS transport procedure",
  "action": "be changed by sending a UE parameters update transparent container to the UE",
  "exception": "",
  "gold_summary_ko": "NAS transport procedure 중 UE parameters update transparent container를 UE에 전송하여 default configured NSSAI를 변경할 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

NAS transport procedure 중에는 UE parameters update transparent container를 UE에 보내는 방식으로 default configured NSSAI를 변경하도록 허용된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 124 501 V18.12.0 (2025-10)973GPP TS 24.501 version 18.12.0 Release 18
NOTE 3: In roaming scenarios, when the UE is compliant with earlier versions of the specification or when the 
serving network does not provide a mapped S-NSSAI for one or more S-NSSAIs in the allowed NSSAI 
or configured NSSAI, the UE can omit a mapped S-NSSAI for one or more S-NSSAIs in requested 
NSSAI. 
The set of network slice(s) for a UE can be changed at any time while the UE is registered to a PLMN or SNPN, and the 
change may be initiated by the network or the UE. In this case, the allowed NSSAI and associated registration area may 
be changed during the registration procedure or the generic UE configuration update procedure. The configured NSSAI 
and the rejected NSSAI may be changed during the registration procedure or the generic UE configuration update 
procedure. 
[대상 문장]
. The pending NSSAI may be changed during the registration procedure. In 
addition, using the generic UE configuration update procedure, the network may trigger the registration procedure in 
order to update the allowed NSSAI. 
The UE in NB-N1 mode does not include the requested NSSAI during the registration procedure if the 5GS registration 
type IE indicates "mobility registration updating", procedure is not initiated to change the slice(s) that the UE is 
currently registered to, and the UE is still in the current registration area. 
The AMF does not include the allowed NSSAI during a registration procedure with the 5GS registration type IE 
indicating "mobility registration updating" for the UE in NB-N1 mode, except if the allowed NSSAI has changed for 
the UE. 
The UE does not include the requested NSSAI during the registration procedure if the 5GS registration type IE indicates 
"SNPN onboarding registration" or the UE is register
```

</details>

## V2-P1-079
기준 G001 · 3GPP TS 23.501 V18.12.0 · 4.2.4 · PDF 50쪽(인쇄 49쪽)

원문: The N38 references point can be between V-SMFs in the same VPLMN, or between V-SMFs in different VPLMNs (to enable inter-PLMN mobility).

질문: V-SMF 사이 N38 reference point의 VPLMN 배치 관계를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "can",
  "polarity": "positive",
  "actor": "N38 reference point",
  "condition": "",
  "action": "exist between V-SMFs in the same VPLMN or in different VPLMNs",
  "exception": "the inter-VPLMN case enables inter-PLMN mobility",
  "gold_summary_ko": "N38 reference point는 같은 VPLMN의 V-SMF 사이 또는 서로 다른 VPLMN의 V-SMF 사이에 존재할 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

N38 reference point는 같은 VPLMN의 V-SMF들 사이에 있거나, 서로 다른 VPLMN의 V-SMF들 사이에 있을 수 있도록 허용된다. 이는 inter-PLMN mobility를 enable하기 위한 경우이다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 123 501 V18.12.0 (2026-01)493GPP TS 23.501 version 18.12.0 Release 18

[대상 문장]
). 
NOTE 10: For clarity, the NWDAF(s) with roaming exchange capability (RE-NWDAF) and their connections with 
other NFs, are not depicted in the reference point architecture figure. For more information on network 
data analytics architecture refer to TS 23.288 [86]. 
For the roaming scenarios described above each PLMN implements proxy functionality to secure interconnection and 
hide topology on the inter-PLMN interfaces. 
vNRFVPLMN
NF
VPLMN HPLMN
hNRFN27
 
Figure 4.2.4-7: NRF Roaming architecture in reference point representation 
NOTE 11: For the sake of clarity, SEPPs on both sides of PLMN borders are not depicted in figure 4.2.4-7. 
Figure 4.2.4-8: Void 
Operators can deploy UPFs supporting the Inter PLMN UP Security (IPUPS) functionality at the border of their 
network to protect their network from invalid inter PLMN N9 traffic in home routed roaming scenarios. The UPFs 
supporting the IPUPS functionality in VPLMN and HPLMN are c
```

</details>

## V2-P1-080
기준 G023 · 3GPP TS 24.501 V18.12.0 · 4.6.2.2 · PDF 98쪽(인쇄 97쪽)

원문: The allowed NSSAI(s) should be stored in a non-volatile memory in the ME as specified in annex C.

질문: allowed NSSAI를 ME에 저장하는 위치와 방식을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should",
  "polarity": "positive",
  "actor": "allowed NSSAI(s)",
  "condition": "",
  "action": "be stored in non-volatile memory in the ME",
  "exception": "as specified in annex C",
  "gold_summary_ko": "allowed NSSAI는 annex C에 따라 ME의 non-volatile memory에 저장하는 것이 권고된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

allowed NSSAI(s)는 부속서 C에 명시된 바와 같이 ME의 비휘발성 메모리에 저장하는 것이 권고된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
ated NSSRG information, the NSSRG information sha ll also be stored in a non-volatile memory in the ME 
as specified in annex C; 
b) associated NSAG information, the NSAG information shall be stored in the ME; 
c) associated S-NSSAI time validity information, the S-NSSAI time validity information shall also be stored in a 
non-volatile memory in the ME as specified in annex C; 
d) associated S-NSSAI location validity information, the S-NSSAI location validity information shall also be stored 
in a non-volatile memory in the ME as specified in annex C; and 
e) associated on-demand NSSAI, the on-de mand NSSAI shall also be stored in a non-volatile memory in the ME as 
specified in annex C. 
Each of the configured NSSAI stored in the UE, including the default configured NSSAI, is a set composed of at most 
16 S-NSSAIs. Each of the configured NSSAI, except the default configured NSSAI, is associated with a PLMN identity 
or SNPN identity and, if the UE supports access to an SNPN using credentials from a credentials holder, equivalent 
SNPNs or both, the selected entry of the "list of subscriber data" or the selected PLMN subscription. 

[대상 문장]
. The partially 
allowed NSSAI(s) should be stored in a non-volatile memory in the ME as specified in annex C. For an allowed 
NSSAI, if there is associated alternative NSSAI, the alternative NSSAI should also be stored in a non-volatile memory 
in the ME as specified in annex C. 
Each of the allowed NSSAI stored in the UE is a set composed of at most 8 S-NSSAIs and is associated with a PLMN 
identity or SNPN identity, an access type and, if the UE supports access to an SNPN using credentials from a 
credentials holder, equivalent SNPNs or both, the selected entry of the "list of subscriber data" or the selected PLMN 
subscription. Each of the alternative NSSAI stored in the UE is a set composed of at most 8 pairs of S-NSSAI to be 
replaced and alternative S-NSSAI, and is associated with a PLMN identity or SNPN identity, an access type and, if the 
UE supports access to an SNPN using credentials from a credentials holder, equivalent SNP
```

</details>

## V2-P1-081
기준 G027 · 3GPP TS 24.501 V18.12.0 · 5.3.26 · PDF 223쪽(인쇄 222쪽)

원문: If the AMF does not provide the Unavailability configuration IE or the AMF sets the EUPR bit value in the Unavailability configuration IE to "UE needs to report end of unavailability period", the UE should trigger registration procedure for mobility registration update when the unavailability period duration has ended.

질문: Unavailability configuration IE가 없거나 EUPR이 종료 보고를 요구할 때 unavailability period 종료 후 UE 동작을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should",
  "polarity": "positive",
  "actor": "UE",
  "condition": "if the AMF omits the Unavailability configuration IE or sets EUPR to require an end-of-period report, when the unavailability duration ends",
  "action": "trigger registration for mobility registration update",
  "exception": "",
  "gold_summary_ko": "해당 조건에서 unavailability period가 끝나면 UE는 mobility registration update를 위한 registration procedure를 시작하는 것이 권고된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

AMF가 Unavailability configuration IE를 제공하지 않거나, AMF가 해당 IE의 EUPR 비트 값을 "UE needs to report end of unavailability period"로 설정한 경우, UE는 unavailability period duration이 끝났을 때 mobility registration update를 위한 registration procedure를 트리거하는 것이 권고된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
1 version 18.12.0 Release 18
not initiate any NAS signalling on that NR satellite access and PLMN while the discontinuous coverage maximum time 
offset timer is running. The UE shall stop the discontinuous coverage maximum time offset timer and initiate NAS 
signalling if the UE receives paging message receives a NOTIFICATION message over non-3GPP access as described 
in case b) subclause 5.6.3.1, has pending emergency services, is establishing an emergency PDU session, is performing 
emergency services fallback procedure, or when the UE enters a TAI outside the registration area. At expiry of the 
discontinuous coverage maximum time offset timer, the UE shall perform a registration procedure for mobility 
registration update. 
If the AMF sets the EUPR bit value in the Unavailability configuration IE to "UE does not need to report end of 
unavailability period", then upon returning to a TA in the current registration area the UE shall choose an appropriate 
substate of 5GMM-REGISTERED and the UE is not required to trigger the registration procedure for mobility 
registration update when the unavailability period duration has ended. 
[대상 문장]
. 
When the unavailability period is activated, all NAS timers are stopped and associated procedures aborted except for 
timers T3512, T3324, T3346, T3444, T3445, T3447, T3448, T3396, T3526, T3584, T3585, T3587, any back-off timers, 
T3245, T3247, the timer T controlling the periodic search for HPLMN or EHPLMN or higher prioritized PLMNs, the 
timer T
SENSE controlling the periodic search for PLMNs satisfying the operator controlled signal level threshold, the 
timer TF, the timer TG (see 3GPP TS 23.122 [5]), the timer TNSU and the timer instance associated with the entry in the 
list of "PLMNs not allowed to operate at the present UE location", slice deregistration inactivity timer when the UE 
activates the unavailability period using registration procedure, the UE shall reset the registration attempt counter and 
service request attempt counter. 
When the UE activates the unavailability period using registration procedure without pro
```

</details>

## V2-P1-082
기준 G020 · 3GPP TS 23.501 V18.12.0 · 5.3.4.1.2 · PDF 109쪽(인쇄 108쪽)

원문: The Registration Area of a UE in the Non-Allowed Area should consist of a set of TAs which belongs to a NonAllowed Area of the UE.

질문: Non-Allowed Area에 있는 UE의 Registration Area를 구성하는 TA 범위를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should",
  "polarity": "positive",
  "actor": "Registration Area of a UE in a Non-Allowed Area",
  "condition": "when the UE is in a Non-Allowed Area",
  "action": "consist of a set of TAs belonging to a Non-Allowed Area of the UE",
  "exception": "",
  "gold_summary_ko": "해당 Registration Area는 UE의 Non-Allowed Area에 속하는 TA 집합으로 구성하는 것이 권고된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

Non-Allowed Area에 있는 UE의 Registration Area는 해당 UE가 위치한 Non-Allowed Area를 포함하는 TA 범위로 구성되어야 한다. 즉, UE가 그 영역에 있을 때 등록 영역은 그 Non-Allowed Area를 포괄하도록 설정된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
ing wireline 
access, see TS 23.316 [84]. 
A Service Area Restriction may contain one or more (e.g. up to 16) entire Tracking Areas each or the Service Area 
Restriction may be set as unlimited (i.e. contain all Tracking Areas of the PLMN). The UE's subscription data in the 
UDM includes a Service Area Restriction which may contain either Allowed or Non-Allowed Areas–specified by using 
explicit Tracking Area identities and/or other geographical information (e.g. longitude/latitude, zip code, etc). The 
geographical information used to specify Allowed or Non-Allowed Area is only managed in the network and the 
network will map it to a list of TAs before sending Service Area Restriction information to the PCF, NG-RAN and UE. 
When the AMF assigns a limited allowed area to the UE, the AMF shall provide the UE with Service Area Restrictions 
which consist of either Allowed Areas or Non-Allowed Areas. The Allowed Areas included in the Service Area 
Restrictions can be pre-configured and/or dynamically assigned by the AMF. 
The Allowed Area may alternatively be configured as unlimited i.e. it may contain all Tracking Areas of the PLMN. 

[대상 문장]
. The Registration Area of a UE in the Allowed Area should consist of a set of TAs which 
belongs to an Allowed Area of the UE. The AMF provides the Service Area Restriction in the form of TA(s), which 
may be a subset of full list stored in UE's subscription data or provided by the PCF, to the UE during the Registration 
procedure. 
NOTE: As the finest granularity for Service Area Restri ctions are at TA level, subscriptions with limited 
geographical extent, like subscriptions for Fixed Wireless Access, will be allocated one or a few TAs and 
will consequently be allowed to access services in a larger area than in e.g. a FWA system. 
The limited allowed area may also be limited by the AMF by a maximum allowed number of Tracking Areas, even 
though this limitation is not sent to the UE. If maximum allowed number of Tracking Areas is used in combination with 
Allowed Area, the maximum allowed number of Tracking Areas indicates (to the A
```

</details>

## V2-P1-083
기준 G019 · 3GPP TS 24.501 V18.12.0 · 4.6.2.1 · PDF 98쪽(인쇄 97쪽)

원문: The configured NSSAI and the rejected NSSAI may be changed during the registration procedure or the generic UE configuration update procedure.

질문: configured NSSAI와 rejected NSSAI의 변경 절차를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "may",
  "polarity": "positive",
  "actor": "configured NSSAI and rejected NSSAI",
  "condition": "during the registration procedure or the generic UE configuration update procedure",
  "action": "be changed",
  "exception": "",
  "gold_summary_ko": "configured NSSAI와 rejected NSSAI는 registration procedure 또는 generic UE configuration update procedure 중 변경될 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

configured NSSAI와 rejected NSSAI는 등록 절차 또는 일반 UE 구성 업데이트 절차 동안 변경하도록 허용된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 124 501 V18.12.0 (2025-10)973GPP TS 24.501 version 18.12.0 Release 18
NOTE 3: In roaming scenarios, when the UE is compliant with earlier versions of the specification or when the 
serving network does not provide a mapped S-NSSAI for one or more S-NSSAIs in the allowed NSSAI 
or configured NSSAI, the UE can omit a mapped S-NSSAI for one or more S-NSSAIs in requested 
NSSAI. 
The set of network slice(s) for a UE can be changed at any time while the UE is registered to a PLMN or SNPN, and the 
change may be initiated by the network or the UE. In this case, the allowed NSSAI and associated registration area may 
be changed during the registration procedure or the generic UE configuration update procedure. 
[대상 문장]
. The default configured NSSAI may be changed by sending a UE parameters update transparent container to 
the UE during the NAS transport procedure. The pending NSSAI may be changed during the registration procedure. In 
addition, using the generic UE configuration update procedure, the network may trigger the registration procedure in 
order to update the allowed NSSAI. 
The UE in NB-N1 mode does not include the requested NSSAI during the registration procedure if the 5GS registration 
type IE indicates "mobility registration updating", procedure is not initiated to change the slice(s) that the UE is 
currently registered to, and the UE is still in the current registration area. 
The AMF does not include the allowed NSSAI during a registration procedure with the 5GS registration type IE 
indicating "mobility registration updating" for the UE in NB-N1 mode, except if the allowed NSSAI has changed for 
the UE. 
The UE does not include th
```

</details>

## V2-P1-084
기준 G037 · 3GPP TS 23.501 V18.12.0 · 4.2.5 · PDF 52쪽(인쇄 51쪽)

원문: Each NF Service Consumer accessing the UDR, via Nudr, shall be able to add, modify, update or delete only the data it is authorised to change.

질문: Nudr를 통해 UDR에 접근하는 NF Service Consumer의 데이터 변경 범위를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall",
  "polarity": "positive",
  "actor": "each NF Service Consumer accessing the UDR via Nudr",
  "condition": "when accessing the UDR via Nudr",
  "action": "add, modify, update, or delete data",
  "exception": "only data that the NF Service Consumer is authorized to change",
  "gold_summary_ko": "각 NF Service Consumer는 자신에게 변경 권한이 있는 데이터만 추가·수정·갱신·삭제해야 한다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

Nudr를 통해 UDR에 접근하는 각 NF Service Consumer는 자신이 변경하도록 권한을 부여받은 데이터만 추가, 수정, 갱신 또는 삭제할 수 있는 기술적 가능성이 있어야 한다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 123 501 V18.12.0 (2026-01)513GPP TS 23.501 version 18.12.0 Release 18
NOTE 4: The UDR deployed in each PLMN can store application data for roaming subscribers. 
Subscription Data
Policy Data
Structured Data
for exposure
Application Data
UDR
UDM
PCF
NEF
Data Access Provider
Nudr
N35
N37
N36
 
Figure 4.2.5-2: Data Storage Architecture 
NOTE 5: There can be multiple UDRs deployed in the network, each of which can accommodate different data sets 
or subsets, (e.g. subscription data, subscription policy data, data for exposure, application data) and/or 
serve different sets of NFs. Deployments where a UDR serves a single NF and stores its data and, thus, 
can be integrated with this NF, can be possible. 
NOTE 6: The internal structure of the UDR in figure 4.2.5-2 is shown for information only. 
The Nudr interface is defined for the network functions (i.e. NF Service Consumers), such as UDM, PCF and NEF, to 
access a particular set of the data stored and to read, update (including add, modify), delete and subscribe to notification 
of relevant data changes in the UDR. 

[대상 문장]
. This authorisation shall be performed by the UDR on a per data set and NF service consumer 
basis and potentially on a per UE, subscription granularity. 
The following data in the UDR sets exposed via Nudr to the respective NF service consumer and stored shall be 
standardized: 
- Subscription Data, 
- Policy Data, 
- Structured Data for exposure, 
- Application data: Packet Flow Descriptions (PFDs) for application detection and AF request information for 
multiple UEs, as defined in clause 5.6.7. 
The service based Nudr interface defines the content and format/encoding of the 3GPP defined information elements 
exposed by the data sets. 
In addition, it shall be possible to access operator specific data sets by the NF Service Consumers from the UDR as well 
as operator specific data for each data set. 
NOTE 7: The content and format/encoding of operator specific data and operator specific data sets are not subject 
to standardization.
```

</details>

## V2-P1-085
기준 G012 · 3GPP TS 23.501 V18.12.0 · 4.4.8.3 · PDF 92쪽(인쇄 91쪽)

원문: The network instance for the N6 interface (clause 5.6.12) may be indicated by the SMF to the UPF for a given PDU Session during PDU Session establishment procedure.

질문: PDU Session establishment 중 N6 interface의 network instance를 UPF에 전달하는 방식을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "may",
  "polarity": "positive",
  "actor": "SMF",
  "condition": "for a given PDU Session during PDU Session establishment",
  "action": "indicate the N6-interface network instance to the UPF",
  "exception": "",
  "gold_summary_ko": "SMF는 해당 PDU Session의 N6-interface network instance를 UPF에 표시할 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

PDU Session establishment 시 SMF는 선택된 UPF에 N6 interface에 대응하는 network instance 정보를 전달해야 한다. 이를 통해 UPF는 해당 PDU Session의 N6 측 연결을 올바른 네트워크 인스턴스에 연계할 수 있다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
clause 5.27. The NEF exposes 5GS capability to support Time Synchronization 
service as described in clause 5.27.1.8. TSCTSF controls the DS-TT(s) and NW-TT for the (g)PTP based time 
synchronization service. In addition, TSCTSF supports TSC assistance container related functionalities. 
 
 
AMF PCF 
Device side 
 
(R)AN UPF
N7
N3
N2 N4
N1 
AF
SMFN11
N9 
N8
UDM
N10
UE DS -TTEnd Station
Device
TSCTSF N 33 
U -plane
NW -TT
N84
N52 
DN 
NEF 
N30
N85N87
 
Figure 4.4.8.3-1: Architecture to enable Time Sensitive Communication and Time Synchronization 
services 
NOTE 1: If the AF is considered to be trusted by the operator, the AF could interact directly with TSCTSF, the 
connection between AF and TSCTSF is not depicted in the architecture diagram for brevity. 
UPF/NW-TT distributes the (g)PTP messages as described in clause 5.27.1. 
When the UPF supports one or more NW-TT(s), there is one-to-one association between an NW-TT and the network 
instance or between an NW-TT and network instance together with DNN/S-NSSAI in the UPF. When there are multiple 
network instances within a UPF, each network instance is considered logically separate. 
[대상 문장]
. UPF allocates resources based on the Network Instance and S-NSSAI and it is supported 
according to TS 29.244 [65]. DNN/S-NSSAI may be indicated by the SMF together with the network instance to the 
UPF for a given PDU Session during PDU Session establishment procedure. 
NOTE 2: The same NW-TT is used for all PDU Sessions in the UPF for the given DNN/S-NSSAI; the NW-TT is 
unique per DNN/S-NSSAI. This ensures that the UPF selects an N4 session associated with the correct 
TSCTSF when the NW-TT initiates an UMIC or PMIC. At any given time, the NW-TT is associated with 
a single TSCTSF. 
4.4.8.4 Architecture to support IETF Deterministic Networking 
The 5G System is integrated with the Deterministic Network as defined in IETF RFC 8655 [150] as a logical DetNet 
transit router, see Figure 4.4.8.4-1. The TSCTSF performs mapping in the control plane between the 5GS internal 
functions and the DetNet controller. 5G System specific procedure
```

</details>

## V2-P1-086
기준 G002 · 3GPP TS 23.501 V18.12.0 · 4.2.16 · PDF 75쪽(인쇄 74쪽)

원문: Not all events can be subscribed to UPF directly.

질문: event를 UPF에 직접 subscribe하는 기능의 적용 범위를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "can",
  "polarity": "negative",
  "actor": "events",
  "condition": "for direct subscription to the UPF",
  "action": "be subscribed to the UPF directly",
  "exception": "not all events support direct UPF subscription",
  "gold_summary_ko": "모든 event를 UPF에 직접 subscribe할 수 있는 것은 아니며, 일부 event에는 그 기능이 불가능하다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

모든 이벤트가 UPF에 직접 구독될 수 있는 것은 아니다. 즉, UPF에 직접 subscribe하는 기능은 일부 이벤트에만 기술적으로 가능하다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 123 501 V18.12.0 (2026-01)743GPP TS 23.501 version 18.12.0 Release 18
 
Swa’ 
UE
AUSF
WLAN Access
Nausf
 
SNPN CH
NSWOF
Swd 
Nudm 
UDM
Nnssaaf 
NSSAAF AAA Proxy
AAA Server
Swd 
 
Figure 4.2.15-4b: Service based reference architecture to support authentication for Non-seamless 
WLAN offload using credentials from Credentials Holder using AAA Server via 5GC 
4.2.16 Architecture to support User  Plane Information Exposure via a 
service-based interface 
As depicted in Figure 4.2.16-1, the 5G System architecture allows user plane information exposure to some NFs via 
service-based interface in UPF. 
UPF
(Exposure Service)
SMF NWDAF NEF/AF TSNAF/TSCTSF
 
Figure 4.2.16-1: Architecture to support User Plane Information Exposure via a service-based 
interface 
NOTE 1: In this Release of the specification, only NWDAF/DCCF/MFAF, NEF/AF and TSNAF/TSCTSF are 
considered as the receiver of the UPF event notifications. 
NOTE 2: UPF information exposure is not restricted to SBI interface, i.e. reporting via PFCP over N4 to SMF is 
still applicable. 

[대상 문장]
. The details and constraints for the subscription to UPF event exposure 
service (i.e. direct vs. indirect) and the information exposed to certain NFs by UPF, as well as the information contained 
in the event notifications, are defined in clause 5.2.26.2 of TS 23.502 [3] and clause 5.8.2.17. 
4.2.17 Architecture for Ranging based services and Sidelink Positioning 
The architecture for Ranging based services and Sidelink Positioning is defined in TS 23.586 [180]. 
```

</details>
