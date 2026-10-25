# preflight 검토 자료 35–51

원문·정답 참고 자료이며 판정은 별도 JSONL 사본에 기록한다.

## G035
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

## G036
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

## G037
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

## G038
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

## G039
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

## G040
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

## G041
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

## G042
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

## G043
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

## G044
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

## G045
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

## G046
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

## G047
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

## G048
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

## G049
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

## G050
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

## G051
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
