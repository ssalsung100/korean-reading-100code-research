# YZ blind packet

- passage_group: G159
- group_case_ids: YZ, ZA, ZB, ZC
- blind_sources: data/기본기_연구/prepared_backlog/blind_sources/YZ.json; data/기본기_연구/prepared_backlog/blind_sources/ZA.json; data/기본기_연구/prepared_backlog/blind_sources/ZB.json; data/기본기_연구/prepared_backlog/blind_sources/ZC.json
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.
