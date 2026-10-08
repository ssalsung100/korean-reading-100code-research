

<!-- luna-raw:AMN-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "official_answer": 1,
  "blind_answer": 1,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "logic_without_codes": "단어의 위치를 찾는 작업과 그 의미를 밝히는 작업이 별도로 제시되므로 위치 지식만으로 의미 해독을 보장할 수 없다.",
  "correction": "없음",
  "passage_group": "G247",
  "quota_status": "unavailable",
  "all_group_blind_records_before_any_group_answer_check": true,
  "original_blind_preserved": true
}
```


<!-- luna-raw:AMN-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    62
  ],
  "primary_candidates": [
    62,
    12
  ],
  "working_primary": 62,
  "unique_primary_confirmed": false,
  "auxiliary": [
    16
  ],
  "surface": [
    90,
    31
  ],
  "judgment_reason": "위치식별이라는성과에서의미해독을보장하는①의충분성을기각한다.위치와의미는별도연구성과.",
  "competing_codes": [
    {
      "code": 12,
      "verdict": "공동 후보",
      "reason": "위치를알면의미를안다는조건방향의근거없음을판정."
    },
    {
      "code": 16,
      "verdict": "보조",
      "reason": "단어의위치와의미라는다른개념을유지."
    },
    {
      "code": 90,
      "verdict": "⑤오답검사",
      "reason": "4×4=16의경우의수는⑤를확인하나①직접오류와별개."
    },
    {
      "code": 31,
      "verdict": "⑤오답검사",
      "reason": "64단어와16유의어군의계수단위를구별."
    }
  ],
  "minimal_change_test": "①을 위치를 알더라도 의미 해독은 별도 작업이 필요할 수 있다로 고치면 불필요한 보장이 사라진다.",
  "confidence": 0.97,
  "passage_group": "G247",
  "quota_status": "unavailable",
  "sdss_seen": false,
  "all_group_answer_check_complete": true
}
```
