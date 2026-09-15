# pass1 검토 자료 130–172

원문·정답 참고 자료이며 판정은 별도 JSONL 사본에 기록한다.

## V2-P1-130
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

non-3GPP access network는 자신이 trusted connectivity를 지원하는 PLMN 또는 SNPN과, 지원하는 trusted connectivity의 유형(예: "5G connectivity")을 광고하도록 허용된다.

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

## V2-P1-131
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

N5CW device가 trusted WLAN access network에 연결하기 위해 EAP-based access authentication 절차를 수행하는 경우, PLMN 또는 SNPN의 5GC에 동시에 등록되어 있을 수 있도록 허용된다.

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

## V2-P1-132
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

UE는 등록 절차 동안 REGISTRATION COMPLETE 메시지에서 네트워크에 SOR transparent container IE를 제공할 수 있다. 이는 기술적으로 가능한 동작이다.

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

## V2-P1-133
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

선택된 PLMN/SNPN이 UE의 위치에서 계속 서비스를 제공할 수 있는 동안에는, 네트워크는 UE를 다른 이용 가능한 PLMN/SNPN으로 이동시키지 않는 것이 권고된다. 예를 들어 핸드오버를 통해 이동시키는 것도 권고되지 않는다.

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

## V2-P1-134
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

Nudr를 통해 UDR에 접근하는 NF Service Consumer는 자신이 변경하도록 권한을 부여받은 데이터만 추가, 수정, 갱신 또는 삭제할 수 있어야 한다. 즉, 권한이 없는 데이터는 변경 범위에 포함되지 않는다.

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

## V2-P1-135
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

AMF는 UE의 unavailability period 정보를 바탕으로 mobile reachable timer와 implicit deregistration timer를 설정해야 한다. 이때 두 타이머는 UE가 다시 도달 가능해질 것으로 예상되는 시점과 암묵적 등록 해제 시점을 반영하도록 조정된다.

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

## V2-P1-136
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

non-3GPP access로 5G Core Network에 접근하는 UE는 UE 등록 후 반드시 N1 reference point를 사용하여 5G Core Network 제어면 기능과 NAS signalling을 지원해야 한다.

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

## V2-P1-137
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

5GS는 TSN network로 동작하는 경우 sub-network로 작동할 수 있다. 이는 clause 4.4.8.2의 architecture를 기반으로 하는 3GPP specifications에 의해 지원된다.

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

## V2-P1-138
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

Nudr를 통해 UDR에 접근하는 각 NF Service Consumer는 자신이 변경하도록 권한을 부여받은 데이터만 추가, 수정, 갱신 또는 삭제할 수 있도록 반드시 되어야 한다. 권한이 없는 데이터는 변경 범위에 포함되지 않는다.

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

## V2-P1-139
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

UE는 emergency service가 완료된 뒤 emergency callback을 지원하기 위해, MICO mode를 요청하기 전에 먼저 MICO mode를 해제하거나 요청하지 않는 상태로 두어야 한다. 즉, emergency callback이 가능하도록 일반적인 연결 가능 상태를 유지하는 것이 요구된다.

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

## V2-P1-140
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

UE가 한 access에서 등록 중이고 같은 PLMN의 다른 access로도 등록하려는 경우, 첫 번째 access의 Registration procedure가 완료될 때까지 다른 access에서의 등록을 시작해서는 안 된다.

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

## V2-P1-141
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

NAS transport procedure에서 default configured NSSAI를 변경하려면, UE는 해당 변경을 NAS 메시지로 네트워크에 전달해야 한다. 이 절차는 UE가 새 default configured NSSAI를 설정하거나 기존 값을 갱신하는 데 사용된다.

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

## V2-P1-142
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

UE가 registration 과정에서 MICO mode 선호를 표시하지 않은 경우, AMF는 UE를 MICO mode로 등록하거나 MICO 관련 동작을 적용해서는 안 된다. 즉, MICO mode는 UE가 명시적으로 선호를 표시한 경우에만 고려된다.

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

## V2-P1-143
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

ngKSI가 가리키는 5G NAS security context는 새 N1 NAS signalling connection이 새 primary authentication and key agreement procedure 없이 설정되거나, AMF가 security mode control procedure를 시작하는 경우에 NAS 메시지의 안전한 교환을 위해 사용하도록 허용된다.

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

## V2-P1-144
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

