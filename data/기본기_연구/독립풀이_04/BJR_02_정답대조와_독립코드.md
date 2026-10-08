

<!-- luna-raw:BJR-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G449",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2018/2018_answer_2018학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "관계특수성과계약불완전성증가는기회주의·속박우려를높이는쪽이지거래비용감소근거가아니다.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외.BJR인라인명칭은답공개전복원."
  ]
}
```


<!-- luna-raw:BJR-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G449",
  "sdss_seen": false,
  "general_task": "윌리엄슨의성과와관계변수의방향평가",
  "decisive_relation": "특수성·불완전성증가는속박위험과거래어려움증가방향",
  "primary": {
    "code": 49,
    "scope": "④",
    "reason": "특수성/불완전성과거래비용의방향을반대로바꾼오류."
  },
  "auxiliary": [
    {
      "code": 46,
      "reason": "대안가치하락→기회주의우려→안전장치필요의경로."
    },
    {
      "code": 19,
      "scope": "②③⑤",
      "reason": "코즈의설명부족에행동가정·계약유형을추가한이론보완."
    },
    {
      "code": 64,
      "scope": "①",
      "reason": "거래비용발생기제설명과권위원천설명은범위가다르다."
    }
  ],
  "surface": [
    {
      "code": 88,
      "reason": "비용을언급해도정확한편익-비용차를계산하는문항은아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 75,
      "verdict": "전체비교보조",
      "refutation": "학자별귀속은필요하나④는같은이론내변수방향의오류다."
    },
    {
      "code": 43,
      "verdict": "조건경계",
      "refutation": "안전장치강화후실제비용과거래특성에따른기본위험을같은관측값으로비교하면안되지만이문항은실험설계검토가아니다."
    },
    {
      "code": 54,
      "verdict": "기각",
      "refutation": "관계특수성하나만으로모든거래비용수치가충분히결정된다고하지않는다."
    }
  ],
  "counterfactual": "특수성높은거래에더강한안전장치를도입해사후위험이낮아지는사례는가능하지만이는특수성자체가비용을낮춘다는④의관계와다르다.개입전조건과대응후결과를나눈다.",
  "source_restoration": "윌리엄슨의기업이론명칭과발문은답공개전blind보충복원.최초hold보존.",
  "confidence": 0.98
}
```
