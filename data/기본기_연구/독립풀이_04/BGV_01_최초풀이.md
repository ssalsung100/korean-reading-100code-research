

<!-- luna-raw:BGV-blind-20261002-r4-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G424",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BGV.json",
  "necessary_information": [
    {
      "location": "선법 음악 설명",
      "evidence": "선율의 독립성/동등한 중요성, 수직 음향 부차적"
    },
    {
      "location": "조성 음악 설명",
      "evidence": "다성부 구조 쇠퇴, 선율이 화음에 근거하여 만들어짐"
    },
    {
      "location": "끝문단",
      "evidence": "5도 관계에 놓인 세 화음이 근본 역할"
    }
  ],
  "minimal_logic_without_codes": "선법의 독립된 선율들이 조성의 화음에 근거한 선율로 바뀌면서 선율의 독립성이 쇠퇴한다. 전환의 방향을 보존하면②이다.",
  "intermediate_reasoning": [
    "①협화/불협화 교체로 설명되지 않는다. ③수평→수직 중시를 역전했다.",
    "④화음 내부에3도를 쌓는 것과 주요화음 근음끼리5도 관계인 것을 혼동한다.",
    "⑤조성에서는 화음에 근거해 선율이 만들어지므로 화성이 선율의 결과라는 설명은 의존 방향을 역전한다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "3화음 구성 내부의3도 간격을 주요화음들 사이의5도 관계로 옮겼다. 숫자 자체보다 간격을 재는 두 항이 달라졌다."
  },
  "source_limitations": []
}
```
