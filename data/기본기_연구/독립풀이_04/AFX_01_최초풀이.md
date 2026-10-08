

<!-- luna-raw:AFX-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G197",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "2문단 신용위험은지급능력부족등으로원금·이자를못받을가능성.",
    "3문단지급능력최상채권AAA,위험커질수록낮은등급."
  ],
  "minimal_logic_without_codes": "발행자의지급능력이커지면미지급가능성인신용위험은낮아지는방향이다.②는반대로높아진다고하므로틀림.",
  "intermediate_reasoning": [
    "① 채권발행은자금조달목적.",
    "③ 신용평가제도는투자자보호.",
    "④ 등급하락→위험상승,다른조건일정시가격하락.",
    "⑤ 지급약속과불이행가능성은양립."
  ],
  "most_attractive_wrong_answer": 5,
  "exact_error": "지급약속을이행의확정적보장으로읽으면신용위험설명과모순된다고오인한다. 약속과실제이행가능성은별개.",
  "quota_status": "unavailable"
}
```
