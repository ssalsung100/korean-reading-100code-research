

<!-- luna-raw:BKC-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G453",
  "selected_answer": 5,
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
      "location": "2문단·끝문단",
      "evidence": "광학은 시료에서 산란한 빛을 집속하고 전자는 산란한 전자의 물질파를 집속해 분포를 측정한다."
    },
    {
      "location": "2~4문단",
      "evidence": "해상도는 파장에 비례. 진공 필요. 전자 렌즈의 중심·가장자리 전자를 한 점에 모으기 어렵다. 전하 축적은 상 왜곡."
    }
  ],
  "minimal_logic_without_codes": "빛과 전자의 관찰 매체는 다르지만 둘 다 산란된 파동을 모아 상을 얻으므로 ⑤가 공통 원리에 맞는다.",
  "intermediate_reasoning": [
    "① 파장 의존을 부정하여 오류.",
    "② 기압을 높여 충돌을 늘리는 방향은 진공을 요구하는 이유와 반대.",
    "③ 초점이 명확하지 않다는 한계를 무시하고 같은 점 도달을 일반적으로 단정.",
    "④ 전자 축적이 전자빔을 밀어내 왜곡한다는 방향을 반대로 바꿈."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "렌즈가 전자를 모아 준다는 일반 기능을 중심과 가장자리의 모든 전자가 같은 점에 정확히 모인다는 성능 보장으로 강화한다."
  }
}
```
