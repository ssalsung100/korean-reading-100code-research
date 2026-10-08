

<!-- luna-raw:BPG-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G498",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "법제 사례 문단",
      "evidence": "볼리비아는 자연의 고유한 권리를 인정하고 뉴질랜드도 특정 강을 법적 인격체로 규정한다. 에콰도르는 누구나 청원할 수 있고 뉴질랜드는 지정 후견인이 대리한다."
    }
  ],
  "minimal_logic_without_codes": "두 법 모두 자연의 권리 주체성을 인정하는데②는 이를 뉴질랜드만의 차이로 만들었다.",
  "intermediate_reasoning": [
    "① 포괄적 자연 권리와 특정 생태계 권리의 방식 차이다.",
    "③ 에콰도르는 청원으로 권리 집행, 볼리비아는 유지·회복을 돕는 국민 의무를 규정한다.",
    "④ 누구나와 법정 후견인이라는 대리 자격 범위가 다르다.",
    "⑤ 두 법은 인간의 이익과 별개로 자연 자체의 회복 권리를 인정한다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "권리 주체가 자연이라는 공통점만 보고, 그 권리를 누가 대리 집행할 수 있는지는 다른 문제라는 점을 놓친다."
  }
}
```
