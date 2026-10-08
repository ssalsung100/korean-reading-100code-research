

<!-- luna-raw:BHY-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G434",
  "selected_answer": 3,
  "confidence": 0.96,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BHY.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G434_visual01.md",
    "data/기본기_연구/prepared_backlog/blind_sources/G434_visual02.md"
  ],
  "necessary_information": [
    {
      "location": "마지막문단",
      "evidence": "작동온도 근처 임계온도와 외부장 변화에 큰 엔트로피 변화가 적합성의 기준."
    },
    {
      "location": "보기표",
      "evidence": "C18℃,1T,2.61; D21℃,5T,2.60; B10℃,1T,1.52; A-5℃,5T,2.75; E42℃,5T,1.80."
    }
  ],
  "minimal_logic_without_codes": "실온 근처에서 작동하면서 작은 자기장으로 큰 엔트로피 변화를 내는 C가 적합하다.실온 근처인D보다 약한 장에서 약간 큰 변화이고 같은1T의B보다 변화가 크므로③.",
  "intermediate_reasoning": [
    "A는표의감소량이최대지만임계온도-5℃로 실온 목적과 맞지 않는다. E는42℃이고5T에서변화도작다.",
    "C와D는둘다실온근처로 볼 수 있으나C는1T에서2.61,D는5T에서2.60이므로 자기장조건까지보면C가 유리하다.",
    "B와C는자기장1T가같아서 엔트로피감소량을 직접비교할 수 있다.",
    "표의단일점만으로 모든자기장에서 변화량이선형이라고 추정하거나 임계온도차이를 숫자 가중합으로 환산하지 않는다.실온의정확한 목표값도미제시이므로18/21의온도차만으로 결정하지 않는다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "21℃라는값이실온에더가깝다는직관만으로D를고르면5T라는더강한장에도C보다엔트로피변화가작다는조건을놓친다."
  },
  "unresolved": "정확한목표실온·자기장생성비용함수·장세기별응답곡선은미제시.본표와정성적적합성기준범위에서C를선택한다."
}
```
