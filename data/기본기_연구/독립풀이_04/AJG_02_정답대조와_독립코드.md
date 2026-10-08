

<!-- luna-raw:AJG-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G219",
  "blind_answer": 2,
  "official_answer": 2,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "좋은소리는상반속성의균형이아니라여러요건을충족하고바름에맞는것이다.②은선별조건을대립특성조화로바꾼다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2026__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,원답셀직접검증아님",
  "barrier_verified": "G219전체blind5후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJG-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G219",
  "primary": [],
  "primary_candidates": [
    16,
    25,
    10
  ],
  "working_representative": 16,
  "auxiliary": [
    23,
    39
  ],
  "surface": [
    26
  ],
  "judgment_reason": "좋은소리의정의는여러요건충족과바름이지상반속성의균형이아님.정의16·선별분류25·바름요건10이같은오류검출.",
  "competing_codes": [
    {
      "code": 25,
      "verdict": "후보",
      "reason": "쓸모·아름다움·실상·바름으로좁히는구조를조화구조로바꿈"
    },
    {
      "code": 10,
      "verdict": "후보",
      "reason": "좋은소리에바름을요구하며삿됨과균형을허용하지않음"
    },
    {
      "code": 23,
      "verdict": "보조",
      "reason": "요건들이함께성립해야함"
    },
    {
      "code": 26,
      "verdict": "표면",
      "reason": "상반어가반복돼도그양극을통합균형시키는논리라는뜻아님"
    }
  ],
  "minimal_change_test": "②상반특성균형을여러요건을충족하고바름에합당함으로고치면정의복원.",
  "sdss_seen": false,
  "confidence": 0.96,
  "quota_status": "unavailable"
}
```
