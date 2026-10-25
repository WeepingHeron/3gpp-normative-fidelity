# pass1 검토 자료 216–255

원문·정답 참고 자료이며 판정은 별도 JSONL 사본에 기록한다.

## V2-P1-216
기준 G015 · 3GPP TS 24.501 V18.12.0 · 4.6.1 · PDF 95쪽(인쇄 94쪽)

원문: In addition, the HPLMN may configure a UE with a single default configured NSSAI and consider the default configured NSSAI as valid in a PLMN for which the UE has neither a configured NSSAI nor an allowed NSSAI.

질문: UE에 configured NSSAI와 allowed NSSAI가 모두 없는 PLMN에서 HPLMN의 default configured NSSAI 처리를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "may",
  "polarity": "positive",
  "actor": "HPLMN",
  "condition": "in a PLMN for which the UE has neither a configured NSSAI nor an allowed NSSAI",
  "action": "configure the UE with one default configured NSSAI and consider it valid in that PLMN",
  "exception": "a single default configured NSSAI",
  "gold_summary_ko": "HPLMN은 UE에 하나의 default configured NSSAI를 구성하고 이를 해당 PLMN에서 유효한 것으로 간주할 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

HPLMN은 UE에 단일 default configured NSSAI를 구성하고, UE에 configured NSSAI와 allowed NSSAI가 모두 없는 PLMN에서 그 default configured NSSAI를 유효한 것으로 간주하도록 허용된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 124 501 V18.12.0 (2025-10)943GPP TS 24.501 version 18.12.0 Release 18
g) on-demand S-NSSAIs; and 
h) on-demand NSSAI. 
In roaming scenarios, rejected NSSAI for the current PLMN or SNPN, rejected NSSAI for the current registration area, 
rejected NSSAI for the maximum number of UEs reached, or partially rejected NSSAI includes one or more S-NSSAIs 
for the current PLMN and also contains a set of mapped S-NSSAI(s). An S-NSSAI included in the rejected NSSAI for 
the failed or revoked NSSAA is an HPLMN S-NSSAI. 
In case of a PLMN, a serving PLMN may configure a UE with: 
a) the configured NSSAI per PLMN; 
b) NSSRG information if the UE has indicated that it supports the subscription-based restrictions to simultaneous 
registration of network slices feature; 
c) on-demand NSSAI if the UE has indicated it supports the network slice usage control feature; 
d) S-NSSAI time validity information if the UE has indicated that it supports S-NSSAI time validity information; 
and 
e) S-NSSAI location validity information if the UE has indicated that it supports S-NSSAI location validity 
information. 

[대상 문장]
. The 
support for NSSRG information by the UE and the network, respectively, is optional. 
NOTE 0: In this version of the specification, the network slice usage control feature is not supported in roaming 
scenarios. 
NOTE 1: The value(s) used in the default configured NSSAI are expected to be commonly decided by all roaming 
partners, e.g., values standardized by 3GPP or other bodies. 
In case of an SNPN, the SNPN may configure a UE which is neither registering nor registered for onboarding services 
in SNPN with: 
a) a configured NSSAI applicable to the SNPN; 
b) NSSRG information if the UE has indicated that it supports the subscription-based restrictions to simultaneous 
registration of network slices feature; 
c) S-NSSAI time validity information if the UE has indicated that it supports S-NSSAI time validity information; 
d) on-demand NSSAI if the UE has indicated it supports the network slice usage control feature; and 
e) S-NSSA
```

</details>

## V2-P1-217
기준 G029 · 3GPP TS 23.501 V18.12.0 · 5.18.4 · PDF 334쪽(인쇄 333쪽)

원문: The network should not move the UE to another available PLMN/SNPN, e.g. by handover, as long as the selected PLMN/SNPN is available to serve the UE's location.

질문: 선택된 PLMN 또는 SNPN이 UE 위치에서 계속 서비스를 제공하는 동안 다른 network로 이동시키는 정책을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should_not",
  "polarity": "negative",
  "actor": "network",
  "condition": "as long as the selected PLMN or SNPN remains available at the UE location",
  "action": "move the UE to another available PLMN or SNPN, including by handover",
  "exception": "",
  "gold_summary_ko": "선택된 PLMN 또는 SNPN이 계속 서비스 가능하면 network는 UE를 다른 PLMN 또는 SNPN으로 이동시키지 않는 것이 권고된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

네트워크는 선택된 PLMN/SNPN이 UE의 위치에서 계속 서비스를 제공하는 동안에는 UE를 다른 사용 가능한 PLMN/SNPN으로 이동시키지 않는 것이 권고된다. 예를 들어 핸드오버를 통한 이동도 포함된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
red NG-RAN shall in the broadcast system information include the PLMN-IDs concerning available 
core network operators in the shared network. 
When a UE performs an Initial Registration to a network, one of available PLMNs shall be selected to serve the UE. UE 
uses all the received broadcast PLMN-IDs in its PLMN (re)selection processes which is specified in TS 23.122 [17]. 
UE shall inform the NG-RAN of the selected PLMN so that the NG-RAN can route correctly. The NG-RAN shall 
inform the core network of the selected PLMN. 
As per any network, after Initial Registration to the shared network and while remaining served by the shared network, 
the network selection procedures specified in TS 23.122 [17] may cause the UE to perform a reselection of another 
available PLMN. 
UE uses all of the received broadcast PLMN-IDs in its cell and PLMN (re)selection processes. 
5.18.4 Network selection by the network 
The NG-RAN uses the selected PLMN/SNPN (provided by the UE at RRC establishment, or, provided by the 
AMF/source NG-RAN at N2/Xn handover) to select target cells for future handovers (and radio resources in general) 
appropriately. 
[대상 문장]
. 
In the case of handover or network controlled release to a PLMN in a shared network: 
- When multiple PLMN IDs are broadcasted in a cell sel ected by NG-RAN, NG-RAN shall select a target PLMN, 
taking into account the prioritized list of PLMN IDs provided via Mobility Restriction List from AMF. 
- For Xn based HO procedure, Source NG-RAN indicates the selected PLMN ID to the target NG-RAN, see 
TS 38.300 [27]. 
- For N2 based HO procedure, the NG-RAN indicates a selected PLMN ID to the AMF as part of the TAI sent in 
the HO required message. Source AMF uses the TAI information supplied by the source NG-RAN to select the 
target AMF/MME. The source AMF should forward the selected PLMN ID to the target AMF/MME. The target 
AMF/MME indicates the selected PLMN ID to the target NG-RAN/eNB so that the target NG-RAN/eNB can 
select target cells for future handover appropriately. 
- For RRC connection release with redirection to E-UTRAN proc
```

</details>

## V2-P1-218
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

모든 event가 UPF에 직접 subscribe될 수 있는 것은 아니다. 즉, event의 UPF 직접 subscribe는 일부 event에 대해서만 기술적으로 가능하다.

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

## V2-P1-219
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

UE가 Registration procedure 동안 MICO mode 선호를 표시하지 않으면, AMF는 해당 UE에 대해 MICO mode를 활성화해서는 안 된다.

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

## V2-P1-220
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

secure exchange of NAS messages가 설정된 뒤에는 UE의 receiving 5GMM entity는 NAS에 의해 성공적으로 integrity checked된 경우가 아니면 어떤 NAS signalling messages도 처리해서는 안 된다.

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

## V2-P1-221
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

allowed NSSAI(s)는 부속서 C에 명시된 방식에 따라 ME의 비휘발성 메모리에 저장하는 것이 권고된다.

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

## V2-P1-222
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

## V2-P1-223
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

