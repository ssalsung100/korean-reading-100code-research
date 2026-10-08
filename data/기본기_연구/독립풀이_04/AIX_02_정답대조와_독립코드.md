

<!-- luna-raw:AIX-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G217",
  "blind_answer": 2,
  "official_answer": 2,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "대풍·물결의힘이돛대와돛의형태변화로가시화됨.과거회상의존재와현재아쉬움의여부는별도.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2024__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,정답셀직접검증아님",
  "barrier_verified": "G217유일case blind후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIX-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G217",
  "primary": [],
  "primary_candidates": [
    46,
    5
  ],
  "working_representative": 46,
  "auxiliary": [
    100,
    39
  ],
  "surface": [
    3
  ],
  "judgment_reason": "외부풍랑의힘을돛대굽음·돛팽창이라는변화에서읽는다. 작용원인46과상태변화5가같은물리묘사를설명하므로후보보존.",
  "competing_codes": [
    {
      "code": 5,
      "verdict": "후보",
      "reason": "형태변화의구체양상을확인하여외부힘을추론"
    },
    {
      "code": 100,
      "verdict": "보조",
      "reason": "나뭇잎·반달비유가형태와움직임을생생히표현"
    },
    {
      "code": 39,
      "verdict": "특정오답 보조",
      "reason": "현재만족과과거위험대조를아쉬움으로읽은①기각"
    },
    {
      "code": 3,
      "verdict": "표면",
      "reason": "회상자체는존재하지만정답의환경힘판독을결정하는순서역전은없음"
    }
  ],
  "minimal_change_test": "풍랑속돛대가굽고돛이팽창하는변화를없애면②의형태변화를통한영향력근거가약해진다.비유만있어도환경영향을자동추론하지않음.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
