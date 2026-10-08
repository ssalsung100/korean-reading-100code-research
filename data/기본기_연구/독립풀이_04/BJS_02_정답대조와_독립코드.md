

<!-- luna-raw:BJS-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G449",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2018/2018_answer_2018학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "속박위험심각성은복잡장기계약·자체조달의안전장치를요구하므로초단기계약을최대위험의결과로보기어렵다.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외.BJR인라인명칭은답공개전복원."
  ]
}
```


<!-- luna-raw:BJS-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G449",
  "sdss_seen": false,
  "general_task": "계약기간·형태선택을속박위험과입증가능성으로설명",
  "decisive_relation": "관계특수적위험이클수록복잡장기계약또는자체조달로대응",
  "primary": {
    "code": 59,
    "scope": "②대①③",
    "reason": "심각한속박문제에단순초단기계약보다안전장치가필요하다는대응관계를적용한다."
  },
  "auxiliary": [
    {
      "code": 49,
      "scope": "②",
      "reason": "위험수준과안전장치필요방향을반대로바꾸지않음."
    },
    {
      "code": 46,
      "scope": "③④⑤",
      "reason": "설비특수성·입증어려움→지속거래보장·계약복잡성의기제."
    },
    {
      "code": 17,
      "scope": "④⑤",
      "reason": "품질·가격조건과최소물량조건을다른입증대상으로구분."
    },
    {
      "code": 78,
      "reason": "기업이장기계약·자체생산을택하는목표와유인을설명."
    }
  ],
  "surface": [
    {
      "code": 84,
      "reason": "조사비율이여러개지만정답판정에조건부비율계산은필요없다."
    }
  ],
  "competing_codes": [
    {
      "code": 88,
      "verdict": "보조",
      "refutation": "직접경영비용과계약위험의비교는①에유효하나각조건의복잡성까지구체화하려면기회주의·입증기제를읽어야한다."
    },
    {
      "code": 91,
      "verdict": "기각",
      "refutation": "특수성이두배면계약기간도두배라는정확비례는주어지지않았다."
    },
    {
      "code": 54,
      "verdict": "기각",
      "refutation": "위험이크면현실모든기업이항상같은기간을택한다는충분결정까지확정하지않는다."
    }
  ],
  "counterfactual": "최소물량도검증불가능하거나모호하게표현된다면그조건또한복잡한안전장치를요구할수있다.전체계약의일률복잡성이아니라각대상의입증가능성이기준이다.",
  "confidence": 0.98
}
```
