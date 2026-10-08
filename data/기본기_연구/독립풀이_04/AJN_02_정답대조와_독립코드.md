

<!-- luna-raw:AJN-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G221",
  "blind_answer": 1,
  "official_answer": 1,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "ⓐ는시름을적어멀리보내소멸시키려는연이므로①.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2026__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,원답셀직접검증아님",
  "barrier_verified": "G221전체blind4후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJN-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G221",
  "primary": [],
  "primary_candidates": [
    44,
    17
  ],
  "working_representative": 44,
  "auxiliary": [
    100,
    39
  ],
  "surface": [
    93
  ],
  "judgment_reason": "시름을적은연을멀리보내소멸시키는행위목적을확인.수단목적44와연의기능귀속17이겹침.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "후보",
      "reason": "임의전언기능을(나)의시름연에잘못옮기지않음"
    },
    {
      "code": 93,
      "verdict": "특정오답 표면",
      "reason": "글을적었다고임에게보내는메시지전달이성립하지않음"
    },
    {
      "code": 100,
      "verdict": "보조",
      "reason": "시름을연에담아보내는정서대응이행위목적설명"
    },
    {
      "code": 39,
      "verdict": "보조",
      "reason": "연소재가같아도두작품역할은다름"
    }
  ],
  "minimal_change_test": "연을다시가까이회수하려는행동으로바꾸면①멀리떠나보냄의목적이깨짐.집단의지나임수신자를외부에서추가안함.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
