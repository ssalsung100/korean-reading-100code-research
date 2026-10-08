

<!-- luna-raw:ALT-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "official_answer": 4,
  "blind_answer": 4,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "logic_without_codes": "유도 진화로 개체를 얻는 준비는 그 개체의 자율적 제작 활동과 다르다.",
  "correction": "없음",
  "passage_group": "G240",
  "quota_status": "unavailable",
  "all_group_blind_records_before_any_group_answer_check": true,
  "original_blind_preserved": true
}
```


<!-- luna-raw:ALT-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    16
  ],
  "primary_candidates": [
    16,
    17,
    3
  ],
  "working_primary": 16,
  "unique_primary_confirmed": false,
  "auxiliary": [
    45
  ],
  "surface": [
    100
  ],
  "judgment_reason": "생화학적 춤의 정의인 프로그램된미생물의자율적작동과그미생물준비과정을구별한다.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "공동 후보",
      "reason": "활동주체·과정의범위를준비와작동에정확히귀속."
    },
    {
      "code": 3,
      "verdict": "공동 후보",
      "reason": "작동이전준비단계와실제수행단계를구별하는동일행동."
    },
    {
      "code": 100,
      "verdict": "표면",
      "reason": "춤이라는비유명칭을평범한제조활동으로바꿔도④배제가능."
    }
  ],
  "minimal_change_test": "④를준비된미생물이설계된기능을수행하는과정으로고치면정의에맞음.유도진화의외부절차를새로추가하지않는다.",
  "confidence": 0.96,
  "passage_group": "G240",
  "quota_status": "unavailable",
  "sdss_seen": false,
  "all_group_answer_check_complete": true
}
```
