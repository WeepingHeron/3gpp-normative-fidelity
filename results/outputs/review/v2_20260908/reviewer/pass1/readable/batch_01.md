# pass1 검토 자료 1–43

원문·정답 참고 자료이며 판정은 별도 JSONL 사본에 기록한다.

## V2-P1-001
기준 G048 · 3GPP TS 24.501 V18.12.0 · 4.6.1 · PDF 96쪽(인쇄 95쪽)

원문: The number of S-NSSAIs included in the partially allowed NSSAI or the partially rejected NSSAI shall not exceed 7.

질문: partially allowed 또는 partially rejected NSSAI의 S-NSSAI 개수 상한을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall_not",
  "polarity": "negative",
  "actor": "number of S-NSSAIs in the partially allowed NSSAI or partially rejected NSSAI",
  "condition": "",
  "action": "exceed 7",
  "exception": "maximum is 7",
  "gold_summary_ko": "해당 NSSAI에 포함되는 S-NSSAI 수는 7개를 초과해서는 안 된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

partially allowed NSSAI 또는 partially rejected NSSAI에 포함되는 S-NSSAI의 개수는 7을 초과해서는 안 된다. 즉, 최대 7개이다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
ins TAIs 
belonging to different PLMNs, which are equivalent PLMNs, the UE shall treat the received rejected NSSAI for the 
maximum number of UEs reached as applicable to these equivalent PLMNs when the UE is in this registration area. 
If the UE has indicated that the UE supports network slice replacement feature and the AMF determines to provide the 
mapping information between the S-NSSAI to be replaced and the alternative S-NSSAI to the UE, the network shall 
provide the UE with the alternative NSSAI. The alternative NSSAI is managed per access type independently, i.e. 3GPP 
access or non-3GPP access, and is applicable for the registration area. 
If the UE has indicated that the UE supports the partial network slice feature and includes the S-NSSAI(s) in the 
requested NSSAI, the AMF determines the S-NSSAI(s) to be included in the partially allowed NSSAI or the partially 
rejected NSSAI as specified in subclause 4.6.2.11. When the AMF provides both the partially allowed NSSAI and the 
partially rejected NSSAI to the UE, each S-NSSAI shall be either in the partially allowed NSSAI or in the partially 
rejected NSSAI but not both. 
[대상 문장]
. The sum of the number of S-NSSAI(s) stored in the partially allowed NSSAI and the 
allowed NSSAI shall not exceed 8. The partially allowed NSSAI is only applicable to 3GPP access and is applicable for 
the registration area. The partially rejected NSSAI is only applicable to 3GPP access and is applicable for the 
registration area. 
NOTE 2: Based on local policies, the UE can remove an  S-NSSAI from the rejected NSSAI for the failed or 
revoked NSSAA when the UE wants to register to the slice identified by this S-NSSAI. 
NOTE 3: Based on network local policy, network slice-sp ecific authentication and authorization procedure can be 
initiated by the AMF for an S-NSSAI in rejected NSSAI for the failed or revoked NSSAA when the S-
NSSAI is requested by the UE based on its local policy. 
NOTE 4: At least one S-NSSAI in the default configured NSSAI or at least one default S-NSSAI is recommended 
as not subject to network slice-specific au
```

</details>

## V2-P1-002
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

네트워크는 선택된 PLMN/SNPN이 UE의 위치를 계속 서비스할 수 있는 동안 UE를 다른 사용 가능한 PLMN/SNPN으로 이동시키면 안 된다. 예를 들어 핸드오버로 이동시키는 것도 포함된다.

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

## V2-P1-003
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

모든 event가 UPF에 직접 subscribe될 수 있는 것은 아니다. 즉, UPF에 직접 subscribe하는 기능은 일부 event에만 기술적으로 가능하다.

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

## V2-P1-004
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

## V2-P1-005
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

전체 PLMN paging을 피하기 위해 AMF가 Active Time을 할당할 때, AMF는 UE에 "all PLMN" registration area를 할당하지 않는 것이 권고된다. 이는 전체 PLMN paging을 피하려는 조건에서 적용된다.

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

## V2-P1-006
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

AMF는 UE가 PLMN이 운용할 수 없는 지리적 지역에 위치한다고 판단할 수 있을 만큼 충분히 정확한 UE 위치정보가 없는 한, 해당 요청을 거절하거나 UE를 등록해제해서는 안 된다. 즉, 충분히 정확한 위치정보가 있을 때에만 거절 또는 등록해제가 가능하다.

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

## V2-P1-007
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

각 SMF는 하나의 PDU Session 내에서 local UPF와 central UPF를 모두 제어하도록 허용된다. 이는 의무가 아니라 허용 사항이다.

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

## V2-P1-008
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

초기 등록 절차 중 K_AUSF가 유효하지 않을 때 UE는 ngKSI를 반드시 삭제해야 한다.

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

## V2-P1-009
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

UE를 5GC에서 EPC로 redirect할 때, UE가 Registration Request 또는 Service Request를 보내면 AMF는 EMM cause 값이 UE가 5GC를 사용하지 않아야 함을 나타내는 Registration Reject 또는 Service Reject를 보낸다. 이 원문은 AMF가 해당 거절 메시지의 EMM cause로 UE가 5GC를 사용하지 않아야 한다는 지침을 전달함을 설명한다.

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

## V2-P1-010
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

NG-RAN node가 N2 인터페이스 OVERLOAD START 메시지 수신 때문에 UAC를 시작하기로 결정한 경우, 해당 절차는 OVERLOAD START 메시지에 포함된 요청과 관련되고 이 NG-RAN node에 연결된 모든 AMF가 네트워크에 접근하는 UE에 대한 부하를 제한해 달라고 요청하는 경우에만 시작하는 것이 권고된다.

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

## V2-P1-011
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

UE가 현재 TAI와 cell CGI가 multicast MBS session service area에 없더라도, UE가 유효한 area 정보를 가지고 있으면 join request를 보낼 수 있다. 이 경우 join request는 해당 유효한 area 정보를 바탕으로 처리되는 것으로 이해된다.

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

## V2-P1-012
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

emergency callback을 가능하게 하기 위해, UE는 emergency services 완료 후 MICO mode 사용을 요청하기 전에 UE 구현체별 지속 시간 동안 기다리는 것이 권고된다.

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

## V2-P1-013
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

AMF가 Unavailability configuration IE를 제공하지 않거나, 해당 IE에서 EUPR 비트를 "UE needs to report end of unavailability period"로 설정한 경우, UE는 unavailability period duration이 끝났을 때 mobility registration update를 위한 registration procedure를 트리거하는 것이 권고된다.

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

## V2-P1-014
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

PDU Session establishment 절차 동안, 특정 PDU Session에 대해 SMF가 N6 interface의 network instance를 UPF에 표시하도록 허용된다. 이는 선택 가능한 동작이며, 반드시 해야 하는 의무는 아니다.

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

## V2-P1-015
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

UE가 SNPN에서 onboarding 서비스에 대해 등록 중이거나 등록된 경우, serving SNPN은 UE에게 configured NSSAI를 제공해서는 안 된다.

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

## V2-P1-016
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

## V2-P1-017
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

NG-RAN 노드가 N2 인터페이스 OVERLOAD START 메시지 수신 때문에 UAC를 시작하기로 결정한 경우, 해당 절차는 OVERLOAD START 메시지에 포함된 요청과 관련되고 이 NG-RAN 노드에 연결된 모든 AMF가 네트워크에 접속하는 UE에 대한 부하 제한을 요청할 때에만 시작하는 것이 권고된다.

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

## V2-P1-018
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

각 N3IWF, TNGF, TWIF, W-AGF는 다른 TAI 값을 구성하도록 허용되며, 다른 N3IWF, TNGF, TWIF 및/또는 W-AGF와 동일한 TAI 값을 구성하도록도 허용된다.

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

## V2-P1-019
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

UE가 한 access에서 등록 절차를 수행 중이고 같은 PLMN의 다른 access에서도 등록하려는 경우, UE는 첫 번째 access의 Registration procedure가 완료될 때까지 다른 access에서의 등록을 시작해서는 안 된다.

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

## V2-P1-020
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

Any UE를 대상으로 하는 subscription은 UE 이동성 때문에 현재 AMF에서 더 적절한 다른 AMF로 이동할 수 있으며, 이때 해당 subscription은 새 AMF로 전달되도록 처리해야 한다. 즉, UE mobility로 인해 AMF 간에 subscription을 이전하는 정책을 적용한다.

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

## V2-P1-021
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

SMF는 PDU Session establishment 중 특정 PDU Session에 대해 N6 interface의 network instance를 UPF에 표시하도록 허용된다. 이는 의무가 아니라 선택 가능한 동작이다.

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

## V2-P1-022
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

UE가 유효한 MBS 서비스 영역 정보를 가지고 있고 현재 TAI와 현재 셀 CGI가 모두 multicast MBS session의 서비스 영역에 속하지 않는 경우, UE는 local MBS service를 위한 multicast MBS session 가입을 요청하지 않는 것이 권고된다.

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

## V2-P1-023
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

UE는 ngKSI를 삭제해야 하는 경우 ngKSI를 "no key is available" 값으로 설정해야 하며, 연관된 K_AMF 또는 K'_AMF, 5G NAS ciphering key, 5G NAS integrity key도 무효로 간주해야 한다. 즉, ngKSI와 그에 연결된 5G NAS security context는 더 이상 유효하지 않은 것으로 처리해야 한다.

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

## V2-P1-024
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

AMF가 UE에 active time value를 알리는 경우, AMF는 UE에 대한 MICO indication IE에서 "all PLMN registration area allocated" 표시를 알리지 않는 것이 권고된다.

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

## V2-P1-025
기준 G048 · 3GPP TS 24.501 V18.12.0 · 4.6.1 · PDF 96쪽(인쇄 95쪽)

원문: The number of S-NSSAIs included in the partially allowed NSSAI or the partially rejected NSSAI shall not exceed 7.

질문: partially allowed 또는 partially rejected NSSAI의 S-NSSAI 개수 상한을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall_not",
  "polarity": "negative",
  "actor": "number of S-NSSAIs in the partially allowed NSSAI or partially rejected NSSAI",
  "condition": "",
  "action": "exceed 7",
  "exception": "maximum is 7",
  "gold_summary_ko": "해당 NSSAI에 포함되는 S-NSSAI 수는 7개를 초과해서는 안 된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

부분적으로 허용된 NSSAI 또는 부분적으로 거부된 NSSAI에 포함되는 S-NSSAI의 수는 7을 초과해서는 안 된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
ins TAIs 
belonging to different PLMNs, which are equivalent PLMNs, the UE shall treat the received rejected NSSAI for the 
maximum number of UEs reached as applicable to these equivalent PLMNs when the UE is in this registration area. 
If the UE has indicated that the UE supports network slice replacement feature and the AMF determines to provide the 
mapping information between the S-NSSAI to be replaced and the alternative S-NSSAI to the UE, the network shall 
provide the UE with the alternative NSSAI. The alternative NSSAI is managed per access type independently, i.e. 3GPP 
access or non-3GPP access, and is applicable for the registration area. 
If the UE has indicated that the UE supports the partial network slice feature and includes the S-NSSAI(s) in the 
requested NSSAI, the AMF determines the S-NSSAI(s) to be included in the partially allowed NSSAI or the partially 
rejected NSSAI as specified in subclause 4.6.2.11. When the AMF provides both the partially allowed NSSAI and the 
partially rejected NSSAI to the UE, each S-NSSAI shall be either in the partially allowed NSSAI or in the partially 
rejected NSSAI but not both. 
[대상 문장]
. The sum of the number of S-NSSAI(s) stored in the partially allowed NSSAI and the 
allowed NSSAI shall not exceed 8. The partially allowed NSSAI is only applicable to 3GPP access and is applicable for 
the registration area. The partially rejected NSSAI is only applicable to 3GPP access and is applicable for the 
registration area. 
NOTE 2: Based on local policies, the UE can remove an  S-NSSAI from the rejected NSSAI for the failed or 
revoked NSSAA when the UE wants to register to the slice identified by this S-NSSAI. 
NOTE 3: Based on network local policy, network slice-sp ecific authentication and authorization procedure can be 
initiated by the AMF for an S-NSSAI in rejected NSSAI for the failed or revoked NSSAA when the S-
NSSAI is requested by the UE based on its local policy. 
NOTE 4: At least one S-NSSAI in the default configured NSSAI or at least one default S-NSSAI is recommended 
as not subject to network slice-specific au
```

