

<!-- luna-raw:AIN-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G214",
  "blind_answer": 2,
  "official_answer": 2,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "바람이참나무를흔든뒤이윽고홀씨가일어나버섯이핀다.②의[B]→[C]순차관계가명시된연결에맞다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2023__국어_1교시_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,공식PDF정답셀직접검증아님.AIN범위crop은직접검증완료",
  "barrier_verified": "AIN해소후G214blind4저장후answer만공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIN-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G214",
  "primary": [
    3
  ],
  "auxiliary": [
    39,
    17
  ],
  "surface": [
    46,
    5
  ],
  "judgment_reason": "[B]흔들림뒤[C]이윽고홀씨일어나버섯생성이라는시점연결이②순차관계를직접지지.시간순서를곧필연적발생원인으로강화하지않음.",
  "competing_codes": [
    {
      "code": 46,
      "verdict": "특정오답",
      "reason": "④[D]변화가[E]낙엽바람상황을발생시킨다는인과는없음"
    },
    {
      "code": 39,
      "verdict": "보조",
      "reason": "③대립·⑤동질이라는관계기술의적합성대조"
    },
    {
      "code": 5,
      "verdict": "보조후보",
      "reason": "사건들이상태변화이긴하나②가명시적으로묻는것은그사건사이의순서"
    },
    {
      "code": 18,
      "verdict": "기각",
      "reason": "대립·순환·동질을전부논리모순문제로환원하면해당관계의유형을구별못함"
    }
  ],
  "minimal_change_test": "이윽고대신이미그이전에버섯이피었다고하면[B]→[C]의현재순차근거가바뀜. 같은생성내용만으로순서는확정못함.",
  "sdss_seen": false,
  "confidence": 0.96,
  "quota_status": "unavailable"
}
```
