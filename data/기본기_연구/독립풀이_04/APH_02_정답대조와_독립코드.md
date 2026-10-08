

<!-- luna-raw:APH-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G273",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "수입증가량이국내감소량보다크다는②는공급부족설명의방향과맞지않음.정확량·전시조건은미확정.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:APH-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 86,
      "reason": "수입증가량과국내감소량의상대크기에따른총공급방향대조"
    }
  ],
  "auxiliary": [
    {
      "code": 92,
      "reason": "단순모형Δ공급=수입증가−국내감소"
    },
    {
      "code": 60,
      "reason": "공급차질결론을지지하는전제인지확인"
    },
    {
      "code": 46,
      "reason": "곡가하락→농업축소→공급/수요효과"
    }
  ],
  "surface": [
    {
      "code": 84,
      "reason": "비율분모분자문제가아닌두증감량의차이"
    }
  ],
  "competitors": [
    {
      "code": 43,
      "refutation": "정량적통제자료가없으므로실제공급변화를인과적으로추정하는계산아님"
    },
    {
      "code": 10,
      "refutation": "전시위험을포함한전체논지의유일필요조건을평시감소량부등식으로강제하지않음"
    },
    {
      "code": 49,
      "refutation": "방향만아니라두반대방향변화의상대크기가②에명시됨"
    }
  ],
  "counterfactual_probe": "②감소량이더적을을더클로고치면단순합산상공급감소와부합.그역부등식이역사적으로실제성립했다는수치는본문에없음.",
  "boundary_status": "86/92상대량과차이계산중첩.③주로와④토지수요기제는정량검증자료없다는한계보존",
  "confidence": 0.94,
  "passage_group": "G273",
  "sdss_disclosed": false
}
```
