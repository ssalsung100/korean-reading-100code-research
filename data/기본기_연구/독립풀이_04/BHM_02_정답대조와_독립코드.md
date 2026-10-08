

<!-- luna-raw:BHM-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G430",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2012/2012_answer_2012_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "기초분해 고정과 다른 조직 효과 제외 조건하에 성별·부위별 저장/분해 방향을 투여 예측에 대응한다.ㄱㄴ증가,ㄷㄹ감소.정성 예측 이상의 인과 확정은 유보.",
  "limitations": [
    "봉인 공식 전사 답 대조,원정답표 시각 재대조 미실시.unknown strict 제외 및 최초 유보 유지."
  ]
}
```


<!-- luna-raw:BHM-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G430",
  "sdss_seen": false,
  "general_task": "호르몬 투여 조건의 부위별 지방량 변화 예측",
  "decisive_relation": "성별/부위/호르몬 조합에 따라 저장 및 분해 증감 방향을 결합",
  "primary": {
    "code": 49,
    "scope": "ㄱ~ㄹ",
    "reason": "축적 증가 여부는 저장 증가·분해 감소 또는 그 반대 방향을 해당 조직에 맞춰 결합해야 판단된다."
  },
  "auxiliary": [
    {
      "code": 45,
      "reason": "동일 호르몬이라도 부위 입력에 따라 예측 출력이 달라진다."
    },
    {
      "code": 43,
      "scope": "보기단서",
      "reason": "기초 분해량은 고정하고 다른 조직을 매개한 효과는 제외한다."
    },
    {
      "code": 98,
      "reason": "대퇴부와 내장,여성형과 남성형 특성을 서로 교환하지 않는다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "나이 수치가 있지만 지방량의 정확한 증가량을 계산할 수 없다."
    }
  ],
  "competing_codes": [
    {
      "code": 46,
      "verdict": "모형 설명 보조",
      "refutation": "성장호르몬 경로는 명시되어 있으나 성호르몬 기전은 미확정이다.성별 관측에서 투여 효과를 현실 인과확정으로 올리지 않는다."
    },
    {
      "code": 53,
      "verdict": "보조 후보",
      "refutation": "차이를 설명하는 호르몬 가설이 배경이지만 성별 차이를 만드는 다른 모든 요인이 통제되었다는 자료는 없다."
    },
    {
      "code": 54,
      "verdict": "주 기각",
      "refutation": "보기의 한정된 정성 예측이 모든 개인·용량에서 충분히 결정된 결과라는 명제는 아니다."
    },
    {
      "code": 86,
      "verdict": "보조",
      "refutation": "축적 대소를 묻지만 절대량 수치 비교보다 여러 경로의 증감 방향이 직접 연산이다."
    }
  ],
  "counterfactual": "기초 분해량 고정을 제거하면 세포 크기 변화에 따른 추가 분해 변화가 들어와 단순 저장/자극분해 방향만의 결론이 약해질 수 있다.명시 통제는 결과 해석 범위를 좁히지만 호르몬 인과의 완전한 식별을 보장하지 않는다.",
  "unresolved": "성호르몬 투여 반응의 크기·개인차·시점은 미제시.문항 내 예상과 현실 인과를 구분한다.",
  "confidence": 0.94
}
```
