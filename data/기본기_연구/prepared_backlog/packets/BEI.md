# BEI blind packet

- passage_group: G401
- group_case_ids: BEG, BEH, BEI
- blind_sources: data/기본기_연구/prepared_backlog/blind_sources/BEG.json; data/기본기_연구/prepared_backlog/blind_sources/BEH.json; data/기본기_연구/prepared_backlog/blind_sources/BEI.json
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.
