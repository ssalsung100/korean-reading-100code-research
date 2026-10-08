

<!-- luna-raw:AMF-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "official_answer": 3,
  "blind_answer": 3,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "logic_without_codes": "언어 능력을 보여주는 사례를 그 능력 자체가 생기는 원인으로 바꾸면 설명 방향이 틀린다.",
  "correction": "없음",
  "passage_group": "G245",
  "quota_status": "unavailable",
  "all_group_blind_records_before_any_group_answer_check": true,
  "original_blind_preserved": true
}
```


<!-- luna-raw:AMF-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    60
  ],
  "primary_candidates": [
    60,
    46,
    56
  ],
  "working_primary": 60,
  "unique_primary_confirmed": false,
  "auxiliary": [
    17
  ],
  "surface": [
    6
  ],
  "judgment_reason": "능력의 증거 사례인 크레올화를 그 능력의 원인으로 바꾼③의 논증 역할 오류.",
  "competing_codes": [
    {
      "code": 46,
      "verdict": "공동 후보",
      "reason": "일반 능력과 그 발현 현상의 인과 방향을 교체."
    },
    {
      "code": 56,
      "verdict": "공동 후보",
      "reason": "증거로 설명함과 발생 원인으로 설명함의 관계 차이."
    },
    {
      "code": 6,
      "verdict": "소재",
      "reason": "선천성 논의이지만③의 오류는 선천/후천 자체보다 예시의 역할 교체."
    }
  ],
  "minimal_change_test": "③의 있기 때문이다를 보여주는 예가 크레올화이다로 바꾸면 맞음.",
  "confidence": 0.97,
  "passage_group": "G245",
  "quota_status": "unavailable",
  "sdss_seen": false,
  "all_group_answer_check_complete": true
}
```
