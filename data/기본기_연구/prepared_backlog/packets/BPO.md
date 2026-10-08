# BPO blind packet

- passage_group: G501
- group_case_ids: BPO, BPP, BPQ
- blind_sources: data/기본기_연구/prepared_backlog/blind_sources/BPO.json; data/기본기_연구/prepared_backlog/blind_sources/BPP.json; data/기본기_연구/prepared_backlog/blind_sources/BPQ.json
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.
