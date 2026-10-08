

<!-- luna-raw:APS-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G277",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "뮤어가채택한ㄴㄷㅁ과제시됐으나미채택인정보·상급심근거를구별.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:APS-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 60,
      "reason": "판결의실제논거로채택된명제를식별"
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "뮤어/상급법원/가족증언의근거귀속"
    },
    {
      "code": 75,
      "reason": "상반판결의입장분리"
    },
    {
      "code": 10,
      "reason": "전뇌사와본인의사확인의요건미충족"
    }
  ],
  "surface": [
    {
      "code": 3,
      "reason": "재판시간순서만으로채택여부알수없음"
    }
  ],
  "competitors": [
    {
      "code": 23,
      "refutation": "사건에등장한정보들의공통집합을고르는게아니라특정결론의근거필터"
    },
    {
      "code": 2,
      "refutation": "회복가능성희박함을뇌사필연으로강화하면오류지만정답조합전체는논거귀속"
    },
    {
      "code": 63,
      "refutation": "독자가증언을얼마나강하게평가하는지와판사가실제채택했는지는다름"
    }
  ],
  "counterfactual_probe": "가족증언을판사가결정적으로받아들였다는문장이있다면ㄹ포함가능하나본문은반대.제시·청취·채택세단계분리.",
  "confidence": 0.97,
  "passage_group": "G277",
  "sdss_disclosed": false
}
```
