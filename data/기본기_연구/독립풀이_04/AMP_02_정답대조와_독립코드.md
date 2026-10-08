

<!-- luna-raw:AMP-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "official_answer": 5,
  "blind_answer": 5,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "logic_without_codes": "같은 손상 위치에서 서로 다른 기능 장애가 생기면 위치와 기능의 일대일 대응은 부족하지만 기능적 단계의 구별은 유지될 수 있다.",
  "correction": "없음",
  "passage_group": "G248",
  "quota_status": "unavailable",
  "all_group_blind_records_before_any_group_answer_check": true,
  "original_blind_preserved": true
}
```


<!-- luna-raw:AMP-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    74
  ],
  "primary_candidates": [
    74,
    36,
    56
  ],
  "working_primary": 74,
  "unique_primary_confirmed": false,
  "auxiliary": [
    17,
    39
  ],
  "surface": [
    1
  ],
  "judgment_reason": "동일손상영역·상이한기능장애는위치일대일모형에서어렵고기능독립·비국재모형에서설명가능한차별사례.",
  "competing_codes": [
    {
      "code": 36,
      "verdict": "공동 후보",
      "reason": "기존국재화의설명기대에맞지않는사례를찾음."
    },
    {
      "code": 56,
      "verdict": "공동 후보",
      "reason": "어느모형으로어떤현상을설명할수있는가의적합성비교."
    },
    {
      "code": 1,
      "verdict": "표면",
      "reason": "장애정도의많고적음아니라위치-기능대응유형의차이."
    }
  ],
  "minimal_change_test": "⑤의손상영역동일을서로다름으로바꾸면기존모형에서도설명가능하여차별성상실.",
  "confidence": 0.97,
  "passage_group": "G248",
  "quota_status": "unavailable",
  "sdss_seen": false,
  "all_group_answer_check_complete": true
}
```
