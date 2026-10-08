

<!-- luna-raw:BQD-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G506",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false,
    "visual_supplement_seen": true
  },
  "necessary_information": [
    {
      "location": "3문단 반발력 설명",
      "evidence": "이종분자 반발력으로 첨가 부피보다 총부피가 더 증가할 때에도 증가 정도는 구성 비율에 따라 달라진다."
    }
  ],
  "minimal_logic_without_codes": "반발력의 경우에도 비율에 따른 부피 변화 차이가 있으므로 비율 영향을 받지 않는다는⑤가 틀린다.",
  "intermediate_reasoning": [
    "① 순수 물은 수소결합 네트워크로 분자 간 거리를 유지한다.",
    "② 본문은 자발 반응의 역반응은 비자발적이라고 명시한다.",
    "③ 특정 온도의 순물질 몰부피는 물질마다 고유하다는 설명에 맞는다.",
    "④ 깁스-뒤엠식은 두 성분 분몰부피 변화의 의존 관계를 나타낸다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "식에 분몰부피의 변화량이 등장한다는 이유로 분몰부피 사이 관계가 아니라고 좁혀 읽으면 안 된다.독립적으로 변하지 않는다는 제약이 두 분몰부피를 연결한다."
  },
  "source_exposure_note": "blind supplement가 tight crop이 아닌 공식 page14 전체여서 옆단의 다음 지문 일부도 보였다.정답·SDSS는 없었으며 다음G507은 과거지문일부노출을명시해야한다."
}
```
