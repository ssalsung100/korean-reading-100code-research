

<!-- luna-raw:AEZ-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G192",
  "selected_answer": 4,
  "confidence": 0.96,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "3문단: 암모니아:질소:수소 반응 몰수2:1:3, 열분해 전환율0.9이상·부반응거의없음.",
    "보기: 공급10 중 반응6, 암모늄 등 부반응물 상당량."
  ],
  "minimal_logic_without_codes": "같은10몰 공급을 기준으로 A는9몰 이상이 거의 의도된 분해반응을 하고 B는6몰만 반응하며 일부가 부반응으로 빠진다. 주어진 분해비에서 B의 수소 생성량이A보다 적으므로④.",
  "intermediate_reasoning": [
    "B 전환율6/10=0.6으로A의0.9이상보다 낮다.",
    "A 주반응 기준 수소 약13.5몰이상, B는 반응6몰 전부 주반응에 쓰인다는 상한에서도9몰 수준이며 실제 부반응 때문에 그대로9라고 확정하지 않는다.",
    "① B도 암모니아 분해를 수행하므로 질소 미생성이라고 할 수 없음.",
    "② A수소는 의도한 생성물.",
    "⑤ A도 수소/반응암모니아=3/2>1이라 B만의 특징이 아님."
  ],
  "most_attractive_wrong_answer": 5,
  "exact_error": "보기에서 특별히 명시한 수소 몰수>반응암모니아를 B만의 성질로 오인한다. 본문A에도2:3 비가 적용된다.",
  "scope_limit": "부반응 경로가 없으므로B의 정확한 수소 생성 몰수는 확정하지 않는다. 반응물의 수소가 부반응 생성물로도 남는 범위에서 상한 비교를 사용한다. A의 거의없음을 정확히0으로 바꾸지 않고 수치는 주반응 근사 비교로 표시.",
  "quota_status": "unavailable"
}
```
