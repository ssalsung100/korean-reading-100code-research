# PO blind packet

- case_id: PO
- passage_group: G107
- blind_source: data/기본기_연구/prepared_backlog/blind_sources/PO.json
- group_case_ids: PL, PM, PN, PO, PP
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 anonymous blind-only source만 읽고 group barrier를 지킨다.
