

<!-- luna-raw:BIN-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G439",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2017/2017_answer_2017학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "수정후제재에나이·형편예외는없다.혼인절차위반과재가자체,구법과신법을구분해사례에적용한다.",
  "limitations": [
    "봉인 공식 전사 답 대조.원정답표 시각재대조 미실시.unknown strict제외 및 BIN본인형벌유보 유지."
  ]
}
```


<!-- luna-raw:BIN-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G439",
  "sdss_seen": false,
  "general_task": "시기별법규의요건을새사례에적용",
  "decisive_relation": "개정규정에없는나이·형편예외를추가하지않으며중매절차와재가조건을분리",
  "primary": {
    "code": 12,
    "scope": "④및②③",
    "reason": "규정의적용요건을그시기대로지키고원문에없는조건을추가하지않는다."
  },
  "auxiliary": [
    {
      "code": 3,
      "reason": "구법적용반사실과개정후제재를구별."
    },
    {
      "code": 17,
      "scope": "①⑤",
      "reason": "혼인절차위반과재가자체,여성본인과자손제재,재가상대남성을각각구분."
    },
    {
      "code": 24,
      "scope": "④",
      "reason": "정상참작예외를개정법에그대로남아있다고간주하지않음."
    },
    {
      "code": 37,
      "reason": "목씨사례의두번째혼인·오빠중매를법요건에대응."
    }
  ],
  "surface": [
    {
      "code": 78,
      "reason": "목씨가어떤개인동기로재가했는지는사례의명시된요건적용과별개."
    }
  ],
  "competing_codes": [
    {
      "code": 10,
      "verdict": "국소중첩",
      "refutation": "요건의필요성을읽는관점은12와겹치며별개논리식으로강제분리하지않는다."
    },
    {
      "code": 79,
      "verdict": "직접규범보조",
      "refutation": "법상허용·금지를다루지만정답을결정하는실제행동은시기별적용조건복원이다."
    },
    {
      "code": 54,
      "verdict": "주기각",
      "refutation": "명시자손자격제재를여성본인의구체적형벌결과로충분결정해서는안된다."
    }
  ],
  "counterfactual": "목씨가오빠중매없이혼인했다면①의조씨와같은죄목배제근거가사라진다.그러나중매가있다는것이개정후자손의과거응시금지를제거하지는않는다.",
  "unresolved": "수정대전인용은자손의관직자격제재를명시한다.④의유죄라는선지표현에서여성본인처벌의종류·정도를추론하지않는다.",
  "confidence": 0.97
}
```