ngKSI는 UE와 네트워크가 이미 보유한 5G NAS 보안 컨텍스트를 식별하는 키 세트 식별자이며, 이 값이 가리키는 컨텍스트가 유효하면 새 인증 절차 없이 그 보안 컨텍스트를 재사용할 수 있다. 즉, 동일한 5G NAS 보안 컨텍스트를 계속 사용할 수 있는 상황을 나타내는 식별자이다.

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

## V2-P1-224
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

E-UTRAN connected to EPC와 상호동작하기 위해, S1 mode와 N1 mode를 모두 지원하는 UE는 단일 등록 모드 또는 이중 등록 모드로 동작할 수 있다.

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

## V2-P1-225
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

Non-Allowed Area에 있는 UE의 Registration Area는 UE의 Non-Allowed Area에 속하는 TA들의 집합으로 구성하는 것이 권고된다. 이는 UE가 Non-Allowed Area에 있을 때 적용된다.

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

## V2-P1-226
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

secure NAS 메시지 교환이 설정된 뒤, UE의 수신 5GMM 엔티티는 NAS에 의해 성공적으로 무결성 검사가 된 경우를 제외하고는 어떤 NAS 시그널링 메시지도 처리해서는 안 된다.

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

## V2-P1-227
기준 G044 · 3GPP TS 23.501 V18.12.0 · 5.3.4.4 · PDF 114쪽(인쇄 113쪽)

원문: Subscriptions targeted to Any UE shall not be moved to another AMF due to UE mobility.

질문: Any UE를 대상으로 하는 subscription을 UE mobility 때문에 다른 AMF로 이동하는 정책을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall_not",
  "polarity": "negative",
  "actor": "subscriptions targeted to Any UE",
  "condition": "due to UE mobility",
  "action": "be moved to another AMF",
  "exception": "",
  "gold_summary_ko": "Any UE 대상 subscription은 UE mobility를 이유로 다른 AMF로 이동되어서는 안 된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

UE 이동성 때문에 Any UE를 대상으로 하는 subscription을 다른 AMF로 이동해서는 안 된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
resence in the Area Of 
Interest, the AMF notifies the UE presence in the Area Of Interest and the new UE location to the subscribed NF 
service consumer. 
If the Area Of Interest in the subscription to the UE mobility event notification includes "RAN timing synchronization 
status change event" indicator as described in Table 5.2.2.3.1-1 of TS 23.502 [3] and the registration request from the 
UE includes a UE 5GMM Core Network Capability with an indication for "support for network reconnection due to 
RAN timing synchronization status change " as described in clause 5.4.4a, the AMF reports the UE presence in Area of 
Interest based on the most recent N2 connection as described in Annex D of TS 23.502 [3]. 
If the Area Of Interest in the subscription to the UE mobility event notification includes "Adjust AoI based on RA" 
indicator as described in Table 5.2.2.3.1-1 in TS 23.502 [3], the AMF reports the UE presence in Area of Interest based 
on the most recent N2 connection as described in Annex D in TS 23.502 [3]. 
When the AMF is changed, the subscription of mobility event for a UE or group of UEs is transferred from the old 
AMF. 
[대상 문장]
. The new AMF may 
decide not to notify the SMF with the current status related to the subscription of mobility event if the new AMF 
determines that, based on MM Context of the UE, the event is reported by the old AMF. 
In the network deployment where a UE may leave or enter the Area Of Interest without any notification to the 5GC in 
CM-CONNECTED state (i.e. in the case that RRC_INACTIVE state applies to the NG-RAN), the AMF may initiate 
the NG-RAN location reporting as described in clause 5.4.7 or N2 Notification as described in clause 4.8.3 of 
TS 23.502 [3] to track the UE presence in the Area Of Interest. 
The AMF may provide UE mobility event reporting to PCF, using Policy Control Request Triggers defined in 
TS 23.503 [45]. 
5.3.5 Triggers for network analytics 
Triggers for the AMF to request for or subscribe to the analytics information from the NWDAF are internal logic in the 
AMF and may include for example: 
- UE access an
```

</details>

## V2-P1-228
기준 G015 · 3GPP TS 24.501 V18.12.0 · 4.6.1 · PDF 95쪽(인쇄 94쪽)

원문: In addition, the HPLMN may configure a UE with a single default configured NSSAI and consider the default configured NSSAI as valid in a PLMN for which the UE has neither a configured NSSAI nor an allowed NSSAI.

질문: UE에 configured NSSAI와 allowed NSSAI가 모두 없는 PLMN에서 HPLMN의 default configured NSSAI 처리를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "may",
  "polarity": "positive",
  "actor": "HPLMN",
  "condition": "in a PLMN for which the UE has neither a configured NSSAI nor an allowed NSSAI",
  "action": "configure the UE with one default configured NSSAI and consider it valid in that PLMN",
  "exception": "a single default configured NSSAI",
  "gold_summary_ko": "HPLMN은 UE에 하나의 default configured NSSAI를 구성하고 이를 해당 PLMN에서 유효한 것으로 간주할 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

또한 HPLMN은 UE에 단일 default configured NSSAI를 구성하도록 허용된다. 그리고 UE에 configured NSSAI도 allowed NSSAI도 없는 PLMN에서 그 default configured NSSAI를 유효한 것으로 간주하도록 허용된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 124 501 V18.12.0 (2025-10)943GPP TS 24.501 version 18.12.0 Release 18
g) on-demand S-NSSAIs; and 
h) on-demand NSSAI. 
In roaming scenarios, rejected NSSAI for the current PLMN or SNPN, rejected NSSAI for the current registration area, 
rejected NSSAI for the maximum number of UEs reached, or partially rejected NSSAI includes one or more S-NSSAIs 
for the current PLMN and also contains a set of mapped S-NSSAI(s). An S-NSSAI included in the rejected NSSAI for 
the failed or revoked NSSAA is an HPLMN S-NSSAI. 
In case of a PLMN, a serving PLMN may configure a UE with: 
a) the configured NSSAI per PLMN; 
b) NSSRG information if the UE has indicated that it supports the subscription-based restrictions to simultaneous 
registration of network slices feature; 
c) on-demand NSSAI if the UE has indicated it supports the network slice usage control feature; 
d) S-NSSAI time validity information if the UE has indicated that it supports S-NSSAI time validity information; 
and 
e) S-NSSAI location validity information if the UE has indicated that it supports S-NSSAI location validity 
information. 

[대상 문장]
. The 
support for NSSRG information by the UE and the network, respectively, is optional. 
NOTE 0: In this version of the specification, the network slice usage control feature is not supported in roaming 
scenarios. 
NOTE 1: The value(s) used in the default configured NSSAI are expected to be commonly decided by all roaming 
partners, e.g., values standardized by 3GPP or other bodies. 
In case of an SNPN, the SNPN may configure a UE which is neither registering nor registered for onboarding services 
in SNPN with: 
a) a configured NSSAI applicable to the SNPN; 
b) NSSRG information if the UE has indicated that it supports the subscription-based restrictions to simultaneous 
registration of network slices feature; 
c) S-NSSAI time validity information if the UE has indicated that it supports S-NSSAI time validity information; 
d) on-demand NSSAI if the UE has indicated it supports the network slice usage control feature; and 
e) S-NSSA
```

</details>

## V2-P1-229
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

AMF가 Unavailability configuration IE를 제공하지 않거나, AMF가 Unavailability configuration IE의 EUPR 비트 값을 "UE needs to report end of unavailability period"로 설정한 경우, UE는 unavailability period duration이 끝났을 때 mobility registration update를 위한 registration procedure를 트리거하는 것이 권고된다.

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

## V2-P1-230
기준 G016 · 3GPP TS 24.501 V18.12.0 · 4.4.2.1.1 · PDF 53쪽(인쇄 52쪽)

