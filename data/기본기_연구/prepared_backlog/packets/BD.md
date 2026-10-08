# BD blind packet

- case_id: BD
- passage_group: G008
- blind_source: data/기본기_연구/prepared_backlog/blind_sources/BD.json
- group_case_ids: AZ, BA, BB, BC, BD
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 이 anonymous blind-only source만 읽는다. 동일 passage group의 모든 case에 대해 blind record를 queue에 저장하고, group 전체 independent_code raw 저장까지 확인한 뒤에만 해당 group의 sealed provenance·answer·SDSS를 접근한다. 학년도·시험명·문항번호·canonical ID·candidate ID·site title은 blind 단계에서 제공하지 않는다.

