

<!-- luna-raw:BGK-answer_check-20261002-r3-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G420",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "answer_verification": "봉인 official_answer 전사필드 대조. 원정답표 독립 시각 대조 미실시.",
  "official_answer_source": "자료/LEET_언어이해/원본/2010/2010_answer_2010_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "주제와 표현양식은 다른 축이며, 개성 드러남과 저자 자신이 나로 등장함도 다르다.ㄱㄷ참,ㄴ거짓.",
  "unresolved": null,
  "sdss_disclosed": false
}
```


<!-- luna-raw:BGK-independent_code-20261002-r3-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G420",
  "general_task": "주제와 장르의 속성 비교",
  "decisive_relation": "주제/양식,개성/저자 직접등장이라는 다른 속성축 보존",
  "primary": [
    17
  ],
  "auxiliary": [
    39,
    14
  ],
  "surface": [
    25,
    26
  ],
  "code_rationale": {
    "17": "개성이 드러나는 것과 저자가 등장하는 것을 다른 대상으로 처리",
    "39": "세 장르의 직접등장 여부 비교",
    "14": "하나의 주제와 다른 장르 양식의 결합이 가능"
  },
  "competing_codes": [
    {
      "code": 25,
      "rebuttal": "세분류를 알고도 서로 다른 축을 혼동하면 틀린다.분류형식보다 속성 귀속이 결정적."
    },
    {
      "code": 26,
      "rebuttal": "세범주가 전체주제를 포섭해도 주제/양식 1대1 배타대응을 뜻하지 않는다."
    },
    {
      "code": 23,
      "rebuttal": "공통속성 검사로 표현할 수 있지만ㄴ은ⓐ의 직접등장 부정으로 판정 가능."
    }
  ],
  "confidence": 0.95,
  "sdss_disclosed": false
}
```
