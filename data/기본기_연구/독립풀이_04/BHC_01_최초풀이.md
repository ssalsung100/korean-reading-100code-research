

<!-- luna-raw:BHC-blind-20261002-r4-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G426",
  "selected_answer": 2,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BHC.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G426_visual02.md",
    "data/기본기_연구/prepared_backlog/blind_sources/G426_visual03.md"
  ],
  "necessary_information": [
    {
      "location": "본문 온도/최대파장",
      "evidence": "최대 에너지 파장은 절대온도에 반비례"
    },
    {
      "location": "본문 산란/흡수",
      "evidence": "대기입자에 의한 산란, 수증기의 특정 대역 흡수"
    },
    {
      "location": "보기 전제",
      "evidence": "세 기초 정보 외 모든 조건 지구와 동일"
    }
  ],
  "minimal_logic_without_codes": "다른 조건을 고정하고 각각의 변화 방향을 추적한다. 온도 감소→최대파장 증가라ㄱ틀림, 밀도 감소→산란 약화라ㄴ틀림, 수증기 감소→흡수 완화→사용 가능 중적외 확대라ㄷ맞음.",
  "intermediate_reasoning": [
    "ㄱ의 짧아진다는 계획은 반비례 방향을 역전한다.",
    "ㄴ은 산란 원인 입자가 줄어드는 효과를 강해진다고 역전한다.",
    "ㄷ은 방해하는 흡수의 원인이 줄어들어 통과 가능성이 개선되는 방향이다. 산소 등 다른 흡수체까지 없어지는 것으로 확대하지 않는다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "ㄴ의 낮은 대기밀도를 지표 신호가 잘 드러남과 혼동하여 산란 자체가 강해진다고 판정한다. 관측 용이성과 산란 강도는 같은 변수가 아니다."
  },
  "source_limitations": [
    "각 변수의 방향을 판정하며 다른 행성의 실제 정량 예측이나 센서 설계 지침으로 확장하지 않음."
  ]
}
```
