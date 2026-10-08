

<!-- luna-raw:BJW-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G451",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2018/2018_answer_2018학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "유류분권자의후보범주와최우선순위의실제권리취득을구분한다.비속·배우자가있으면형제자매는배제.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외.2018제시지문규정의독해이며현행법안내가아님."
  ]
}
```


<!-- luna-raw:BJW-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G451",
  "sdss_seen": false,
  "general_task": "상속권리자의범주와순위규칙적용",
  "decisive_relation": "목록에포함되어도선순위가있으면후순위는현재권리자가아님",
  "primary": {
    "code": 8,
    "scope": "④",
    "reason": "비속·배우자의우선순위가형제자매권리행사를배제한다."
  },
  "auxiliary": [
    {
      "code": 12,
      "reason": "최우선순위상속인이라는조건을충족해야유류분권취득."
    },
    {
      "code": 17,
      "reason": "잠재권리자범주와실제권리자집합을구분."
    },
    {
      "code": 98,
      "scope": "①",
      "reason": "사회관념과혁명입법자태도를바꾸지않음."
    }
  ],
  "surface": [
    {
      "code": 4,
      "reason": "모든범주가동시권리라는범위확대가있지만직접오류는순위조건누락이다."
    }
  ],
  "competing_codes": [
    {
      "code": 9,
      "verdict": "국소중첩",
      "refutation": "순위서열로표상할수있지만판정은상위존재시하위선택제외라는조건부우선성이다."
    },
    {
      "code": 29,
      "verdict": "보조",
      "refutation": "권리자목록집합만표시하면현재권리자선택규칙을설명하지못한다."
    },
    {
      "code": 88,
      "verdict": "배경",
      "refutation": "재산자유와상속인보호의조정이전체주제이나정답④는구체순위규칙이다."
    }
  ],
  "counterfactual": "선순위자들이모두없거나권리자격이없다는조건이라면형제자매가권리자가될수있다.범주포함만으로현재동시권리를인정할수없다.",
  "confidence": 0.99
}
```
