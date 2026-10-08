

<!-- luna-raw:AIV-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G216",
  "blind_answer": 1,
  "official_answer": 1,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "집안의비하대화가밖으로들려인물의속마음이노출되므로①.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2024__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,공식PDF정답셀직접검증아님.AIW범위crop직접확인",
  "barrier_verified": "AIW해소후G216전체blind2저장후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIV-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G216",
  "primary": [],
  "primary_candidates": [
    93,
    80,
    17
  ],
  "working_representative": 93,
  "auxiliary": [
    96,
    39
  ],
  "surface": [
    42
  ],
  "judgment_reason": "집안대화가예상청자밖이웃에게전달되어속내가노출됨. 발화전달93·인물속내파악80·발화내용귀속17이동일장면에서겹침.",
  "competing_codes": [
    {
      "code": 80,
      "verdict": "후보",
      "reason": "외부로들린대화로비하하는속마음판독"
    },
    {
      "code": 17,
      "verdict": "후보",
      "reason": "집주름부부의비하말을해당인물의속내에귀속"
    },
    {
      "code": 42,
      "verdict": "보조후보",
      "reason": "집안/대문밖은전달범위이지만경계자체의포함판정보다내용노출이핵심"
    },
    {
      "code": 5,
      "verdict": "특정오답 기각",
      "reason": "⑤추궁중단이앙금해소의관계변화를보장하지않음"
    }
  ],
  "minimal_change_test": "대화가밖으로들리지않았다면이웃에게속내가노출된다는①근거가사라짐.속내가존재한다는것과그속내를타인이알게됨은다름.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
