

<!-- luna-raw:BGC-answer_check-20261002-r3-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G417",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "answer_verification": "봉인 official_answer 전사필드 대조. 원정답표 독립 시각 대조 미실시.",
  "official_answer_source": "자료/LEET_언어이해/원본/2010/2010_answer_2010_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "모델들은 위험 보도를 받아들여 위험과 대상에 대한 인식을 증폭시키는 경로다.②는 보도내용 자체를 믿지 않아 정정을 요구하므로 이 경로의 대상·방향이 다르다.",
  "unresolved": null,
  "sdss_disclosed": false
}
```


<!-- luna-raw:BGC-independent_code-20261002-r3-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G417",
  "general_task": "모델의 사례 설명 가능범위 평가",
  "decisive_relation": "불신 대상이 보도된 위험대상인지 보도내용 자체인지 구별",
  "primary": [
    17
  ],
  "auxiliary": [
    56,
    93
  ],
  "surface": [
    46,
    63
  ],
  "code_rationale": {
    "17": "보도대상 신뢰훼손을 보도 자체 불신으로 바꿈",
    "56": "제시 모델이 설명하는 결과 범위 평가",
    "93": "정보 전달 내용과 메시지 대상의 층위 구분"
  },
  "competing_codes": [
    {
      "code": 56,
      "rebuttal": "일반 과제명이나 설명 불가의 직접 이유는 대상 교체17."
    },
    {
      "code": 63,
      "rebuttal": "새증거가 이론을 반박하는지보다 어떤 반응이 설명경로에 들어가는지 묻는다."
    },
    {
      "code": 55,
      "rebuttal": "③의 실제 인과 정당성을 평가하는 것이 아니므로 의혹을 허위인과라 제외하면 오독."
    }
  ],
  "confidence": 0.96,
  "sdss_disclosed": false
}
```
