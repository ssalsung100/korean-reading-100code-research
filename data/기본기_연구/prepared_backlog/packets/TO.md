# TO blind packet

- passage_group: G128
- group_case_ids: TO, TP, TQ, TR, TS, TT
- blind_sources: data/기본기_연구/prepared_backlog/blind_sources/TO.json; data/기본기_연구/prepared_backlog/blind_sources/TP.json; data/기본기_연구/prepared_backlog/blind_sources/TQ.json; data/기본기_연구/prepared_backlog/blind_sources/TR.json; data/기본기_연구/prepared_backlog/blind_sources/TS.json; data/기본기_연구/prepared_backlog/blind_sources/TT.json
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.
