

<!-- luna-raw:BKZ-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G461",
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
      "location": "1414년 수정 기준",
      "evidence": "적통 다툼에서 신분·혼서·혼례로 처첩을 조사하고 자식에게 노비를 차등 분급한다."
    },
    {
      "location": "1413년 규제·1414년 말미",
      "evidence": "혼서·혼례로 처첩 구분,지위 뒤바꿈 처벌,후처 이혼,기준일 이후 중혼 금지."
    }
  ],
  "minimal_logic_without_codes": "②는 수정 기준의 처첩에 따른 자식 노비 분급 차이를 그대로 나타낸다.다른 선지는 판정 기준·적용 시기·처벌 범위를 바꾼다.",
  "intermediate_reasoning": [
    "① 생사는 지위 복구·이혼 가능 여부에 관련되고 처첩 구분 기준 자체는 혼서·혼례다.",
    "③ 지위 변경 처벌은 최초 규제부터 존재한다.",
    "④ 이혼 대상은 모든 처가 아닌 후처다.",
    "⑤ 은의·동거 고려를 기준일 이후 중혼 허용으로 확대하면 명시된 금지와 충돌한다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "과거 중혼 관계의 처리 기준을 규제 이후의 새 중혼 허용 조건으로 옮긴다."
  }
}
```