UE는 ngKSI를 삭제해야 하는 경우 ngKSI 값을 "no key is available"로 설정해야 하며, 관련된 K AMF 또는 K'AMF, 5G NAS 암호화 키, 5G NAS 무결성 키도 무효로 간주해야 한다. 즉, ngKSI와 연관된 5G NAS 보안 컨텍스트는 더 이상 유효하지 않은 것으로 본다.

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

## V2-P1-145
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

dual-registration mode로 동작하는 UE는 initial registration procedure를 수행할 때 반드시 5G NAS security context를 사용하기 시작해야 하며, 이 security context의 처리는 본 규격에 설명된 방식에 따라 따라야 한다.

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

## V2-P1-146
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

UE를 5GC에서 EPC로 redirect할 때, UE가 Registration Request 또는 Service Request를 보내면 AMF는 EMM cause 값으로 UE가 5GC를 사용하지 않아야 함을 나타내는 Registration Reject 또는 Service Reject를 보낸다. 이는 UE가 5GC를 사용하지 않는 것이 권고된다는 뜻이다.

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

## V2-P1-147
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

non-3GPP access로 5G Core Network에 접근하는 UE는 UE 등록 후 N1 reference point를 사용하여 5G Core Network 제어면 기능과 NAS signalling을 지원해야 한다. 이는 반드시 해야 하는 의무이다.

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

## V2-P1-148
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

UE가 REGISTRATION REQUEST의 5GMM capability IE에 설정한 비트 또는 이전 등록 절차 동안 AMF에 저장된 5GMM context의 비트 중 하나 이상과, UDM에서 얻은 사용자의 subscription context를 바탕으로 PC5 reference point를 통한 V2X communication 사용이 허가된 경우, AMF는 등록 절차 완료 직후 NAS signalling connection을 즉시 해제하지 않는 것이 권고된다.

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

## V2-P1-149
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

N5CW device가 trusted WLAN access network에 연결하기 위해 EAP 기반 access authentication procedure를 수행할 때, 그 N5CW device는 PLMN 또는 SNPN의 5GC에 동시에 등록되어 있을 수 있도록 허용된다.

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

## V2-P1-150
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

NAS transport procedure 중에는 UE parameters update transparent container를 UE로 보내는 방식으로 default configured NSSAI를 변경할 수 있다.

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

## V2-P1-151
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

UE가 SNPN onboarding service에 등록 중이거나 이미 등록된 경우, serving SNPN은 UE에게 configured NSSAI를 제공해야 한다. 이는 해당 상태의 UE에 대해 serving SNPN의 NSSAI 제공 정책이 적용됨을 의미한다.

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

## V2-P1-152
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

Non-Allowed Area에 있는 UE의 Registration Area는 UE의 Non-Allowed Area에 속하는 TA들의 집합으로 구성하는 것이 권고된다.

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

## V2-P1-153
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

UE는 registration procedure에서 SOR transparent container IE를 등록 요청 메시지에 포함하여 네트워크에 전달해야 한다. 이 IE는 UE가 보유한 SOR 정보를 네트워크로 전달하는 용도로 사용된다.

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

## V2-P1-154
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

각 N3IWF, TNGF, TWIF 및 W-AGF는 다른 N3IWFs, TNGFs, TWIFs 및/또는 W-AGFs와 다른 TAI 값으로 구성되거나 같은 TAI 값으로 구성되도록 허용된다.

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

## V2-P1-155
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

dual-registration mode로 동작하는 UE가 initial registration procedure를 수행할 때, 반드시 5G NAS security context를 사용하기 시작해야 하며, 이 security context의 처리는 현 규격에 설명된 절차를 따라야 한다.

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

## V2-P1-156
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

NG-RAN node가 N2 인터페이스 OVERLOAD START 메시지 수신 때문에 UAC를 시작하기로 결정한 경우, 해당 NG-RAN node는 OVERLOAD START 메시지에 포함된 요청과 관련되고 이 NG-RAN node에 연결된 모든 AMF가 네트워크에 접근하는 UE에 대한 부하 제한을 요청할 때에만 그러한 절차를 시작하는 것이 권고된다.

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

## V2-P1-157
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

non-3GPP access로 5G Core Network에 접근하는 UE는 UE 등록 후 N1 reference point를 사용하여 5G Core Network 제어면 기능과 NAS signalling을 지원해야 한다. 이는 반드시 해야 하는 의무이다.

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

## V2-P1-158
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