원문: A new 5G NAS security context may also be created during an N1 mode to N1 mode handover.

질문: N1 mode 간 handover 중 새로운 5G NAS security context의 생성 시점을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "may",
  "polarity": "positive",
  "actor": "new 5G NAS security context",
  "condition": "during an N1 mode to N1 mode handover",
  "action": "be created",
  "exception": "",
  "gold_summary_ko": "N1 mode에서 N1 mode로 handover하는 동안 새로운 5G NAS security context가 생성될 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

N1 mode 간 handover에서는 새로운 5G NAS security context가 handover 절차 중에 생성되는 것이 아니라, handover가 완료된 뒤 새 AMF에서 NAS 보안 절차를 다시 설정할 때 생성된다. 즉, 새로운 NAS 보안 컨텍스트는 대상 측으로의 이동이 끝난 후에 마련된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
e. UL NAS TRANSPORT message and the DL NAS TRANSPORT message). 
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
Before security can be activated, the AMF and the UE need to establish a 5G NAS security context. Usually, the 5G 
NAS security context is created as the result of a primary authentication and key agreement procedure between the 
AMF and the UE. 
[대상 문장]
. 
Alternatively, during inter-system change from S1 mode to N1 mode, the AMF not supporting interworking without 
```

</details>

## V2-P1-231
기준 G025 · 3GPP TS 24.501 V18.12.0 · 5.3.6 · PDF 193쪽(인쇄 192쪽)

원문: To enable an emergency call back, the UE should wait for a UE implementation-specific duration of time before requesting the use of MICO mode after the completion of the emergency services.

질문: emergency service 완료 후 emergency callback을 지원하기 위해 UE가 MICO mode를 요청하기 전 취할 동작을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should",
  "polarity": "positive",
  "actor": "UE",
  "condition": "after completion of emergency services and before requesting MICO mode, to enable an emergency callback",
  "action": "wait for a UE-implementation-specific duration",
  "exception": "",
  "gold_summary_ko": "UE는 emergency service 완료 후 MICO mode를 요청하기 전에 구현별 시간 동안 기다리는 것이 권고된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

긴급 서비스가 완료된 후 긴급 콜백을 가능하게 하려면, UE는 MICO 모드 사용을 요청하기 전에 UE 구현체별 지속 시간 동안 기다리는 것이 권고된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
imers T3512, 
T3346, T3447, T3448, T3396, T3526, T3584, T3585, T3587 any back-off timers, T3245, T3247, any slice 
deregistration inactivity timers, the timer T controlling the periodic search for HPLMN or EHPLMN or higher 
prioritized PLMNs (see 3GPP TS 23.122 [5]) and the timer T
SENSE controlling the periodic search for PLMNs satisfying 
the operator controlled signal level threshold (see 3GPP TS 23.122 [5]). 
NOTE 2: When MICO mode is activated and if the UE is also registered over the non-3GPP access, the AMF will 
not send a NOTIFICATION message with access type indicating 3GPP access over the non-3GPP access 
for PDU sessions associated with 3GPP access. 
The UE may deactivate MICO mode and activate the AS layer at any time. Upon deactivating MICO mode, the UE 
may initiate 5GMM procedures (e.g., for the transfer of mobile originated signalling or user data). 
When an emergency PDU session is successfully established after the MICO mode was enabled, the UE and the AMF 
shall locally disable MICO mode. The UE and the AMF shall not enable MICO mode until the AMF accepts the use of 
MICO mode in the next registration procedure. 
[대상 문장]
. 
If the AMF accepts the use of MICO mode and does not indicate "strictly periodic registration timer supported" in the 
MICO indication IE to the UE, the AMF starts the implicit de-registration timer for 3GPP access when entering 
5GMM-IDLE mode for 3GPP access. If AMF accepts the use of MICO mode and indicates "strictly periodic 
registration timer supported" in the MICO indication IE to the UE, AMF shall start the strictly periodic monitoring 
timer with T3512 value indicated in the T3512 value IE after the registration procedure is completed. The AMF shall 
neither stop nor reset the strictly periodic monitoring timer when the NAS signalling connection is established or 
released for the UE. If the strictly periodic monitoring timer expires when NAS signalling connection is established for 
the UE, AMF shall restart the strictly periodic monitoring timer with the T3512 value, otherwise AMF shall start the 
implicit de-registration 
```

</details>

## V2-P1-232
기준 G025 · 3GPP TS 24.501 V18.12.0 · 5.3.6 · PDF 193쪽(인쇄 192쪽)

원문: To enable an emergency call back, the UE should wait for a UE implementation-specific duration of time before requesting the use of MICO mode after the completion of the emergency services.

질문: emergency service 완료 후 emergency callback을 지원하기 위해 UE가 MICO mode를 요청하기 전 취할 동작을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should",
  "polarity": "positive",
  "actor": "UE",
  "condition": "after completion of emergency services and before requesting MICO mode, to enable an emergency callback",
  "action": "wait for a UE-implementation-specific duration",
  "exception": "",
  "gold_summary_ko": "UE는 emergency service 완료 후 MICO mode를 요청하기 전에 구현별 시간 동안 기다리는 것이 권고된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

