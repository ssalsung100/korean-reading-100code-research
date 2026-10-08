# IT blind packet

- case_id: IT
- passage_group: G057
- blind_source: data/기본기_연구/prepared_backlog/blind_sources/IT.json
- group_case_ids: IS, IT, IU
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 이 anonymous blind-only source만 읽는다. group 전체 blind 및 independent_code raw 저장 전 sealed 자료를 열지 않는다.
