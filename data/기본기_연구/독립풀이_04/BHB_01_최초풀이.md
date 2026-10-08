

<!-- luna-raw:BHB-blind-20261002-r4-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G426",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BHB.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G426_visual01.tif"
  ],
  "necessary_information": [
    {
      "location": "그래프 범례",
      "evidence": "점선 A반사율, 실선 B반사율, 음영 대기흡수율"
    },
    {
      "location": "그래프1.4와2.2",
      "evidence": "1.4대기흡수 거의100%, 2.2대기흡수 낮음·A약50/B약10"
    },
    {
      "location": "본문 대기창",
      "evidence": "센서는 대기의 창에 맞추어 설계"
    }
  ],
  "minimal_logic_without_codes": "물체 반사율의 차이만 아니라 반사 에너지가 대기를 통과하는 조건도 필요하다.1.4는 대기가 거의 다 흡수하고2.2는 잘 통과하며 A/B 차이가 커서⑤이다.",
  "intermediate_reasoning": [
    "①1.4의 A반사율 봉우리만 보고 대기흡수를 무시한다.②B는 가시광에서70%대이고 중적외에서 대체로 낮다.",
    "③1.9는 흡수율이 높아 대기창이 아니다.④가시광은 A/B차이가 작고 일부 중적외 창에서는 차이가 크다."
  ],
  "most_attractive_wrong": {
    "choice": 1,
    "exact_error": "물체 자체의 반사율이 크다는 조건만으로 센서 영상 밝기를 결정하고 중간 전달 경로의 흡수를 누락한다."
  },
  "source_limitations": [
    "그래프 값은 근삿값 판독이며 정밀 계측 아님."
  ]
}
```
