# XS blind packet

- passage_group: G150
- group_case_ids: XS, XT, XU, XV, XW, XX
- blind_sources: data/기본기_연구/prepared_backlog/blind_sources/XS.json; data/기본기_연구/prepared_backlog/blind_sources/XT.json; data/기본기_연구/prepared_backlog/blind_sources/XU.json; data/기본기_연구/prepared_backlog/blind_sources/XV.json; data/기본기_연구/prepared_backlog/blind_sources/XW.json; data/기본기_연구/prepared_backlog/blind_sources/XX.json
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.
