

<!-- luna-raw:BQN-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G509",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false,
    "visual_supplements_seen": true
  },
  "necessary_information": [
    {
      "location": "사례와4문단",
      "evidence": "A와B가 동시에 널판을 잡은 것은 저마다 생명을 구하려는 불가피한 행위이며,A의 밀어낸 행위도 위난 회피 목적이었다."
    },
    {
      "location": "마지막 문단",
      "evidence": "자기희생은 숭고한 선행이지만 이를 하지 않았다고 법적 비난하기는 어렵다."
    }
  ],
  "minimal_logic_without_codes": "두 사람의 행위가 모두 현재 생명의 위난에서 벗어나려는 것이었다는①이 본문과 맞는다.",
  "intermediate_reasoning": [
    "② 행위자 이름을 교환해도 같은 상황의 책임 판단이 자동 반대로 바뀌지 않는다.",
    "③ A가 B를 밀어 죽게 한 행위는 살인의 구성요건에 해당하며 책임 부정과 구별된다.",
    "④ 법적 비난 불가능성을 윤리적 타당성 때문에라고 바꾸었다.본문은 윤리적 비판 가능성을 남긴다.",
    "⑤ 자기희생을 택했다면 숭고한 선행이라고 명시된다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "형법상 책임이 없다는 결론을 윤리적으로 옳다는 결론과 같게 본다."
  },
  "scope_limit": "문항이 제시한 형법 논리만 적용하며 현재 법률의 모든 실제 사건에 일반화하지 않는다."
}
```
