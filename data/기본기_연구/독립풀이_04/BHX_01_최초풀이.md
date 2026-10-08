

<!-- luna-raw:BHX-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G434",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BHX.json",
  "necessary_information": [
    {
      "location": "3문단 순환 정의",
      "evidence": "열 출입 없는 과정은 엔트로피 변화가 없다.Ⅲ은 열 출입을 차단하고 자기장을 제거하는 과정."
    },
    {
      "location": "2~3문단",
      "evidence": "자화는 외부장 세기에 비례.Ⅱ열방출 냉각,Ⅳ내부열흡수.강한장일수록Ⅰ에서 더 많은 열 발생."
    }
  ],
  "minimal_logic_without_codes": "Ⅲ의 쌍극자 배열이 무질서해져도 해당 과정은 열 출입이 차단되었으므로 본문 규칙상 작용물질 엔트로피는 변하지 않는다.증가한다는③이 틀리다.",
  "intermediate_reasoning": [
    "①Ⅰ자기장 가함→자화 증가.②Ⅱ열 방출로온도 하강.④Ⅳ는 열 흡수하므로 냉장고 내부 접촉.",
    "⑤강한 자기장에 따른 열 발생과 이후 방출의 증가라는 본문 방향 관계에 부합한다.전 범위에서 정확한 선형 열량식까지 주어지지는 않는다.",
    "상전이시 엔트로피 증가라는2문단을Ⅲ에 무조건 적용하면 열출입 차단이라는 조건을 놓친다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "열출입이 없는Ⅰ에서 발생한 열과 실제 외부로 나가는Ⅱ의 열을 혼동해 순환 전체의 방출량 증가를 부정하면 안 된다.①단계의 발생과Ⅱ단계의 방출은 연결된 순환이다."
  }
}
```
