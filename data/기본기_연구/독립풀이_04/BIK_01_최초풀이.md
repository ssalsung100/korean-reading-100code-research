

<!-- luna-raw:BIK-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G438",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BIK.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G438_visual01.jpg",
    "data/기본기_연구/prepared_backlog/blind_sources/G438_visual02.jpg",
    "data/기본기_연구/prepared_backlog/blind_sources/G438_visual04.md"
  ],
  "necessary_information": [
    {
      "location": "3문단",
      "evidence": "쌍성의가림은대칭적인밝기변화,세페이드팽창수축은비대칭변화."
    },
    {
      "location": "A/B그래프",
      "evidence": "A는깊고얕은대칭최저점이반복되고ⓐ는얕은최저.B는빠른상승·느린하강의비대칭.ⓑ는A주기,ⓒ는B주기."
    }
  ],
  "minimal_logic_without_codes": "A는쌍성,B는세페이드.ⓐ의작은밝기감소는어두운별이가려져밝은별이앞에있는시기이므로③.",
  "intermediate_reasoning": [
    "①A를세페이드로분류하면대칭적가림형상과맞지않는다.②B의비대칭을두별가림으로설명할수없다.",
    "④쌍성A의주기ⓑ에세페이드주기-고유밝기관계를적용할수없다.",
    "⑤ⓒ는B의고유밝기를알아내는데관련된다.겉보기최대밝기는관측되는양이므로주기를먼저알아야만알수있는양이아니다.",
    "ⓐ에서는작은광원기여분만사라지므로얕게어두워진다.깊은최저는밝은별이어두운별뒤에있는경우다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "주기를통해알아내는고유밝기와직접관측되는겉보기밝기를서로바꾼다.그래프의정규화100%만으로절대측광값이주어졌다고주장하는것과는별개다."
  },
  "source_limitations": [
    "B그래프는상대밝기100%표시이다.정확한절대최대측광값은도표에없지만ⓒ주기가그값의논리적필수조건은아니다."
  ]
}
```
