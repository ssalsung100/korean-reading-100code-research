

<!-- luna-raw:AJK-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G220",
  "blind_answer": 3,
  "official_answer": 3,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "허명두는불안정을낳는원인을상대와달리보는것이아니라원인과사리의옳음을알면서실리를앞세운다.③은원인인식차이를없는곳에추가.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2026__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,원답셀직접검증아님.AJH범위crop직접확인",
  "barrier_verified": "G220전체blind4후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJK-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G220",
  "primary": [],
  "primary_candidates": [
    80,
    75,
    17
  ],
  "working_representative": 80,
  "auxiliary": [
    46,
    77
  ],
  "surface": [
    63
  ],
  "judgment_reason": "허명두는상대가본피해원인을이해·인정하면서실리선택을고수한다.인식차와선택차를혼동한③.인식80·견해관계75·내용귀속17중첩.",
  "competing_codes": [
    {
      "code": 75,
      "verdict": "후보",
      "reason": "두인물의공통원인인식과상반선택을분리"
    },
    {
      "code": 17,
      "verdict": "후보",
      "reason": "허명두에게없는원인해석차를귀속"
    },
    {
      "code": 46,
      "verdict": "보조",
      "reason": "외부자본→관광지화→안정상실의공유된원인경로복원"
    },
    {
      "code": 77,
      "verdict": "특정선지 보조",
      "reason": "④과거실리승리경험의일반화는있지만③정답오류는다름"
    }
  ],
  "minimal_change_test": "허명두가주민방황원인을다른요인으로돌렸다는서술이추가되면③을검토가능.현재는온씨주장옳음을명시적으로인정.",
  "sdss_seen": false,
  "confidence": 0.96,
  "quota_status": "unavailable"
}
```
