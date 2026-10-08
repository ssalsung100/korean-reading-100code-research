

<!-- luna-raw:AKW-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G233",
  "official_answer": 2,
  "blind_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2023/2023_answer_언어이해정답.pdf",
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "logic_without_codes": "도덕적 행동을 못 하는 범주 전체를 수동적 의식만 있는 범주로 축소하면, 감응력이 있는 영유아라는 포함 사례를 놓친다.",
  "correction": "답 수정 없음. AKW의 능동적 감응과 능동적 주의력을 어휘만으로 동일시하지 않는다. 도덕 피동자의 정의는 도덕적 행위 불능이며 수동 의식만이라는 추가 속성을 전부에 붙일 근거가 없다는 판단을 고정.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AKW-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    17
  ],
  "primary_candidates": [
    17,
    4
  ],
  "working_primary": 17,
  "unique_primary_confirmed": false,
  "auxiliary": [
    16
  ],
  "surface": [
    79
  ],
  "judgment_reason": "②는 도덕적 행위 불능으로 정한 피동자 전체를 감응력 마비자처럼 수동 의식만 있는 대상으로 대체한다. 피동자에는 감응력 있는 영유아도 속한다.",
  "competing_codes": [
    {
      "code": 4,
      "verdict": "공동 주 후보",
      "reason": "특정 수동 의식 사례의 성질을 피동자 일반에 확대했다는 범위 연산으로 같은 오류를 기술한다."
    },
    {
      "code": 16,
      "verdict": "보조",
      "reason": "피동자 정의의 이성·자의식/도덕 행위 불능을 감응력/주의력 결여와 구별해야 한다. 정의 설명 자체보다 잘못된 범주 일반화가②의 오류 위치다."
    },
    {
      "code": 1,
      "verdict": "주 기각",
      "reason": "능력의 유무 표현은 있으나 어떤 능력이 어떤 범주에 귀속되는지 고정하지 않으면 오류를 설명하지 못한다."
    },
    {
      "code": 79,
      "verdict": "표면",
      "reason": "도덕 소재지만②는 어떤 의무를 도출할지보다 대상의 속성 귀속을 묻는다."
    }
  ],
  "minimal_change_test": "②의 도덕 피동자를 감응력 마비자로 바꾸면5문단 서술과 맞는다. 능동적 주의력과 능동적 감응을 무조건 같은 개념으로 합치지 않는다.",
  "confidence": 0.94,
  "passage_group": "G233",
  "sdss_seen": false,
  "all_group_answer_check_complete": true,
  "quota_status": "unavailable"
}
```
