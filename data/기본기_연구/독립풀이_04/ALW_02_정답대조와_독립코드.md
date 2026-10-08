

<!-- luna-raw:ALW-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "official_answer": 5,
  "blind_answer": 5,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "logic_without_codes": "능력을 알아보고 현명한 인재를 쓰는 교훈이 군주를 위한 일반화.",
  "correction": "없음",
  "passage_group": "G241",
  "quota_status": "unavailable",
  "all_group_blind_records_before_any_group_answer_check": true,
  "original_blind_preserved": true
}
```


<!-- luna-raw:ALW-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    79
  ],
  "primary_candidates": [
    79,
    64
  ],
  "working_primary": 79,
  "unique_primary_confirmed": false,
  "auxiliary": [
    77,
    78
  ],
  "surface": [
    46
  ],
  "judgment_reason": "두 성공 사례의 인재 인정·등용을 군주가 따라야 할 교훈으로 확장한다.여러 유교적 교훈 중 글의 중심 기준을 보존하는⑤를 고름.",
  "competing_codes": [
    {
      "code": 64,
      "verdict": "공동 후보",
      "reason": "인화·충언·향수 등 주변 주제가 아니라 인재 등용이라는 논점에 맞는지 판정."
    },
    {
      "code": 77,
      "verdict": "보조",
      "reason": "두 사례에서 군주의 일반 교훈을 구성하지만 모든 인과 법칙의 경험적 검증은 아님."
    },
    {
      "code": 78,
      "verdict": "보조",
      "reason": "사적 원분을 넘는 행위의 이유가 교훈 내용을 지탱."
    }
  ],
  "minimal_change_test": "⑤의 현명한 이를 씀을 백성의 생활 돌봄으로 바꾸면 일반적으로 훌륭해도 본문 사례와 직접 연결되지 않는다.",
  "confidence": 0.96,
  "passage_group": "G241",
  "quota_status": "unavailable",
  "sdss_seen": false,
  "all_group_answer_check_complete": true
}
```
