

<!-- luna-raw:BIU-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G442",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2017/2017_answer_2017학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "소낭줄기세포의분열산물이상피로분화해융모를채운다.원줄기세포와이동·분화한후손세포를구분한다.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외및본문기전범위유지."
  ]
}
```


<!-- luna-raw:BIU-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G442",
  "sdss_seen": false,
  "general_task": "세포공급과분화과정의기원·정체성확인",
  "decisive_relation": "소낭줄기세포의분화산물이융모상피를이룬다는과정대응",
  "primary": {
    "code": 45,
    "scope": "④",
    "reason": "줄기세포분열→이동하는후손→상피분화→융모구성이라는입출력경로를보존한다."
  },
  "auxiliary": [
    {
      "code": 98,
      "scope": "②③",
      "reason": "Wnt분비/반응주체및원줄기세포/후손세포의행위를바꾸지않는다."
    },
    {
      "code": 17,
      "scope": "②",
      "reason": "세포의발생기원과분화후유형을구분."
    },
    {
      "code": 49,
      "scope": "①",
      "reason": "융모는표면적을늘리는방향이며반비례가아니다."
    }
  ],
  "surface": [
    {
      "code": 40,
      "reason": "융모의구성요소가상피라는부분관계가있으나생성과분화경로까지설명하지는않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 3,
      "verdict": "보조",
      "refutation": "순서는중요하지만전후관계만으로각세포의정체성과작용을복원할수없다."
    },
    {
      "code": 42,
      "verdict": "보조",
      "refutation": "소낭/융모의공간위치는필요하나단순위치이동과분화를구별해야한다."
    },
    {
      "code": 46,
      "verdict": "국소중첩",
      "refutation": "공급원과분화원인을잇는인과관점도가능하며45와배타적으로나누지않는다."
    }
  ],
  "counterfactual": "②가줄기세포의분열로생긴세포가상피로분화하며융모로이동한다고서술하면본문과맞는다.단순히위치명만뒤집으면분화정체성오류가남는다.",
  "confidence": 0.97
}
```
