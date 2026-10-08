

<!-- luna-raw:AIS-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G215",
  "blind_answer": 3,
  "official_answer": 3,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "그말이옳을까는방금세운가정적결론의부당함을지적한다.③은가정이맞다고강조하는질문으로기능을뒤집었다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2024__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,공식PDF정답셀직접검증아님.AIR범위crop은직접검증완료",
  "barrier_verified": "AIR해소후G215blind6저장후answer만공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIS-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G215",
  "primary": [],
  "primary_candidates": [
    97,
    96
  ],
  "working_representative": 97,
  "auxiliary": [
    76,
    39
  ],
  "surface": [
    2
  ],
  "judgment_reason": "그말이옳을까는부당한가정결론에대한의문을통해그것을기각하는말.긍정확정이아님. 발화기능97과문맥판독96중첩.",
  "competing_codes": [
    {
      "code": 76,
      "verdict": "보조",
      "reason": "가정후받아들이기어려운결론을보여돌아오는반증적전개가질문기능을뒷받침하나형식논리모순증명으로과장안함"
    },
    {
      "code": 96,
      "verdict": "후보",
      "reason": "옳을까의수사적부정기능을뒤문장과함께판독"
    },
    {
      "code": 39,
      "verdict": "보조",
      "reason": "ⓐⓑ의설정·근거질문과ⓒ의반박기능구별"
    },
    {
      "code": 2,
      "verdict": "주 기각",
      "reason": "물음이가능성을나타낸다고양상판정으로환원하면긍정/반박기능을놓침"
    }
  ],
  "minimal_change_test": "그말이옳다라고확정하고뒤문장도그가정을지지하면③이성립가능.원문은잊으면안될것의망각을문제삼아반대.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
