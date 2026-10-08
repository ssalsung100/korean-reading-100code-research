

<!-- luna-raw:AJF-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G219",
  "blind_answer": 4,
  "official_answer": 4,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "구름과비의경험도성장·성숙과정의일부로권유하므로④가적절하다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2026__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,원답셀직접검증아님",
  "barrier_verified": "G219전체blind5후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJF-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G219",
  "primary": [],
  "primary_candidates": [
    44,
    46,
    100
  ],
  "working_representative": 46,
  "auxiliary": [
    17,
    4
  ],
  "surface": [
    3
  ],
  "judgment_reason": "구름·비의경험을감과내면성숙과정에의미있는조건으로판독.성장작용46·과정의목적기여44·자연내면대응100중첩.",
  "competing_codes": [
    {
      "code": 44,
      "verdict": "후보",
      "reason": "맞아보라는권유의성숙지향과연결"
    },
    {
      "code": 100,
      "verdict": "후보",
      "reason": "자연열매와내면동일시로구름비의의미판독"
    },
    {
      "code": 4,
      "verdict": "특정오답 보조",
      "reason": "①뿐의한정대상을흔드는원인에서흔들리는대상으로교환"
    },
    {
      "code": 3,
      "verdict": "특정오답",
      "reason": "②미래익음을현재완숙으로옮김"
    }
  ],
  "minimal_change_test": "구름비를성장과무관한폐해로부정하는시구가추가되면④판정변화.현재는다양한경험을겪어성숙하라는권유맥락.",
  "sdss_seen": false,
  "confidence": 0.93,
  "quota_status": "unavailable"
}
```
