

<!-- luna-raw:BJT-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G450",
  "selected_answer": 5,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BJT.json",
  "necessary_information": [
    {
      "location": "1~3문단",
      "evidence": "합의제는권력공유정치주체수확대,다당제·연정친화.성장차이는유의하지않음.선진/신생에모두도입시도."
    },
    {
      "location": "목적분리성문단",
      "evidence": "과도한권력분산은거부권자수를늘려교착위험을높일수있음."
    }
  ],
  "minimal_logic_without_codes": "권력분산·공유가큰합의제에서거부권자증가에따른교착가능성을말한⑤가적절하다.항상교착한다는단정은아니다.",
  "intermediate_reasoning": [
    "①다당제적경향을양당제로거꾸로바꿈.②두부류모두관심을보였으나어디서더많이주목받는지는비교근거없음.",
    "③성장차이없음을열세로바꿈.④늘리는대상은권력공유정치주체/연합다수이지유권자전체인원수를최대화한다는내용이아니다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "다수를최대화한다는문장을권력공유연합참여주체대신권력위임유권자수로옮긴다.무엇의수가늘어나는지대상이바뀐다."
  }
}
```