긴급 서비스가 완료된 후, UE는 MICO 모드 사용을 요청하기 전에 UE 구현에 따라 정해지는 기간 동안 기다리는 것이 권고된다. 이는 emergency call back을 가능하게 하기 위한 것이다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
imers T3512, 
T3346, T3447, T3448, T3396, T3526, T3584, T3585, T3587 any back-off timers, T3245, T3247, any slice 
deregistration inactivity timers, the timer T controlling the periodic search for HPLMN or EHPLMN or higher 
prioritized PLMNs (see 3GPP TS 23.122 [5]) and the timer T
SENSE controlling the periodic search for PLMNs satisfying 
the operator controlled signal level threshold (see 3GPP TS 23.122 [5]). 
NOTE 2: When MICO mode is activated and if the UE is also registered over the non-3GPP access, the AMF will 
not send a NOTIFICATION message with access type indicating 3GPP access over the non-3GPP access 
for PDU sessions associated with 3GPP access. 
The UE may deactivate MICO mode and activate the AS layer at any time. Upon deactivating MICO mode, the UE 
may initiate 5GMM procedures (e.g., for the transfer of mobile originated signalling or user data). 
When an emergency PDU session is successfully established after the MICO mode was enabled, the UE and the AMF 
shall locally disable MICO mode. The UE and the AMF shall not enable MICO mode until the AMF accepts the use of 
MICO mode in the next registration procedure. 
[대상 문장]
. 
If the AMF accepts the use of MICO mode and does not indicate "strictly periodic registration timer supported" in the 
MICO indication IE to the UE, the AMF starts the implicit de-registration timer for 3GPP access when entering 
5GMM-IDLE mode for 3GPP access. If AMF accepts the use of MICO mode and indicates "strictly periodic 
registration timer supported" in the MICO indication IE to the UE, AMF shall start the strictly periodic monitoring 
timer with T3512 value indicated in the T3512 value IE after the registration procedure is completed. The AMF shall 
neither stop nor reset the strictly periodic monitoring timer when the NAS signalling connection is established or 
released for the UE. If the strictly periodic monitoring timer expires when NAS signalling connection is established for 
the UE, AMF shall restart the strictly periodic monitoring timer with the T3512 value, otherwise AMF shall start the 
implicit de-registration 
```

</details>

## V2-P1-233
기준 G044 · 3GPP TS 23.501 V18.12.0 · 5.3.4.4 · PDF 114쪽(인쇄 113쪽)

원문: Subscriptions targeted to Any UE shall not be moved to another AMF due to UE mobility.

질문: Any UE를 대상으로 하는 subscription을 UE mobility 때문에 다른 AMF로 이동하는 정책을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall_not",
  "polarity": "negative",
  "actor": "subscriptions targeted to Any UE",
  "condition": "due to UE mobility",
  "action": "be moved to another AMF",
  "exception": "",
  "gold_summary_ko": "Any UE 대상 subscription은 UE mobility를 이유로 다른 AMF로 이동되어서는 안 된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

UE mobility 때문에 Any UE를 대상으로 하는 subscription을 다른 AMF로 이동해서는 안 된다. 이는 UE 이동성만을 이유로 해당 subscription을 다른 AMF로 옮기는 행위를 금지한다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
resence in the Area Of 
Interest, the AMF notifies the UE presence in the Area Of Interest and the new UE location to the subscribed NF 
service consumer. 
If the Area Of Interest in the subscription to the UE mobility event notification includes "RAN timing synchronization 
status change event" indicator as described in Table 5.2.2.3.1-1 of TS 23.502 [3] and the registration request from the 
UE includes a UE 5GMM Core Network Capability with an indication for "support for network reconnection due to 
RAN timing synchronization status change " as described in clause 5.4.4a, the AMF reports the UE presence in Area of 
Interest based on the most recent N2 connection as described in Annex D of TS 23.502 [3]. 
If the Area Of Interest in the subscription to the UE mobility event notification includes "Adjust AoI based on RA" 
indicator as described in Table 5.2.2.3.1-1 in TS 23.502 [3], the AMF reports the UE presence in Area of Interest based 
on the most recent N2 connection as described in Annex D in TS 23.502 [3]. 
When the AMF is changed, the subscription of mobility event for a UE or group of UEs is transferred from the old 
AMF. 
[대상 문장]
. The new AMF may 
decide not to notify the SMF with the current status related to the subscription of mobility event if the new AMF 
determines that, based on MM Context of the UE, the event is reported by the old AMF. 
In the network deployment where a UE may leave or enter the Area Of Interest without any notification to the 5GC in 
CM-CONNECTED state (i.e. in the case that RRC_INACTIVE state applies to the NG-RAN), the AMF may initiate 
the NG-RAN location reporting as described in clause 5.4.7 or N2 Notification as described in clause 4.8.3 of 
TS 23.502 [3] to track the UE presence in the Area Of Interest. 
The AMF may provide UE mobility event reporting to PCF, using Policy Control Request Triggers defined in 
TS 23.503 [45]. 
5.3.5 Triggers for network analytics 
Triggers for the AMF to request for or subscribe to the analytics information from the NWDAF are internal logic in the 
AMF and may include for example: 
- UE access an
```

</details>

## V2-P1-234
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

이 기능은 UPF가 생성하는 이벤트를 직접 구독해야 하는 경우에 적용되며, 주로 UPF와 관련된 이벤트 전달을 위해 사용된다. 즉, 다른 네트워크 기능을 거치지 않고 UPF 이벤트를 직접 수신하는 구성이 필요한 경우에 선택할 수 있다.

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

## V2-P1-235
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

AMF가 UE에 대한 NSAG Information을 받지 못한 경우, UE는 Network Slice 기반으로 셀 재선택이나 Random Access를 수행할 때 해당 정보를 이용한 특별한 최적화 없이 일반 절차로 동작해야 한다. 즉, NSAG Information이 없는 UE에 대해서는 slice 기반 선택을 전제로 한 추가 처리를 기대하지 않는 것으로 이해된다.

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

## V2-P1-236
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

모든 event가 UPF에 직접 subscribe될 수 있는 것은 아니다. 즉, UPF에 직접 subscribe하는 기능은 일부 event에만 적용된다.

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

## V2-P1-237
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

NG-RAN 노드는 N2 인터페이스 OVERLOAD START 메시지를 수신해 UAC를 시작하기로 결정한 경우, 해당 OVERLOAD START 메시지에 포함된 요청과 관련되고 이 NG-RAN 노드에 연결된 모든 AMF가 네트워크에 접근하는 UE에 대한 부하 제한을 요청할 때에만 그러한 절차를 시작하는 것이 권고된다.

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

## V2-P1-238
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

secure NAS message exchange가 설정된 뒤에는 UE가 수신한 NAS signalling message를 5GMM 절차에 따라 처리해야 한다. 다만 해당 메시지가 보안 NAS 보호가 적용된 상태로 수신되었는지, 그리고 현재 보안 컨텍스트와 일치하는지에 따라 처리 가능 여부가 달라진다.

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

## V2-P1-239
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

UE는 현재 TAI와 현재 셀의 CGI가 해당 multicast MBS session의 MBS service area에 속하지 않고, UE가 그 MBS service area에 대한 유효한 정보를 가진 경우 local MBS service를 위한 multicast MBS session join request를 하지 않는 것이 권고된다.

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

## V2-P1-240
기준 G010 · 3GPP TS 23.501 V18.12.0 · 4.2.3 · PDF 45쪽(인쇄 44쪽)

원문: However, each SMF may also have the capability to control both a local and a central UPF within a PDU Session.

질문: 하나의 PDU Session에서 SMF가 local UPF와 central UPF를 제어하는 구성을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "may",
  "polarity": "positive",
  "actor": "each SMF",
  "condition": "within a PDU Session",
  "action": "have the capability to control both a local and a central UPF within a PDU Session",
  "exception": "",
  "gold_summary_ko": "각 SMF가 하나의 PDU Session에서 local UPF와 central UPF를 모두 제어할 수 있는 능력을 갖추는 것은 선택 사항이다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

