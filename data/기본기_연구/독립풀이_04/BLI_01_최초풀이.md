

<!-- luna-raw:BLI-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G464",
  "selected_answer": 1,
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
      "location": "2문단",
      "evidence": "소유자노력·기여와무관한임대소득을환수.사용·처분권은자유,수익권중개량수익은제외."
    },
    {
      "location": "2~3문단",
      "evidence": "다른세금을없앨충분세수기대.공정성과효율성은불로소득부담귀속과초과부담이라는별도근거."
    }
  ],
  "minimal_logic_without_codes": "개량에의한수익을제외한토지수익을불로소득으로환수하자는주장이므로개량되지않은토지임대료를불로소득으로본다는①이맞는다.",
  "intermediate_reasoning": [
    "② 충분한세수를기대했다는서술과반대다.",
    "③ 자유로둔사용권에제약을붙인다.",
    "④ 효율성향상이공정성향상의원인이라고본문은설명하지않고각각별도의근거를준다.",
    "⑤ 토지를제외한영역의자유시장을옹호했다는예외범위를없앤다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "좋은세금의두장점을함께갖는다는사실을하나가다른하나를발생시킨다는인과관계로바꾼다."
  },
  "scope_limit": "본문의조지입장판독이며현행조세의가치평가나정책권고로확장하지않는다."
}
```
