# 기존 장면과 코드북 v0.2 매핑

기존 46장면을 보존한다. 아래 같은 event가 여러 행에 나타나는 것은 복수 관계이며 추가 사건이 아니다. `legacy_pattern_ids`는 출처 보존용이고 계수에 사용하지 않는다.

|event / case|선지|후보·하위형|pattern_relation|판정|
|---|---|---|---|---|
|E001 / AA|2|미분류 / |unclassified|unclassified|
|E002 / AA|4|P04 / P04.explicit_requirements|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E003 / AB|4,5|P02 / P02.responsibility_degree|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E003 / AB|4,5|S05 / |boundary_case|non_applicable_inherited|
|E004 / AC|2|P03 / P03.inverse_order|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E004 / AC|2|P02 / |boundary_case|non_applicable_inherited|
|E005 / AD|4,5|P03 / P03.conditional_chain|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E005 / AD|4,5|P07 / |boundary_case|non_applicable_inherited|
|E005 / AD|4,5|S01 / |boundary_case|non_applicable_inherited|
|E006 / AF|2|미분류 / |unclassified|unclassified|
|E007 / AG|2,4|P01 / P01.attribution|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E008 / AH|2|P04 / |boundary_case|non_applicable_inherited|
|E008 / AH|2|미분류 / |unclassified|unclassified|
|E009 / AI|5|S01 / S01.update_possibility|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E009 / AI|5|S04 / |boundary_case|non_applicable_inherited|
|E010 / AJ|2,5|P05 / P05.lexical_comparison|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E011 / BI|3|P01 / P01.attribution|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E012 / BJ|5|P03 / |boundary_case|non_applicable_inherited|
|E012 / BJ|5|P04 / |boundary_case|non_applicable_inherited|
|E012 / BJ|5|P06 / |boundary_case|non_applicable_inherited|
|E012 / BJ|5|미분류 / |unclassified|unclassified|
|E013 / BK|4|P04 / P04.authority_scope|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E014 / BK|2|S01 / |boundary_case|non_applicable_inherited|
|E014 / BK|2|미분류 / |unclassified|unclassified|
|E015 / BL|2|P05 / P05.lexical_comparison|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E016 / BY|2,4|P01 / P01.cause_type|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E017 / BZ|2,4,5|P07 / P07.processing_state|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E017 / BZ|2|P03 / |boundary_case|non_applicable_inherited|
|E018 / CA|2,4|P03 / P03.relative_ratio|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E019 / CB|1,4|P05 / P05.lexical_comparison|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E020 / GK|1,2|S02 / S02.discriminating_observation|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E021 / GL|1|P07 / P07.causal_sequence|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E022 / GM|5|P04 / P04.measurement_mechanism|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E023 / OX|3,5|S03 / S03.discourse_actions|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E024 / OY|5|P01 / |boundary_case|non_applicable_inherited|
|E024 / OY|3,5|미분류 / |unclassified|unclassified|
|E025 / OZ|2,5|P02 / P02.viewpoint_axes|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E025 / OZ|2,5|S02 / |boundary_case|non_applicable_inherited|
|E026 / PA|2,3|P02 / P02.viewpoint_axes|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E027 / ZD|4|미분류 / |unclassified|unclassified|
|E028 / ZE|5|P05 / P05.description_only|structure_present, explanatory_only, boundary_case|confirmed_inherited|
|E029 / ZF|3|S04 / S04.remaining_candidates|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E029 / ZF|3|P05 / |boundary_case|non_applicable_inherited|
|E030 / ZF|4,5|P05 / P05.contextual_confirmation|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E031 / AJP|2|S05 / S05.norm_execution|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E031 / AJP|2|P07 / |boundary_case|non_applicable_inherited|
|E032 / AJP|1|P07 / |boundary_case|non_applicable_inherited|
|E032 / AJP|1|미분류 / |unclassified|unclassified|
|E033 / AJQ|5|P01 / P01.relation_endpoints|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E034 / AJR|5|미분류 / |unclassified|unclassified|
|E035 / ANV|5|P07 / P07.historical_placement|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E035 / ANV|5|P06 / |boundary_case|non_applicable_inherited|
|E035 / ANV|5|S06 / |boundary_case|non_applicable_inherited|
|E036 / ANW|3|P01 / P01.attribution|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E036 / ANW|3|P02 / |boundary_case|non_applicable_inherited|
|E037 / ANX|3,4|P06 / P06.control_power|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E038 / AQN|3|S06 / S06.group_identity|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E039 / AQO|2,5|P06 / P06.correct_dependence|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E040 / AQP|1,4|P01 / P01.evaluation_target|structure_present, item_utilized, solution_helpful|confirmed_inherited|
|E041 / AVS|4,5|S03 / |boundary_case|non_applicable_inherited|
|E041 / AVS|4,5|미분류 / |unclassified|unclassified|
|E042 / AVT|1|P01 / |boundary_case|non_applicable_inherited|
|E042 / AVT|1,2|미분류 / |unclassified|unclassified|
|E043 / AVU|1|미분류 / |unclassified|unclassified|
|E044 / AA|1|미분류 / |unclassified|unclassified|
|E045 / AH|4|미분류 / |unclassified|unclassified|
|E046 / AJP|3|미분류 / |unclassified|unclassified|

E028/ZE의 P05 연결은 구조 설명+explanatory_only+boundary_case이며 item_utilized·solution_helpful이 없다. E030/ZF④·⑤는 보조 선지 판단으로 item_utilized·solution_helpful을 유지한다.

E044~E046은 기존 정답 경로를 보완한 장면이지만 후보 미분류를 유지한다. 다른 후보의 경계 사례라는 이유만으로 원래 미분류 상태를 삭제하지 않는다.

인용은 `event_mapping_v0.2.jsonl`의 quotation_audit에 application의 교정 인용·정확한 원장 좌표를 승계했다. 이번에는 원장을 열거나 정본과 의미를 재대조하지 않았다.
