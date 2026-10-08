

<!-- luna-raw:BJK-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G447",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2018/2018_answer_2018학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "포유류암컷수정란의성결정유전자삽입후수컷기관발달은발생중추가유전자지령가설의직접강화이다.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외.본문정상발달모형과명시된개입범위에한정."
  ]
}
```


<!-- luna-raw:BJK-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G447",
  "sdss_seen": false,
  "general_task": "발생가설을직접검증하는개입증거선별",
  "decisive_relation": "기본암컷수정란에성결정유전자를추가하고비기본수컷기관발달을관찰",
  "primary": {
    "code": 63,
    "scope": "④",
    "reason": "가설이핵심원인으로지목한성결정유전자와발생시점을직접조작해예상결과를얻은증거이다."
  },
  "auxiliary": [
    {
      "code": 46,
      "reason": "유전자추가→고환·음경발달의원인경로대응."
    },
    {
      "code": 64,
      "scope": "①②③⑤",
      "reason": "성체전환·온도·행동변화는지정가설의발생유전자범위와다름."
    },
    {
      "code": 3,
      "scope": "①③대④",
      "reason": "성체변화와수정란부터의개체발생을구별."
    },
    {
      "code": 37,
      "scope": "④",
      "reason": "포유류암컷기본에서비기본성이추가된사례요건확인."
    }
  ],
  "surface": [
    {
      "code": 52,
      "scope": "①",
      "reason": "효소발현감소라는억제표현이있어도그자체가지정가설강화의충분근거는아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 43,
      "verdict": "보조후보",
      "refutation": "인위적개입이있으나대조군과모든통제조건이제시된것은아니므로완전한효과식별실험이라고추가확정하지않는다."
    },
    {
      "code": 74,
      "verdict": "배경",
      "refutation": "상반경쟁가설의구체예측비교가아니라한가설과가장직접맞는증거를고른다."
    },
    {
      "code": 36,
      "verdict": "기각",
      "refutation": "다른선지가핵심가설의직접지지가아니라는것과모두가가설을거짓으로반증한다는것은다르다."
    }
  ],
  "counterfactual": "④에서수정란유전자삽입대신성체행동만바뀌었다면개체발생기관분화라는예측과의연결이약해진다.가설의대상·시점·기제세조건을보존한다.",
  "confidence": 0.98
}
```
