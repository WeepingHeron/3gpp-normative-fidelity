-- counts
SELECT status, COUNT(*) AS count, (SELECT COUNT(*) FROM eligibility_cases) AS total, 1.0 * COUNT(*) / (SELECT COUNT(*) FROM eligibility_cases) AS share FROM eligibility_cases GROUP BY status ORDER BY CASE status WHEN '적격' THEN 0 WHEN '사전 예외 조건부 적격' THEN 1 WHEN '부적격' THEN 2 ELSE 3 END;

-- by_modal
SELECT modal, SUM(status_code = 'ELIGIBLE') AS eligible, SUM(status_code = 'ELIGIBLE_WITH_RECORDED_EXCEPTION') AS exception, SUM(status_code = 'INELIGIBLE') AS ineligible, SUM(status_code = 'HOLD') AS hold, COUNT(*) AS total FROM eligibility_cases GROUP BY modal ORDER BY modal;

-- cases
SELECT case_id, status, source, locator, reason, next_action, source_text_en, question_ko FROM eligibility_cases ORDER BY case_id;
