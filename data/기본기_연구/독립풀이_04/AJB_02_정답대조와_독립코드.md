

<!-- luna-raw:AJB-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G218",
  "blind_answer": 2,
  "official_answer": 2,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "호랑이는먹고싶은욕망을약효말과함께노골적으로표현한다.②의지식으로속내를숨기는위선이라는해석은은폐근거가없다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2026__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,원답셀직접검증아님",
  "barrier_verified": "G218전체blind4후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJB-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G218",
  "primary": [],
  "primary_candidates": [
    80,
    64,
    17
  ],
  "working_representative": 80,
  "auxiliary": [
    97,
    100
  ],
  "surface": [
    63
  ],
  "judgment_reason": "공개적으로먹겠다는호랑이의의도를은폐된욕망으로해석한②.속내표출여부80·근거없는은폐추가64·태도귀속17이같은오류검출.",
  "competing_codes": [
    {
      "code": 64,
      "verdict": "후보",
      "reason": "지식이등장할뿐욕망숨김의근거없음"
    },
    {
      "code": 17,
      "verdict": "후보",
      "reason": "노골적욕망을위선적은폐범주에귀속"
    },
    {
      "code": 97,
      "verdict": "보조",
      "reason": "너를먹으리라는말이위협·욕망의직접표출"
    },
    {
      "code": 63,
      "verdict": "표면",
      "reason": "인간비판이라는소재가논증증거강약평가와같지않음"
    }
  ],
  "minimal_change_test": "호랑이가치료해준다고거짓명분을앞세우고먹겠다는말을숨겼다면은폐해석을검토할수있음.현재는반복해먹겠다고밝힘.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
