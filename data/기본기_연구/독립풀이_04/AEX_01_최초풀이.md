

<!-- luna-raw:AEX-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G192",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "마지막 문단: 수소 이온은 전해질, 전자는 도선을 통해 환원 극으로 이동.",
    "1문단 재생 에너지 전기분해,2문단MCH 취급 안전성,3문단 암모니아 분해법."
  ],
  "minimal_logic_without_codes": "목적지는 같아도 이동 통로가 다르다.⑤는 전자의 도선 경로를 수소 이온에 옮겨 두 입자가 같은 통로를 쓰는 것으로 만든다.",
  "intermediate_reasoning": [
    "① 재생에너지 전기로 물을 분해하여 탄소배출 없이 수소 생산 가능.",
    "② MCH의 안전성은 휘발유와 유사.",
    "③ 광분해도 암모니아 분해 방식 중 하나.",
    "④ 산화극에 수소, 환원극에 산소 공급."
  ],
  "most_attractive_wrong_answer": 4,
  "exact_error": "물이 최종 생성된다는 설명과 물을 전기분해해 수소를 생산하는 앞문단을 혼동하면 연료전지에도 물을 공급해야 한다고 오인한다.",
  "quota_status": "unavailable"
}
```
