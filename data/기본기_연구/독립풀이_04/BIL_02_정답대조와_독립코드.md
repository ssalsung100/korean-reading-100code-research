

<!-- luna-raw:BIL-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G439",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2017/2017_answer_2017학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "수정은재가횟수뿐아니라현관에서모든관직으로제재범위도확대하므로그대로적용이아니다.",
  "limitations": [
    "봉인 공식 전사 답 대조.원정답표 시각재대조 미실시.unknown strict제외 및 BIN본인형벌유보 유지."
  ]
}
```


<!-- luna-raw:BIL-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G439",
  "sdss_seen": false,
  "general_task": "개정전후 법 적용범위와제재범위 비교",
  "decisive_relation": "현관제한에서모든관직제한으로범위가확대되어기존제재그대로가아님",
  "primary": {
    "code": 4,
    "scope": "②",
    "reason": "특정한요직과모든관직은적용대상의양화범위가다르다."
  },
  "auxiliary": [
    {
      "code": 5,
      "scope": "②",
      "reason": "혼인횟수기준뿐아니라제재내용도변했음을확인."
    },
    {
      "code": 3,
      "reason": "1477논의와1485수정전후규정을구분."
    },
    {
      "code": 17,
      "scope": "①",
      "reason": "재가자체와중매·혼례절차위반은다른처벌대상."
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "역사법규범이소재이나정답오류는규범의좋고나쁨이아닌범위변경이다."
    }
  ],
  "competing_codes": [
    {
      "code": 39,
      "verdict": "전체과제",
      "refutation": "구법신법을비교하는전체과제지만정답을가르는국소차이는특정/전체관직범위다."
    },
    {
      "code": 98,
      "verdict": "보조",
      "refutation": "제재를어느시기법에귀속하는지도필요하나핵심은그제재범위가같지않다는점."
    },
    {
      "code": 1,
      "verdict": "국소유사",
      "refutation": "제재대상의증가로기술할수있으나정확한수치증가를계산하기보다특정집합에서전체집합으로확대를읽는다."
    }
  ],
  "counterfactual": "신법이혼인횟수만바꾸고현관제한은유지했다면그대로적용이라는설명이가능해진다.실제신법은어떤관직에도임용불가라그반사실이성립하지않는다.",
  "confidence": 0.98
}
```
