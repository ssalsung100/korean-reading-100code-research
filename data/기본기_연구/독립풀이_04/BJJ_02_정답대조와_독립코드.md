

<!-- luna-raw:BJJ-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G447",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2018/2018_answer_2018학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "고환과항뮐러관인자생산은유지되고테스토스테론/DHT수용경로만차단되어내부고환이남는다.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외.본문정상발달모형과명시된개입범위에한정."
  ]
}
```


<!-- luna-raw:BJJ-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G447",
  "sdss_seen": false,
  "general_task": "선택적수용체결함후기관발달의남는경로판정",
  "decisive_relation": "호르몬생산과수용반응을분리하고결함이없는항뮐러관경로를보존",
  "primary": {
    "code": 50,
    "scope": "①②⑤",
    "reason": "테스토스테론/DHT결합차단의후속기관만차단되고고환생성과다른호르몬경로는남는다."
  },
  "auxiliary": [
    {
      "code": 17,
      "reason": "외부성징과내부기관,호르몬생산과수용반응을다른판정대상으로구분."
    },
    {
      "code": 98,
      "reason": "어느호르몬의수용체결함인지정확히귀속."
    },
    {
      "code": 45,
      "reason": "분기신호별기관산출을연결."
    },
    {
      "code": 3,
      "reason": "이미형성된고환과후속외부기관발생의시차를보존."
    }
  ],
  "surface": [
    {
      "code": 4,
      "reason": "모든호르몬이반응불가라고범위를넓히는오류는있지만핵심은선택적경로구별이다."
    }
  ],
  "competing_codes": [
    {
      "code": 40,
      "verdict": "보조",
      "refutation": "외부/내부기관의구성관계도필요하나결함효과를판정하려면각기원·신호경로를따로읽어야한다."
    },
    {
      "code": 52,
      "verdict": "주기각",
      "refutation": "항뮐러관신호는제거작용이나그제거작용이억제된것이아니다.명시수용체결함은다른호르몬경로이다."
    },
    {
      "code": 54,
      "verdict": "기각",
      "refutation": "외형하나로내부기관전체를충분히결정한다는관계는본문에없다."
    }
  ],
  "counterfactual": "항뮐러관인자의수용반응까지결함이라고보기에추가된다면⑤의내부기관가능성을별도로검토해야한다.현재테스토스테론/DHT결함만으로그경로를제거할수없다.",
  "confidence": 0.99
}
```
