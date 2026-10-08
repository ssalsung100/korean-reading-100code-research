

<!-- luna-raw:BFW-answer_check-20261002-r3-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G415",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "answer_verification": "봉인 official_answer 전사필드 대조. 원정답표 독립 시각 대조 미실시.",
  "official_answer_source": "자료/LEET_언어이해/원본/2010/2010_answer_2010_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "같다고 모두 묶는 것이 아니라 공통이면서 파생이어야 한다.ㄱ의 공유 원시는 제외,ㄴ 자가파생·ㄷ 공유파생·ㄹ 최소 사건수 원칙은 맞다.",
  "unresolved": null,
  "sdss_disclosed": false
}
```


<!-- luna-raw:BFW-independent_code-20261002-r3-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G415",
  "general_task": "분기론의 형질 분류·묶음 규칙 적용",
  "decisive_relation": "공통성 AND 파생성의 두 조건을 동시에 요구",
  "primary": [
    15
  ],
  "auxiliary": [
    23,
    16
  ],
  "surface": [
    1,
    25
  ],
  "code_rationale": {
    "15": "어떤 형질이 묶음의 기준에 포함되는지 판단",
    "23": "공통이더라도 원시면 안 되고 파생이더라도 하나면 묶음에 못 씀",
    "16": "자가/공유 파생형질 정의 적용"
  },
  "competing_codes": [
    {
      "code": 23,
      "rebuttal": "두 조건 결합은15의 구체 내부 구조로 중첩.별개 필수 행동으로 중복계수하지 않음."
    },
    {
      "code": 1,
      "rebuttal": "-와+ 유무 표상이지만 왜 공통-를 배제하는지는 파생성 기준이 설명."
    },
    {
      "code": 92,
      "rebuttal": "거리 산술은 수리분류학자의 방법으로 이번 발문에 적용하면 틀림."
    }
  ],
  "confidence": 0.95,
  "sdss_disclosed": false
}
```