</details>

## V2-P1-026
기준 G038 · 3GPP TS 23.501 V18.12.0 · 5.3.2.3 · PDF 97쪽(인쇄 96쪽)

원문: When AMF allocates registration area for UE registered for Disaster Roaming service as specified in clause 5.40.4, AMF shall only consider TAIs covering the area with the Disaster Condition.

질문: Disaster Roaming service에 등록된 UE의 registration area를 AMF가 할당할 때 고려할 TAI 범위를 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall",
  "polarity": "positive",
  "actor": "AMF",
  "condition": "when allocating a registration area for a UE registered for Disaster Roaming service",
  "action": "consider TAIs covering the area with the Disaster Condition",
  "exception": "only TAIs covering the Disaster Condition area",
  "gold_summary_ko": "AMF는 해당 registration area를 할당할 때 Disaster Condition이 있는 지역을 포함하는 TAI만 반드시 고려해야 한다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

AMF는 Disaster Roaming service에 등록된 UE의 registration area를 할당할 때 반드시 재난 조건(Disaster Condition) 영역을 포함하는 TAI만 고려해야 한다. 즉, 재난 조건 영역을 덮는 TAI만 고려하도록 제한된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
ion Management State models 
 
RM-REGISTERED 
Registration Accept 
Deregistration 
Registration Reject 
Registration Reject Registration Update Accept 
RM-DEREGISTERED 
 
