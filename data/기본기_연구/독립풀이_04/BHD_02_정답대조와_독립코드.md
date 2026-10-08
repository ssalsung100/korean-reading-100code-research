

<!-- luna-raw:BHD-answer_check-20261002-r5-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G427",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2012/2012_answer_2012_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "㉡/㉢은 위헌심사 필요성은 공유하지만 판단 성격·담당 주체에서 다르다.",
  "limitations": [
    "봉인 공식 전사 답 대조이며 원정답표 시각 재대조 미실시. strict blind 제외 유지."
  ]
}
```


<!-- luna-raw:BHD-independent_code-20261002-r5-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G427",
  "sdss_seen": false,
  "general_task": "복수 입장의 비교 축별 귀속",
  "decisive_relation": "심사 필요성이라는 공통점과 판단 성격이라는 차이의 분리",
  "primary": {
    "code": 75,
    "scope": "①~⑤ 전체",
    "reason": "누가 심사 필요성·기관·성격·가치를 어떻게 주장했는지를 보존해야 한다."
  },
  "auxiliary": [
    {
      "code": 39,
      "reason": "공통점과 차이점을 심사 필요/방식의 동일 축에서 비교."
    },
    {
      "code": 98,
      "reason": "법리성·정치성 판단을 각각㉡/㉢에 정확히 귀속."
    },
    {
      "code": 23,
      "scope": "④",
      "reason": "양측 모두 위헌 통제를 요구한다는 공통 전제."
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "법 제도의 규범적 주제 자체는 결정 연산을 설명하지 못한다."
    }
  ],
  "competing_codes": [
    {
      "code": 74,
      "verdict": "실질 연구군 통합 유지",
      "refutation": "경험 예측이 없다는 이유만으로75와 본질 경계를 강제하지 않는다. 기존74/75 통합가설의 견해 귀속 하위형으로 기록."
    },
    {
      "code": 63,
      "verdict": "주 기각",
      "refutation": "새 증거가 특정 주장을 얼마나 약화하는지 평가하지 않고 기존 주장끼리 비교한다."
    },
    {
      "code": 17,
      "verdict": "국소 보조",
      "refutation": "④의 심사 자체와 담당 기관 구분에는 유효하나 전체 입장 귀속을 대체하지 않는다."
    }
  ],
  "counterfactual": "㉢이 모든 위헌심사를 불필요하다고 주장했다면④의 차이는 성립한다. 실제 원문은 위헌 통제를 요구하여 이를 차단한다.",
  "confidence": 0.98
}
```
