

<!-- luna-raw:BHK-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G430",
  "selected_answer": 1,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BHK.json",
  "necessary_information": [
    {
      "location": "1~2문단",
      "evidence": "에스테르화는 지방산·글리세롤 결합으로 중성지방을 저장.카테콜아민은 호르몬-민감 리파아제를 활성화해 중성지방 분해."
    },
    {
      "location": "2문단/4~5문단",
      "evidence": "큰 지방세포에서 기초 분해가 빠르며 성별 지방 축적 부위가 다르다."
    }
  ],
  "minimal_logic_without_codes": "카테콜아민이 촉진하는 저장 지방의 분해를 지방산·글리세롤 결합으로 바꾼①이 불일치한다.나머지는 본문 과정·성별 차이·크기와 속도 방향에 대응한다.",
  "intermediate_reasoning": [
    "②에너지원은 저장 중성지방이 분해되어 혈액으로 나온 지방산·글리세롤이다.④작은창자 흡수 전 리파아제 분해가 필요.",
    "③은 지방 축적의 지역 차이에 부합하는 취지이나 지방세포가 더 축적된다는 전사 표현은 지방량과 세포수를 엄밀히 동일시할 근거로 확대하지 않는다.",
    "⑤의 비례는 본문에서 크기가 클수록 빠르다는 동방향 관계까지 확인된다.정확한 일정비율 식은 제시되지 않는다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "본문이 세포 크기 증가에 따른 속도 증가를 명시하는데 수식 계수가 없다는 이유만으로 방향 관계까지 없다고 판단하면 안 된다.다만 비례를 엄밀한 선형식으로 확장할 수는 없다."
  },
  "unresolved": [
    "③세포 축적/지방 축적 표현 차이 및⑤엄밀 비례식은 최초부터 유보."
  ]
}
```
