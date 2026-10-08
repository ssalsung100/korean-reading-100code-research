

<!-- luna-raw:BIY-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G443",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2018/2018_answer_2018학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "강행규정이없는한이라는조건을규정이있더라도로뒤집어자유계약정당화를확대한것이오류.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외.주어진역사적지문모형의독해범위로한정."
  ]
}
```


<!-- luna-raw:BIY-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G443",
  "sdss_seen": false,
  "general_task": "조건부계약정당화의적용범위확인",
  "decisive_relation": "강행규정부재라는조건을강행규정존재상황에옮긴오류",
  "primary": {
    "code": 12,
    "scope": "③",
    "reason": "규정이없는한이라는분기조건을반대로바꾸면계약이임금차이를정당화한다는근거가유지되지않는다."
  },
  "auxiliary": [
    {
      "code": 10,
      "scope": "⑤",
      "reason": "인권보호취지를정책목적이대체할수없음."
    },
    {
      "code": 2,
      "scope": "②④⑤",
      "reason": "입법가능성·침해여지·정당성미보장이라는각결론강도를유지."
    },
    {
      "code": 17,
      "scope": "③",
      "reason": "당사자의계약자유영역과강행규정영역을분리."
    }
  ],
  "surface": [
    {
      "code": 8,
      "reason": "규정과계약의우선관계로기술할수있지만단순서열암기보다본문의적용조건이근거."
    }
  ],
  "competing_codes": [
    {
      "code": 24,
      "verdict": "국소중첩",
      "refutation": "계약자유의예외인강행규정으로도기술가능하나기본행동은조건분기적용과같다."
    },
    {
      "code": 75,
      "verdict": "배경",
      "refutation": "마지막반대견해가있어도이문항은지정반대입장적용이아닌본문규칙추론이다."
    },
    {
      "code": 59,
      "verdict": "주기각",
      "refutation": "최선노동정책대안을설계하지않고주어진정당화관계를판정한다."
    }
  ],
  "counterfactual": "③의강행규정이있더라도를없는한으로바꾸면자유계약이합리적이유가될수있다는본문가능성과맞는다.규정의존재여부가판정을바꾼다.",
  "confidence": 0.98
}
```
