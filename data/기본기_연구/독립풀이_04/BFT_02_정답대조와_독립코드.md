

<!-- luna-raw:BFT-answer_check-20261002-r3-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G414",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "answer_verification": "봉인 official_answer 전사필드 대조. 원정답표 독립 시각 대조 미실시.",
  "official_answer_source": "자료/LEET_언어이해/원본/2010/2010_answer_2010_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "국전의 충돌이 법전 완비를 어렵게 했다는 사실을 전율 체제 자체의 출현 지연 원인으로 옮긴②는 근거가 없다.",
  "unresolved": null,
  "sdss_disclosed": false
}
```


<!-- luna-raw:BFT-independent_code-20261002-r3-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G414",
  "general_task": "법제 형성에 대한 추론 평가",
  "decisive_relation": "법전 완비 지연과 두 법원 병존체제 출현 지연의 설명 대상 교체",
  "primary": [
    17
  ],
  "auxiliary": [
    3,
    46
  ],
  "surface": [
    59,
    79
  ],
  "code_rationale": {
    "17": "원인설명이 걸리는 결과가 완비에서 전율 출현으로 바뀜",
    "3": "국전끼리 충돌할 때에는 대명률과 국전이 이미 병존",
    "46": "국전 충돌이라는 원인의 효과 범위를 추적"
  },
  "competing_codes": [
    {
      "code": 46,
      "rebuttal": "인과연결이 있지만 오류는 원인 자체의 부재보다 결과대상 교체.17을 결정 관계로 우선."
    },
    {
      "code": 59,
      "rebuttal": "본문 편찬은 문제해결 구조이나 정답은 해결책 적합성보다 설명 대상 혼동."
    },
    {
      "code": 3,
      "rebuttal": "시간순서는 반증 근거이나 단순 선후 역전만으로 두 결과 개념 차이를 모두 설명하지 못함."
    }
  ],
  "confidence": 0.9,
  "sdss_disclosed": false
}
```
