# Fresh AI context review — 24 responses

검토자: fresh-context AI /root/microstudy_fresh_review_24
최종 기록 시각(UTC): 2026-09-09T06:24:15.735509+00:00

허용된 동결 protocol/cases/prompt/schema/input manifest, reviewer guide/packets/blank judgments, source preflight review.json/md만 읽었다. root_review, coordinator 조건 키, 실험 raw run, README/결과 문서, 과거 v2 판정, 다른 agent 기록, MEMORY는 읽지 않았다. 원본 PDF/TXT/PNG는 이번 검토에서 직접 열지 않았다. 원문 의미 판단은 packet/cases에 포함된 인용과 이미 허용된 source preflight 기록을 사용했다. 따라서 원본 PDF 재검증 수행을 주장하지 않는다.

24개 packet을 MCR-001부터 MCR-024까지 순서대로 읽고 개별 의미 판정을 작성했다. 각 기록의 reviewed_at은 실제 파일 기록 시각이며, 마지막 자가 재검토에서 MCR-010의 불명확한 조건 연결을 null로 남기면서 해당 기록 시각을 갱신했다. 코드는 수동으로 작성한 판정의 직렬화와 ID/인용/타입/전체 규칙 검증에만 사용했고 응답 텍스트의 의미를 추론하여 점수를 채우는 코드는 쓰지 않았다. 모든 packet delivery_status는 EXPLANATION이었다. 거절/빈응답/잘림은 이번 packet에서 확인되지 않았으며, 별도 raw generation의 완전성을 재감사한 것은 아니다.

## 적용한 판정 정책

- 의미 완전성 및 미지원/왜곡은 explanation_ko 전체만 평가했다. metadata는 target 문장 기준 별도 감사했다. 라벨이 정확해도 설명을 복구하지 않고 라벨만 잘못된 경우 설명 점수를 바꾸지 않았다.
- should not을 맥락상 단정적인 해서는 안 된다/경우에만 할 수 있다로 옮기고 권고를 표현하지 않으면 강도 강화로 판정했다. should를 단정적인 저장해야 한다/저장되어야 한다로 옮긴 경우도 의무화다. 반면 저장해야 한다고 권고된다는 바깥 권고가 명시된 표현은 권고로 읽었다.
- capability의 선택성이 능력 보유에 걸리는지를 확인했다. 첫 문장의 정확성만 취하고 불명확한 후속 선행조건을 버리지 않았다. 단일 세션과 두 UPF 대상은 별도로 판정했다.
- CTX-002 저장 자체의 should/can과 SUPI 결합/일치 시만 사용/불일치 삭제를 분리했다. 저장 의무화는 STORAGE_RECOMMENDATION/claim 축에서 기록하며 identity의 실제 보존 여부와 중복 혼동하지 않았다.
- 복합 예외는 저장 금지 매체, ME 임시 저장, 모든 열거된 삭제 trigger를 함께 확인했다. emergency에만 문법적으로 붙은 저장 조항을 eCall로 자동 확장하지 않았다. HPLMN/VPLMN 매핑이나 Annex C 전체, CTX-003의 NOTE 전체를 새 요구사항으로 추가하지 않았다.
- 실제 additional_context_supplied_to_generator=false인 경우 누락된 문맥 요구를 INPUT_CONTEXT_GAP으로 남겼다. 이 누락 자체를 왜곡으로 세지 않았고, 질문의 예외 명칭도 예외 내용의 근거로 쓰지 않았다. 비-SNPN이라는 질문의 적용 사례를 받아 설명하는 것과 target 문장 자체를 비-SNPN에만 한정하는 주장을 구별했다. 후자의 metadata 확장은 별도 범위 오류로 기록했다.
- 설명 누락과 metadata 모순은 다르다. metadata에만 있는 정확한 예외를 설명에 보충하지 않았으며, metadata의 condition/exception 역할 배치나 추가 문맥 합성은 target 기준 오류로 별도 기록했다. 모호한 라벨 하나로 확정적인 사실 명제를 만들어내지 않았다.
- overall은 요구 0 또는 확인된 미지원/왜곡 true가 하나라도 있으면 0, 그 외 미해결 의미 항목이 있으면 null, 모두 1 및 claim false일 때만 1이다. metadata의 null은 이 의미 overall 계산에 포함하지 않았다.

## 애매하거나 해석 주의가 필요한 기록

- MCR-008: 비-SNPN 언급을 질문의 적용 사례로 읽었으며 다른 모드의 적용을 명시적으로 배제하지 않는다고 판단했다. explanation의 저장 권고는 보존된다. metadata condition이 target에 없는 모드 조건을 포함한 문제는 별도다.
- MCR-010: 첫 문장의 선택적 능력은 정확하지만 “해당 기능을 갖는 경우에만 적용된다.”가 제어 실행을 뜻하는지, 능력 보유 허용 자체의 선행조건인지 불분명하다. 이 자가 재검토는 봉인 전에 이루어졌고 다른 검토 결과를 읽지 않았다. CAPABILITY_POSSESSION, claim, overall 및 cross-field 모순은 null이다. 두 UPF/단일 세션 대상은 명확하다.
- MCR-011/016/019: 긴급 서비스 등록 해제 삭제를 누락했다. eCall 세 삭제 trigger는 있어도 eCall에 대한 금지 매체와 임시 저장이 별도로 없다. 앞 긴급 서비스 조건을 자동 상속하지 않았다. metadata에 정보가 더 있어도 설명 coverage에는 쓰지 않았다.
- MCR-017: “저장해야 한다고 권고된다.”는 저장 의무라는 단정을 인용한 것이 아니라 전체 저장 명제를 권고하는 표현으로 읽었다. 비-SNPN 여부와 예외가 target에 직접 없다는 유보는 입력 범위에 충실하다.
- MCR-022: “eCall only mode인 경우에도 동일하게 저장하지 않고”에서 앞 USIM/비휘발성 저장 금지는 연결되지만 “동일하게”가 ME 임시 저장까지 포함하는지는 확정하기 어렵다. ECALL_EXCEPTION=null이다. 긴급 등록 해제 삭제의 명확한 누락 및 저장 의무화 때문에 overall은 0이다.
- MCR-023: explanation은 선택적 능력을 명시해 두 의미 요구를 충족한다. metadata의 capability/action=control은 target의 선택적 능력 보유 객체를 잃는 오류다. 그러나 라벨만으로 이미 모든 SMF가 능력을 보유한다고 명제화할 수 있는지는 불명확하여 metadata_inconsistency=null로 남겼다. 이 메타데이터 불확실성은 설명 overall을 바꾸지 않는다.

이 검토는 같은 모델 계열의 별도 fresh AI context 검토다. 사람 전문가 검증이나 통계적 오류 독립을 보장하지 않는다. 문맥 제공 여부는 평가에 필요하여 보였고, 응답별 hint/replicate 조건 키는 읽지 않았다. 완전한 눈가림, held-out 평가, 일반화 가능한 성능을 주장하지 않는다. 조건별 집계나 다른 검토자의 판정과의 대조는 이 검토에서 수행하지 않았다.