allowed NSSAI는 ME의 비휘발성 저장소에 저장해야 하며, 일반적으로 PLMN별로 구분하여 보관해야 한다. 저장 방식은 해당 PLMN에 대해 네트워크가 허용한 NSSAI를 유지하고, 이후 등록 절차에서 재사용할 수 있도록 하는 것이다.

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

## V2-P1-159
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

AMF는 Disaster Roaming 서비스에 등록된 UE의 registration area를 할당할 때, 해당 UE가 재난 로밍 서비스에 대해 허용된 TAI 범위 안에서만 등록 영역을 구성해야 한다. 즉, 등록 영역은 재난 로밍용으로 지정된 TAI들로 제한되어야 하며 그 범위를 벗어난 TAI는 포함해서는 안 된다.

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

## V2-P1-160
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

NAS transport procedure 중에는 UE에 UE parameters update transparent container를 보내는 방식으로 default configured NSSAI를 변경하도록 허용된다.

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

## V2-P1-161
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

UE가 어떤 PLMN에서 configured NSSAI와 allowed NSSAI를 모두 가지고 있지 않으면, HPLMN의 default configured NSSAI를 사용해 NSSAI를 처리하는 것이 권고된다. 즉, 해당 PLMN에서 별도 NSSAI 정보가 없을 때 HPLMN 기본 구성을 기준으로 동작하도록 하는 방향이다.

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

## V2-P1-162
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

5GS가 Paging Policy Differentiation(PPD) 기능을 지원하는 경우, 애플리케이션이 설정한 DSCP 값(TOS in IPv4 / TC in IPv6)에 따라 특정 IP packet에 적용할 Paging Policy가 선택되는 것이 권고된다. 즉, 애플리케이션은 DSCP 값을 통해 5GS에 어떤 Paging Policy를 적용할지 표시한다.

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

## V2-P1-163
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

N38 reference point는 같은 VPLMN의 V-SMF들 사이에 있을 수 있고, 서로 다른 VPLMN의 V-SMF들 사이에도 있을 수 있다. 이는 기술적으로 가능하며, 서로 다른 VPLMN 간 이동성을 지원하기 위한 것이다.

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

## V2-P1-164
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

AMF는 clause 5.40.4에 따라 Disaster Roaming service에 등록된 UE의 registration area를 할당할 때, Disaster Condition이 있는 영역을 포함하는 TAI만 반드시 고려해야 한다. 다른 TAI는 고려해서는 안 된다.

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

## V2-P1-165
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

## V2-P1-166
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

NAS transport procedure 중에는 UE에 UE parameters update transparent container를 보내는 방식으로 default configured NSSAI를 변경하도록 허용된다.

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

## V2-P1-167
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

관련 RAT가 서로 다른 Tracking Area Codes에 배치되어 있어 모든 primary RAT restriction을 적용하는 경우, subscriber는 해당 제한된 RAT를 사용하는 TA에서 네트워크에 접근해서는 안 된다.

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

## V2-P1-168
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

동일한 K_AMF로 새 5G NAS security context를 유도할 때, target AMF는 Intra N1 mode NAS transparent container IE에 downlink NAS COUNT의 하위 8비트를 포함하고, 새 K_AMF가 유도되어서는 안 된다고 표시해야 한다. 이 표시를 통해 새 K_AMF 유도 금지를 나타낸다.

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

## V2-P1-169
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

N1 mode에서 N1 mode로의 handover 중에는 새로운 5G NAS security context가 생성되도록 허용된다. 이는 해당 시점에 생성될 수 있음을 뜻하며, 반드시 생성해야 한다는 의미는 아니다.

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

## V2-P1-170
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

등록 절차 중 UE가 MICO mode 선호를 표시하지 않으면, AMF는 이 UE에 대해 MICO mode를 활성화해서는 안 된다.

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

## V2-P1-171
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

UE를 5GC에서 EPC로 redirect할 때, UE가 Registration Request 또는 Service Request를 보낸 경우 AMF는 Registration Reject 또는 Service Reject의 EMM cause 값으로 UE가 5GC를 사용하지 않아야 함을 전달한다. 이는 UE의 5GC 사용에 대한 하지 않는 것이 권고됨을 의미한다.

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

## V2-P1-172
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

5G NAS security를 활성화하기 전에 AMF와 UE는 5G NAS 보안 컨텍스트를 수립할 기술적 가능성이 있어야 한다. 즉, 보안 활성화의 전제조건은 AMF와 UE가 5G NAS security context를 establish하는 것이다.

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
