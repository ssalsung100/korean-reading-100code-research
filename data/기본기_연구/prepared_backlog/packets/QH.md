# QH blind packet

- passage_group: G111
- group_case_ids: QH, QI, QJ, QK, QL
- blind_sources: data/기본기_연구/prepared_backlog/blind_sources/QH.json; data/기본기_연구/prepared_backlog/blind_sources/QI.json; data/기본기_연구/prepared_backlog/blind_sources/QJ.json; data/기본기_연구/prepared_backlog/blind_sources/QK.json; data/기본기_연구/prepared_backlog/blind_sources/QL.json
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.
