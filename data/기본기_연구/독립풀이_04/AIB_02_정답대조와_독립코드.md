

<!-- luna-raw:AIB-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G211",
  "blind_answer": 1,
  "official_answer": 1,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "금부감금은권위실현이나 한곳에서왕은몸을숨기고듣는다.①의후반 권위를내세움은실제행동과어긋난다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2022__국어_1교시_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조. AIC 공식PDF범위직접검증과정답셀직접대조는구별",
  "barrier_verified": "AICscope해소후유효blind4개모두저장한다음G211첫answer공개; SDSS미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIB-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G211",
  "primary": [],
  "primary_candidates": [
    17,
    96
  ],
  "working_representative": 17,
  "auxiliary": [
    39,
    3
  ],
  "surface": [
    42,
    75
  ],
  "judgment_reason": "한 곳에서 왕이 몸을 숨겨 듣는 행동에 권위 과시를 귀속한① 후반이 틀림. 공간의 기능17은 그 안의 실제 행동 의미96에 의해 판독되므로 단독우위 유보.",
  "competing_codes": [
    {
      "code": 96,
      "verdict": "후보",
      "reason": "은신하여듣는다는 행위와 권위를내세운다는 행위의 의미 불일치"
    },
    {
      "code": 42,
      "verdict": "표면",
      "reason": "공간이 등장하지만 내부외부 경계의 포함이나 출입 가능성이 정답연산 아님"
    },
    {
      "code": 39,
      "verdict": "보조",
      "reason": "금부/한곳의 기능 대비를 묻지만 후반 하나의 잘못된 귀속만으로① 기각 가능"
    },
    {
      "code": 75,
      "verdict": "표면",
      "reason": "군주와백성 갈등소재만으로 견해논쟁 코드를 주로 삼지 않음"
    }
  ],
  "minimal_change_test": "한곳의 행동을 공개적으로왕명을내리는 장면으로 바꾸면 권위과시 반증근거가 사라짐. 지명이같다는사실로 공간기능을 고정하지 않는다.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
