# AIA blind packet

- passage_group: G211
- group_case_ids: AIA, AIB, AIC, AID
- blind_sources: data/기본기_연구/prepared_backlog/blind_sources/AIA_official_stem.json; data/기본기_연구/prepared_backlog/blind_sources/AIB.json; data/기본기_연구/prepared_backlog/blind_sources/AIC.json; data/기본기_연구/prepared_backlog/blind_sources/AID.json
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 문학 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.
