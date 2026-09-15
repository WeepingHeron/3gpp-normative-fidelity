# pass1 검토 자료 87–129

원문·정답 참고 자료이며 판정은 별도 JSONL 사본에 기록한다.

## V2-P1-087
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

AMF는 UE 요청을 처리할 때, UE가 PLMN이 운용할 수 없는 지리적 지역에 있다고 판단할 수 있을 만큼 충분히 정확한 UE 위치정보가 없는 한, 요청을 거절하거나 UE를 등록 해제하지 않는 것이 권고된다. 예외적으로, 충분히 정확한 위치정보가 UE가 해당 지역에 있음을 보여주는 경우에는 이 권고가 적용되지 않는다.

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

## V2-P1-088
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

5GS가 Paging Policy Differentiation(PPD) 기능을 지원하는 경우, 애플리케이션은 특정 IP 패킷에 적용할 Paging Policy를 5GS에 표시하기 위해 DSCP 값(TOS in IPv4 / TC in IPv6)을 설정한다. 이는 반드시 해야 하는 의무로 표현된다.

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

## V2-P1-089
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

AMF가 UE에 active time value를 알리는 경우, AMF는 MICO indication IE에서 UE에 "all PLMN registration area allocated" 표시를 해서는 안 된다. 이는 금지에 해당한다.

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

## V2-P1-090
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

이 목적을 위해 5GSM 메시지는 5GMM transport message의 정보 요소 안에서 전송될 수 있다. 즉, 5GSM 메시지를 5GMM transport message로 전달하는 기술적 가능성이 있다.

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

## V2-P1-091
기준 G036 · 3GPP TS 23.501 V18.12.0 · 4.2.8.1 · PDF 58쪽(인쇄 57쪽)

원문: A UE that accesses the 5G Core Network over a non-3GPP access shall, after UE registration, support NAS signalling with 5G Core Network control-plane functions using the N1 reference point.

질문: non-3GPP access로 5G Core Network에 접근하는 UE의 등록 후 NAS signalling 방식을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall",
  "polarity": "positive",
  "actor": "UE accessing the 5G Core Network over non-3GPP access",
  "condition": "after UE registration",
  "action": "support NAS signalling with 5G Core Network control-plane functions using the N1 reference point",
  "exception": "",
  "gold_summary_ko": "UE는 등록 후 N1 reference point를 사용해 5G Core Network control-plane function과의 NAS signalling을 반드시 지원해야 한다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

non-3GPP access를 통해 5G Core Network에 접속한 UE는 등록 후에도 NAS signalling을 계속 수행할 수 있어야 하며, 이 NAS signalling은 해당 non-3GPP access와 5GC 사이의 보안 및 연결 절차를 통해 전달된다. 즉, UE는 비3GPP 접속 환경에서도 5GC와의 등록 상태를 유지하면서 NAS 절차를 진행하는 방식으로 동작한다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 123 501 V18.12.0 (2026-01)573GPP TS 23.501 version 18.12.0 Release 18
- the UE selects a PLMN/SNPN and an N3IWF in this PLMN/SNPN. The PLMN/SNPN/N3IWF selection and the 
non-3GPP access network selection are independent. The N3IWF selection is defined in clause 6.3.6. 
When the UE decides to use trusted non-3GPP access to connect to a 5G Core Network in a PLMN: 
- the UE first selects a PLMN/SNPN; and then 
- the UE selects a non-3GPP access network (a TNAN) that supports trusted connectivity to the selected 
PLMN/SNPN. In this case, the non-3GPP access network selection is affected by the PLMN/SNPN selection. 