각 SMF는 하나의 PDU Session 내에서 local UPF와 central UPF를 모두 제어할 기술적 가능성이 있다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 [128]. 
NOTE 7: For clarity, the TSCTSF and its connections with ot her NFs, e.g. PCF, NEF, UDR are not depicted in the 
point-to-point and service-based architecture diagrams. For more information on TSC architecture refer to 
clause 4.4.8. 
NOTE 8: For exposure of the QoS monitoring information as specified in clause 5.8.2.18, exposure of data 
collected for analytics as specified in clause 5.2.26.2 of TS 23.502 [3] and exposure of the TSC 
management information as specified in clause 5.8.5.14, direct interaction between UPF and NFs can be 
supported via the Nupf interface (see clause 4.2.16). 
NOTE 9: For clarity, the EASDF and its connections with SMF is not depicted in the point-to-point and service-
based architecture diagrams. For more information on edge computing architecture refer to 
TS 23.548 [130]. 
Figure 4.2.3-3 depicts the non-roaming architecture for UEs concurrently accessing two (e.g. local and central) data 
networks using multiple PDU Sessions, using the reference point representation. This figure shows the architecture for 
multiple PDU Sessions where two SMFs are selected for the two different PDU Sessions. 
[대상 문장]
. 
```

</details>

## V2-P1-241
기준 G015 · 3GPP TS 24.501 V18.12.0 · 4.6.1 · PDF 95쪽(인쇄 94쪽)

원문: In addition, the HPLMN may configure a UE with a single default configured NSSAI and consider the default configured NSSAI as valid in a PLMN for which the UE has neither a configured NSSAI nor an allowed NSSAI.

질문: UE에 configured NSSAI와 allowed NSSAI가 모두 없는 PLMN에서 HPLMN의 default configured NSSAI 처리를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "may",
  "polarity": "positive",
  "actor": "HPLMN",
  "condition": "in a PLMN for which the UE has neither a configured NSSAI nor an allowed NSSAI",
  "action": "configure the UE with one default configured NSSAI and consider it valid in that PLMN",
  "exception": "a single default configured NSSAI",
  "gold_summary_ko": "HPLMN은 UE에 하나의 default configured NSSAI를 구성하고 이를 해당 PLMN에서 유효한 것으로 간주할 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

HPLMN은 UE에 단일 default configured NSSAI를 구성할 수 있으며, UE에 configured NSSAI와 allowed NSSAI가 모두 없는 PLMN에서 그 default configured NSSAI를 유효한 것으로 간주할 수 있다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 124 501 V18.12.0 (2025-10)943GPP TS 24.501 version 18.12.0 Release 18
g) on-demand S-NSSAIs; and 
h) on-demand NSSAI. 
In roaming scenarios, rejected NSSAI for the current PLMN or SNPN, rejected NSSAI for the current registration area, 
rejected NSSAI for the maximum number of UEs reached, or partially rejected NSSAI includes one or more S-NSSAIs 
for the current PLMN and also contains a set of mapped S-NSSAI(s). An S-NSSAI included in the rejected NSSAI for 
the failed or revoked NSSAA is an HPLMN S-NSSAI. 
In case of a PLMN, a serving PLMN may configure a UE with: 
a) the configured NSSAI per PLMN; 
b) NSSRG information if the UE has indicated that it supports the subscription-based restrictions to simultaneous 
registration of network slices feature; 
c) on-demand NSSAI if the UE has indicated it supports the network slice usage control feature; 
d) S-NSSAI time validity information if the UE has indicated that it supports S-NSSAI time validity information; 
and 
e) S-NSSAI location validity information if the UE has indicated that it supports S-NSSAI location validity 
information. 

[대상 문장]
. The 
support for NSSRG information by the UE and the network, respectively, is optional. 
NOTE 0: In this version of the specification, the network slice usage control feature is not supported in roaming 
scenarios. 
NOTE 1: The value(s) used in the default configured NSSAI are expected to be commonly decided by all roaming 
partners, e.g., values standardized by 3GPP or other bodies. 
In case of an SNPN, the SNPN may configure a UE which is neither registering nor registered for onboarding services 
in SNPN with: 
a) a configured NSSAI applicable to the SNPN; 
b) NSSRG information if the UE has indicated that it supports the subscription-based restrictions to simultaneous 
registration of network slices feature; 
c) S-NSSAI time validity information if the UE has indicated that it supports S-NSSAI time validity information; 
d) on-demand NSSAI if the UE has indicated it supports the network slice usage control feature; and 
e) S-NSSA
```

</details>

## V2-P1-242
기준 G028 · 3GPP TS 23.501 V18.12.0 · 5.4.11.4 · PDF 133쪽(인쇄 132쪽)

원문: The AMF should not reject the request or deregister the UE unless it has sufficiently accurate UE location information to determine that the UE is located in a geographical area where the PLMN is not allowed to operate.

질문: PLMN 운용 제한 지역과 관련된 UE 요청을 AMF가 처리할 때 필요한 위치정보 조건을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should_not",
  "polarity": "negative",
  "actor": "AMF",
  "condition": "when handling the request and the UE",
  "action": "reject the request or deregister the UE",
  "exception": "unless sufficiently accurate location information shows that the UE is in an area where the PLMN may not operate",
  "gold_summary_ko": "AMF는 UE가 PLMN 운용 금지 지역에 있다고 판단할 만큼 정확한 위치정보가 없는 한 요청을 reject하거나 UE를 deregister하지 않는 것이 권고된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

