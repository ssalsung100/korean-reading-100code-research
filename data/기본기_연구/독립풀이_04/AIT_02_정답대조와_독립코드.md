

<!-- luna-raw:AIT-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G215",
  "blind_answer": 2,
  "official_answer": 2,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "문은그자리에서버티며열리고가지는담을넘어영역을넓힌다.②의대조가본문행동을보존.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2024__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,공식PDF정답셀직접검증아님.AIR범위crop은직접검증완료",
  "barrier_verified": "AIR해소후G215blind6저장후answer만공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIT-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G215",
  "primary": [],
  "primary_candidates": [
    39,
    17
  ],
  "working_representative": 39,
  "auxiliary": [
    5,
    100
  ],
  "surface": [
    42
  ],
  "judgment_reason": "문은자리유지와개방,가지는담넘어영역확장의행동차이를비교. 행위귀속17과비교39중첩.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "후보",
      "reason": "머무는문·넘는가지의동작을바르게귀속"
    },
    {
      "code": 42,
      "verdict": "보조후보",
      "reason": "담안밖경계는가지확장의구체근거이나문과가지의전체비교를대신하지않음"
    },
    {
      "code": 5,
      "verdict": "보조",
      "reason": "문열림과가지이동의변화방식구별"
    },
    {
      "code": 80,
      "verdict": "특정오답 기각",
      "reason": "④⑤불안감추기·반성이라는공통내면근거없음"
    }
  ],
  "minimal_change_test": "문이자리를떠나이동했다는서술이추가되면②앞절판정이달라짐.문이열렸다는사실만으로자리유지가부정되지는않음.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