[대상 문장]
. 
When a UE is connected via a NG-RAN and via a non-3GPP access, multiple N1 instances shall exist for the UE i.e. 
there shall be one N1 instance over NG-RAN and one N1 instance over non-3GPP access. 
A UE simultaneously connected to the same 5G Core Network of a PLMN/SNPN over a 3GPP access and a non-3GPP 
access shall be served by a single AMF in this 5G Core Network. 
When a UE is connected to a 3GPP access of a PLMN, if the UE selects a N3IWF and the N3IWF is located in a PLMN 
different from the PLMN of the 3GPP access, e.g. in a different VPLMN or in the HPLMN, the UE is served separately 
by the two PLMNs. The UE is registered with two separate AMFs. PDU Sessions over the 3GPP access are served by 
V-SMFs different from the V-SMF serving the PDU Sessions over the non-3GPP access. The same can be true when 
the UE uses trusted non-3GPP access, i.e. the UE may select one PLMN for 3GPP access and a different PLMN for 
trusted non-
```

</details>

## V2-P1-092
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

그러나 각 SMF는 하나의 PDU Session 내에서 local UPF와 central UPF를 모두 제어할 수 있는 능력이 있다. 이는 허용 또는 선택 가능을 나타내며, 반드시 해야 한다는 의미는 아니다.

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

## V2-P1-093
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

선택된 PLMN 또는 SNPN이 UE의 현재 위치에서 계속 서비스를 제공할 수 있는 동안에는, UE를 다른 네트워크로 이동시키는 정책을 적용해서는 안 된다. 즉, 해당 네트워크가 계속 서비스를 제공하는 한 UE는 그 네트워크에 머물도록 유지되어야 한다.

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

## V2-P1-094
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

현재 5G NAS 보안 컨텍스트는 native 유형 또는 mapped 유형일 수 있으며, 이는 각각 native 5G NAS 보안 컨텍스트에서 유래했거나 mapped 5G NAS 보안 컨텍스트에서 유래했음을 뜻한다.

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

## V2-P1-095
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

5GS가 Paging Policy Differentiation을 지원하는 경우, 특정 IP packet에 적용할 Paging Policy는 해당 패킷을 식별할 수 있는 표시를 통해 나타낸다. 이 표시는 네트워크가 그 IP packet에 대해 어떤 paging 동작을 적용해야 하는지 구분할 수 있게 해준다.

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

## V2-P1-096
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

initial registration 중 UE는 선택한 K_AUSF에 대응하는 ngKSI를 사용해 등록 절차를 진행해야 한다. 만약 그 K_AUSF가 유효하지 않다면, UE는 해당 ngKSI를 계속 사용하지 말고 새로 유효한 보안 컨텍스트에 맞는 ngKSI로 처리해야 한다.

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

## V2-P1-097
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

partially allowed NSSAI와 partially rejected NSSAI는 각각 S-NSSAI를 최대 8개까지 포함할 수 있다. 따라서 해당 목록의 S-NSSAI 개수는 8개를 초과할 수 없다.

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

## V2-P1-098
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

partially allowed NSSAI 또는 partially rejected NSSAI에 포함된 S-NSSAI의 개수는 7을 초과해서는 안 된다.

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

## V2-P1-099
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

AMF가 5.40.4절에 규정된 Disaster Roaming 서비스에 등록된 UE의 registration area를 할당할 때에는, Disaster Condition이 적용되는 영역을 포함하는 TAI만 반드시 고려해야 한다.

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

## V2-P1-100
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

새로운 5G NAS security context는 N1 mode에서 N1 mode로의 handover 중에도 생성하도록 허용된다. 이는 해당 시점에 생성될 수 있음을 뜻하며, 반드시 생성해야 한다는 의미는 아니다.

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

## V2-P1-101
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

AMF는 clause 5.40.4에 명시된 Disaster Roaming service에 등록된 UE의 registration area를 할당할 때, Disaster Condition이 있는 영역을 포함하는 TAI만 반드시 고려해야 한다.

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

## V2-P1-102
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

UE가 ngKSI를 삭제해야 하는 경우, UE는 ngKSI를 "no key is available" 값으로 설정해야 한다. 또한 연관된 키 K AMF 또는 K'AMF, 5G NAS ciphering key, 5G NAS integrity key도 무효로 간주해야 하며, 이는 ngKSI와 연관된 5G NAS security context가 더 이상 유효하지 않음을 뜻한다.

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

## V2-P1-103
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

AMF는 PLMN 운용 제한 지역과 관련된 UE 요청을 처리할 때, 해당 UE의 위치정보가 그 제한 지역과의 관련성을 판단할 수 있을 만큼 확보되어 있어야 한다. 즉, 위치정보를 바탕으로 요청이 운용 제한 지역과 연관되는지 확인할 수 있어야 한다.

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

## V2-P1-104
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

## V2-P1-105
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

NF Service Consumer는 Nudr를 통해 UDR에 대해 자신이 접근 권한을 가진 데이터만 변경할 수 있다. 즉, 데이터 변경 범위는 해당 소비자에게 허용된 UDR 데이터로 제한된다.

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

## V2-P1-106
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

최대 UE 수 도달 사유의 거절 NSSAI를 수신했을 때 S-NSSAI(s)에 연관된 T3526이 시작되었다면, 그 타이머가 만료될 때 UE는 해당 S-NSSAI(s)를 거절 NSSAI에서 제거할 수 있도록 허용된다. 여기에는 거절 사유가 "S-NSSAI not available due to maximum number of UEs reached"인 S-NSSAI(s)도 포함된다.

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

## V2-P1-107
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

동일한 K AMF로 새 5G NAS security context를 유도할 때 target AMF는 Intra N1 mode NAS transparent container IE에 downlink NAS COUNT의 하위 8비트를 포함하고, 새 KAMF를 유도해서는 안 된다고 표시해야 한다. 이 표현은 새 KAMF 유도를 금지하는 의미이다.

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

## V2-P1-108
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

non-3GPP access network는 trusted connectivity를 지원하는 PLMN 또는 SNPN과, 지원하는 trusted connectivity의 유형을 광고하도록 허용된다. 예를 들어 “5G connectivity”를 광고할 수 있다.

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

## V2-P1-109
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

AMF는 UE가 PLMN이 운용할 수 없는 지리적 지역에 위치한다고 판단할 수 있을 만큼 충분히 정확한 UE 위치정보가 없는 한, 해당 요청을 거절하거나 UE를 등록 해제하지 않는 것이 권고된다. 위치정보가 그 정도로 충분히 정확한 경우에는 이 권고가 적용되지 않는다.

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

## V2-P1-110
기준 G035 · 3GPP TS 23.501 V18.12.0 · 4.2.8.1 · PDF 58쪽(인쇄 57쪽)

원문: A UE simultaneously connected to the same 5G Core Network of a PLMN/SNPN over a 3GPP access and a non-3GPP access shall be served by a single AMF in this 5G Core Network.

질문: 동일한 5G Core Network에 3GPP access와 non-3GPP access로 동시에 연결된 UE의 AMF 구성을 설명해줘.

정답 참고 필드(원문으로 검증):

```json
{
  "modal_class": "shall",
  "polarity": "positive",
  "actor": "UE simultaneously connected to the same 5G Core Network over 3GPP and non-3GPP access",
  "condition": "",
  "action": "be served by a single AMF in that 5G Core Network",
  "exception": "",
  "gold_summary_ko": "해당 UE는 그 5G Core Network에서 하나의 AMF에 의해 반드시 서비스되어야 한다."
}
```

전달 상태: `EXPLANATION`

설명 원문:

동일한 5G Core Network에 3GPP access와 non-3GPP access로 동시에 연결된 UE는 이 5G Core Network에서 단일 AMF의 서비스를 반드시 받아야 한다.

<details><summary>판정자 전용 PDF 전후 문맥 — 원래 모델 입력으로 소급하지 않음</summary>

```text
 
