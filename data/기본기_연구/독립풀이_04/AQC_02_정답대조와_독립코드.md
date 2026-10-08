

<!-- luna-raw:AQC-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G280",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "일종의복장은실제옷이아닌전시대상으로꾸며진외관이라는확장뜻.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:AQC-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 100,
      "reason": "복장이라는비유를전시를위한가장·구성으로해석"
    }
  ],
  "auxiliary": [
    {
      "code": 16,
      "reason": "벌거벗음과누드의문맥정의구별"
    },
    {
      "code": 80,
      "reason": "타인의시선속대상으로보이는방식"
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "모델의수치심이나도덕성을평가하는표현아님"
    }
  ],
  "competitors": [
    {
      "code": 10,
      "refutation": "가식표정이라는특정연기를모든누드의필요조건으로추가못함"
    },
    {
      "code": 17,
      "refutation": "실제옷/몸의물리적범주만보면④처럼비유를문자화"
    },
    {
      "code": 69,
      "refutation": "새사실을유비로도출하기보다표현의의미를문맥에서해제하는단계"
    }
  ],
  "counterfactual_probe": "복장을옷한벌로치환하면피부·체모자체의전시가장이라는본문근거가사라짐.비유의공유속성은꾸며짐이다.",
  "confidence": 0.96,
  "passage_group": "G280",
  "sdss_disclosed": false
}
```
