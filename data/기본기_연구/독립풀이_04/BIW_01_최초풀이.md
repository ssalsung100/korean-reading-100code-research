

<!-- luna-raw:BIW-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G442",
  "selected_answer": 2,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BIW.json",
  "necessary_information": [
    {
      "location": "2문단",
      "evidence": "Wnt지나친불활성→뼈형성저해→골다공증."
    },
    {
      "location": "3문단",
      "evidence": "Wnt자극증가→GSK3β억제→β카테닌인산화분해감소→β카테닌증가. APC복합체결함도β카테닌증가."
    }
  ],
  "minimal_logic_without_codes": "Wnt불활성이문제인골다공증을이경로로완화하려면Wnt작용을높이는방향이므로β카테닌이증가한다는②가맞다.본문경로안의예측이며실제약물선택이나효능확정은아니다.",
  "intermediate_reasoning": [
    "①줄기세포공급감소에서흡수증가를도출할근거가없다.",
    "③APC는인산화복합체구성으로분해를돕는쪽이지인산화β카테닌분해를막지않는다.",
    "④APC결함으로인산화가막혀있는데Wnt를더해도β카테닌을분해시켜낮추는경로가생기지않는다.",
    "⑤인산화불가변이는β카테닌분해를줄여농도를높이고자기복제유지쪽으로작용하므로줄기세포수감소와반대다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "정상신호Wnt를추가하면어떤돌연변이도정상화될것이라는복구가정을넣는다.본문에서Wnt는β카테닌분해를오히려억제하는방향이며APC결함을수리한다는기능도없다."
  },
  "unresolved": "②는골다공증의본문상Wnt기전과그기전을조절하는대책이라는조건안의방향예측.실제전신효과·투여량·안전성등은판정하지않는다."
}
```
