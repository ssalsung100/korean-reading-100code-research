

<!-- luna-raw:AJA-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G218",
  "blind_answer": 3,
  "official_answer": 3,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "서로다른주체가상대의위협으로자신의위기에반응한것이ⓒ와ⓕ공통점이므로③.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2026__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,원답셀직접검증아님",
  "barrier_verified": "G218전체blind4후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJA-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G218",
  "primary": [],
  "primary_candidates": [
    23,
    39,
    17
  ],
  "working_representative": 23,
  "auxiliary": [
    46,
    80
  ],
  "surface": [
    96
  ],
  "judgment_reason": "ⓒ자라와ⓕ호랑이의위협반응을각각복원하여서로다른주체·같은위기반응이라는공통/차이축을맞춤.23·39·17국소중첩.",
  "competing_codes": [
    {
      "code": 39,
      "verdict": "후보",
      "reason": "반응주체차이와원인공통을대조"
    },
    {
      "code": 17,
      "verdict": "후보",
      "reason": "놀람·질색을각인물과상대행동에귀속"
    },
    {
      "code": 46,
      "verdict": "보조",
      "reason": "위협→놀람의발생계기를먼저복원"
    },
    {
      "code": 96,
      "verdict": "주 기각",
      "reason": "같은놀람표현이있어도기쁨·공포·위협의원인이달라어휘유사성만으로선택못함"
    }
  ],
  "minimal_change_test": "ⓕ가위기아닌숙원성취기쁨이었다면③의공통원인이깨짐.표현모양보다주체와계기확인필요.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
