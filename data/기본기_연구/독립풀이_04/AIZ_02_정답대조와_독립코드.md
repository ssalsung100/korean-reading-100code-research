

<!-- luna-raw:AIZ-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G218",
  "blind_answer": 4,
  "official_answer": 4,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "산중위기는자라의말실수로생기고수궁내력은위기탈출을위한거짓말에등장한다.④이현실사건공간과말속공간의역할을구별.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2026__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,원답셀직접검증아님",
  "barrier_verified": "G218전체blind4후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIZ-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G218",
  "primary": [],
  "primary_candidates": [
    17,
    44
  ],
  "working_representative": 17,
  "auxiliary": [
    2,
    39
  ],
  "surface": [
    42
  ],
  "judgment_reason": "산중위기는실제말실수의결과,수궁이야기는위기탈출수단. 공간의실제사건/속임수발화귀속17과언급목적44중첩.",
  "competing_codes": [
    {
      "code": 44,
      "verdict": "후보",
      "reason": "수궁을왜언급했는지속임수의목적을판독"
    },
    {
      "code": 42,
      "verdict": "표면",
      "reason": "공간명존재만으로안팎경계분석이핵심아님"
    },
    {
      "code": 2,
      "verdict": "보조",
      "reason": "②이미대비했다는사실주장은거짓내력을실제과거로승격"
    },
    {
      "code": 39,
      "verdict": "특정선지",
      "reason": "⑤호랑이자기용맹과잡놈대조는자기위엄부정이아닌긍정"
    }
  ],
  "minimal_change_test": "수궁사냥준비를객관서술로실제확인하면②의현재반증근거가약해짐.원문은속임수계획을직접명시.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
