# FA blind packet

- case_id: FA
- passage_group: G032
- blind_source: data/기본기_연구/prepared_backlog/blind_sources/FA.json
- group_case_ids: EZ, FA, FB, FC
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 이 anonymous blind-only source만 읽는다. 동일 passage group의 모든 case에 대해 blind record를 queue에 저장하고, group 전체 independent_code raw 저장까지 확인한 뒤에만 봉인된 후속 자료에 접근한다. 실제 시험 식별 정보는 blind 단계에서 제공하지 않는다.

- blind_only_math_supplement: data/기본기_연구/prepared_backlog/blind_sources/G032_math_supplement.md
- blind_only_exact_runs: data/기본기_연구/prepared_backlog/blind_sources/G032_math_runs.json

- blind_only_passage_figure: data/기본기_연구/prepared_backlog/blind_sources/G032_body_figure.bmp
