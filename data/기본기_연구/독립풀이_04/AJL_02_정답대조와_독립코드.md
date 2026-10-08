

<!-- luna-raw:AJL-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G221",
  "blind_answer": 2,
  "official_answer": 2,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "대구로고생을나란히보이고잠깐감사와오랜원한을대조하여어사처지의괴로움을강조하므로②.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2026__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,원답셀직접검증아님",
  "barrier_verified": "G221전체blind4후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJL-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G221",
  "primary": [],
  "primary_candidates": [
    39,
    96,
    17
  ],
  "working_representative": 39,
  "auxiliary": [
    80,
    3
  ],
  "surface": [
    100
  ],
  "judgment_reason": "대구문장과감사잠깐/원한대대의대조가고충을드러냄.형식비교39·언어표현96·정서효과귀속17이함께작동.",
  "competing_codes": [
    {
      "code": 96,
      "verdict": "후보",
      "reason": "평행구조와반대내용의문맥기능을판독"
    },
    {
      "code": 17,
      "verdict": "후보",
      "reason": "해당표현에어사고충이라는효과를귀속"
    },
    {
      "code": 100,
      "verdict": "특정오답",
      "reason": "백룡비유는연의움직임이지자연현상변화아님"
    },
    {
      "code": 3,
      "verdict": "보조",
      "reason": "잠깐/대대의시간차가대조내용을형성하나사건선후판정아님"
    }
  ],
  "minimal_change_test": "감사와원한의기간을동일하게바꾸면②의해당대조근거가약해짐.대구유무와고충이라는효과모두확인해야함.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
