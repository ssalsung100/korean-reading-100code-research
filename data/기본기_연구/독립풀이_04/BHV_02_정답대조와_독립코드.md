

<!-- luna-raw:BHV-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G433",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2012/2012_answer_2012_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "수준·시간·평가 등은 동일하게 유지하고 더 유능한 동료의 협력 유무를 달리해 학습 효과를 비교한다.",
  "limitations": [
    "봉인 공식 전사 답 대조. 원정답표 시각 재대조 미실시. unknown strict 제외 유지."
  ]
}
```


<!-- luna-raw:BHV-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G433",
  "sdss_seen": false,
  "general_task": "이론의 교수적 도움 효과를 검증하는 비교실험 수정",
  "decisive_relation": "초기능력·시간·평가 조건은 통제하고 이론에 해당하는 유능한 동료 도움 유무를 변별",
  "primary": {
    "code": 43,
    "scope": "①③④⑤",
    "reason": "학습결과 차이를 목표한 교수적 도움의 효과와 연결할 수 있도록 다른 조건의 차이를 제거한다."
  },
  "auxiliary": [
    {
      "code": 53,
      "scope": "③",
      "reason": "모두 협동하는 기존 설계는 검증할 원인의 차이가 없으므로 처리조건 차이를 만들어야 한다."
    },
    {
      "code": 10,
      "scope": "③",
      "reason": "도움 제공자가 더 유능하다는 이론적 요건이 충족되어야 하며 단순히 인원이 늘기만 해서는 부족하다."
    },
    {
      "code": 15,
      "scope": "②",
      "reason": "고난도라는 외형이 아니라 혼자/도움받아 수행 가능한 범위라는 근접발달 기준을 보존."
    }
  ],
  "surface": [
    {
      "code": 63,
      "reason": "이론 지지 가설이라는 발문이지만 결과가 아직 없어 실제 강화 정도를 평가하지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 46,
      "verdict": "전체 목적",
      "refutation": "인과효과를 알아보는 목적이지만 효과 방향을 이미 계산하는 단계가 아니라 식별 가능한 설계인지 검토한다."
    },
    {
      "code": 59,
      "verdict": "전체 과제",
      "refutation": "설계의 잘못을 고치는 해결 구조이나 어떤 수정이 유효한지 결정하는 연산은 통제와처리차이다."
    },
    {
      "code": 74,
      "verdict": "주 기각",
      "refutation": "두 경쟁 가설의 상반 예측 비교가 아니라 한 가설의 처리/비교집단 설계다."
    }
  ],
  "counterfactual": "초기 능력 차이를 허용하면 A성적 상승이 도움 효과인지 선행능력 차이인지 구분하기 어렵다.반대로 모든 조건을 완전히 같게만 두면 도움 유무의 효과를 비교할 차이도 사라진다.",
  "unresolved": "상위 동료 도움과 협동방식이 함께 변하므로 유능성의 순수효과와 협동의 순수효과를 각각 분해하는 설계는 아니다.본문의 결합처리 효과 검증으로 한정한다.",
  "confidence": 0.98
}
```