AMF는 UE의 요청을 거절하거나 UE를 등록 해제하지 않는 것이 권고된다. 다만 AMF가 UE가 PLMN이 운용할 수 없는 지리적 지역에 위치한다고 판단할 수 있을 만큼 충분히 정확한 UE 위치정보를 가지고 있는 경우에는 이 권고가 적용되지 않는다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
he regulatory requirements are met, the network may be configured to enforce that the selected 
PLMN is allowed to operate in the current UE location by verifying the UE location during Mobility Management and 
Session Management procedures. The UE that supports network verified UE location over NTN NR shall indicate this 
capability in UE 5GMM Core Network Capability and LPP as defined in TS 37.355 [191]. 
In this case, when the AMF receives a NGAP message containing User Location Information for a UE using NR 
satellite access, the AMF takes into account the capability of the UE in UE 5GMM Core Network Capability for the 
support by the UE of network verified UE location over NR NTN and may decide to verify the UE location. If the AMF 
determines based on the Selected PLMN ID and ULI (including Cell ID) received from the gNB that it is not allowed to 
operate at the present UE location the AMF should reject any NAS request with a suitable cause value. If the UE is 
already registered to the network when the AMF determines that it is not allowed to operate at the present UE location, 
the AMF may initiate deregistration of the UE. 
[대상 문장]
. 
NOTE 1: The area where the UE is allowed to operate can be determined based on the regulatory area where the 
PLMN is allowed to operate based on its licensing conditions. 
If the AMF, based on the ULI, is not able to determine the UE's location with sufficient accuracy to make a final 
decision or if the received ULI is not sufficiently reliable, the AMF takes into account the UE 5GMM Core Network 
Capability related to the UE support of network verified UE location over NR NTN and may proceed with the Mobility 
Management or Session Management procedure and may initiate UE location procedure after the Mobility Management 
or Session Management procedure is complete, as specified in clause 6.10.1 of TS 23.273 [87], to determine the UE 
location. 
NOTE 2: In order to ensure that the regulatory requirements are met, based on operator configuration, the AMF can 
prevent the UE from accessing certain services (e.g. services related with
```

</details>

## V2-P1-243
기준 G004 · 3GPP TS 24.501 V18.12.0 · 4.2 · PDF 49쪽(인쇄 48쪽)

원문: To this purpose, the 5GSM messages can be transmitted in an information element in the 5GMM transport messages.

질문: 5GSM message를 5GMM transport message로 전달하는 방식을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "can",
  "polarity": "positive",
  "actor": "5GSM messages",
  "condition": "for transmission via 5GMM transport messages",
  "action": "be transmitted in an information element of the 5GMM transport messages",
  "exception": "",
  "gold_summary_ko": "5GSM message는 5GMM transport message의 information element 안에서 전송될 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

5GSM 메시지는 5GMM transport message의 정보 요소 안에서 전송될 수 있다. 즉, 5GSM 메시지를 5GMM transport message로 전달하는 것이 허용된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
I container, UE policy 
container, SOR transparent container and UE parameters update information payload. 
Principles for the handing of 5GS security contexts and for the activation of ciphering and integrity protection, when a 
NAS signalling connection is established, are provided in subclause 4.4. 
For the support of the above functions, the following procedures are supplied within this specification: 
a) elementary procedures for 5GS mobility management in clause 5; and 
b) elementary procedures for 5GS session management in clause 6. 
Signalling procedures for the control of NAS security are described as part of the 5GMM common procedures in 
subclause 5.4. 
Complete NAS transactions consist of specific sequences of elementary procedures. Examples of such specific 
sequences can be found in 3GPP TS 23.502 [9]. 
The NAS for 5GS follows the protocol architecture model for layer 3 as described in 3GPP TS 24.007 [11]. 
4.2 Coordination between the protocols for 5GS mobility 
management and 5GS session management 
A 5GS session management (5GSM) message is piggybacked in specific 5GS mobility management (5GMM) transport 
messages. 
[대상 문장]
. In this case, the UE, the AMF and the SMF execute the 5GMM procedure and the 5GSM procedure in 
parallel. The success of the 5GMM procedure is not dependent on the success of the piggybacked 5GSM procedure. 
The UE can only initiate the 5GSM procedure when there is a 5GMM context established at the UE. 
During 5GMM procedures, the UE and the AMF shall suspend the transmission of 5GSM messages, except when: 
a) the 5GMM procedure is piggybacking 5GSM messages; or 
b) the UE is in 5GMM-CONNECTED mode and a service request procedure for re-establishing user-plane 
resources of PDU session(s) is initiated without including PDU session status IE or Allowed PDU session status 
IE. In this case, the UE and the AMF need not suspend the transmission of 5GSM messages related to other PDU 
session(s) than the one(s) for which the user- plane resources re-establishment is requested. 
If the UE determines to locally release the N1 NAS signalling c
```

</details>

## V2-P1-244
기준 G004 · 3GPP TS 24.501 V18.12.0 · 4.2 · PDF 49쪽(인쇄 48쪽)

원문: To this purpose, the 5GSM messages can be transmitted in an information element in the 5GMM transport messages.

질문: 5GSM message를 5GMM transport message로 전달하는 방식을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "can",
  "polarity": "positive",
  "actor": "5GSM messages",
  "condition": "for transmission via 5GMM transport messages",
  "action": "be transmitted in an information element of the 5GMM transport messages",
  "exception": "",
  "gold_summary_ko": "5GSM message는 5GMM transport message의 information element 안에서 전송될 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

5GSM 메시지는 5GMM transport messages의 정보 요소 안에 전송될 수 있다. 이는 5GMM transport messages를 통해 전송하는 경우에 적용되는 기술적 가능성을 나타낸다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
I container, UE policy 
container, SOR transparent container and UE parameters update information payload. 
Principles for the handing of 5GS security contexts and for the activation of ciphering and integrity protection, when a 
NAS signalling connection is established, are provided in subclause 4.4. 
For the support of the above functions, the following procedures are supplied within this specification: 
a) elementary procedures for 5GS mobility management in clause 5; and 
b) elementary procedures for 5GS session management in clause 6. 
Signalling procedures for the control of NAS security are described as part of the 5GMM common procedures in 
subclause 5.4. 
Complete NAS transactions consist of specific sequences of elementary procedures. Examples of such specific 
sequences can be found in 3GPP TS 23.502 [9]. 
The NAS for 5GS follows the protocol architecture model for layer 3 as described in 3GPP TS 24.007 [11]. 
4.2 Coordination between the protocols for 5GS mobility 
management and 5GS session management 
A 5GS session management (5GSM) message is piggybacked in specific 5GS mobility management (5GMM) transport 
messages. 
[대상 문장]
. In this case, the UE, the AMF and the SMF execute the 5GMM procedure and the 5GSM procedure in 
parallel. The success of the 5GMM procedure is not dependent on the success of the piggybacked 5GSM procedure. 
The UE can only initiate the 5GSM procedure when there is a 5GMM context established at the UE. 
During 5GMM procedures, the UE and the AMF shall suspend the transmission of 5GSM messages, except when: 
a) the 5GMM procedure is piggybacking 5GSM messages; or 
b) the UE is in 5GMM-CONNECTED mode and a service request procedure for re-establishing user-plane 
resources of PDU session(s) is initiated without including PDU session status IE or Allowed PDU session status 
IE. In this case, the UE and the AMF need not suspend the transmission of 5GSM messages related to other PDU 
session(s) than the one(s) for which the user- plane resources re-establishment is requested. 
If the UE determines to locally release the N1 NAS signalling c
```

</details>

## V2-P1-245
기준 G024 · 3GPP TS 24.501 V18.12.0 · 4.9.2 · PDF 133쪽(인쇄 132쪽)

원문: The UE should memorize the identity of the PLMNs or SNPNs where N1 mode capability for 3GPP access was disabled.

질문: 3GPP access의 N1 mode capability가 비활성화된 경우 UE가 기억할 network identity를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should",
  "polarity": "positive",
  "actor": "UE",
  "condition": "where N1 mode capability for 3GPP access was disabled",
  "action": "memorize the identity of the affected PLMNs or SNPNs",
  "exception": "",
  "gold_summary_ko": "UE는 N1 mode capability가 비활성화된 PLMN 또는 SNPN의 identity를 기억하는 것이 권고된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

UE는 3GPP access에 대한 N1 mode capability가 비활성화되었던 PLMN 또는 SNPN의 식별자를 기억하는 것이 권고된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 N1 mode capability again are UE implementation specific. 
The UE shall disable the N1 mode capability for 3GPP access if requested by the upper layers (e.g. see 
subclause U.2.2.6.4 in 3GPP TS 24.229 [14]). If the UE disabled the N1 mode capability for 3GPP access based on the 
request from the upper layers (e.g. see subclause U.2.2.6.4 in 3GPP TS 24.229 [14]), the criteria to re-enable the N1 
mode capability for 3GPP access after the completion of an emergency service are UE implementation specific. 
If the N1 mode capability for 3GPP access was disabled due to the UE initiated de-registration procedure for 3GPP 
access or for 3GPP access and non-3GPP access and the UE is operating in single-registration mode (see 
subclause 5.5.2.2.3), upon request of the upper layers to re-register for 5GS services over 3GPP access or the UE needs 
to come out of unavailability period and resume normal services, the UE shall enable the N1 mode capability for 3GPP 
access again. 
As an implementation option, the UE may start a timer for enabling the N1 mode capability for 3GPP access when the 
UE disables the N1 mode capability for 3GPP access. 
[대상 문장]
. On expiry of this timer: 
a) if the UE is in Iu mode or A/Gb mode and is in idle mode as specified in 3GPP TS 24.008 [13], the UE should 
enable the N1 mode capability for 3GPP access; 
b) if the UE is in Iu mode and a PS signalling connection exists, but no RR connection exists, the UE may abort the 
PS signalling connection before enabling the N1 mode capability for 3GPP access; 
c) if the UE is in S1 mode and is in EMM-IDLE mode as specified in 3GPP TS 24.301 [15], the UE should enable 
the N1 mode capability for 3GPP access; and 
d) If the UE is in Iu mode or A/Gb mode and an RR connection exists, the UE should delay enabling the N1 mode 
capability for 3GPP access until the RR connection is released. If the UE is in S1 mode and is in EMM-
CONNECTED mode as specified in 3GPP TS 24.301 [15], the UE should delay enabling the N1 mode capability 
for 3GPP access until the NAS signalling connection in S1 mode is released. 
When the UE 
```

</details>

## V2-P1-246
기준 G044 · 3GPP TS 23.501 V18.12.0 · 5.3.4.4 · PDF 114쪽(인쇄 113쪽)

원문: Subscriptions targeted to Any UE shall not be moved to another AMF due to UE mobility.

질문: Any UE를 대상으로 하는 subscription을 UE mobility 때문에 다른 AMF로 이동하는 정책을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall_not",
  "polarity": "negative",
  "actor": "subscriptions targeted to Any UE",
  "condition": "due to UE mobility",
  "action": "be moved to another AMF",
  "exception": "",
  "gold_summary_ko": "Any UE 대상 subscription은 UE mobility를 이유로 다른 AMF로 이동되어서는 안 된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

