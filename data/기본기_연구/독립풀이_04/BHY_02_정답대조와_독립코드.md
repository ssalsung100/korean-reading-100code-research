

<!-- luna-raw:BHY-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G434",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2012/2012_answer_2012_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "실온 부근 임계온도 조건과 자기장에 대한 큰 엔트로피 반응을 함께 고려하면C가 적합.단일점 자료를 전범위 선형식으로 확대하지 않는다.",
  "limitations": [
    "봉인 공식 전사 답 대조. 원정답표 시각 재대조 미실시. unknown strict 제외 및 최초 유보 유지."
  ]
}
```


<!-- luna-raw:BHY-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G434",
  "sdss_seen": false,
  "general_task": "목표온도와 자기장 반응 조건으로 작용물질 선정",
  "decisive_relation": "실온 부근 임계온도 적합성과 같은 또는 더 작은 장에서 큰 엔트로피 변화의 결합",
  "primary": {
    "code": 15,
    "scope": "A~E",
    "reason": "온도 적합성과 자기장 변화에 따른 엔트로피 반응이라는 두 기준을 함께 적용한다."
  },
  "auxiliary": [
    {
      "code": 86,
      "scope": "C/B,C/D",
      "reason": "같은1T의B보다C가 크고 C는D보다 작은 장에서도 약간 큰 엔트로피 변화."
    },
    {
      "code": 43,
      "scope": "B/C",
      "reason": "제시된 장세기1T가 같아 해당 조건의 반응량 비교가 가능.실험설계 자체를 고치는 문항은 아니다."
    },
    {
      "code": 88,
      "scope": "C/D",
      "reason": "비슷한 엔트로피 변화를 더 작은 외부장으로 얻는다는 정성 효율 비교."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "표가 수치를 주지만 복잡한 계산 없이 기준과 대소 비교로 선택 가능."
    }
  ],
  "competing_codes": [
    {
      "code": 84,
      "verdict": "국소 보조 후보",
      "refutation": "엔트로피변화/장세기의 비로 정규화할 수는 있지만 입력응답이 전범위 선형이라는 근거는 없다.비율값을 실제 열효율 공식으로 확정하지 않는다."
    },
    {
      "code": 91,
      "verdict": "주 기각",
      "refutation": "본문 자화의 비례성을 엔트로피변화와장세기의 엄밀비례로 옮길 수 없다."
    },
    {
      "code": 59,
      "verdict": "전체과제",
      "refutation": "좋은 냉장고 개발의 해결책이지만 표 선택을 결정하는 구체 연산은 두기준과수량비교다."
    }
  ],
  "counterfactual": "엔트로피감소량만 최대화하면A가 선택되어실온조건을 놓친다.온도 숫자만으로D를선택하면자기장조건을 놓친다.서로 다른 오답이 각 기준의 필요를 보여 준다.",
  "unresolved": "실온 정확값과 각 물질의 전체 응답곡선·장 생성 비용은 미제시.모든실온/장조건에서C가 지배한다고 주장하지 않는다.",
  "confidence": 0.95
}
```
