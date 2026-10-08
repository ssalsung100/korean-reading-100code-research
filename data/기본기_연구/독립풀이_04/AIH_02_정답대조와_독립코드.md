

<!-- luna-raw:AIH-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G213",
  "blind_answer": 5,
  "official_answer": 5,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "사건을겪는중심인물나가자신의판단과감정을직접서술하므로⑤.",
  "official_answer_source": "자료/평가원_정답표/원본/모의평가/2023_9월_국어_1교시_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,공식PDF정답셀직접검증아님",
  "barrier_verified": "G213blind4저장후answer만공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIH-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G213",
  "primary": [],
  "primary_candidates": [
    80,
    17
  ],
  "working_representative": 80,
  "auxiliary": [
    96
  ],
  "surface": [
    3,
    39
  ],
  "judgment_reason": "경험하고생각하는나와서술하는나가같음을확인하여내적반응을본인목소리로제시한다는⑤을수용. 인식주체80과서술주체귀속17이겹침.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "후보",
      "reason": "누가경험·판단·서술하는지를같은인물에귀속"
    },
    {
      "code": 3,
      "verdict": "특정오답",
      "reason": "시간역전서술이라는①은근거없음"
    },
    {
      "code": 39,
      "verdict": "주 기각",
      "reason": "다른시점서술자와실제로대조하는구성이아님"
    },
    {
      "code": 97,
      "verdict": "주 기각",
      "reason": "직접서술의목소리를확인하는것이지독자에게한특정발화의의도를추론하는것아님"
    }
  ],
  "minimal_change_test": "내면반응을관찰자인다른인물이추측해전달하도록바꾸면⑤이깨짐.1인칭표현과내적접근근거를함께확인.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
