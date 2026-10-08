# AIL blind packet

- passage_group: G214
- group_case_ids: AIL, AIM, AIN, AIO
- blind_sources: data/기본기_연구/prepared_backlog/blind_sources/AIL_official_stem.json; data/기본기_연구/prepared_backlog/blind_sources/AIM.json; data/기본기_연구/prepared_backlog/blind_sources/AIN.json; data/기본기_연구/prepared_backlog/blind_sources/AIO.json
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 문학 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.
