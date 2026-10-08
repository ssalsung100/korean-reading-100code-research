

<!-- luna-raw:BHA-blind-20261002-r4-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G426",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BHA.json",
  "necessary_information": [
    {
      "location": "중적외선·고령토 문단",
      "evidence": "광물·암석의 고유 분광 반사 특성으로 자원 탐사; 특정 파장 흡수 특성을 고령토 판단에 이용"
    },
    {
      "location": "끝문단 대기 흡수",
      "evidence": "대기 물질의 흡수가 통과를 방해하여 해당 파장 제외"
    }
  ],
  "minimal_logic_without_codes": "관측 대상의 고유 흡수는 식별 단서이고 전달 경로인 대기의 흡수는 관측을 방해한다.③은 흡수라는 같은 작용을 주체·역할과 무관하게 방해로 일반화한다.",
  "intermediate_reasoning": [
    "①가시광/근적외/중적외/열적외를 이용한다.②근적외 식별과 중적외 수분 함량으로 분포·생육을 파악한다.",
    "④산란은 밝기·대비를 감쇠시키며 흡수 파장을 제외하므로 대기 영향을 고려해야 한다.⑤태양→대기→지표 반사→대기→센서로 두 번 통과한다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "보정이라는 말이 그대로 없다는 이유로 배제하면, 산란·흡수 영향을 고려하여 영상 및 센서를 설계해야 한다는 본문 기능적 재진술을 놓친다."
  },
  "source_limitations": [
    "파장 단위 기호가 전사에서 빠져 있으나 이 문항의 주체·역할 판정에는 영향 없음."
  ]
}
```
