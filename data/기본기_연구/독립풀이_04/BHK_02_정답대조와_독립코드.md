

<!-- luna-raw:BHK-answer_check-20261003-01 -->
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
  "logic_without_codes_fixed": "카테콜아민의 중성지방 분해 촉진을 에스테르화 결합으로 바꿀 수 없다.⑤는 동방향 관계까지이고 엄밀 비례식은 미제시.",
  "limitations": [
    "봉인 공식 전사 답 대조,원정답표 시각 재대조 미실시.unknown strict 제외 및 최초 유보 유지."
  ]
}
```


<!-- luna-raw:BHK-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G430",
  "sdss_seen": false,
  "general_task": "분해·결합 과정의 방향 및 담당물질 대조",
  "decisive_relation": "카테콜아민의 작용을 분해 방향에 유지",
  "primary": {
    "code": 45,
    "scope": "①",
    "reason": "중성지방→지방산·글리세롤이라는 입력·출력 방향을 역방향 결합으로 바꾼 오류."
  },
  "auxiliary": [
    {
      "code": 98,
      "scope": "①",
      "reason": "카테콜아민에 귀속시킨 작용이 무엇인지 유지."
    },
    {
      "code": 49,
      "scope": "⑤",
      "reason": "세포 크기와 기초 분해 속도의 같은 증가 방향."
    },
    {
      "code": 10,
      "scope": "②④",
      "reason": "에너지원 이용 및 흡수 전 분해 요건."
    }
  ],
  "surface": [
    {
      "code": 91,
      "scope": "⑤",
      "reason": "비례라는 표현이 있지만 비례상수 일정이나 선형식은 미제시.정성 관계 이상 확정 금지."
    }
  ],
  "competing_codes": [
    {
      "code": 46,
      "verdict": "보조 및 국소 중첩",
      "refutation": "카테콜아민→효소 활성→분해 경로로도 기술 가능하나 정답 오류는 마지막 변환 방향이다.45와 배타 분리하지 않는다."
    },
    {
      "code": 17,
      "verdict": "보조",
      "refutation": "결합/분해의 과정 범주 구분은 유효하나 입력과 출력 복원과 독립 행동으로 중복 계수하지 않는다."
    },
    {
      "code": 54,
      "verdict": "주 기각",
      "refutation": "특정 생리 결과를 카테콜아민 하나로 충분히 결정한다는 강한 명제를 요구하지 않는다."
    }
  ],
  "counterfactual": "①에스테르화 반응을 저장 중성지방 분해로 바꾸면 본문과 일치한다.카테콜아민이라는 주체만 지우면 어느 작용인지 결정할 수 없으므로 변환 방향과 작용 귀속을 함께 확인한다.",
  "unresolved": [
    "③지방세포 축적 표현을 지방량/세포수 동일성으로 일반화하지 않음.",
    "⑤동방향을 선형 비례로 강화하지 않음."
  ],
  "confidence": 0.96
}
```