ETSI 
ETSI TS 123 501 V18.12.0 (2026-01)573GPP TS 23.501 version 18.12.0 Release 18
- the UE selects a PLMN/SNPN and an N3IWF in this PLMN/SNPN. The PLMN/SNPN/N3IWF selection and the 
non-3GPP access network selection are independent. The N3IWF selection is defined in clause 6.3.6. 
When the UE decides to use trusted non-3GPP access to connect to a 5G Core Network in a PLMN: 
- the UE first selects a PLMN/SNPN; and then 
- the UE selects a non-3GPP access network (a TNAN) that supports trusted connectivity to the selected 
PLMN/SNPN. In this case, the non-3GPP access network selection is affected by the PLMN/SNPN selection. 
A UE that accesses the 5G Core Network over a non-3GPP access shall, after UE registration, support NAS signalling 
with 5G Core Network control-plane functions using the N1 reference point. 
When a UE is connected via a NG-RAN and via a non-3GPP access, multiple N1 instances shall exist for the UE i.e. 
there shall be one N1 instance over NG-RAN and one N1 instance over non-3GPP access. 

[대상 문장]
. 
When a UE is connected to a 3GPP access of a PLMN, if the UE selects a N3IWF and the N3IWF is located in a PLMN 
different from the PLMN of the 3GPP access, e.g. in a different VPLMN or in the HPLMN, the UE is served separately 
by the two PLMNs. The UE is registered with two separate AMFs. PDU Sessions over the 3GPP access are served by 
V-SMFs different from the V-SMF serving the PDU Sessions over the non-3GPP access. The same can be true when 
the UE uses trusted non-3GPP access, i.e. the UE may select one PLMN for 3GPP access and a different PLMN for 
trusted non-3GPP access. 
NOTE: The registrations with different PLMNs over diff erent Access Types doesn't apply to UE registered for 
Disaster Roaming service as described in the clause 5.40. 
The PLMN selection for the 3GPP access does not depend on the PLMN that is used for non-3GPP access. In other 
words, if a UE is registered with a PLMN over a non-3GPP access, the UE perform
```

</details>

## V2-P1-111
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

UE는 네트워크로부터 새 configured NSSAI와 rejected NSSAI를 받으면, 기존에 저장된 해당 정보는 새 값으로 갱신해야 한다. 이 변경 절차는 등록 절차나 재구성 과정에서 네트워크가 제공한 최신 NSSAI 정보를 UE가 반영하는 방식으로 이해하면 된다.

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

## V2-P1-112
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

각 N3IWF, TNGF, TWIF 및 W-AGF는 다른 TAI 값으로 구성되도록 허용되며, 다른 N3IWFs, TNGFs, TWIFs 및/또는 W-AGFs와 동일한 TAI 값으로 구성되도록도 허용된다.

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

## V2-P1-113
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

## V2-P1-114
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

## V2-P1-115
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

UE는 3GPP access에 대해 N1 mode capability가 비활성화되었던 PLMN 또는 SNPN의 식별자를 기억하는 것이 권고된다. 원문은 특정 조건에서 기억할 대상을 PLMN 또는 SNPN의 identity로 한정한다.

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

## V2-P1-116
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

emergency callback을 가능하게 하기 위해, UE는 emergency services 완료 후 MICO mode 사용을 요청하기 전에 UE 구현별 지속 시간 동안 기다리는 것이 권고된다.

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

## V2-P1-117
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

전달 상태: `EXPLANATION`

설명 원문:

UE는 등록 절차 동안 REGISTRATION COMPLETE 메시지에서 네트워크에 SOR transparent container IE를 제공할 수 있다. 이는 기술적으로 가능한 동작을 뜻하며, 의무나 허용의 표현으로 바꾸지 않는다.

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

## V2-P1-118
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

전달 상태: `EXPLANATION`

설명 원문:

UE는 등록 절차 동안 REGISTRATION COMPLETE 메시지에서 SOR transparent container IE를 네트워크에 제공할 수 있다. 이는 허용 사항이며, 반드시 해야 한다는 의미는 아니다.

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

## V2-P1-119
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

dual-registration mode로 동작하는 UE가 initial registration procedure를 수행할 때, 반드시 5G NAS security context를 사용해야 하며 이 security context의 처리는 현 규격에 설명된 절차를 따라야 한다.

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

## V2-P1-120
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

## V2-P1-121
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

allowed NSSAI는 부속서 C에 명시된 방식에 따라 ME의 비휘발성 메모리에 저장하는 것이 권고된다.

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

## V2-P1-122
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

N3IWF, TNGF, TWIF, W-AGF는 각각 자신이 연결되는 비3GPP 액세스의 TAI 값을 구성할 때, 해당 액세스에 맞는 TAI 형식을 사용해야 한다. 즉, 이들 기능은 서로 다른 액세스 유형에 대해 동일한 TAI를 공유하는 것이 아니라, 각 기능이 담당하는 액세스에 대응하는 TAI value를 구성하는 관계이다.

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

## V2-P1-123
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

ngKSI가 가리키는 5G NAS security context는 새 N1 NAS signalling connection이 설정될 때 새 primary authentication and key agreement procedure를 수행하지 않고도, 또는 AMF가 security mode control procedure를 시작할 때 NAS 메시지의 안전한 교환을 설정하는 데 사용될 수 있다. 이는 기술적으로 가능한 상황을 설명하는 것이며, 별도의 새 인증 절차를 반드시 수행해야 한다는 뜻은 아니다.

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

## V2-P1-124
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

동일한 K AMF로 새 5G NAS security context를 유도할 때 target AMF는 Intra N1 mode NAS transparent container IE에 downlink NAS COUNT의 하위 8비트를 포함하고, 새 KAMF가 유도되어서는 안 된다고 표시한다.

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

## V2-P1-125
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

current 5G NAS security context는 native 또는 mapped 유형일 수 있으며, 즉 native 5G NAS security context 또는 mapped 5G NAS security context에서 기원할 수 있다. 이는 기술적으로 가능한 유형을 설명한다.

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

## V2-P1-126
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

최대 UE 수 도달 사유에 대해 해당 S-NSSAI와 연관된 T3526이 만료되면, UE는 그 S-NSSAI에 대한 해당 절차를 중단하고 이후 다시 시도할 수 있는 상태로 돌아가야 한다. 즉, 해당 S-NSSAI에 대해 더 이상 대기하지 않고 재시도 가능 상태로 전환하는 것이 요구된다.

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

## V2-P1-127
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

UE가 REGISTRATION REQUEST의 5GMM capability IE에 설정한 비트 또는 이전 등록 절차에서 AMF에 저장된 5GMM context의 비트와, UDM에서 얻은 사용자의 subscription context를 바탕으로 PC5 reference point를 통한 V2X communication 사용이 허용된 경우, AMF는 등록 절차 완료 직후 NAS signalling connection을 즉시 해제하지 않는 것이 권고된다.

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

## V2-P1-128
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

이 current 5G NAS security context는 native 또는 mapped 유형일 수 있으며, 즉 native 5G NAS security context 또는 mapped 5G NAS security context에서 기원할 수 있다. 이는 기술적으로 가능한 경우를 설명하는 것이다.

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

## V2-P1-129
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

5GS는 TSN network로 동작하는 경우 sub-network로 동작할 수 있다. 이는 clause 4.4.8.2의 아키텍처에 기반한 특별한 경우이다.

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
