

<!-- luna-raw:BGO-answer_check-20261002-r3-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G422",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "answer_verification": "봉인 official_answer 전사필드 대조. 원정답표 독립 시각 대조 미실시.",
  "official_answer_source": "자료/LEET_언어이해/원본/2011/2011_answer_2011_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "음속 정도는 두 이론의 계산 차이가 무시할 만큼 작다는⑤가 본문과 일치한다.",
  "unresolved": null,
  "sdss_disclosed": false
}
```


<!-- luna-raw:BGO-independent_code-20261002-r3-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G422",
  "general_task": "두 이론의 유효범위 내용확인",
  "decisive_relation": "속도가 낮다는 조건에서 계산값의 근사적 일치를 적용",
  "primary": [
    12
  ],
  "auxiliary": [
    86,
    17
  ],
  "surface": [
    92,
    46
  ],
  "code_rationale": {
    "12": "저속조건이면두예측이실용적으로일치",
    "86": "거의차이없음의양적비교",
    "17": "수식자체의동일함과예측값근사를구별"
  },
  "competing_codes": [
    {
      "code": 92,
      "rebuttal": "실제속도공식을계산하지않고본문조건에적용."
    },
    {
      "code": 11,
      "rebuttal": "저속일때근사유효라는방향이지그때에만동일하다는필충은주어지지않음."
    },
    {
      "code": 46,
      "rebuttal": "상대론적효과의인과기제를복원하는문제가아님."
    }
  ],
  "confidence": 0.96,
  "sdss_disclosed": false
}
```
