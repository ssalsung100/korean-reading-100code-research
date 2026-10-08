

<!-- luna-raw:AGV-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G202",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "1문단방전시단자전압감소,변화하는단자전압의평균이공칭전압."
  ],
  "minimal_logic_without_codes": "감소하는전압의일부값은평균보다낮을수있으므로②가맞다. 공칭전압은모든순간값의하한이아니다.",
  "intermediate_reasoning": [
    "① 과충전은수명감소요인.",
    "③ 정전압회로는입력변해도출력일정.",
    "④ 전극물질다르면공칭전압달라짐. 크기만바꿀때불변.",
    "⑤ 니켈카드뮴은부분방전후충전반복시메모리효과로용량감소."
  ],
  "most_attractive_wrong_answer": 4,
  "exact_error": "크기를바꿔도물질이같으면전압불변이라는조건을물질을바꿔도불변으로옮긴다. 고정조건과변경조건의자리교환.",
  "quota_status": "unavailable"
}
```
