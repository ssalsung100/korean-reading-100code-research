

<!-- luna-raw:AJJ-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G220",
  "blind_answer": 1,
  "official_answer": 1,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "교통접속전망으로독가촌이외부관심을받는다는①이부합한다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2026__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,원답셀직접검증아님.AJH범위crop직접확인",
  "barrier_verified": "G220전체blind4후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJJ-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G220",
  "primary": [],
  "primary_candidates": [
    46,
    17
  ],
  "working_representative": 46,
  "auxiliary": [
    3,
    2,
    44
  ],
  "surface": [
    88
  ],
  "judgment_reason": "교통연결전망·관광조건이외부관심을일으킨관계와그귀속을확인.①직접경로와②의시제·⑤의목적오류는구별.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "후보",
      "reason": "외부관심의조건을교통접속예정에맞춤"
    },
    {
      "code": 3,
      "verdict": "특정오답 보조",
      "reason": "불하시기득권예정을매입전이미부여로역전"
    },
    {
      "code": 2,
      "verdict": "특정오답 보조",
      "reason": "②예정과실현상태교환"
    },
    {
      "code": 44,
      "verdict": "특정오답 보조",
      "reason": "⑤정착목적을관광지조성목적으로바꿈"
    }
  ],
  "minimal_change_test": "교통·관광조건에의한각광이라는문장을없애면①근거상실.개척자들의고생만으로관광개발목적추론못함.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
