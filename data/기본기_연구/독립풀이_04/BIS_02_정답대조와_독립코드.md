

<!-- luna-raw:BIS-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G441",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2017/2017_answer_2017학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "비개념주의는사람으로해석하기전비개념적감각경험을선행요건으로본다.재료를개념적으로알아채야한다는조건은추가하지않는다.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외및BIT지지/확정구분유지."
  ]
}
```


<!-- luna-raw:BIS-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G441",
  "sdss_seen": false,
  "general_task": "지정견해로새사례의인식조건설명",
  "decisive_relation": "해석되지않은감각경험을개념적사람인지의선행필요조건으로적용",
  "primary": {
    "code": 10,
    "scope": "③",
    "reason": "비개념주의가제시한판단전감각의필요성을그림인지에적용한다."
  },
  "auxiliary": [
    {
      "code": 80,
      "reason": "감각내용과사람이라는개념적판단을구분."
    },
    {
      "code": 75,
      "reason": "그림의원래개념주의해석을지정된비개념주의와혼합하지않음."
    },
    {
      "code": 3,
      "reason": "감각선행→판단후행순서를유지."
    },
    {
      "code": 17,
      "scope": "⑤",
      "reason": "물감이감각되는것과물감이라고판단하는것은다르다."
    }
  ],
  "surface": [
    {
      "code": 100,
      "reason": "그림의사람이상징적으로그려졌다는미술표현자체를해석하는문항이아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 12,
      "verdict": "국소중첩",
      "refutation": "사람인지가있으면선행감각이있다는조건문으로도표현된다.10과별개논리식으로분리하지않는다."
    },
    {
      "code": 63,
      "verdict": "주기각",
      "refutation": "이사례가실제로어느이론을더강화하는지평가하기보다지정이론의설명을선택한다."
    },
    {
      "code": 95,
      "verdict": "넓은표현중첩",
      "refutation": "판단에감각존재가필요하다는표현은가능하지만여기서는무해석감각이라는정확한조건이핵심.일반존재추론으로축약하지않는다."
    }
  ],
  "counterfactual": "⑤의재료구성에대한개념적깨달음이없어도비개념적감각에서사람인지로갈수있다는본문설명이성립한다.재료판단을추가필수조건으로만들수없다.",
  "confidence": 0.98
}
```