Any UE를 대상으로 하는 subscription은 UE mobility 때문에 다른 AMF로 이동해서는 안 된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
resence in the Area Of 
Interest, the AMF notifies the UE presence in the Area Of Interest and the new UE location to the subscribed NF 
service consumer. 
If the Area Of Interest in the subscription to the UE mobility event notification includes "RAN timing synchronization 
status change event" indicator as described in Table 5.2.2.3.1-1 of TS 23.502 [3] and the registration request from the 
UE includes a UE 5GMM Core Network Capability with an indication for "support for network reconnection due to 
RAN timing synchronization status change " as described in clause 5.4.4a, the AMF reports the UE presence in Area of 
Interest based on the most recent N2 connection as described in Annex D of TS 23.502 [3]. 
If the Area Of Interest in the subscription to the UE mobility event notification includes "Adjust AoI based on RA" 
indicator as described in Table 5.2.2.3.1-1 in TS 23.502 [3], the AMF reports the UE presence in Area of Interest based 
on the most recent N2 connection as described in Annex D in TS 23.502 [3]. 
When the AMF is changed, the subscription of mobility event for a UE or group of UEs is transferred from the old 
AMF. 
[대상 문장]
. The new AMF may 
decide not to notify the SMF with the current status related to the subscription of mobility event if the new AMF 
determines that, based on MM Context of the UE, the event is reported by the old AMF. 
In the network deployment where a UE may leave or enter the Area Of Interest without any notification to the 5GC in 
CM-CONNECTED state (i.e. in the case that RRC_INACTIVE state applies to the NG-RAN), the AMF may initiate 
the NG-RAN location reporting as described in clause 5.4.7 or N2 Notification as described in clause 4.8.3 of 
TS 23.502 [3] to track the UE presence in the Area Of Interest. 
The AMF may provide UE mobility event reporting to PCF, using Policy Control Request Triggers defined in 
TS 23.503 [45]. 
5.3.5 Triggers for network analytics 
Triggers for the AMF to request for or subscribe to the analytics information from the NWDAF are internal logic in the 
AMF and may include for example: 
- UE access an
```

</details>

## V2-P1-247
기준 G040 · 3GPP TS 24.501 V18.12.0 · 4.4.2.1.1 · PDF 54쪽(인쇄 53쪽)

원문: However, when the UE operating in dual-registration mode performs an initial registration procedure, it shall take into use a 5G NAS security context and follow the handling of this security context as described in the present specification.

질문: dual-registration mode UE가 initial registration을 수행할 때 5G NAS security context를 어떻게 처리하는지 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall",
  "polarity": "positive",
  "actor": "UE operating in dual-registration mode",
  "condition": "when performing an initial registration procedure",
  "action": "take a 5G NAS security context into use and handle it as described in the specification",
  "exception": "",
  "gold_summary_ko": "해당 UE는 5G NAS security context를 반드시 사용하기 시작하고 규격에 기술된 방식으로 처리해야 한다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

dual-registration mode로 동작하는 UE가 initial registration procedure를 수행할 때, 반드시 5G NAS security context를 사용하기 시작하고 이 security context의 처리는 본 규격에 설명된 대로 따라야 한다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
NAS message. 
In the present document, when the UE is required to delete an ngKSI, the UE shall set the ngKSI to the value "no key is 
available" and consider also the associated keys K
AMF or K'AMF, 5G NAS ciphering key and 5G NAS integrity key 
invalid (i.e. the 5G NAS security context associated with the ngKSI as no longer valid). In the initial registration 
procedure, when the key K
AUSF, is invalid, the UE shall delete the ngKSI. 
NOTE: In some specifications the term ciphering key sequence number might be used instead of the term key set 
identifier (KSI). 
As described in subclause 4.8 in order to interwork with E-UTRAN connected to EPC, the UE supporting both S1 mode 
and N1 mode can operate in either single-registration mode or dual-registration mode. A UE operating in dual-
registration mode shall independently maintain and use both EPS security context (see 3GPP TS 24.301 [15]) and 5G 
NAS security context. When the UE operating in dual-registration mode performs an EPS attach procedure, it shall take 
into use an EPS security context and follow the handling of this security context as specified in 3GPP TS 24.301 [15]. 

[대상 문장]
. 
The UE and the AMF need to be able to maintain two 5G NAS security contexts simultaneously, i.e. a current 5G NAS 
security context and a non-current 5G NAS security context, since: 
a) after a 5G re-authentication, the UE and the AMF can have both a current 5G NAS security context and a non-
current 5G NAS security context which has not yet been taken into use (i.e. a partial native 5G NAS security 
context); and 
b) after an inter-system change from S1 mode to N1 mode, the UE and the AMF can have both a mapped 5G NAS 
security context, which is the current 5G NAS security context, and a non-current native 5G NAS security 
context that was created during a previous access in N1 mode. 
The number of 5G NAS security contexts that need to be maintained simultaneously by the UE and the AMF is limited 
by the following requirements: 
a) after a successful 5G (re-)authentication, which creates a new partial native 5G NAS security context,
```

</details>

## V2-P1-248
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

UE가 한 access에서 등록 절차를 수행 중이고 같은 PLMN의 다른 access에서도 등록하려는 경우, 첫 번째 access의 Registration procedure가 완료될 때까지 다른 access에서 등록을 시작해서는 안 된다. 이는 3GPP access와 선택된 N3IWF, TNGF 또는 W-AGF가 같은 PLMN에 있는 경우를 포함한다.

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

## V2-P1-249
기준 G018 · 3GPP TS 24.501 V18.12.0 · 4.6.1 · PDF 96쪽(인쇄 95쪽)

원문: If the timer T3526 associated with the S-NSSAI(s) was started upon reception of the rejected NSSAI for the maximum number of UEs reached, the UE may remove the S-NSSAI(s) from the rejected NSSAI including S-NSSAI(s) with the rejection cause "S-NSSAI not available due to maximum number of UEs reached", if the timer T3526 associated with the S-NSSAI(s) expires.

질문: 최대 UE 수 도달 사유의 S-NSSAI와 연관된 T3526이 만료될 때 UE의 처리를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "may",
  "polarity": "positive",
  "actor": "UE",
  "condition": "if T3526 was started for rejected S-NSSAI(s) due to the maximum number of UEs being reached and that timer expires",
  "action": "remove the affected S-NSSAI(s) from the rejected NSSAI",
  "exception": "only S-NSSAI(s) carrying the stated maximum-UE rejection cause",
  "gold_summary_ko": "해당 T3526이 만료되면 UE는 'maximum number of UEs reached' 거절 사유를 가진 S-NSSAI를 rejected NSSAI에서 제거할 수 있다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

