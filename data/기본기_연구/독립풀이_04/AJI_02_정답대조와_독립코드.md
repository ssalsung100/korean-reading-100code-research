

<!-- luna-raw:AJI-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G220",
  "blind_answer": 5,
  "official_answer": 5,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "온씨는앞소문을듣고허명두를만나확인한일을뒤이야기로퍼뜨린다.⑤이두정보의시간·연결관계를보존.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2026__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,원답셀직접검증아님.AJH범위crop직접확인",
  "barrier_verified": "G220전체blind4후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJI-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G220",
  "primary": [],
  "primary_candidates": [
    3,
    93,
    45
  ],
  "working_representative": 3,
  "auxiliary": [
    17
  ],
  "surface": [
    63
  ],
  "judgment_reason": "ⓑ소문수용→방문확인→ⓐ전파의사건순서와정보생성과정을복원.3선후·93전달·45처리흐름국소중첩.",
  "competing_codes": [
    {
      "code": 93,
      "verdict": "후보",
      "reason": "온씨가정보수신자에서확인후발신자로변함"
    },
    {
      "code": 45,
      "verdict": "후보",
      "reason": "선행정보가확인행동을거쳐후행이야기에반영되는과정"
    },
    {
      "code": 17,
      "verdict": "보조",
      "reason": "누가무엇을듣고퍼뜨렸는지귀속"
    },
    {
      "code": 63,
      "verdict": "주 기각",
      "reason": "소문의진실성이새증거로강화되는정도를평가하기보다관계흐름확인"
    }
  ],
  "minimal_change_test": "글의제시순서를바꿔도사건은ⓑ→확인→ⓐ.ⓑ가없으면방문의정보계기가없어현재관계복원불가.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
