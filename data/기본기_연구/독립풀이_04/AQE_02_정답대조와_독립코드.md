

<!-- luna-raw:AQE-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G281",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "응결법칙+차가운잔/수증기조건에서습기필연도출.과학소재만이나가능성증가는부족.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:AQE-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 60,
      "reason": "법칙과초기조건에서현상을필연유도하는논증형식에사례대조"
    }
  ],
  "auxiliary": [
    {
      "code": 2,
      "reason": "필연성과개연성구별"
    },
    {
      "code": 56,
      "reason": "제시된과학적설명모형의요건"
    },
    {
      "code": 37,
      "reason": "설명모형에맞는사례선택"
    }
  ],
  "surface": [
    {
      "code": 46,
      "reason": "과학적원인설명소재라는것만으로모형적합성보장안함"
    }
  ],
  "competitors": [
    {
      "code": 44,
      "refutation": "기능/목적제시만으로법칙적필연도출을대신못함"
    },
    {
      "code": 77,
      "refutation": "관측반복에서법칙을일반화하는단계가아닌주어진일반관계의적용"
    },
    {
      "code": 10,
      "refutation": "생존에산소필요하다는③만으로폐존재가연역되는것은아님.필요기능에서특정기관존재도출은다른논증"
    }
  ],
  "counterfactual_probe": "⑤가능성이가장높다를구체초기조건과법칙에따른필연적발생으로구성하면모형에가까워질수있지만현선지는그보장을주지않음.",
  "confidence": 0.97,
  "passage_group": "G281",
  "sdss_disclosed": false
}
```
