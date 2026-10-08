# BDK blind packet

- passage_group: G393
- group_case_ids: BDI, BDJ, BDK
- blind_sources: data/기본기_연구/prepared_backlog/blind_sources/BDI.json; data/기본기_연구/prepared_backlog/blind_sources/BDJ.json; data/기본기_연구/prepared_backlog/blind_sources/BDK.json
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.
