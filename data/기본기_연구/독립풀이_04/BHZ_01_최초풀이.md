

<!-- luna-raw:BHZ-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G435",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BHZ.json",
  "necessary_information": [
    {
      "location": "이익분배 이론 문단",
      "evidence": "지역구 이해가 비슷한 의원들이 상임위 구성.서로 다른 상임위 의원 사이 지지 교환이며 다수당 영향은 축소."
    },
    {
      "location": "정보확산/정당이익 문단",
      "evidence": "의회 다수 선호와정보제공/정당 지지자 대표와지도부 감독의 역할을 각기 강조."
    }
  ],
  "minimal_logic_without_codes": "이익분배 이론의 투표 거래 주체는 다른 상임위 소속 의원들인데①은 이를 정당 사이 거래로 바꾸어 틀리다.",
  "intermediate_reasoning": [
    "②는 지역구이익 수요와 정책정보 공급 기능의 정확한 대비.③자율배정과정당간협의 역할도 본문과 일치.",
    "④지역구/정당지지자 대표의 차이와⑤불확실성 축소/정당성과 극대화의 차이도 각 이론 귀속이 맞다.",
    "의원에게 정당 소속이 있다는 사실은 그 의원 간 거래의 중심 단위가 정당이라는 결론을 보장하지 않는다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "정보확산 이론의 본회의 중심성을 정당간협의회 역할 부정으로 읽으면 안 된다.그 협의회는 본회의 주도로 상임위를 조직하기 위한 기제다."
  }
}
```
