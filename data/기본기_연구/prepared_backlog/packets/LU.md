# LU blind packet

- passage_group: G083
- group_case_ids: LU, LV, LW, LX, LY
- blind_sources: data/기본기_연구/prepared_backlog/blind_sources/LU.json; data/기본기_연구/prepared_backlog/blind_sources/LV.json; data/기본기_연구/prepared_backlog/blind_sources/LW.json; data/기본기_연구/prepared_backlog/blind_sources/LX.json; data/기본기_연구/prepared_backlog/blind_sources/LY.json
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.
