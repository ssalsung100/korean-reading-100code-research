

<!-- luna-raw:BIZ-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G443",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2018/2018_answer_2018학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "본문전체가아닌㉠의연령차별금지반대견해를세고용차등사례에일관되게적용한다.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외.주어진역사적지문모형의독해범위로한정."
  ]
}
```


<!-- luna-raw:BIZ-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G443",
  "sdss_seen": false,
  "general_task": "지정된규범입장을세연령차등사례에적용",
  "decisive_relation": "연령차별금지를정당하지않다고보는㉠에맞춰사례의차별금지위반여부를판정",
  "primary": {
    "code": 75,
    "scope": "ㄱㄴㄷ",
    "reason": "본문의조건부입법가능성설명과별도의㉠반대견해를구분해지정견해만적용한다."
  },
  "auxiliary": [
    {
      "code": 37,
      "reason": "세사례가모두연령기준고용차등이라는적용범주에속함을확인."
    },
    {
      "code": 79,
      "reason": "차등금지의정당성부정이라는규범관계를사례에적용."
    },
    {
      "code": 64,
      "reason": "필자전체설명이나현실법이아닌㉠의주장범위로한정."
    }
  ],
  "surface": [
    {
      "code": 86,
      "reason": "연령숫자가등장하지만연령차이의계산이나집단수량비교를하지않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 12,
      "verdict": "보조",
      "refutation": "연령차등이면㉠은금지정당성을인정하지않는다는조건으로형식화할수있으나먼저어느입장인지귀속해야한다."
    },
    {
      "code": 63,
      "verdict": "주기각",
      "refutation": "㉠주장이옳은지비판하거나증거로강화하는과제는아니다."
    },
    {
      "code": 83,
      "verdict": "배경",
      "refutation": "노동능력변화라는사실에서규범결론을내리는㉠의논증이배경이지만그당위도출의타당성을심사하는발문은아니다."
    }
  ],
  "counterfactual": "발문이본문전체취지에비추어라고바뀌면인권취지·정책목적·영업제한조건을함께검토해야한다.현재㉠을지정한발문이적용범위를좁힌다.",
  "confidence": 0.97
}
```
