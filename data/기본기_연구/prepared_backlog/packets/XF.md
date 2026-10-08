# XF blind packet

- passage_group: G147
- group_case_ids: XF, XG, XH, XI
- blind_sources: data/기본기_연구/prepared_backlog/blind_sources/XF.json; data/기본기_연구/prepared_backlog/blind_sources/XG.json; data/기본기_연구/prepared_backlog/blind_sources/XH.json; data/기본기_연구/prepared_backlog/blind_sources/XI.json
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.
