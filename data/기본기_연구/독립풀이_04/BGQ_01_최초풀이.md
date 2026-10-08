

<!-- luna-raw:BGQ-blind-20261002-r3-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G422",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "prior_exposure": "unknown",
    "official_answer_read": false,
    "sdss_read": false,
    "existing_case_analysis_read": false,
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "보기",
      "evidence": "뉴턴법칙은거리에따른중력변화를설명,작은낙하구간에서는중력을상수로근사"
    },
    {
      "location": "특수상대/고전관계",
      "evidence": "새이론의설명범위안에옛이론유효조건이포함됨"
    }
  ],
  "minimal_logic_without_codes": "뉴턴의 더 넓은 설명 안에서 작은 구간의 갈릴레오 법칙이 근사적으로 유효하므로 포섭 관계①이다.",
  "intermediate_inference": [
    "②는서로다른영토의접경연결로묘사하여포함관계와다름.",
    "③근사라는이유로연결불가라고할수없음.",
    "④혼돈은두이론의다리가아니라본문상고전전용영역.",
    "⑤설명방향이뒤집히고별도영역상보관계로잘못바꿈."
  ],
  "attractive_wrong_answer": 2,
  "exact_error": "②는포함되는유효영역을서로겹치지않는두영역이경계에서만나는구조로바꾼다.",
  "unresolved": "보기수식과변수기호의전사누락있으나중력가속도상수근사와포섭관계는문장으로판정가능."
}
```