Figure 5.3.2.2.4-1: RM state model in UE 
 
RM-REGISTERED 
Registration Accept 
Deregistration 
Registration Reject 
Registration Reject Registration Update Accept 
RM-DEREGISTERED 
 
Figure 5.3.2.2.4-2: RM state model in AMF 
5.3.2.3 Registration Area management 
Registration Area management comprises the functions to allocate and reallocate a Registration area to a UE. 
Registration area is managed per access type i.e. 3GPP access or Non-3GPP access. 
When a UE registers with the network over the 3GPP access, the AMF allocates a set of tracking areas in TAI List to 
the UE. When the AMF allocates registration area, i.e. the set of tracking areas in TAI List, to the UE it may take into 
account various information (e.g. Mobility Pattern and Allowed/Non-Allowed Area (refer to clause 5.3.4.1)). An AMF 
which has the whole PLMN as serving area may alternatively allocate the whole PLMN ("all PLMN") as registration 
area to a UE in MICO mode (refer to clause 5.4.1.3). 
[대상 문장]
. 
The 5G System shall support allocating a Registration Area using a single TAI List which includes tracking areas of any 
NG-RAN nodes in the Registration Area for a UE. 
In the case of SNPN, the TAI list allocated by AMF does not support Tracking Areas belonging to different SNPNs. 
```

</details>

## V2-P1-027
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

5GS는 TSN network로 동작하는 경우 sub-network로 작동할 수 있는 기술적 가능성이 있다. 이는 4.4.8.2절의 아키텍처를 바탕으로 한 3GPP 규격에서 지원된다.

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

## V2-P1-028
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

전체 PLMN에서 paging이 발생하는 것을 피하기 위해, AMF가 Active Time을 할당할 때 UE에 'all PLMN' registration area를 할당하지 않는 것이 권고된다.

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

## V2-P1-029
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

전달 상태: `NOT_GENERATED`

설명 원문:

[설명이 생성되지 않은 슬롯. 원문 설명 문자열 없음.]

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

## V2-P1-030
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

T3526가 최대 UE 수 도달 사유의 rejected NSSAI 수신 시 S-NSSAI(s)와 연관되어 시작되었고, 그 T3526이 만료되면 UE는 해당 S-NSSAI(s)를 rejected NSSAI에서 제거하도록 허용된다. 이때 제거 대상에는 "S-NSSAI not available due to maximum number of UEs reached" 거절 사유를 가진 S-NSSAI(s)도 포함된다.

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

## V2-P1-031
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

AMF는 UE가 PC5 reference point를 통한 V2X communication 사용 권한을 가지고, 그 권한이 REGISTRATION REQUEST의 5GMM capability IE에 UE가 설정한 비트 또는 이전 등록 절차 동안 AMF의 5GMM context에 이미 저장된 비트와 UDM에서 얻은 사용자의 subscription context에 근거하는 경우, 등록 절차 완료 후 NAS signalling connection을 즉시 해제하지 않는 것이 권고된다.

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

## V2-P1-032
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

N38 reference point는 같은 VPLMN의 V-SMF들 사이에 있을 수 있고, 서로 다른 VPLMN의 V-SMF들 사이에도 있을 수 있다. 서로 다른 VPLMN 사이의 경우는 inter-PLMN mobility를 가능하게 하기 위한 것이다.

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

## V2-P1-033
기준 G043 · 3GPP TS 23.501 V18.12.0 · 5.3.4.1.1 · PDF 109쪽(인쇄 108쪽)

원문: In order to enforce all primary RAT restrictions, the related RAT has to be deployed in different Tracking Area Codes and the subscriber shall not be allowed to access the network in TAs using the particular RAT.

질문: primary RAT restriction을 적용할 때 subscriber의 해당 RAT 기반 TA 접근 제한을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall_not",
  "polarity": "negative",
  "actor": "subscriber",
  "condition": "to enforce all primary RAT restrictions when the related RAT is deployed in different Tracking Area Codes",
  "action": "access the network in TAs using the restricted RAT",
  "exception": "",
  "gold_summary_ko": "관련 RAT가 서로 다른 Tracking Area Code에 배치된 조건에서 subscriber는 그 RAT를 사용하는 TA의 network에 접근해서는 안 된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

primary RAT restriction을 적용하여 모든 primary RAT restriction을 강제하려면, 관련 RAT는 서로 다른 Tracking Area Codes에 배치되어야 한다. 이 경우 subscriber는 해당 RAT를 사용하는 TAs에서 네트워크에 접근해서는 안 된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 123 501 V18.12.0 (2026-01)1083GPP TS 23.501 version 18.12.0 Release 18

[대상 문장]
. 
With all secondary RAT restrictions, the subscriber shall not be allowed to use this RAT as secondary RAT. 
5.3.4.1.2 Management of Service Area Restrictions 
This clause describes Service Area Restrictions for 3GPP access. For Service Area Restrictions when using wireline 
access, see TS 23.316 [84]. 
A Service Area Restriction may contain one or more (e.g. up to 16) entire Tracking Areas each or the Service Area 
Restriction may be set as unlimited (i.e. contain all Tracking Areas of the PLMN). The UE's subscription data in the 
UDM includes a Service Area Restriction which may contain either Allowed or Non-Allowed Areas–specified by using 
explicit Tracking Area identities and/or other geographical information (e.g. longitude/latitude, zip code, etc). The 
geographical information used to specify Allowed or Non-Allowed Area is only managed in the network and the 
network will map it to a list of TAs before sending Service Area Res
```

