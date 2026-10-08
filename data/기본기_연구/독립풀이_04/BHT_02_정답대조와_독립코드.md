

<!-- luna-raw:BHT-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G433",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2012/2012_answer_2012_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "인식 이전에 사회적으로 존재한 대상을 개인 내부의 선재 대상으로 옮긴 오류다.",
  "limitations": [
    "봉인 공식 전사 답 대조. 원정답표 시각 재대조 미실시. unknown strict 제외 유지."
  ]
}
```


<!-- luna-raw:BHT-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G433",
  "sdss_seen": false,
  "general_task": "사회적 대상과 개인 내면화의 위치·시점 구분",
  "decisive_relation": "대상의 선재 위치를 사회에서 개인 내부로 옮긴 오류",
  "primary": {
    "code": 42,
    "scope": "②",
    "reason": "개인 내부와 사회적 관계의 영역을 구분해야 한다."
  },
  "auxiliary": [
    {
      "code": 3,
      "scope": "②⑤",
      "reason": "사회적 존재와 상호작용이 먼저이고 개인 내부 습득이 이후임을 유지."
    },
    {
      "code": 80,
      "scope": "전체",
      "reason": "인식 대상과 개인의 표상·내면화 결과를 분리."
    },
    {
      "code": 2,
      "scope": "④",
      "reason": "잠재 수준의 미래 실제 수준 전환 가능성과 무조건 보장을 구분."
    }
  ],
  "surface": [
    {
      "code": 6,
      "scope": "②",
      "reason": "선재한다는 어휘만으로 선천성/후천성의 일반 이론을 확정하지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 98,
      "verdict": "국소 중첩",
      "refutation": "존재 장소를 무엇에 귀속하는지 복원하면42 오류도 함께 고쳐진다.독립 필수 연산으로 중복 계수하지 않는다."
    },
    {
      "code": 81,
      "verdict": "배경",
      "refutation": "사회적 선재를 말하지만 외부 대상 실재의 철학적 증명을 새로 요구하지 않는다."
    },
    {
      "code": 46,
      "verdict": "보조",
      "refutation": "인지 발달의 원인 경로가 배경이지만②의 결정 오류는 대상의 위치와 선후다."
    }
  ],
  "counterfactual": "②개인의 내면을 사회적 관계로 바꾸면 선재성 진술이 본문에 맞는다.학습 이전이라는 말만 지우면 잘못된 위치 귀속이 남는다.",
  "confidence": 0.98
}
```
