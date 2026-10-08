

<!-- luna-raw:AIL-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G214",
  "blind_answer": 1,
  "official_answer": 1,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "채전의충만한생명과참나무상처에서피는버섯의생명을모두긍정적으로예찬한다.①이공통태도이다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2023__국어_1교시_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,공식PDF정답셀직접검증아님.AIN범위crop은직접검증완료",
  "barrier_verified": "AIN해소후G214blind4저장후answer만공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIL-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G214",
  "primary": [],
  "primary_candidates": [
    23,
    80
  ],
  "working_representative": 23,
  "auxiliary": [
    17,
    39
  ],
  "surface": [
    100
  ],
  "judgment_reason": "두작품에서중심생명을긍정·예찬하는태도를각각확인하여공통특성을수용.태도판독80과공통부분확인23이최소과제로겹쳐유일주유보.",
  "competing_codes": [
    {
      "code": 80,
      "verdict": "후보",
      "reason": "충족·빛남과황홀한꽃·고통멈춤의긍정태도를판독"
    },
    {
      "code": 17,
      "verdict": "보조",
      "reason": "각작품에긍정속성을귀속한뒤양쪽성립확인"
    },
    {
      "code": 39,
      "verdict": "보조",
      "reason": "두작품대조는필요하지만차이보다공통태도수용이직접과제"
    },
    {
      "code": 100,
      "verdict": "표면",
      "reason": "상징·비유표현이있어도예찬어휘와관계로태도판독가능"
    }
  ],
  "minimal_change_test": "한작품이생명대상을명시적으로혐오한다면공통예찬명제는깨진다. 고통소재유무와그속생명에대한태도는별개.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
