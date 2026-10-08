

<!-- luna-raw:BJB-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G444",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2018/2018_answer_2018학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "반공주의역사가들도민족주의·반유대주의와희생자의식을공유하므로전복의주체로귀속할수없다.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외.누락인라인표현은전체답공개전복원."
  ]
}
```


<!-- luna-raw:BJB-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G444",
  "sdss_seen": false,
  "general_task": "역사집단의기억공유와필자의성찰평가대조",
  "decisive_relation": "반공주의를희생자의식전복과동일시하지않고좌우공유코드를보존",
  "primary": {
    "code": 75,
    "scope": "②",
    "reason": "반공주의역사가와트랜스내셔널성찰주체의입장을서로교환하지않는다."
  },
  "auxiliary": [
    {
      "code": 23,
      "scope": "②⑤",
      "reason": "좌우모두의민족적희생서사공유를확인."
    },
    {
      "code": 98,
      "scope": "②",
      "reason": "전복하려는기억대상과그행위주체를잘못귀속."
    },
    {
      "code": 63,
      "scope": "④",
      "reason": "말소된유대계희생정보가일방적피해서사의약화근거가될가능성을평가."
    },
    {
      "code": 2,
      "scope": "④",
      "reason": "약화시킬수있음이지모든피해의부정이나가해규모확정은아님."
    }
  ],
  "surface": [
    {
      "code": 86,
      "scope": "④",
      "reason": "과반수라는크기정보가있지만그수량만으로정치적기억의변화가수학적으로결정되지는않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 26,
      "verdict": "표면대비유보",
      "refutation": "좌/우정치대비가희생의식유무를완전히분할하지않는다.공유요소가존재한다."
    },
    {
      "code": 36,
      "verdict": "④국소가능",
      "refutation": "일방적피해서사에대한다른기억은반증방향이지만유대계희생비율만으로모든국민의가해를추론할수없다."
    },
    {
      "code": 78,
      "verdict": "보조",
      "refutation": "민족명예보호동기는배경이나②는의도추측보다공유된기억의귀속을확인한다."
    }
  ],
  "counterfactual": "반공주의가반유대주의와희생자의식을거부했다는추가문장이있다면②전복설명에근거가생긴다.본문은오히려공산당애국분파와공유한다고명시한다.",
  "source_restoration": "누락명칭및발문은답공개전BJB_source_restoration.md로복원.최초hold와blind의조건기록보존.",
  "unresolved": "④의단독비율사실로가해규모나전체민족의책임을확정하지않는다.말소된기억과자발적협력맥락에서약화가능성만기록.",
  "confidence": 0.97
}
```
