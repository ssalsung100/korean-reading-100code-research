

<!-- luna-raw:AHO-blind-20260921-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G207",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_and_location": [
    "4문단 스위치가 변동적은 전압을 변화심한 전압으로 변환",
    "2문단 각 소자 기능"
  ],
  "minimal_logic_without_codes": "스위치의 온오프는 변압기에 필요한 전압 변화를 만들며 평활 회로가 변동을 억제한다.②은 스위치에 반대 기능을 부여한다.",
  "intermediate_inferences": [
    "① 변압기는 교류 높이거나 낮춤",
    "③ 정전압 소자 안정화",
    "④ 전체 높은교류→낮은직류",
    "⑤ 정류의 방향 단일화 일치"
  ],
  "most_attractive_wrong_answer": {
    "choice": 1,
    "attraction": "어댑터는 낮추는 장치이므로 변압기도 높일 수 없다고 생각",
    "error": "부품 일반 기능은 높이거나 낮춤으로 명시되어 전체 장치의 목적과 다르다."
  },
  "quota_status": "unavailable"
}
```
