

<!-- luna-raw:BJQ-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G449",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2018/2018_answer_2018학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "계약제도와안전장치는시장거래의이행·입증어려움을줄일수있다.현물의다른거래비용은남는다.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외.BJR인라인명칭은답공개전복원."
  ]
}
```


<!-- luna-raw:BJQ-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G449",
  "sdss_seen": false,
  "general_task": "거래비용정의와완화수단관계확인",
  "decisive_relation": "계약안전장치가거래이행의어려움을완화할수있음",
  "primary": {
    "code": 59,
    "scope": "③",
    "reason": "거래의어려움을계약제도로줄이는문제-대응관계이다."
  },
  "auxiliary": [
    {
      "code": 16,
      "scope": "④",
      "reason": "거래비용은시장거래어려움이라는정의범위를보존."
    },
    {
      "code": 17,
      "scope": "②④",
      "reason": "현물/계약거래와기업내부조직비용을구분."
    },
    {
      "code": 2,
      "scope": "③",
      "reason": "줄일수있다는완화가능성을완전제거로강화하지않음."
    },
    {
      "code": 49,
      "scope": "⑤",
      "reason": "불확실성감소의비용완화방향을거꾸로읽지않음."
    }
  ],
  "surface": [
    {
      "code": 91,
      "scope": "①",
      "reason": "거래량과반비례라는수리관계는근거없음."
    }
  ],
  "competing_codes": [
    {
      "code": 19,
      "verdict": "국소중첩",
      "refutation": "불완전계약의빈틈을장치로보완한다는표현과겹치나모든비용을보충으로만환원하지않는다."
    },
    {
      "code": 50,
      "verdict": "보조가능",
      "refutation": "기회주의경로를차단하는효과는가능하지만거래비용에는탐색·협상등다른요소도있다."
    },
    {
      "code": 54,
      "verdict": "기각",
      "refutation": "계약제도발전이모든이행문제를완전히해결한다는보장은없다."
    }
  ],
  "counterfactual": "시간차없는현물거래에서도상대방탐색이나가격흥정이어려울수있다.계약특수불확실성의부재를거래비용전체0으로확대할수없다.",
  "confidence": 0.98
}
```