S-NSSAI와 연관된 T3526이 만료되면, UE는 거부된 NSSAI에서 해당 S-NSSAI(s)를 제거하도록 허용된다. 여기에는 거부 사유가 "S-NSSAI not available due to maximum number of UEs reached"인 S-NSSAI(s)도 포함된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
red PLMN or SNPN regardless 
of the access type. The AMF shall only send a rejected NSSAI for the current PLMN when the registration area consists 
of TAIs that only belong to the registered PLMN. If the UE receives a rejected NSSAI for the current PLMN, and the 
registration area also contains TAIs belonging to different PLMNs, the UE shall treat the received rejected NSSAI for 
the current PLMN as applicable to the whole registered PLMN. 
The rejected NSSAI for the failed or revoked NSSAA includes one or more S-NSSAIs that have failed the network 
slice-specific authentication and authorization or for which the authorization have been revoked, and are applicable for 
the whole registered PLMN or SNPN regardless of the access type. 
The rejected NSSAI for the maximum number of UEs reached is applicable for the whole registered PLMN or SNPN, 
and the access type over which the rejected NSSAI was sent. The AMF shall send a rejected NSSAI including S-
NSSAI(s) with the rejection cause "S-NSSAI not available due to maximum number of UEs reached", when one or 
more S-NSSAIs are indicated that the maximum number of UEs has been reached. 
[대상 문장]
. If one 
or more S-NSSAIs are removed from the rejected NSSAI for the maximum number of UEs reached, the timer T3526 
associated with the removed S-NSSAI(s) shall be stopped, if running. The UE shall not stop the timer T3526 if the UE 
selects an E-UTRA cell connected to EPC. 
If the UE receives a rejected NSSAI for the maximum number of UEs reached, the registration area contains TAIs 
belonging to different PLMNs, which are equivalent PLMNs, the UE shall treat the received rejected NSSAI for the 
maximum number of UEs reached as applicable to these equivalent PLMNs when the UE is in this registration area. 
If the UE has indicated that the UE supports network slice replacement feature and the AMF determines to provide the 
mapping information between the S-NSSAI to be replaced and the alternative S-NSSAI to the UE, the network shall 
provide the UE with the alternative NSSAI. The alternative NSSAI is managed per access type independe
```

</details>

## V2-P1-250
기준 G024 · 3GPP TS 24.501 V18.12.0 · 4.9.2 · PDF 133쪽(인쇄 132쪽)

원문: The UE should memorize the identity of the PLMNs or SNPNs where N1 mode capability for 3GPP access was disabled.

질문: 3GPP access의 N1 mode capability가 비활성화된 경우 UE가 기억할 network identity를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should",
  "polarity": "positive",
  "actor": "UE",
  "condition": "where N1 mode capability for 3GPP access was disabled",
  "action": "memorize the identity of the affected PLMNs or SNPNs",
  "exception": "",
  "gold_summary_ko": "UE는 N1 mode capability가 비활성화된 PLMN 또는 SNPN의 identity를 기억하는 것이 권고된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

UE는 3GPP access의 N1 mode capability가 비활성화되었던 PLMN 또는 SNPN의 식별자를 기억하는 것이 권고된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 N1 mode capability again are UE implementation specific. 
The UE shall disable the N1 mode capability for 3GPP access if requested by the upper layers (e.g. see 
subclause U.2.2.6.4 in 3GPP TS 24.229 [14]). If the UE disabled the N1 mode capability for 3GPP access based on the 
request from the upper layers (e.g. see subclause U.2.2.6.4 in 3GPP TS 24.229 [14]), the criteria to re-enable the N1 
mode capability for 3GPP access after the completion of an emergency service are UE implementation specific. 
If the N1 mode capability for 3GPP access was disabled due to the UE initiated de-registration procedure for 3GPP 
access or for 3GPP access and non-3GPP access and the UE is operating in single-registration mode (see 
subclause 5.5.2.2.3), upon request of the upper layers to re-register for 5GS services over 3GPP access or the UE needs 
to come out of unavailability period and resume normal services, the UE shall enable the N1 mode capability for 3GPP 
access again. 
As an implementation option, the UE may start a timer for enabling the N1 mode capability for 3GPP access when the 
UE disables the N1 mode capability for 3GPP access. 
[대상 문장]
. On expiry of this timer: 
a) if the UE is in Iu mode or A/Gb mode and is in idle mode as specified in 3GPP TS 24.008 [13], the UE should 
enable the N1 mode capability for 3GPP access; 
b) if the UE is in Iu mode and a PS signalling connection exists, but no RR connection exists, the UE may abort the 
PS signalling connection before enabling the N1 mode capability for 3GPP access; 
c) if the UE is in S1 mode and is in EMM-IDLE mode as specified in 3GPP TS 24.301 [15], the UE should enable 
the N1 mode capability for 3GPP access; and 
d) If the UE is in Iu mode or A/Gb mode and an RR connection exists, the UE should delay enabling the N1 mode 
capability for 3GPP access until the RR connection is released. If the UE is in S1 mode and is in EMM-
CONNECTED mode as specified in 3GPP TS 24.301 [15], the UE should delay enabling the N1 mode capability 
for 3GPP access until the NAS signalling connection in S1 mode is released. 
When the UE 
```

</details>

## V2-P1-251
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

Nudr를 통해 UDR에 접근하는 각 NF Service Consumer는 반드시 자신이 변경하도록 권한을 부여받은 데이터만 추가, 수정, 갱신 또는 삭제할 수 있어야 한다. 즉, 권한이 없는 데이터는 변경해서는 안 된다.

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

## V2-P1-252
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

## V2-P1-253
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

등록 절차 동안 UE가 MICO mode 선호를 표시하지 않으면, AMF는 이 UE에 대해 MICO mode를 활성화해서는 안 된다.

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

## V2-P1-254
기준 G029 · 3GPP TS 23.501 V18.12.0 · 5.18.4 · PDF 334쪽(인쇄 333쪽)

원문: The network should not move the UE to another available PLMN/SNPN, e.g. by handover, as long as the selected PLMN/SNPN is available to serve the UE's location.

질문: 선택된 PLMN 또는 SNPN이 UE 위치에서 계속 서비스를 제공하는 동안 다른 network로 이동시키는 정책을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "should_not",
  "polarity": "negative",
  "actor": "network",
  "condition": "as long as the selected PLMN or SNPN remains available at the UE location",
  "action": "move the UE to another available PLMN or SNPN, including by handover",
  "exception": "",
  "gold_summary_ko": "선택된 PLMN 또는 SNPN이 계속 서비스 가능하면 network는 UE를 다른 PLMN 또는 SNPN으로 이동시키지 않는 것이 권고된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

네트워크는 선택된 PLMN/SNPN이 UE의 위치에 서비스를 제공할 수 있는 동안에는 UE를 다른 사용 가능한 PLMN/SNPN으로 이동시키지 않는 것이 권고된다. 예를 들어 핸드오버로 이동시키는 것도 권고되지 않는다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
red NG-RAN shall in the broadcast system information include the PLMN-IDs concerning available 
core network operators in the shared network. 
When a UE performs an Initial Registration to a network, one of available PLMNs shall be selected to serve the UE. UE 
uses all the received broadcast PLMN-IDs in its PLMN (re)selection processes which is specified in TS 23.122 [17]. 
UE shall inform the NG-RAN of the selected PLMN so that the NG-RAN can route correctly. The NG-RAN shall 
inform the core network of the selected PLMN. 
As per any network, after Initial Registration to the shared network and while remaining served by the shared network, 
the network selection procedures specified in TS 23.122 [17] may cause the UE to perform a reselection of another 
available PLMN. 
UE uses all of the received broadcast PLMN-IDs in its cell and PLMN (re)selection processes. 
5.18.4 Network selection by the network 
The NG-RAN uses the selected PLMN/SNPN (provided by the UE at RRC establishment, or, provided by the 
AMF/source NG-RAN at N2/Xn handover) to select target cells for future handovers (and radio resources in general) 
appropriately. 
[대상 문장]
. 
In the case of handover or network controlled release to a PLMN in a shared network: 
- When multiple PLMN IDs are broadcasted in a cell sel ected by NG-RAN, NG-RAN shall select a target PLMN, 
taking into account the prioritized list of PLMN IDs provided via Mobility Restriction List from AMF. 
- For Xn based HO procedure, Source NG-RAN indicates the selected PLMN ID to the target NG-RAN, see 
TS 38.300 [27]. 
- For N2 based HO procedure, the NG-RAN indicates a selected PLMN ID to the AMF as part of the TAI sent in 
the HO required message. Source AMF uses the TAI information supplied by the source NG-RAN to select the 
target AMF/MME. The source AMF should forward the selected PLMN ID to the target AMF/MME. The target 
AMF/MME indicates the selected PLMN ID to the target NG-RAN/eNB so that the target NG-RAN/eNB can 
select target cells for future handover appropriately. 
- For RRC connection release with redirection to E-UTRAN proc
```

</details>

## V2-P1-255
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

AMF는 unavailability period의 지속 시간과 시작 시점을 기준으로 mobile reachable timer와 implicit deregistration timer의 값을 설정하는 것이 권고된다.

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
