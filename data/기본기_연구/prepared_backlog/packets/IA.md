# IA blind packet

- case_id: IA
- passage_group: G051
- blind_source: data/기본기_연구/prepared_backlog/blind_sources/IA.json
- group_case_ids: HY, HZ, IA, IB
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 이 anonymous blind-only source만 읽는다. 동일 passage group의 모든 case blind raw 저장 후 group 전체 answer_check, independent_code를 순서대로 수행한다. 실제 시험 식별 정보는 blind 단계에서 제공하지 않는다.
