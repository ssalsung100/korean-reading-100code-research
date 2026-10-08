# UY blind packet

- passage_group: G135
- group_case_ids: UY, UZ, VA, VB, VC, VD
- blind_sources: data/기본기_연구/prepared_backlog/blind_sources/UY.json; data/기본기_연구/prepared_backlog/blind_sources/UZ.json; data/기본기_연구/prepared_backlog/blind_sources/VA.json; data/기본기_연구/prepared_backlog/blind_sources/VB.json; data/기본기_연구/prepared_backlog/blind_sources/VC.json; data/기본기_연구/prepared_backlog/blind_sources/VD.json
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.
