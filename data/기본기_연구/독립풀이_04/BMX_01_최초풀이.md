

<!-- luna-raw:BMX-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G477",
  "selected_answer": 3,
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
      "location": "3~4문단",
      "evidence": "산소가 부족하면 산화적 인산화가 제한돼 낮은 수율의 해당작용에 의존하고, 암세포는 이를 보상하기 위해 포도당을 더 수송한다."
    },
    {
      "location": "보기",
      "evidence": "방사성 포도당 유도체는 포도당 흡수가 많은 부위에 수송·축적되어 분포가 측정된다."
    }
  ],
  "minimal_logic_without_codes": "산소 감소로 단위 포도당당 ATP 수율이 낮아지는 조건에서 같은 ATP 양을 만들려면 포도당 유입을 늘려야 하므로 유도체 축적도 늘어난다는③이 맞는다.",
  "intermediate_reasoning": [
    "① 발효 증가와 해당 의존의 맥락에서 포도당 흡수·축적 감소를 도출하지 못한다.",
    "② 포도당의 해당 분해 감소를 유도체 축적 증가로 뒤집을 근거가 없다.",
    "④ 해당 의존 증가의 낮은 수율은 같은 에너지 확보를 위한 포도당 수요를 늘리는 방향이다.",
    "⑤ 산화적 인산화 의존 증가로 수율이 높아지면 같은 ATP를 위한 포도당 필요량은 줄어드는 방향이다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "ATP 생산 효율이 높아지는 것을 포도당 흡수량도 더 많아진다는 것으로 같은 방향에 놓고, 같은 ATP 목표량이라는 조건을 빠뜨린다."
  },
  "scope_limit": "본문이 가정한 대사 경로와 추적 물질의 대응을 사용한다. PET 신호만으로 개별 환자의 암 여부를 확정하거나 검사법을 권고한 것이 아니다."
}
```
