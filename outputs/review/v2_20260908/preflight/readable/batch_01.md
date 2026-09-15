# preflight 검토 자료 1–17

원문·정답 참고 자료이며 판정은 별도 JSONL 사본에 기록한다.

## G001
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

## G002
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

## G003
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

## G004
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

## G005
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

## G006
기준 G006 · 3GPP TS 24.501 V18.12.0 · 4.4.7 · PDF 69쪽(인쇄 68쪽)

원문: The UE can provide the SOR transparent container IE during the registration procedure to the network in the REGISTRATION COMPLETE message.

질문: registration procedure에서 UE가 SOR transparent container IE를 network에 전달하는 방법을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "can",
  "polarity": "positive",
  "actor": "UE",
  "condition": "during the registration procedure",
  "action": "provide the SOR transparent container IE to the network in the REGISTRATION COMPLETE message",
  "exception": "",
  "gold_summary_ko": "UE는 registration procedure 중 REGISTRATION COMPLETE message에 SOR transparent container IE를 넣어 network에 제공할 수 있다."
}
```

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 part of the CIoT small data container IE and handle the message as 
specified in subclause 5.6.1.4.2. 
If the UE: 
a) has 5G-EA0 as a selected 5G NAS security algorithm; and 
b) selects a PLMN other than Registered PLMN and EPLMN over one access; 
the UE shall send an initial NAS message including cleartext IEs only via the access type associated with the newly 
selected PLMN as described in this subclause for the case when the UE does not have a valid 5G NAS security context. 
If the UE: 
a) has 5G-EA0 as a selected 5G NAS security algorithm; and 
b) selects a PLMN other than Registered PLMN and EPLMN over one access, and the Registered PLMN or 
EPLMN is not registering or registered over other access; 
the UE shall delete the 5G NAS security context. 
NOTE: UE deletes the 5G NAS security context only if the UE is not in the connected mode. 
4.4.7 Protection of NAS IEs 
The network can provide the SOR transparent container IE during the registration procedure to the UE in the 
REGISTRATION ACCEPT message. The SOR transparent container IE is integrity protected by the HPLMN or 
subscribed SNPN as specified in 3GPP TS 33.501 [24]. 

[대상 문장]
. The SoR-MAC-I
UE in the SOR transparent container IE is generated by the 
UE as specified in 3GPP TS 33.501 [24]. 
The network can provide the Payload container IE during the Network-initiated NAS transport procedure to the UE in 
DL NAS TRANSPORT message. If the Payload container type IE is set to "SOR transparent container" or "UE 
parameters update transparent container", the Payload container IE is integrity protected by the HPLMN or subscribed 
SNPN as specified in 3GPP TS 33.501 [24]. If the Payload container type IE is set to "Multiple payloads" and the 
payload container type field of the payload container entry is set to "SOR transparent container" or "UE parameters 
update transparent container", the payload container entry contents field of the payload container entry is integrity 
protected correspondingly. 
The UE can provide the Payload container IE during the UE-initiated NAS transport procedure to the network in UL 
NA
```

</details>

## G007
기준 G007 · 3GPP TS 24.501 V18.12.0 · 4.4.2.1.1 · PDF 54쪽(인쇄 53쪽)

원문: This current 5G NAS security context can be of type native or mapped, i.e. originating from a native 5G NAS security context or mapped 5G NAS security context.

질문: current 5G NAS security context의 유형을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "can",
  "polarity": "positive",
  "actor": "current 5G NAS security context",
  "condition": "",
  "action": "be either native or mapped",
  "exception": "",
  "gold_summary_ko": "current 5G NAS security context는 native 유형 또는 mapped 유형일 수 있다."
}
```

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 124 501 V18.12.0 (2025-10)533GPP TS 24.501 version 18.12.0 Release 18
N26 and the UE operating in single-registration mode may derive a mapped 5G NAS security context from an EPS 
security context that has been established while the UE was in S1 mode. 
The 5G NAS security context is taken into use by the UE and the AMF, when the AMF initiates a security mode control 
procedure, during an N1 mode to N1 mode handover, or during the inter-system change procedure from S1 mode to N1 
mode. The 5G NAS security context which has been taken into use by the network most recently is called current 5G 
NAS security context. 
[대상 문장]
. 
The key set identifier ngKSI is assigned by the AMF either during the primary authentication and key agreement 
procedure or, for the mapped 5G NAS security context, during the inter-system change. The ngKSI consists of a value 
and a type of security context parameter indicating whether a 5G NAS security context is a native 5G NAS security 
context or a mapped 5G NAS security context. When the 5G NAS security context is a native 5G NAS security context, 
the ngKSI has the value of KSI
AMF, and when the current 5G NAS security context is of type mapped, the ngKSI has the 
value of KSIASME. 
The 5G NAS security context which is indicated by an ngKSI can be taken into use to establish the secure exchange of 
NAS messages when a new N1 NAS signalling connection is established without executing a new primary 
authentication and key agreement procedure (see subclause 5.4.1) or when the AMF initiates a security mode control 
procedure. For
```

</details>

## G008
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

## G009
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

## G010
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

## G011
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

## G012
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

## G013
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

## G014
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

## G015
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

## G016
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

## G017
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
