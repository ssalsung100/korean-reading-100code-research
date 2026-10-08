

<!-- luna-raw:APA-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G271",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "후속치료고려조건은치료효과우열비교근거가아님.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false,
  "source_quality": "APB노드명은blind문자도식,화살표는blindPNG로확인.정답원본새열람없이봉인정본답연결사용."
}
```


<!-- luna-raw:APA-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 39,
      "reason": "두치료효과의우열비교는제시되지않았음을확인"
    }
  ],
  "auxiliary": [
    {
      "code": 12,
      "reason": "보존치료뒤불완화이면수술고려라는조건의정확한결론유지"
    },
    {
      "code": 3,
      "reason": "치료선후와효과순위분리"
    },
    {
      "code": 2,
      "reason": "고려할수있음을더효과적이라는단정으로강화하지않음"
    }
  ],
  "surface": [
    {
      "code": 8,
      "reason": "선택순서는효과의우선순위와동치아님"
    }
  ],
  "competitors": [
    {
      "code": 86,
      "refutation": "효과크기비교라는측면에서39와중첩가능하나수치적비교자료가없음"
    },
    {
      "code": 19,
      "refutation": "보존치료불충분을수술로보완할수있어도일반효과우월이따라오지않음"
    },
    {
      "code": 44,
      "refutation": "통증완화라는공통목적이수단간우열을정해주지않음"
    }
  ],
  "counterfactual_probe": "수술을고려하는이유에는환자상태·위험·대체수단부재도가능하므로후순위만으로효과우열은확정못함.이는논리적대안이며새의학사실주장아님.",
  "boundary_status": "39/86비교요청과3/12절차조건구분.유일주미확정",
  "confidence": 0.95,
  "passage_group": "G271",
  "sdss_disclosed": false
}
```
