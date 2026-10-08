

<!-- luna-raw:AIY-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G218",
  "blind_answer": 2,
  "official_answer": 2,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "호랑이가먼저호생원이라밝히고그뒤자라가자라새끼라고한다.②은정체공개순서를역전.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2026__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,원답셀직접검증아님",
  "barrier_verified": "G218전체blind4후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIY-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G218",
  "primary": [
    3
  ],
  "auxiliary": [
    17,
    96
  ],
  "surface": [
    80
  ],
  "judgment_reason": "호랑이신분공개후자라신분공개라는순서를②이뒤집음.행위주체는각각맞지만먼저라는순서가핵심.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "보조",
      "reason": "각정체공개주체를맞춘후두사건순서검사"
    },
    {
      "code": 96,
      "verdict": "보조",
      "reason": "먼저의의미를적용하나국소시간구조가더구체적"
    },
    {
      "code": 80,
      "verdict": "특정선지",
      "reason": "④얼주검이라고여김은객관상태와자라판단구별"
    }
  ],
  "minimal_change_test": "②먼저를뒤에로바꾸면내용귀속변경없이오류해소.",
  "sdss_seen": false,
  "confidence": 0.96,
  "quota_status": "unavailable"
}
```