</details>

## V2-P1-034
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

전달 상태: `EXPLANATION`

설명 원문:

현재 5G NAS 보안 컨텍스트는 native 또는 mapped 유형일 수 있다. 즉, native 5G NAS 보안 컨텍스트에서 유래하거나 mapped 5G NAS 보안 컨텍스트에서 유래할 수 있다.

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

## V2-P1-035
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

등록 절차 또는 일반 UE 구성 업데이트 절차 동안 configured NSSAI와 rejected NSSAI를 변경할 수 있다. 이는 허용을 나타내며, 반드시 변경해야 한다는 뜻은 아니다.

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

## V2-P1-036
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

dual-registration mode UE가 initial registration을 수행할 때는 5G NAS security context를 사용하지 않고, 해당 보안 컨텍스트를 무효화하거나 초기화한 상태로 등록 절차를 진행해야 한다. 즉, 초기 등록에서는 이전 5G NAS 보안 컨텍스트를 그대로 유지해 적용하는 것이 아니라 새로 보안 절차를 수행하는 방향으로 처리된다.

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

## V2-P1-037
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

N26 인터페이스를 지원하는 망에서 single-registration mode로 동작하는 UE가 emergency bearer services용 PDN connection은 있지만 현재 EPS security context가 없을 때, AMF는 S1 mode to N1 mode NAS transparent container IE에서 선택된 5G NAS security algorithms로 5G-IA0과 5G-EA0을 반드시 설정해야 한다.

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

