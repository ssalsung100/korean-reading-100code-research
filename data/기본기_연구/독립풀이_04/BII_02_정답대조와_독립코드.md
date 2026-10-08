

<!-- luna-raw:BII-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G437",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2017/2017_answer_2017학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "고액예금지급보장제외는그예금주의인출불안을해소하지않으므로㉠원인차단과맞지않는다.",
  "limitations": [
    "봉인 공식 전사 답 대조. 원정답표 시각 재대조 미실시. unknown strict 제외 유지."
  ]
}
```


<!-- luna-raw:BII-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G437",
  "sdss_seen": false,
  "general_task": "원인에대응하는금융위기대책의적합성판별",
  "decisive_relation": "대책이그시각의위기발생경로를실제로줄이는방향인지확인",
  "primary": {
    "code": 59,
    "scope": "전체",
    "reason": "각시각의문제원인과대책을대응하고②의인출불안미해소를판별한다."
  },
  "auxiliary": [
    {
      "code": 46,
      "reason": "지급보장·자본비율·공시·대출한도가각위기기제에작용하는경로."
    },
    {
      "code": 50,
      "scope": "①⑤",
      "reason": "예상→인출 및가격→차입→가격연쇄의일부를차단."
    },
    {
      "code": 75,
      "reason": "대책의평가기준을각시각에귀속."
    },
    {
      "code": 44,
      "reason": "주택구입촉진등다른목적을위기차단목적과섞지않음."
    }
  ],
  "surface": [
    {
      "code": 84,
      "scope": "③⑤",
      "reason": "비율이라는수치지표가등장하나정확한분수값계산은필요없다."
    }
  ],
  "competing_codes": [
    {
      "code": 19,
      "verdict": "보조가능",
      "refutation": "지급불안이나감시부족의보완으로표현할수있으나서로다른정책의적합성을결정하는것은원인차단경로다."
    },
    {
      "code": 54,
      "verdict": "주기각",
      "refutation": "각대책이위기전체를완전히예방한다고보장하는것은아니다."
    },
    {
      "code": 63,
      "verdict": "보조이나주기각",
      "refutation": "대책의효과를평가하지만새실증결과로이론을강화약화하는단계는아니다."
    }
  ],
  "counterfactual": "고액예금제외가다른목적에유익할수있어도㉠의지급불능불안은남는다.정책의일반찬반과특정기제적합성을분리한다.",
  "unresolved": "②정책의현실효과전체나최선보험설계는판정하지않는다.본문기제와의대응만평가.",
  "confidence": 0.98
}
```
