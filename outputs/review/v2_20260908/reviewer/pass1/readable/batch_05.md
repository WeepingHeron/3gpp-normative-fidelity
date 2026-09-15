# pass1 검토 자료 173–215

원문·정답 참고 자료이며 판정은 별도 JSONL 사본에 기록한다.

## V2-P1-173
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

non-3GPP access로 5G Core Network에 접근하는 UE는 UE 등록 후 N1 reference point를 사용하여 5G Core Network 제어면 기능과 NAS signalling을 지원해야 한다.

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

## V2-P1-174
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

Non-Allowed Area에 있는 UE의 Registration Area는 UE의 NonAllowed Area에 속하는 TA들의 집합으로 구성하는 것이 권고된다.

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

## V2-P1-175
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

UE를 5GC에서 EPC로 redirect하기 위해, UE가 Registration Request 또는 Service Request를 보낼 때 AMF는 EMM cause 값으로 UE가 5GC를 사용하지 않아야 함을 나타내는 Registration Reject 또는 Service Reject를 보내는 것이 권고된다.

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

## V2-P1-176
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

non-3GPP access network는 trusted connectivity를 지원하는지 여부를 광고할 수 있다. 이 지원 정보는 해당 액세스 네트워크가 신뢰된 비3GPP 연결을 제공할 수 있는 범위를 나타내는 데 사용된다.

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

## V2-P1-177
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

동일한 K_AMF로 새 5G NAS security context를 유도할 때, target AMF는 Intra N1 mode NAS transparent container IE에 downlink NAS COUNT의 하위 8비트를 포함하고, 새 KAMF를 유도해서는 안 된다고 표시해야 한다. (9.11.2.6 참조)

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

## V2-P1-178
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

## V2-P1-179
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

AMF는 전체 PLMN paging을 피할 수 있도록 Active Time을 할당할 때 등록 영역(registration area)을 정해야 한다. 이 등록 영역은 가능한 한 제한적으로 설정하여, 단말이 Active Time 동안 더 작은 범위에서만 paging되도록 해야 한다.

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

## V2-P1-180
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

PDU Session establishment 절차 동안, 특정 PDU Session에 대해 SMF가 N6 interface의 network instance를 UPF에 표시하도록 허용된다. 이는 반드시 해야 하는 의무가 아니라 허용 사항이다.

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

## V2-P1-181
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

ME는 allowed NSSAI(s)를 부록 C에 명시된 방식에 따라 비휘발성 메모리에 저장하는 것이 권고된다.

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

## V2-P1-182
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

AMF가 UE에 active time value를 알릴 때, MICO indication IE의 all-PLMN 표시는 모든 PLMN에 대해 동일하게 적용되는 값으로 취급되어야 한다. 즉, 특정 PLMN에만 한정된 표시로 사용해서는 안 된다.

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

## V2-P1-183
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

5G NAS security를 활성화하기 전에 AMF와 UE는 5G NAS security context를 설정할 기술적 가능성이 있어야 한다. 이는 보안이 활성화되기 전의 전제조건이다.

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

## V2-P1-184
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

5GSM 메시지는 5GMM 전송 메시지 안에 캡슐화되어 전달되어야 한다. 즉, 5GSM 메시지는 5GMM 절차를 통해 운반되며 별도의 독립 전송으로 처리되지 않는다.

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

## V2-P1-185
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

UE가 capability bit와 subscription context에 따라 PC5 기반 V2X communication 권한을 가진 경우, 등록이 완료된 뒤에도 NAS signalling connection은 유지되며, 네트워크는 해당 권한을 고려해 이를 처리해야 한다. 즉, PC5 V2X 사용 가능 상태가 등록 후 NAS 연결 처리에 반영되도록 해야 한다.

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

## V2-P1-186
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

