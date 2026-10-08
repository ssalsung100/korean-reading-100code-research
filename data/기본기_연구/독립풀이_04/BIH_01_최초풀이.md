

<!-- luna-raw:BIH-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G437",
  "selected_answer": 5,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BIH.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G437_visual01.md"
  ],
  "necessary_information": [
    {
      "location": "㉠~㉣문단",
      "evidence": "인출기대/주주위험유인/은행가사익/지속상승낙관의원인구별."
    },
    {
      "location": "보기",
      "evidence": "가격상승기대의차입증가,낙관적정부규제완화,주식회사전환,파산전경영자보상확대."
    }
  ],
  "minimal_logic_without_codes": "투자자·조합·정부의낙관을공통으로포착해거품과취약성을비판하는㉣의⑤가사례와가설모두에맞는다.",
  "intermediate_reasoning": [
    "①보상과위험투자정도의비례가보기에서제시되지않고㉠은인출쇄도를핵심으로한다.",
    "②㉡이문제삼는주주는예금주와같지않다.보기의차입투자자도예금주라고확정하지않는다.",
    "③주식회사전환후위험투자이익이예금주에게귀속된다는근거가없고㉢은은행가사익추구를비판한다.",
    "④㉢에서약탈의행위주체는지배주주·고위경영자이다.예금주들이공격경영을용인했다는사실은보기에없다."
  ],
  "most_attractive_wrong": {
    "choice": 2,
    "exact_error": "고위험투자라는공통어에끌려㉡의주주유인을예금주의과도한차입으로옮긴다.사례의투자자·예금주·주주를구분해야한다."
  }
}
```
