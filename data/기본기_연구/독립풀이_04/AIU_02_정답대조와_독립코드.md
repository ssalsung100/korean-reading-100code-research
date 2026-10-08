

<!-- luna-raw:AIU-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G215",
  "blind_answer": 5,
  "official_answer": 5,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "예의·분수를기억하는것은병이아니라바람직함이다.⑤은잊지않음이병일수있다는비판을기억해야할도리에적용해대상범주를교환한다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2024__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,공식PDF정답셀직접검증아님.AIR범위crop은직접검증완료",
  "barrier_verified": "AIR해소후G215blind6저장후answer만공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIU-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G215",
  "primary": [
    17
  ],
  "auxiliary": [
    33,
    79,
    39
  ],
  "surface": [
    4,
    40
  ],
  "judgment_reason": "잊지않음이병일수있는대상은버려야할외적집착이다.⑤은기억해야할예의·분수에그평가를옮긴다.부정문해석뒤평가대상범주를고정.",
  "competing_codes": [
    {
      "code": 33,
      "verdict": "보조",
      "reason": "병이아닌것은아니라는이중부정은병일수있음/병인경우를열어주는문맥.그대상을예의로교환하면오류"
    },
    {
      "code": 79,
      "verdict": "보조",
      "reason": "기억해야할도리와잊어도될욕망의가치분류가대상귀속근거"
    },
    {
      "code": 4,
      "verdict": "주 기각",
      "reason": "모든기억이병이라는전칭을본문이주지않음.조건·대상별평가를유지"
    },
    {
      "code": 40,
      "verdict": "특정선지",
      "reason": "①수양부분의혼연일체는맞지만⑤정답연산아님"
    }
  ],
  "minimal_change_test": "⑤예의·분수기억을부당한욕망기억으로바꾸면비판대상범주복원. 이중부정만풀고대상범주를보지않으면선지기각못함.",
  "sdss_seen": false,
  "confidence": 0.96,
  "quota_status": "unavailable"
}
```
