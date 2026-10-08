

<!-- luna-raw:AJH-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G220",
  "blind_answer": 5,
  "official_answer": 5,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "허명두는협박이두렵지않다며직접맞서고온씨도같은경고를반복한다.⑤은에둘러말해관심전환성공으로바꾸어틀림.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2026__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,원답셀직접검증아님.AJH범위crop직접확인",
  "barrier_verified": "G220전체blind4후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJH-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G220",
  "primary": [],
  "primary_candidates": [
    97,
    17,
    64
  ],
  "working_representative": 97,
  "auxiliary": [
    80,
    39
  ],
  "surface": [
    61
  ],
  "judgment_reason": "직접맞서는말을에둘러관심전환에성공한발화로바꿈.기능97·행위귀속17·없는성과추가64중첩.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "후보",
      "reason": "해볼대로하라는말에관심회피행위귀속"
    },
    {
      "code": 64,
      "verdict": "후보",
      "reason": "관심이딴곳으로옮겨갔다는결과없음"
    },
    {
      "code": 61,
      "verdict": "표면",
      "reason": "주의전환실패/성공이실제제시된논점일탈전략아님"
    },
    {
      "code": 80,
      "verdict": "보조",
      "reason": "증오억누름과맞섬태도판독"
    }
  ],
  "minimal_change_test": "허명두가다른화제를꺼내고온씨가그것에집중했다는행동이추가돼야⑤성과를검토할수있음.현재는같은경고반복.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
