# JL blind packet

- case_id: JL
- passage_group: G063
- blind_source: data/기본기_연구/prepared_backlog/blind_sources/JL.json
- group_case_ids: JJ, JK, JL, JM
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 이 anonymous blind-only source만 읽는다. group 전체 blind raw와 independent_code raw 저장 전에는 봉인 자료를 열지 않는다.
