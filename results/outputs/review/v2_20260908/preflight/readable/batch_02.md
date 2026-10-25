# preflight 검토 자료 18–34

원문·정답 참고 자료이며 판정은 별도 JSONL 사본에 기록한다.

## G018
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

## G019
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

## G020
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

## G021
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

## G022
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

## G023
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

## G024
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

## G025
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

## G026
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

## G027
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

## G028
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

## G029
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

## G030
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

## G031
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

## G032
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

## G033
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

## G034
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
