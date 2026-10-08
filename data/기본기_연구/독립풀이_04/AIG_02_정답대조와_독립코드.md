

<!-- luna-raw:AIG-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G212",
  "blind_answer": 1,
  "official_answer": 1,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "미개지로가자는말은기존공동체의건강한전통으로돌아가려는권유이다.①은새터전의확장으로공간방향과목적을바꾸었다.",
  "official_answer_source": "자료/평가원_정답표/원본/모의평가/2023_6월_국어_1교시_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조, 공식PDF정답셀 직접검증은 아직아님",
  "barrier_verified": "G212 전체 blind3 저장 후 answer필드만 공개; SDSS 미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIG-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G212",
  "primary": [],
  "primary_candidates": [
    17,
    44,
    64
  ],
  "working_representative": 17,
  "auxiliary": [
    100,
    39
  ],
  "surface": [
    5
  ],
  "judgment_reason": "①은 돌아가자의 지향을 과거 공동체 회복에서 터전 확장으로 바꾼다. 지향 대상17·목적44·근거 범위64가 동일 추가 오류를 기술하여 유일주 유보.",
  "competing_codes": [
    {
      "code": 44,
      "verdict": "후보",
      "reason": "귀환 권유의 목적을 순수성 회복에서 공간 확장으로 바꾼 기술"
    },
    {
      "code": 64,
      "verdict": "후보",
      "reason": "터전 확장은 시와 보기 어디에도 지지되지 않는 해석 추가"
    },
    {
      "code": 100,
      "verdict": "보조",
      "reason": "미개지는 건강한 전통 지향이라는 작품 내 의미를 지닌다. 문자적 영토 확장으로 바꾸지 않음"
    },
    {
      "code": 5,
      "verdict": "주 기각",
      "reason": "회복이라는 변화 방향은 있으나 단순 변화 유무보다 무엇을 회복/확장하는가의 지향이 핵심"
    }
  ],
  "minimal_change_test": "① 터전을 확장하여를 전통으로 돌아가로 고치면 시와 보기의 목적이 복원된다. 새로운 이주지 개척이라는 행동을 추가하지 않는다.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
