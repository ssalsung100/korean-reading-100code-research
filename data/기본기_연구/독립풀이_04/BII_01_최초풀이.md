

<!-- luna-raw:BII-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G437",
  "selected_answer": 2,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BII.json",
  "necessary_information": [
    {
      "location": "㉠문단",
      "evidence": "지급불능예상때문에먼저인출할유인이생김."
    },
    {
      "location": "㉡~㉣",
      "evidence": "낮은자기자본비율이위험유인을강화,은행지배력의사적사용이약탈,차입·가격상승의양의되먹임이거품확대."
    }
  ],
  "minimal_logic_without_codes": "㉠대책은예금지급불안을낮춰인출유인을줄이는것이다.고액예금을보장밖에두는②는그예금주의인출불안을유지하므로㉠대책으로맞지않는다.",
  "intermediate_reasoning": [
    "①지급보장은위기예상에따른선착순인출유인을낮춘다.③자기자본비율하한은손실을채권자에게전가하는유인을완화한다.",
    "④특수관계인거래공시는은행가의사적지배력이용을감시하는방향이다.⑤담보대출한도비율축소는가격상승→차입증가→추가상승연쇄를제한한다.",
    "고액예금보장제외가다른정책목적에서어떠한효과를갖는지와㉠인출유인을줄이는기제에맞는지는구별한다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "서민의주택구입을도와야한다는일상적목적을금융위기원인차단이라는발문목적에끼워넣으면⑤를배제하게된다.㉣은과도한차입의증폭을문제삼는다."
  }
}
```
