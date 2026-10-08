# AFB blind packet

- passage_group: G193
- group_case_ids: AFB, AFC, AFD, AFE
- blind_source: data/기본기_연구/prepared_backlog/blind_sources/AFB.json
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 group 전체의 anonymous blind-only source만 먼저 읽고 stage barrier를 지킨다.
