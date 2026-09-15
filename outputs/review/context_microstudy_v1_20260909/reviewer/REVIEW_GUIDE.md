# 문맥 개발 실험의 개별 평가 안내

동결 protocol.json의 두 의미 결과 축을 explanation_ko만으로 판단한다. 사례별 참고 문맥은 모든 packet에 있지만 실제 생성자 제공 여부는 additional_context_supplied_to_generator로 구분한다. 이전 검토 결과·조건 키·다른 평가자의 판정은 읽지 않는다. 문맥 제공 여부는 의미 평가에 필요해 숨기지 않으며 완전한 눈가림을 주장하지 않는다.

각 requirement_coverage는 고정 requirement_id 순서로 1/0/null을 직접 판정하고 정확한 응답 인용과 이유를 기록한다. 표현 일치를 요구하지 않지만 복합 requirement에 열거된 모든 조건·삭제 trigger가 남아야 1이다. 누락/명시적 상충은 0, 해석 불확실성은 null이다. 새 요구사항을 추가하지 않는다.

unsupported_or_distorted_claim은 실제 제공된 target/question/context에 대한 미지원 주장 또는 의미 왜곡의 존재다. SHORT에서 제공되지 않은 문맥을 생략한 사실 자체는 왜곡이 아니다. 반대로 참고 문맥에 사실상 맞는 추가 정보여도 실제 입력에 근거가 없다면 source-only 설명의 미지원 주장일 수 있다. 질문은 물음을 제공할 뿐 그에 대한 답 자체를 근거로 공급하지 않는다.

모든 항목이 1이고 미지원/왜곡이 false이면 전체 완수 1이다. 항목에 0이 있거나 미지원/왜곡이 true이면 전체 완수 0이다. 나머지 불확실성은 null이다. 거절·빈응답·잘린 생성은 전체 pipeline 완수 0으로 별도 delivery 상태와 기록하며 의미 오역으로 자동 분류하지 않는다.

JSON 메타데이터는 대상 영문 문장 기준으로 별도 감사한다. metadata_inconsistency는 metadata와 explanation 사이의 모순을 기록하고, target과의 metadata 오류도 metadata_rationale에 구분해 적는다. 올바른 metadata로 설명을 보충하거나 잘못된 metadata 하나만으로 설명 점수를 바꾸지 않는다. 인용 필드와 문체는 주 의미 완수 판정의 대용이 아니다.

사전 source review의 공통 주의사항: CTX-002의 저장 자체는 should/can이며 저장 의무로 강화하지 않는다. SUPI 결합/일치/삭제와 긴급/eCall 임시 저장·삭제 조건을 별도로 읽는다. Annex C 전체/HPLMN 매핑은 고정된 요구사항이 아니므로 자동 누락 감점하지 않는다. FULL의 일부 문맥은 target 반복을 포함하며 이것은 실험 해석의 제한이다.

24개를 모두 개별 작성한다. 실제 기록 시각과 검토자 식별자를 남기고 각 판정을 설명과 exact quote에 연결한다. 코드로 기본 판정을 채우거나 다른 응답 판정을 복사하지 않는다. 결과 파일을 별도 위치에 기록하고 봉인한 후 대조한다. 같은 모델 계열의 별도 AI 검토는 사람 전문가나 통계적 오류 독립을 보장하지 않는다.