## V2-P1-038
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

EPC에 연결된 E-UTRAN과 상호동작하기 위해, S1 mode와 N1 mode를 모두 지원하는 UE는 단일 등록 모드 또는 이중 등록 모드로 동작할 수 있다. 이는 기술적으로 가능한 운용 선택지를 설명하는 것이다.

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

## V2-P1-039
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

secure NAS message exchange가 설정된 뒤에는 UE의 수신 5GMM entity가 NAS에 의해 성공적으로 무결성 검사를 받은 경우가 아니면 어떤 NAS signalling message도 처리해서는 안 된다. 즉, NAS 무결성 검사가 성공한 경우에만 처리할 수 있다.

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

## V2-P1-040
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

3GPP access에서 N1 mode capability가 비활성화된 경우, UE는 해당 네트워크에 대해 3GPP access용 네트워크 식별자를 기억하지 않는 것이 요구된다. 즉, UE는 N1 mode capability가 비활성화된 상태에서는 그 network identity를 저장하거나 유지하지 않아야 한다.

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

## V2-P1-041
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

각 SMF는 하나의 PDU Session 안에서 로컬 UPF와 중앙 UPF를 모두 제어할 수 있는 능력이 있을 수 있다. 이는 의무나 금지가 아니라 기술적 가능성을 나타낸다.

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

