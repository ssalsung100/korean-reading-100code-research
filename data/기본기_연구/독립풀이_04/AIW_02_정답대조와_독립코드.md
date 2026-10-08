

<!-- luna-raw:AIW-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G216",
  "blind_answer": 4,
  "official_answer": 4,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "할머니는고의로가뒀다는비난을파악하고잠근행위는인정하되사람이있음을몰랐다며고의성을부정한다.④비난을파악하지못했다는말이틀림.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2024__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,공식PDF정답셀직접검증아님.AIW범위crop직접확인",
  "barrier_verified": "AIW해소후G216전체blind2저장후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIW-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G216",
  "primary": [],
  "primary_candidates": [
    97,
    80,
    17
  ],
  "working_representative": 97,
  "auxiliary": [
    63,
    39
  ],
  "surface": [
    65
  ],
  "judgment_reason": "[B]는비난의고의성주장을알아듣고그부분을부정하는해명이다.발화기능97·상대의도인식80·인정/부정대상귀속17이같은판정에중첩.",
  "competing_codes": [
    {
      "code": 80,
      "verdict": "후보",
      "reason": "비난을인지했는지말의응답내용으로판단"
    },
    {
      "code": 17,
      "verdict": "후보",
      "reason": "인정한잠금행위와부정한고의동기를분리하여귀속"
    },
    {
      "code": 63,
      "verdict": "보조",
      "reason": "해명과재반박의논쟁구조가있으나진위증거의최종평가아니라발화기능을분석"
    },
    {
      "code": 65,
      "verdict": "표면",
      "reason": "상대가억울한추측을한다해도왜곡논증오류이름만으로④의이해여부판정은대체못함"
    }
  ],
  "minimal_change_test": "[B]가단순히문을잠갔다고만응답했다면고의비난을파악했다는근거가약해짐.모르고·알고야왜라는대응이동기비난인지의직접증거.",
  "sdss_seen": false,
  "confidence": 0.96,
  "quota_status": "unavailable"
}
```
