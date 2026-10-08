

<!-- luna-raw:AIR-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G215",
  "blind_answer": 3,
  "official_answer": 3,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "담은가지를머뭇세우는장애이면서넘는도전을가능하게하는조건이다.[B]는그대상을신명나는일과연결하므로③이적절.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2024__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,공식PDF정답셀직접검증아님.AIR범위crop은직접검증완료",
  "barrier_verified": "AIR해소후G215blind6저장후answer만공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIR-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G215",
  "primary": [],
  "primary_candidates": [
    44,
    19,
    10
  ],
  "working_representative": 44,
  "auxiliary": [
    39,
    40
  ],
  "surface": [
    13
  ],
  "judgment_reason": "넘기를막는담이도전의신명을가능하게하는조건이기도함. 목적실현에기여하는수단44·장애의새역할19·없으면꿈못꿈이라는필요조건10이국소중첩.",
  "competing_codes": [
    {
      "code": 19,
      "verdict": "후보",
      "reason": "한계가넘기라는새의미의조건으로작동.단순장애제거와는다름"
    },
    {
      "code": 10,
      "verdict": "후보",
      "reason": "담이없었으면담열기를꿈도못꾸었다는가정이기여의필수성을표현"
    },
    {
      "code": 40,
      "verdict": "특정오답 보조",
      "reason": "⑤수양의부분들협력과목련·감나무의별개사례열거를혼동"
    },
    {
      "code": 13,
      "verdict": "주 기각",
      "reason": "장애와도반역할은동일대상의서로다른관점으로양립가능.논리적배타관계아님"
    }
  ],
  "minimal_change_test": "담을완전히삭제하면방해가사라지지만담을넘는도전이라는목적자체도달라진다.문학적가정의의미를모든성취의일반필요조건으로확대하지않음.",
  "sdss_seen": false,
  "confidence": 0.93,
  "quota_status": "unavailable"
}
```
