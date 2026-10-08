

<!-- luna-raw:AIJ-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G213",
  "blind_answer": 3,
  "official_answer": 3,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "㉠은경관의출현으로숨었고㉡은몸의변화를관찰하기위해숨었다.③의원인차이가맞음.",
  "official_answer_source": "자료/평가원_정답표/원본/모의평가/2023_9월_국어_1교시_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,공식PDF정답셀직접검증아님",
  "barrier_verified": "G213blind4저장후answer만공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIJ-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G213",
  "primary": [],
  "primary_candidates": [
    39,
    46
  ],
  "working_representative": 39,
  "auxiliary": [
    17,
    44
  ],
  "surface": [
    42,
    79
  ],
  "judgment_reason": "두은신행동의계기를비교한다.첫째경관등장,둘째신체변화확인이라는차이를유지. 원인비교39와각행동발생이유46이국소중첩.",
  "competing_codes": [
    {
      "code": 46,
      "verdict": "후보",
      "reason": "경관출현이은신을유발하는지각장면에서확인"
    },
    {
      "code": 44,
      "verdict": "보조",
      "reason": "둘째숨은목적은회복아닌신체확인이므로①기각"
    },
    {
      "code": 42,
      "verdict": "표면",
      "reason": "안팎경계의포함관계가아니라왜숨었는가의행동계기"
    },
    {
      "code": 79,
      "verdict": "특정오답 표면",
      "reason": "윤리·정치라는②의용어는본문의구체동기를대체하지못함"
    }
  ],
  "minimal_change_test": "둘째도다른사람을피해숨었다는근거가주어지면③의차이는사라짐. 장소이름만바꾸어도사건계기가같으면현재대조유지.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
