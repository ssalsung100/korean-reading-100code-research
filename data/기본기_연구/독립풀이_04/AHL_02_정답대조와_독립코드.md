

<!-- luna-raw:AHL-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G206",
  "blind_answer": 4,
  "official_answer": 4,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "본문은 전기류가 전 생애도 특정 일화도 다룰 수 있다고 허용한다.④은 특정 일화가 아님으로 한 가능성을 배제하여 범위를 축소한다.",
  "official_answer_source": "canonical answer field 기계 연결; 공식 정답표 직접 검증 아님",
  "barrier_verified": "G206 전체 blind3 저장 후 answer필드만 공개; SDSS 미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AHL-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G206",
  "primary": [],
  "primary_candidates": [
    2,
    4,
    17
  ],
  "working_representative": 2,
  "auxiliary": [
    16
  ],
  "surface": [
    3
  ],
  "judgment_reason": "전기류의 허용 유형 중 특정 일화를④이 배제한다. 특정 일화형 가능성을 부정한2, 모든 전기류를 전생애형으로 한정한4, 허용범주를 축소한17이 같은 교체에 대응해 유일주 유보.",
  "competing_codes": [
    {
      "code": 4,
      "verdict": "후보",
      "reason": "명시적 모든 없이도 유형 일반진술이 전기류 전체를 전생애형으로 한정"
    },
    {
      "code": 17,
      "verdict": "후보",
      "reason": "특정 일화형을 대상범주에서 제외한 동일 오류"
    },
    {
      "code": 16,
      "verdict": "보조",
      "reason": "전기류의 정의와 하위형을 복원하지만 정의의 필요충분성 증명은 없음"
    },
    {
      "code": 13,
      "verdict": "주 기각",
      "reason": "특정 일화형과 전생애형 사이의 배타성을 증명하는 문제가 아니라 본문이 인정한 한 유형을 삭제한 오류"
    }
  ],
  "minimal_change_test": "특정 일화가 아닌을 특정 일화나로 바꾸면 허용 범위를 회복해2/4/17이 함께 바뀜. 유형 단위와 개별 작품의 가능성 양화를 구별하며 전 작품이 두 형식을 동시에 갖는다고 읽지 않음.",
  "sdss_seen": false,
  "confidence": 0.93,
  "quota_status": "unavailable"
}
```
