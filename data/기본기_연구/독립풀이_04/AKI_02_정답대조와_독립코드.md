

<!-- luna-raw:AKI-answer_check-20260926-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G228",
  "blind_answer": 1,
  "official_answer": 1,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "지배가 공동체 이익을 위해 수행되어야 한다는 것은 벌리의 목표이다. 준공공회사의 지배가 실제로 이미 공동체 이익을 위해 수행된다는①의 사실 진술은 본문에서 보장되지 않는다.",
  "official_answer_source": "자료/LEET_언어이해/원본/2022/2022_answer_2022_LEET_언어이해_정답표_배포용.pdf",
  "verification_scope": "정본 연결 sealed 공식답 필드 대조; 이번 단계에서 공식 PDF 답 셀 직접 판독 아님",
  "barrier_verified": "G228 전체 blind raw 저장 후 공식답 필드만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AKI-independent_code-20260926-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    79
  ],
  "auxiliary": [
    83
  ],
  "surface": [
    17,
    44
  ],
  "judgment_reason": "공동체 이익을 위해 수행되어야 한다는 규범을 이미 수행되는 기능이라는 사실로 바꾼①을 판정한다. 준공공회사라는 구조적 명칭이 규범의 실현을 보증하지 않는다.",
  "competing_codes": [
    {
      "code": 83,
      "verdict": "보조·국소 중첩",
      "reason": "사실/가치라는 넓은 구별 중 당위/실태에 특화한79가 작업 대표. 별개 독립 연산으로 중복 셈하지 않음."
    },
    {
      "code": 17,
      "verdict": "⑤ 오답 검토",
      "reason": "같은 경영자가 지배도 수행할 수 있으나 역할 개념은 다름.①의 당위→사실 오류와 구별."
    },
    {
      "code": 44,
      "verdict": "표면",
      "reason": "위한다는 목적 표현이 있으나 목표 내용은 맞고 그 목표가 실제 수행된다는 확정이 틀림."
    },
    {
      "code": 2,
      "verdict": "경쟁 후보",
      "reason": "지향에서 실현 보장으로 강도를 높인다고 표현할 수도 있으나 본문의 명시 당위/사실 구분79가 구체적."
    }
  ],
  "minimal_change_test": "①의 수행되는을 수행되어야 하는으로 고치면 벌리의 결론과 맞는다. 이 수정은 공동체 목적 자체를 바꾸지 않는다.",
  "confidence": 0.97,
  "passage_group": "G228",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
