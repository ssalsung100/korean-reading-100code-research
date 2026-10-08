

<!-- luna-raw:AYM-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G352",
  "selected_answer": 5,
  "confidence": 0.94,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "미확정",
  "required_information_and_location": [
    "4문단 소형서남극R74%,로스R17%",
    "5문단 대형91%면적·D50%,소형9%·D50%",
    "6문단 S=D/면적"
  ],
  "minimal_logic_without_codes": "낮은단위면적융해량을가진대형표본을전체로확대하면작은빙붕의큰융해량을놓쳐전체D,R,S를낮게잡는다.그러나대형로스의낮은R은그표본편향때문에과소평가된것이아니다.",
  "intermediate_reasoning": [
    "①분모면적고정D과소→S과소",
    "②R=D/(C+D),C고정시D과소→R과소",
    "③④소형고융해지역을대형비율로외삽한동일원인",
    "⑤로스는큰빙붕표본의낮은R이지소형누락편향대상아님"
  ],
  "most_attractive_wrong_answer": 2,
  "exact_error": "R분모에도D가들어간다는이유로D가줄때R방향을판단못한다. C가고정이면D/(C+D)는D와같이증가한다.",
  "quota_status": "unavailable"
}
```
