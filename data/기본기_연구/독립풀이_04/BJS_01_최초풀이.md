

<!-- luna-raw:BJS-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G449",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BJS.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G449_visual01.md"
  ],
  "necessary_information": [
    {
      "location": "관계특수적투자설명",
      "evidence": "대체거래시가치하락이큰경우속박우려→복잡계약,그것도어려우면자체조달."
    },
    {
      "location": "보기조사",
      "evidence": "특정탄광인접발전소는자체조달또는복잡장기계약.품질·가격조건복잡,최소물량조건단순."
    }
  ],
  "minimal_logic_without_codes": "속박위험이가장심각하면복잡한장기안전장치나자체조달을택하는방향이다.초단기계약을그최대위험의결과로읽는②는반대이므로부적절하다.",
  "intermediate_reasoning": [
    "①복잡계약으로해결이어려워자체조달한다는최후대안논리에맞는다.③특정탄광에맞춘설비·위치는관계특수성이높아지속거래보장을원한다.",
    "④품질·가격은기회주의행동과이행정도입증이복잡할수있어조건이상세하다.⑤최소물량은예측·언어모호성이비교적작아제3자입증이쉬우므로단순하게정할수있다.",
    "계약기간이길면언제나문제가커진다는일방해석은틀리다.여기서는위험에대응한안전장치로장기계약을선택하는역할도있다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "전체계약이복잡하면모든세부조건도복잡해야한다고확대한다.품질·가격과최소수량은입증난도와모호성이달라조건복잡성도달라질수있다."
  }
}
```
