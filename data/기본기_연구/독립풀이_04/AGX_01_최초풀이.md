

<!-- luna-raw:AGX-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G202",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "전류적산은시간간격마다측정전류×간격을더해전하량추정.",
    "최대시간은완전방전기준,전압강하는니켈카드뮴에서검출가능,온도측정은환경영향가능,각방식최종은전원차단."
  ],
  "minimal_logic_without_codes": "전류가일정하면각간격의전류값이실제와같아측정합의근사가잘맞는다. 전류가변할때보다일정할때추정오차가더커진다는부원2의주장이틀림.",
  "intermediate_reasoning": [
    "1 초기잔량있는데완전방전기준시간동안충전하면과충전가능.",
    "3 검출가능전압강하는모든종류에있는것아님.",
    "4 주변온도가표면온도를바꾸면충전정도만반영하는지표아님.",
    "5 판정뒤실제전원차단이없으면제시된방식의과충전방지작동완성안됨."
  ],
  "most_attractive_wrong_answer": 3,
  "exact_error": "전압강하가일반설명에등장한다고모든충전지에서검출가능한크기로나타난다고확대하면부원3을틀리다고오인한다.",
  "scope_limit": "측정오차·기기고장등원문밖변수는가정하지않고주어진일정전류와샘플링간격합산구조를비교.",
  "quota_status": "unavailable"
}
```
