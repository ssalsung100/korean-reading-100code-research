

<!-- luna-raw:AII-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G213",
  "blind_answer": 4,
  "official_answer": 4,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "규칙을정하는주체는관청이다.시민이받아들인규칙을시민이정한규칙으로바꾼④이틀림.",
  "official_answer_source": "자료/평가원_정답표/원본/모의평가/2023_9월_국어_1교시_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,공식PDF정답셀직접검증아님",
  "barrier_verified": "G213blind4저장후answer만공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AII-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G213",
  "primary": [
    17
  ],
  "auxiliary": [
    96,
    3
  ],
  "surface": [
    79,
    4
  ],
  "judgment_reason": "관청이정한규칙을시민이정했다고하여행위주체가교환됨. 시민의수용과관청의제정이라는술어별주체를분리.",
  "competing_codes": [
    {
      "code": 79,
      "verdict": "표면",
      "reason": "규칙의당위성·정당성평가가아니라누가정했는지확인"
    },
    {
      "code": 4,
      "verdict": "표면",
      "reason": "모든사람이받아들임이라는전칭표현이있지만전칭범위를바꾼오류아님"
    },
    {
      "code": 96,
      "verdict": "보조",
      "reason": "정하다와받아들이다의행위뜻구별이주체귀속을고정"
    },
    {
      "code": 46,
      "verdict": "특정선지",
      "reason": "①진단실패의이유는인과연결이나④정답연산과다름"
    }
  ],
  "minimal_change_test": "④시민을관청으로바꾸면오류해소. 시민모두가수용한다는정보를강화해도규칙제정자로전환되지않음.",
  "sdss_seen": false,
  "confidence": 0.96,
  "quota_status": "unavailable"
}
```
