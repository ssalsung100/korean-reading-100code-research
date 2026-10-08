

<!-- luna-raw:AJD-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G219",
  "blind_answer": 1,
  "official_answer": 1,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "밤을지키는이는찾는연대의상대이다.①은그를피해야할감시자로바꾸어찾아다님을잠행회피로왜곡한다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2026__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,원답셀직접검증아님",
  "barrier_verified": "G219전체blind5후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJD-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G219",
  "primary": [],
  "primary_candidates": [
    17,
    80,
    64
  ],
  "working_representative": 17,
  "auxiliary": [
    100,
    39
  ],
  "surface": [
    46
  ],
  "judgment_reason": "연대의상대를감시자로바꾸어찾기를회피로재해석한①.인물역할귀속17·화자의태도80·근거밖감시추가64가같은변경검출.",
  "competing_codes": [
    {
      "code": 80,
      "verdict": "후보",
      "reason": "그리워찾는태도를피하는태도로뒤집음"
    },
    {
      "code": 64,
      "verdict": "후보",
      "reason": "눈을피해다닌다는감시상황근거없음"
    },
    {
      "code": 100,
      "verdict": "보조",
      "reason": "보기의밤=연대상실대응으로밤지키는이의역할복원"
    },
    {
      "code": 46,
      "verdict": "주 기각",
      "reason": "먼저대상역할과태도가달라짐.단순발생원인계산아님"
    }
  ],
  "minimal_change_test": "①눈을피해다니며를함께할이를찾아다니며로바꾸면상실과탐색의맥락회복.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
