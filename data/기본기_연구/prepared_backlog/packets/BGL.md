# BGL blind packet

- passage_group: G420
- group_case_ids: BGJ, BGK, BGL
- blind_sources: data/기본기_연구/prepared_backlog/blind_sources/BGJ.json; data/기본기_연구/prepared_backlog/blind_sources/BGK.json; data/기본기_연구/prepared_backlog/blind_sources/BGL.json
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.
