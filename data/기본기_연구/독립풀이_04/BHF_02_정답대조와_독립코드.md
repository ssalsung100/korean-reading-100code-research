

<!-- luna-raw:BHF-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G428",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2012/2012_answer_2012_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "이념 위치에 기초한 효용 계산이라는 공통점을 인정하되 거리의 계산 방식과 후기 보완 및 실증 근거를 혼동하지 않는다.",
  "limitations": [
    "봉인된 공식 정답 전사와 대조. 원정답표 시각 재대조 미실시. past_exposure unknown 및 strict 제외 유지."
  ]
}
```


<!-- luna-raw:BHF-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G428",
  "sdss_seen": false,
  "general_task": "다수 이론의 공통 설명 방식과 보완 내용 대조",
  "decisive_relation": "이념 체계/선택의 일관성,심리 요인 수용/이념 기반 실증을 정확한 대상에 귀속",
  "primary": {
    "code": 75,
    "reason": "초기 사회심리학 및 초기·후기 공간 이론의 주장을 구분하고 같은 효용 접근을 확인한다.74/75 통합 연구군의 견해 귀속 하위형.",
    "scope": "문항 전체"
  },
  "auxiliary": [
    {
      "code": 98,
      "scope": "①⑤",
      "reason": "비일관성의 대상은 이념 체계이고 입증 근거는 이념에 따른 선택이다."
    },
    {
      "code": 23,
      "scope": "②",
      "reason": "계산 방식은 다르지만 이념 기반 효용이라는 공통점을 확인한다."
    },
    {
      "code": 19,
      "scope": "③④",
      "reason": "심리 요인 추가에 의한 보완이 이론 간 차이 소멸과 같지 않다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "본문 수식은 배경. 이 문항은 수치를 대입하지 않고 이론 설명을 판별한다."
    }
  ],
  "competing_codes": [
    {
      "code": 74,
      "verdict": "통합 연구군 유지",
      "refutation": "예측 비교 문항이 아니라는 행동 차이는 기록하되75와 전역 배타 경계로 만들지 않는다."
    },
    {
      "code": 63,
      "verdict": "주 기각",
      "refutation": "새 관측으로 이론 신뢰도를 평가하지 않는다.본문의 비판·실증 내용을 재진술한다."
    },
    {
      "code": 39,
      "verdict": "국소 중첩",
      "refutation": "공통·차이 비교는 유효하나 어느 이론과 어떤 단계에 귀속되는지를 함께 보존해야 한다."
    }
  ],
  "counterfactual": "②를 유권자-정당 직접 거리가 가까울수록 두 이론 모두 효용이 높다고 바꾸면 방향 이론에서 반증된다.현재 정답의 포괄적 거리 기술과 구분한다.",
  "unresolved": "②거리라는 표현의 포괄 범위는 양 계산식 차이를 삭제할 근거가 아니다.",
  "confidence": 0.94
}
```
