

<!-- luna-raw:AHZ-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G210",
  "blind_answer": 5,
  "official_answer": 5,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "그리운곳을 떠올리는밤에 잠깬자신을 어쩌자고라고 되묻는 말은 애달픔을 드러냄.대상의거부나현실변화전망을추가하지않음.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2021__국어_1교시_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조, 공식PDF정답셀 직접검증은 아직아님",
  "barrier_verified": "G210유일case blind저장후 answer만공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AHZ-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G210",
  "primary": [],
  "primary_candidates": [
    80,
    96,
    97
  ],
  "working_representative": 96,
  "auxiliary": [
    39,
    64
  ],
  "surface": [
    5,
    2
  ],
  "judgment_reason": "어쩌자고의자기질문을 그리움의맥락에서 읽어 애달픔을판독한다.심리태도80·문맥언어96·질문기능97이 국소적으로같은행동을기술하여 유일주유보.",
  "competing_codes": [
    {
      "code": 97,
      "verdict": "후보",
      "reason": "질문이정보를구하려는것인지 한탄을드러내는지 문맥으로 구별"
    },
    {
      "code": 80,
      "verdict": "후보",
      "reason": "북쪽과그리운이에대한 화자의내면태도 판독"
    },
    {
      "code": 5,
      "verdict": "특정오답 표면",
      "reason": "④ 사물의물리적상태변화를 현실의전망변화로 치환할근거없음"
    },
    {
      "code": 2,
      "verdict": "특정오답 보조후보",
      "reason": "④ 변화가능성을 제시하지만 허용되는가능성강도보다 그런전망자체의근거가 없음"
    }
  ],
  "minimal_change_test": "그리운곳·차마·어쩌자고의결합을 빼면애달픔 해석근거약화.얼어드는사물 하나만 남겨도미래현실변화는추론불가.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
