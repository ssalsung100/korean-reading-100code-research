# ML blind packet

- passage_group: G087
- group_case_ids: ML, MM, MN, MO, MP
- blind_sources: data/기본기_연구/prepared_backlog/blind_sources/ML.json; data/기본기_연구/prepared_backlog/blind_sources/MM.json; data/기본기_연구/prepared_backlog/blind_sources/MN.json; data/기본기_연구/prepared_backlog/blind_sources/MO.json; data/기본기_연구/prepared_backlog/blind_sources/MP.json
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.
