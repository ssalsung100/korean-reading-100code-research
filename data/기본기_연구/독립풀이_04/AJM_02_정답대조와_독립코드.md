

<!-- luna-raw:AJM-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G221",
  "blind_answer": 4,
  "official_answer": 4,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "태수는취향을전해듣고알아보도록준비했다.④의옛인연으로알아봤다는사실은없고너언제날알더냐가오히려뜻밖배려를말한다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2026__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,원답셀직접검증아님",
  "barrier_verified": "G221전체blind4후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJM-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G221",
  "primary": [],
  "primary_candidates": [
    64,
    17,
    46
  ],
  "working_representative": 64,
  "auxiliary": [
    97,
    80
  ],
  "surface": [
    3
  ],
  "judgment_reason": "취향을전해듣고준비한술을옛인연으로알아본결과라함.없는관계추가64·인식근거귀속17·원인교환46중첩.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "후보",
      "reason": "태수가알게된경로를전해들음에서옛교분으로교환"
    },
    {
      "code": 46,
      "verdict": "후보",
      "reason": "좋은술준비의원인을없는옛인연으로바꿈"
    },
    {
      "code": 97,
      "verdict": "보조",
      "reason": "너언제날알더냐는뜻밖배려의질문이지옛만남확인아님"
    },
    {
      "code": 3,
      "verdict": "표면",
      "reason": "옛이라는시간어가있어도선후보다사실관계자체의추가가문제"
    }
  ],
  "minimal_change_test": "옛인연이있었다를취향을전해들었다로바꾸면원문경로복원.좋은대접받았다는사실만으로과거교분추론불가.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
