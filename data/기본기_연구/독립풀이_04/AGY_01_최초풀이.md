

<!-- luna-raw:AGY-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G202",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "본문만충전근처에서단자전압다소감소후일정수준감소시점에만충전추정·차단.",
    "원그래프다=전압최대1.8V,라=전압감소후충전전류2A→0차단."
  ],
  "minimal_logic_without_codes": "전압최대시점다는곧바로만충전판정시점이아니다. 최대이후전압감소를확인한라에서차단하므로③이틀림.",
  "intermediate_reasoning": [
    "가는0.8V에서충전시작으로본문모든공칭전압1.2/2/3.6보다낮음.",
    "나는충전전류2A일정·전압및온도상승구간.",
    "라는충전전류0으로전원차단.",
    "마는충전전류0이며단자전압점차감소하는방전구간."
  ],
  "most_attractive_wrong_answer": 4,
  "exact_error": "라의전압이아직0이아니라는것을전원이차단되지않았다는뜻으로읽으면안된다. 차단의직접지표는충전전류0이며단자전압은남을수있음.",
  "visual_verification": "AGY_Q33_graph_supplement_20260920.png의실선단자전압·점선충전전류·가~마위치와두세로축직접확인.",
  "quota_status": "unavailable"
}
```
