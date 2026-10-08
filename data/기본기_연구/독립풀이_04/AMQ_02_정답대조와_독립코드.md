

<!-- luna-raw:AMQ-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "official_answer": 1,
  "blind_answer": 1,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "logic_without_codes": "이해 또는 산출 영역 자체의 장애가 아니라 들은 말소리 정보를 산출쪽으로 전달·변환하는 연결의 장애이다.",
  "correction": "없음",
  "passage_group": "G248",
  "quota_status": "unavailable",
  "all_group_blind_records_before_any_group_answer_check": true,
  "original_blind_preserved": true
}
```


<!-- luna-raw:AMQ-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    45
  ],
  "primary_candidates": [
    45,
    50,
    46
  ],
  "working_primary": 45,
  "unique_primary_confirmed": false,
  "auxiliary": [
    40
  ],
  "surface": [
    93
  ],
  "judgment_reason": "들은정보의이해와말산출을잇는통로가끊겨입력에서반복출력으로넘어가지못한다.",
  "competing_codes": [
    {
      "code": 50,
      "verdict": "공동 후보",
      "reason": "두단계연결경로단절로뒤단계전달실패."
    },
    {
      "code": 46,
      "verdict": "공동 후보",
      "reason": "궁형속단절→따라말하기불가의기제."
    },
    {
      "code": 93,
      "verdict": "표면",
      "reason": "언어라는소재지만발신의도나전달해석보다내적처리경로가핵심."
    }
  ],
  "minimal_change_test": "통로단절을산출영역자체손상으로바꾸면④유형의산출장애가관련되며원래전도성기제와달라짐.",
  "confidence": 0.97,
  "passage_group": "G248",
  "quota_status": "unavailable",
  "sdss_seen": false,
  "all_group_answer_check_complete": true
}
```
