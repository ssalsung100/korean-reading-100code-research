# BDY blind packet

- passage_group: G398
- group_case_ids: BDX, BDY, BDZ
- blind_sources: data/기본기_연구/prepared_backlog/blind_sources/BDX.json; data/기본기_연구/prepared_backlog/blind_sources/BDY.json; data/기본기_연구/prepared_backlog/blind_sources/BDZ.json
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.