## V2-P1-042
기준 G043 · 3GPP TS 23.501 V18.12.0 · 5.3.4.1.1 · PDF 109쪽(인쇄 108쪽)

원문: In order to enforce all primary RAT restrictions, the related RAT has to be deployed in different Tracking Area Codes and the subscriber shall not be allowed to access the network in TAs using the particular RAT.

질문: primary RAT restriction을 적용할 때 subscriber의 해당 RAT 기반 TA 접근 제한을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall_not",
  "polarity": "negative",
  "actor": "subscriber",
  "condition": "to enforce all primary RAT restrictions when the related RAT is deployed in different Tracking Area Codes",
  "action": "access the network in TAs using the restricted RAT",
  "exception": "",
  "gold_summary_ko": "관련 RAT가 서로 다른 Tracking Area Code에 배치된 조건에서 subscriber는 그 RAT를 사용하는 TA의 network에 접근해서는 안 된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

primary RAT restriction을 모두 강제하기 위해서는 관련 RAT가 서로 다른 Tracking Area Code들에 배치되어야 하며, 가입자는 해당 특정 RAT를 사용하는 TA에서 네트워크에 접근해서는 안 된다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 123 501 V18.12.0 (2026-01)1083GPP TS 23.501 version 18.12.0 Release 18

[대상 문장]
. 
With all secondary RAT restrictions, the subscriber shall not be allowed to use this RAT as secondary RAT. 
5.3.4.1.2 Management of Service Area Restrictions 
This clause describes Service Area Restrictions for 3GPP access. For Service Area Restrictions when using wireline 
access, see TS 23.316 [84]. 
A Service Area Restriction may contain one or more (e.g. up to 16) entire Tracking Areas each or the Service Area 
Restriction may be set as unlimited (i.e. contain all Tracking Areas of the PLMN). The UE's subscription data in the 
UDM includes a Service Area Restriction which may contain either Allowed or Non-Allowed Areas–specified by using 
explicit Tracking Area identities and/or other geographical information (e.g. longitude/latitude, zip code, etc). The 
geographical information used to specify Allowed or Non-Allowed Area is only managed in the network and the 
network will map it to a list of TAs before sending Service Area Res
```

</details>

## V2-P1-043
기준 G043 · 3GPP TS 23.501 V18.12.0 · 5.3.4.1.1 · PDF 109쪽(인쇄 108쪽)

원문: In order to enforce all primary RAT restrictions, the related RAT has to be deployed in different Tracking Area Codes and the subscriber shall not be allowed to access the network in TAs using the particular RAT.

질문: primary RAT restriction을 적용할 때 subscriber의 해당 RAT 기반 TA 접근 제한을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall_not",
  "polarity": "negative",
  "actor": "subscriber",
  "condition": "to enforce all primary RAT restrictions when the related RAT is deployed in different Tracking Area Codes",
  "action": "access the network in TAs using the restricted RAT",
  "exception": "",
  "gold_summary_ko": "관련 RAT가 서로 다른 Tracking Area Code에 배치된 조건에서 subscriber는 그 RAT를 사용하는 TA의 network에 접근해서는 안 된다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

primary RAT restriction을 적용하면, 가입자는 해당 RAT를 주 RAT로 사용하는 TA에 접근할 수 없도록 제한된다. 즉, 그 RAT에 대해 주 RAT 기반 TA 접근이 차단되는 방향으로 동작한다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 123 501 V18.12.0 (2026-01)1083GPP TS 23.501 version 18.12.0 Release 18

[대상 문장]
. 
With all secondary RAT restrictions, the subscriber shall not be allowed to use this RAT as secondary RAT. 
5.3.4.1.2 Management of Service Area Restrictions 
This clause describes Service Area Restrictions for 3GPP access. For Service Area Restrictions when using wireline 
access, see TS 23.316 [84]. 
A Service Area Restriction may contain one or more (e.g. up to 16) entire Tracking Areas each or the Service Area 
Restriction may be set as unlimited (i.e. contain all Tracking Areas of the PLMN). The UE's subscription data in the 
UDM includes a Service Area Restriction which may contain either Allowed or Non-Allowed Areas–specified by using 
explicit Tracking Area identities and/or other geographical information (e.g. longitude/latitude, zip code, etc). The 
geographical information used to specify Allowed or Non-Allowed Area is only managed in the network and the 
network will map it to a list of TAs before sending Service Area Res
```

</details>