하나의 PDU Session에서 SMF는 로컬 UPF와 중앙 UPF를 함께 제어할 수 있으며, 이를 통해 단일 세션의 사용자 평면 경로를 분할해 구성할 수 있다. 이 구성에서는 로컬 UPF가 단말에 가까운 트래픽 처리를 담당하고, 중앙 UPF가 나머지 세션 처리를 담당하는 형태로 운용된다.

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

## V2-P1-187
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

UE가 같은 PLMN의 다른 access에서 등록하려는 경우, 첫 번째 access의 Registration procedure가 완료될 때까지 다른 access에서 등록을 시작해서는 안 된다.

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

## V2-P1-188
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

## V2-P1-189
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

partially allowed NSSAI 또는 partially rejected NSSAI에 포함되는 S-NSSAI의 수는 7을 초과해서는 안 된다.

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

## V2-P1-190
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

동일한 5G Core Network에 3GPP access와 non-3GPP access로 동시에 연결된 UE는 그 5G Core Network에서 단일 AMF에 의해 반드시 서비스되어야 한다.

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

## V2-P1-191
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

전체 PLMN paging을 피하기 위해, AMF가 Active Time을 할당할 때 UE에게 "all PLMN" registration area를 할당하지 않는 것이 권고된다.

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

## V2-P1-192
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

## V2-P1-193
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

5GS가 TSN network로 동작하는 경우, 5GS는 sub-network로 작동할 수 있다. 이는 4.4.8.2절의 아키텍처를 바탕으로 한 3GPP 규격에 의해 지원된다.

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

## V2-P1-194
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

UE가 N26 인터페이스를 지원하는 망에서 single-registration mode로 동작하고, emergency bearer services용 PDN connection은 있지만 현재 EPS security context가 없을 때, AMF는 S1 mode to N1 mode NAS transparent container IE에서 5G-IA0와 5G-EA0를 선택된 5G NAS security algorithms로 설정해야 한다.

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

## V2-P1-195
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

N1 mode에서 N1 mode로의 handover 중에도 새로운 5G NAS security context를 생성하도록 허용된다. 즉, 그 시점에 새 보안 컨텍스트를 만들 수 있다.

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

## V2-P1-196
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

Unavailability configuration IE가 없거나 EUPR이 종료 보고를 요구하는 경우, UE는 unavailability period가 끝난 뒤 종료 보고를 수행해야 한다. 즉, 해당 기간 종료 후 UE는 종료 사실을 네트워크에 보고하는 동작을 해야 한다.

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

## V2-P1-197
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

UE는 registration procedure 동안 REGISTRATION COMPLETE 메시지에서 SOR transparent container IE를 network에 제공할 수 있다. 이는 기술적으로 가능한 동작을 의미하며, 반드시 해야 하거나 허용만 되는 것으로 표현되지 않는다.

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

## V2-P1-198
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

UE는 3GPP access에 대해 N1 mode capability가 비활성화되었던 PLMN 또는 SNPN의 식별자를 기억하는 것이 권고된다.

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

## V2-P1-199
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

AMF가 Unavailability configuration IE를 제공하지 않거나, 해당 IE에서 EUPR 비트 값을 "UE needs to report end of unavailability period"로 설정한 경우, UE는 unavailability period duration이 끝났을 때 mobility registration update를 위한 registration procedure를 트리거하는 것이 권고된다.

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

## V2-P1-200
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

UE는 현재 TAI와 현재 셀의 CGI가 multicast MBS session의 MBS service area에 속하지 않고, UE가 해당 MBS service area에 대한 유효한 정보를 가진 경우 local MBS service를 위한 multicast MBS session join request를 하지 않는 것이 권고된다.

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

## V2-P1-201
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

5GSM 메시지는 5GMM transport message의 정보 요소 안에서 전송될 수 있다. 이는 기술적으로 가능한 방식이다.

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

## V2-P1-202
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

## V2-P1-203
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

