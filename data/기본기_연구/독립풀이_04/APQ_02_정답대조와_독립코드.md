

<!-- luna-raw:APQ-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G276",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "상황별변화·생사비집착·거울응대에부합하는ㄴㄹㅁ.항상아래라는고정방식배제.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:APQ-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 37,
      "reason": "외물에집착하지않는응대의취지를진술사례에적용"
    }
  ],
  "auxiliary": [
    {
      "code": 5,
      "reason": "때로위아래·조건에따라변화"
    },
    {
      "code": 80,
      "reason": "생사·대상을바라보는비집착태도"
    },
    {
      "code": 16,
      "reason": "고정기준회피와무조건겸양을구별"
    }
  ],
  "surface": [
    {
      "code": 100,
      "scope": "ㄴㅁ",
      "reason": "물·거울비유는있지만그기능적뜻을적용해야함"
    }
  ],
  "competitors": [
    {
      "code": 8,
      "refutation": "아래위중항상아래를우선하는처세서열이아님"
    },
    {
      "code": 79,
      "refutation": "예를좋아한다는일반덕목과본문의비속박취지를동일시하지않음"
    },
    {
      "code": 69,
      "refutation": "물/거울의구조유사성은보조이나새결론의유비논증보다주어진취지에맞는지판정"
    }
  ],
  "counterfactual_probe": "ㄷ아래에처함을때에따라위아래를가리지않고조화로수정하면부합.ㄱ은틀린덕목이라는평가가아니라해당취지의직접근거부족.",
  "confidence": 0.95,
  "passage_group": "G276",
  "sdss_disclosed": false
}
```
