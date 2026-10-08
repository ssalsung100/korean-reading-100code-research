

<!-- luna-raw:AXG-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "미확정",
  "required_information_and_location": [
    "1문단: 순수한 물은 어느 온도까지 과냉각으로 존재",
    "2문단: 물은 이력 특성 제외, 우무는 40~80도에서 이력 필요"
  ],
  "minimal_logic_without_codes": "과냉각 가능성과 이력 특성은 별개이다. 같은 온도·압력이어도 직전 상태가 다르면 상태가 달라질 수 있다. 순수함이 모든 상전이를 금지하지는 않는다.",
  "intermediate_reasoning": [
    "ㄱ 물은 이력 특성이 없지만 과냉각될 수 있으므로 참.",
    "ㄴ 우무 60도는 냉각 중 액체와 가열 중 고체가 가능하므로 참.",
    "ㄷ 어느 온도까지 얼지 않는다는 제한을 온도 변화 전체에서 상전이 불가능으로 늘려 거짓."
  ],
  "most_attractive_wrong_answer": 5,
  "exact_error": "응결핵 부재의 제한된 과냉각을 모든 온도 변화의 상전이 부정으로 확장한다.",
  "passage_group": "G342",
  "quota_status": "unavailable"
}
```
