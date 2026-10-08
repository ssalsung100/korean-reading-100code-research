

<!-- luna-raw:APN-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G275",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "자기보호를위한선택제한과타인권리·위험방지를구별.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:APN-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 16,
      "reason": "후견적간섭의자기보호·타인권리비침해조건을복원"
    }
  ],
  "auxiliary": [
    {
      "code": 37,
      "reason": "정의에사례적용"
    },
    {
      "code": 17,
      "reason": "보호대상자신/타인의귀속"
    },
    {
      "code": 79,
      "reason": "행위제한의정당화준거구별"
    }
  ],
  "surface": [
    {
      "code": 44,
      "reason": "안전이라는목적만공유해서는구분못함"
    }
  ],
  "competitors": [
    {
      "code": 46,
      "refutation": "실제피해인과를새로검증하기보다명시사례의보호대상구조판정"
    },
    {
      "code": 23,
      "refutation": "국가개입이라는공통점만으로모두후견이라하면정의요건누락"
    },
    {
      "code": 15,
      "refutation": "판단준거명칭으로16/37과중첩가능하며독립필수연산으로중복계수안함"
    }
  ],
  "counterfactual_probe": "③을안전모를떨어뜨려타인을해치는행위제한으로바꾸면자기보호만의준거를벗어난다.현실외부비용전체를부정하는판정아님.",
  "confidence": 0.96,
  "passage_group": "G275",
  "sdss_disclosed": false
}
```
