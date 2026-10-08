# US blind packet

- passage_group: G134
- group_case_ids: US, UT, UU, UV, UW, UX
- blind_sources: data/기본기_연구/prepared_backlog/blind_sources/US.json; data/기본기_연구/prepared_backlog/blind_sources/UT.json; data/기본기_연구/prepared_backlog/blind_sources/UU.json; data/기본기_연구/prepared_backlog/blind_sources/UV.json; data/기본기_연구/prepared_backlog/blind_sources/UW.json; data/기본기_연구/prepared_backlog/blind_sources/UX.json
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.
