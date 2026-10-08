

<!-- luna-raw:AHY-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G209",
  "blind_answer": 4,
  "official_answer": 4,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "걷기와 모이추구는 안온한 일상에 길들어 새의 비행본질을 잃는 모습이다.④은 본질을 상실하는 과정을 본질에 충실하다고 뒤집었다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2020__국어_국어_정답표.pdf",
  "verification_scope": "sealed필드와 대조했으며 공식PDF 정답셀의 직접시각대조는 아직 아님",
  "barrier_verified": "G209 전체 blind3 저장 후 answer필드만 공개; SDSS 미공개",
  "strict_blind_qualification": "작품친숙성과 stem의편집유형표제 노출기록 보존.완전무오염성과로 단정안함",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AHY-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G209",
  "primary": [],
  "primary_candidates": [
    17,
    100
  ],
  "working_representative": 17,
  "auxiliary": [
    39,
    96
  ],
  "surface": [
    46
  ],
  "judgment_reason": "보기의 새=현대인 알레고리에서 걷기·모이추구는 일상순응과본질상실에 대응한다.④은 이를 본질충실로 귀속.대응관계100과범주귀속17이 같은반전을검출해 유일주유보.",
  "competing_codes": [
    {
      "code": 100,
      "verdict": "후보",
      "reason": "명시적알레고리대응을 보존해야 본질상실의 뜻을판단"
    },
    {
      "code": 39,
      "verdict": "보조",
      "reason": "보기의일상충실/본질상실과선지의본질충실을대조"
    },
    {
      "code": 46,
      "verdict": "주 기각",
      "reason": "일상충실→본질상실 경로는 있으나④ 최소오류는 출발행동의 의미귀속을 본질충실로 바꾼것"
    },
    {
      "code": 18,
      "verdict": "주 기각",
      "reason": "아이러니를 논리적모순으로보아선지③을기각하면 안됨.서로다른평가차원의역설"
    }
  ],
  "minimal_change_test": "④ 자신의본질에충실하다보니를 일상의안온함에길들다보니로 고치면 보기의상실관계회복. 시의가치판단을일반생활훈계로대체하지 않음.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
