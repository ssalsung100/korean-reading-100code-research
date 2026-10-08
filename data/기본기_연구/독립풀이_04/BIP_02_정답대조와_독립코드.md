

<!-- luna-raw:BIP-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G440",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2017/2017_answer_2017학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "과거사례가새로움비판의근거가되려면새로운특징으로주장된현상과대응해야한다.국가총력전은그표적에직접대응하지않는다.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외.BIQ[A]범위공식복원대기."
  ]
}
```


<!-- luna-raw:BIP-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G440",
  "sdss_seen": false,
  "general_task": "새로움비판을뒷받침하는사실의관련성평가",
  "decisive_relation": "과거존재라는시간조건뿐아니라그현상이비판대상특징과일치해야함",
  "primary": {
    "code": 62,
    "scope": "④",
    "reason": "국가총력전의과거존재는새로운전쟁특징의과거존재라는결론과직접관련되지않는다."
  },
  "auxiliary": [
    {
      "code": 63,
      "scope": "①②③⑤",
      "reason": "관련된과거사례는새로움주장을약화하고비판자를지지."
    },
    {
      "code": 36,
      "reason": "새로등장했다는일반화에과거의동일현상을반례로제시."
    },
    {
      "code": 64,
      "scope": "④",
      "reason": "비판하는범위에포함된특징인지제한."
    },
    {
      "code": 3,
      "reason": "현재주장된신규성에대해과거존재를대조."
    }
  ],
  "surface": [
    {
      "code": 77,
      "reason": "선택적표본에대한일반화비판도본문에있지만④배제의직접이유는근거의관련성이다."
    }
  ],
  "competing_codes": [
    {
      "code": 73,
      "verdict": "국소강화후보",
      "refutation": "새로움의전제를부정하는것으로도읽히지만④는그전제를직접부정하지못한다는관련성차이를확인해야한다."
    },
    {
      "code": 75,
      "verdict": "배경",
      "refutation": "비판자의입장을귀속한후에도각사례와그주장사이연결을추가평가해야한다."
    },
    {
      "code": 91,
      "verdict": "기각",
      "refutation": "과거빈도와현대빈도의정확한비율자료가없고이를계산할필요도없다."
    }
  ],
  "counterfactual": "④가국가총력전이아니라전투원/민간인구분이없는과거사례를제시했다면비판표적특징과연결되어관련성이생긴다.옛날이라는시간표지만으로는충분하지않다.",
  "confidence": 0.98
}
```
