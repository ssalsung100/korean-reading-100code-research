

<!-- luna-raw:AIP-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G215",
  "blind_answer": 2,
  "official_answer": 2,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "(가)동일색채어푸른과(나)유사한가정문구조반복이실제로확인되어②.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2024__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,공식PDF정답셀직접검증아님.AIR범위crop은직접검증완료",
  "barrier_verified": "AIR해소후G215blind6저장후answer만공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIP-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G215",
  "primary": [],
  "primary_candidates": [
    17,
    39
  ],
  "working_representative": 17,
  "auxiliary": [
    96
  ],
  "surface": [
    97,
    59
  ],
  "judgment_reason": "푸른이라는반복과가정문형식반복을각작품에맞춘다. 표현특징귀속17과작품간형식대조39의국소중첩.",
  "competing_codes": [
    {
      "code": 39,
      "verdict": "후보",
      "reason": "상이한반복양상을나란히대조"
    },
    {
      "code": 96,
      "verdict": "보조",
      "reason": "유사문장구조인지언어형식확인"
    },
    {
      "code": 97,
      "verdict": "특정오답",
      "reason": "(가)의명시청자근거없음"
    },
    {
      "code": 59,
      "verdict": "표면",
      "reason": "⑤문제해결이라는말만으로연쇄문제해결구조인정불가"
    }
  ],
  "minimal_change_test": "(가)색채반복을제거하거나(나)가정문반복을제거하면②의해당절이깨진다.두작품에같은반복내용이있어야한다는주장아님.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