ngKSI가 가리키는 5G NAS security context는 새 N1 NAS 시그널링 연결이 새 primary authentication and key agreement 절차 없이 설정되거나, AMF가 security mode control 절차를 시작할 때 NAS 메시지의 안전한 교환을 확립하기 위해 사용될 수 있다. 이는 기술적으로 가능한 상황을 설명한다.

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

## V2-P1-204
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

동일한 5G Core Network에 3GPP access와 non-3GPP access로 동시에 연결된 UE는 이 5G Core Network에서 단일 AMF에 의해 반드시 서비스되어야 한다.

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

## V2-P1-205
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

current 5G NAS security context는 현재 5G NAS 보호에 사용 중인 보안 컨텍스트를 뜻하며, 일반적으로 5G NAS 보안 컨텍스트와 그에 대응하는 키 자료를 포함한다. 이 유형은 5G NAS 보안 절차에서 현재 활성 상태인 컨텍스트로 취급된다.

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

## V2-P1-206
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

AMF가 UE에 active time value를 알리는 경우, AMF는 UE에 대한 MICO indication IE에서 "all PLMN registration area allocated" 표시를 하지 않는 것이 권고된다.

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

## V2-P1-207
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

동일한 5G Core Network에 3GPP access와 non-3GPP access로 동시에 연결된 UE의 경우, AMF는 두 접속에 대해 각각 별도의 AMF 인스턴스로 구성될 수 있다. 이때 두 AMF는 서로 연관되어 하나의 UE에 대한 이동성 및 등록 상태를 일관되게 처리하도록 구성된다.

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

## V2-P1-208
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

initial registration 절차에서 키 K_AUSF가 유효하지 않을 때, UE는 ngKSI를 반드시 삭제해야 한다.

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

## V2-P1-209
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

UE가 N26 인터페이스를 지원하는 망에서 single-registration mode로 동작하고, emergency bearer services용 PDN connection은 있지만 현재 EPS security context가 없을 때, AMF는 S1 mode to N1 mode NAS transparent container IE에서 선택된 5G NAS security algorithms로 5G-IA0과 5G-EA0를 반드시 설정해야 한다.

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

## V2-P1-210
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

N1 mode에서 N1 mode로의 handover 중에 새로운 5G NAS security context가 생성될 수 있도록 허용된다. 원문은 생성 시점을 그 handover 동안으로만 제시하며, 반드시 생성해야 한다고는 하지 않는다.

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

## V2-P1-211
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

UE는 최대 UE 수 도달로 인해 거부된 S-NSSAI들에 대해, 해당 S-NSSAI들과 연관된 T3526이 만료되면 그 S-NSSAI들을 rejected NSSAI에서 제거하도록 허용된다. 이 허용은 거부 사유가 "S-NSSAI not available due to maximum number of UEs reached"인 S-NSSAI(s)에만 적용된다.

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

## V2-P1-212
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

primary RAT restriction을 모두 강제하기 위해서는 관련 RAT가 서로 다른 Tracking Area Code들에 배치되어야 하며, 가입자는 해당 RAT를 사용하는 TA에서 네트워크에 접근하도록 허용되어서는 안 된다.

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

## V2-P1-213
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

N26 지원망의 single-registration mode UE가 emergency bearer PDN connection은 보유하지만 현재 EPS security context가 없으면, AMF는 해당 상황에 맞는 보안 알고리즘을 설정해야 한다. 즉, 비상 서비스용 연결이 존재하더라도 현재 EPS 보안 컨텍스트가 없을 때는 AMF가 적절한 알고리즘 선택을 수행하는 것이 의무이다.

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

## V2-P1-214
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

등록 절차 또는 일반 UE 구성 업데이트 절차 동안 configured NSSAI와 rejected NSSAI를 변경하도록 허용된다.

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

## V2-P1-215
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

non-3GPP access network는 자신이 trusted connectivity를 지원하는 PLMN 또는 SNPN과, 지원하는 trusted connectivity의 유형(예: "5G connectivity")을 광고할 수 있다.

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
