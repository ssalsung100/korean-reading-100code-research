

<!-- luna-raw:BHL-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G430",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2012/2012_answer_2012_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "흡수용 외부 리파아제와 저장 지방 분해용 내부 효소를 구분한다.흡수 증가를 분비 억제와 동일시하지 않는다.",
  "limitations": [
    "봉인 공식 전사 답 대조,원정답표 시각 재대조 미실시.unknown strict 제외 및 최초 유보 유지."
  ]
}
```


<!-- luna-raw:BHL-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G430",
  "sdss_seen": false,
  "general_task": "동명 효소의 위치별 기능과 연쇄 효과 구분",
  "decisive_relation": "흡수 촉진을 분비 감소로 바꾸지 않고 외부/내부 효소의 작용 대상을 보존",
  "primary": {
    "code": 98,
    "scope": "②및①",
    "reason": "지방세포가 분비한 효소와 세포 내부 호르몬-민감 효소에 서로 다른 작용을 귀속해야 한다."
  },
  "auxiliary": [
    {
      "code": 42,
      "scope": "세포 경계",
      "reason": "분비 주체가 지방세포여도 작용 장소는 모세혈관 막일 수 있다."
    },
    {
      "code": 45,
      "scope": "②⑤",
      "reason": "혈액 중성지방→흡수 원료→에스테르화와 저장 지방→분비 경로를 분리한다."
    },
    {
      "code": 50,
      "scope": "③",
      "reason": "췌장 효소 억제는 흡수 전 분해 경로를 제한한다."
    },
    {
      "code": 49,
      "scope": "①④⑤",
      "reason": "각 경로 활성 증감의 방향을 전파한다."
    }
  ],
  "surface": [
    {
      "code": 40,
      "reason": "여러 효소가 신체 과정의 구성요소라는 사실만으로 기능 교환을 설명할 수 없다."
    }
  ],
  "competing_codes": [
    {
      "code": 17,
      "verdict": "98과 국소 중첩",
      "refutation": "효소의 종류와 담당 과정 범주를 복원하면 잘못된 귀속도 함께 고쳐진다.이 사례만으로 전역 통합·분할하지 않는다."
    },
    {
      "code": 52,
      "verdict": "국소 후보이나주기각",
      "refutation": "억제 효과가 등장해도②는 억제의 억제라는 이중 경로가 아니라 흡수 촉진을 분비 억제로 잘못 바꾼 선지다."
    },
    {
      "code": 85,
      "verdict": "기각",
      "refutation": "흡수량이 늘면 분비량은 줄어야 한다는 고정총량 관계는 본문에 없다."
    }
  ],
  "falsification_attempt": "흡수가 증가하는 동시에 내부 저장 지방 분해도 증가하는 상황은 논리적으로 가능하다.따라서 흡수 촉진만으로 분비 억제를 도출할 수 없다.실제 생리 수치가 제시되었다는 주장은 아니다.",
  "confidence": 0.97
}
```
