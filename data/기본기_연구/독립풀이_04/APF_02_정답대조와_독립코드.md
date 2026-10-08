

<!-- luna-raw:APF-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G273",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "공장주의이윤·수출우려에서곡물법철폐입장복원.국방목적언급을경제보다우선으로강화금지.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:APF-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 75,
      "reason": "경제주체별정책입장과논거를귀속"
    }
  ],
  "auxiliary": [
    {
      "code": 46,
      "reason": "관세→곡가→임금→이윤/수출경로"
    },
    {
      "code": 44,
      "reason": "제조업확장을위한무역정책수단"
    },
    {
      "code": 8,
      "scope": "⑤",
      "reason": "언급된국방논거에서경제보다우선이라는추가서열배제"
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "정책의공정함에대한독자의평가는묻지않음"
    }
  ],
  "competitors": [
    {
      "code": 74,
      "refutation": "예측차이를검증하는관측자료없이입장과논거대응을묻는다"
    },
    {
      "code": 86,
      "refutation": "임금·가격상승이있어도노동자의실질이득크기를계산할근거없음"
    },
    {
      "code": 17,
      "refutation": "귀속행동으로75와중첩가능하나경제주체의정책견해라는범위가작업대표75의이유"
    }
  ],
  "counterfactual_probe": "⑤경제적차원보다를국방차원에서도로고치면명시논거와부합.목적존재와목적서열별개.",
  "confidence": 0.96,
  "passage_group": "G273",
  "sdss_disclosed": false
}
```
