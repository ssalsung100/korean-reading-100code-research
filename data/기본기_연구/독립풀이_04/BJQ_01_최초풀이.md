

<!-- luna-raw:BJQ-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G449",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BJQ.json",
  "necessary_information": [
    {
      "location": "거래비용정의",
      "evidence": "상대탐색·가격흥정·조건협상·이행확인강제의어려움."
    },
    {
      "location": "윌리엄슨계약설명",
      "evidence": "불완전성·속박에복잡한계약안전장치로대처하고안되면자체조달."
    }
  ],
  "minimal_logic_without_codes": "계약제도와안전장치가발달하면이행위험과입증의어려움을줄일수있어③이맞다.",
  "intermediate_reasoning": [
    "①거래량과정확반비례관계는제시되지않았다.②현물거래에도상대탐색·가격흥정등어려움은있을수있다.",
    "④거래비용은시장거래의어려움이며기업내부권위행사비용과동일하게정의되지않았다.⑤가치불확실성이줄면협상과입증어려움도줄방향이지더커진다는근거가없다.",
    "③줄일수있음이모든계약을완전하게만들어비용0으로제거한다는뜻은아니다."
  ],
  "most_attractive_wrong": {
    "choice": 2,
    "exact_error": "계약에특유한장기불확실성문제가없으면어떤거래비용도없다고확대한다.현물거래에도다른탐색·흥정비용이남는다."
  }
}
```
