

<!-- luna-raw:AJC-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G219",
  "blind_answer": 5,
  "official_answer": 5,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "(나)성숙한감의밝음과(다)소리의속성을가정적표현으로드러내므로⑤.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2026__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,원답셀직접검증아님",
  "barrier_verified": "G219전체blind5후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJC-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G219",
  "primary": [],
  "primary_candidates": [
    17,
    96
  ],
  "working_representative": 17,
  "auxiliary": [
    12,
    23
  ],
  "surface": [
    5,
    75
  ],
  "judgment_reason": "가정적표현이라는형식특징이(나)(다)에있는지언어형식과작품귀속을확인.조건내용을추론하는것과조건표현사용을기술하는것은층위다름.",
  "competing_codes": [
    {
      "code": 96,
      "verdict": "후보",
      "reason": "이라면·하면등가정표현의언어기능확인"
    },
    {
      "code": 12,
      "verdict": "보조",
      "reason": "실제조건문이근거지만전건에서후건을도출해야정답이되는과제아님"
    },
    {
      "code": 23,
      "verdict": "보조",
      "reason": "두작품각각근거를확인해야공통사용수용"
    },
    {
      "code": 5,
      "verdict": "특정오답",
      "reason": "④연쇄표현과태도변화는별개"
    }
  ],
  "minimal_change_test": "(나)의가정표현을단순현재확정으로바꾸면⑤공통형식근거가달라짐.내용의긍정성은같아도형식판정은변함.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
