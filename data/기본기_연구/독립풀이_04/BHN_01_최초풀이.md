

<!-- luna-raw:BHN-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G431",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BHN.json",
  "necessary_information": [
    {
      "location": "5문단",
      "evidence": "상충 이론은 기업 규모가 크면 부채 비율 높음,조달 순서 이론은 크면 낮음으로 예측."
    },
    {
      "location": "1~4문단",
      "evidence": "정보비대칭도 불완전 요인.부채 등 자본 구조가 가치에 주는 영향 탐구.내부자금→부채→주식.완전자본시장 전제를 비판."
    }
  ],
  "minimal_logic_without_codes": "동일한 기업 규모 증가에 대해 부채 비율의 증가/감소라는 반대 예측을 한다는④가 일치한다.",
  "intermediate_reasoning": [
    "①불완전성을 야기하는 열거 요인 중 정보비대칭을 부당하게 제외한다.②주요 영향 방향을 바꾼다.③부채와 주식 순서를 바꾼다.⑤완전시장 전제의 비현실성 비판을 전제 동의로 바꾼다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "이론들이 결론만 비판하고 출발 전제는 공유한다고 오독한다.본문2문단은 완전자본시장 가정의 비현실성에 주안점을 두었다고 명시한다."
  }
}
```
