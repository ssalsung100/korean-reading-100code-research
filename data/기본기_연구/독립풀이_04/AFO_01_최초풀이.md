

<!-- luna-raw:AFO-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G195",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "공식[가]시작crop의㉠실질통화량증가·㉡시장금리하락,이어지는crop의㉢환율상승·장기조정확인.",
    "그림a하락후최초수준복귀,b급상승후최초보다높게수렴,c상승후최초수준복귀.",
    "공식선지표④는㉠c/㉡a/㉢b."
  ],
  "minimal_logic_without_codes": "실질통화량은물가경직시상승했다가물가조정으로원래수준복귀하여c. 금리는하락후반등해a. 환율은오버슈팅후하락하지만증가한명목통화량·물가를반영한더높은장기환율에수렴하므로b.④.",
  "intermediate_reasoning": [
    "㉡의초기하락만으로a를확정하면②또는④가남는다.",
    "㉠과㉢은둘다초기상승하지만최종기준수준이달라c와b로구분.",
    "변수마다수렴기간이달라도곡선의초기방향·최종수준대응은유지."
  ],
  "most_attractive_wrong_answer": 2,
  "exact_error": "둘다상승한다는모양만보고실질통화량b/환율c로교환하면,장기실질통화량복귀와균형환율의새수준을혼동한다.",
  "visual_verification": [
    "AFO_graph_abc_supplement_20260920.png",
    "AFO_scope_[가]_start_v2_20260920.png",
    "AFO_scope_[가]_continuation_end_v2_20260920.png",
    "AFO_graph_matching_choices_v2_20260920.png"
  ],
  "source_qualification": "최초누락및잘린crophold는보존.실제범위상하단·표지·그래프·선지표확인후유효풀이저장.",
  "quota_status": "unavailable"
}
```
