

<!-- luna-raw:AMC-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "official_answer": 5,
  "blind_answer": 5,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "logic_without_codes": "이미 알려진 약의 효과를 높이는 연구와 더 짧고 적은 투여에서도 효과가 있는지 확인하는 연구는 목표가 다르다.",
  "correction": "없음",
  "passage_group": "G244",
  "quota_status": "unavailable",
  "all_group_blind_records_before_any_group_answer_check": true,
  "original_blind_preserved": true
}
```


<!-- luna-raw:AMC-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    44
  ],
  "primary_candidates": [
    44,
    17
  ],
  "working_primary": 44,
  "unique_primary_confirmed": false,
  "auxiliary": [
    75
  ],
  "surface": [
    49
  ],
  "judgment_reason": "연구의 목적을 약효향상이 아니라 단축투여에서의 효과 검증으로 고정한다.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "공동 후보",
      "reason": "개선대상이 약의 효능인지 투약기간·용량인지 구별."
    },
    {
      "code": 75,
      "verdict": "보조",
      "reason": "연구자 입장을비판편과구별."
    },
    {
      "code": 49,
      "verdict": "표면",
      "reason": "효과증감어휘가있어도변수공변계산이아니라목표내용교체."
    }
  ],
  "minimal_change_test": "⑤를 더 적은 투여로도 효과가 있는지 확인으로 수정하면 충돌 해소.",
  "confidence": 0.97,
  "passage_group": "G244",
  "quota_status": "unavailable",
  "sdss_seen": false,
  "all_group_answer_check_complete": true
}
```
