

<!-- luna-raw:AHV-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G208",
  "blind_answer": 5,
  "official_answer": 5,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "가정을 벗어남은 물리적 장소를 나오는 것도 고통이 없어지는 것도 아니라 일정한 사고의 틀·범위에 더 이상 따르지 않는 뜻이다.⑤ 규범의 범위를 이탈하는 용례가 가장 가깝다.",
  "official_answer_source": "canonical answer field 기계 연결; 공식 정답표 직접 검증 아님",
  "barrier_verified": "G208 전체 blind4 저장 후 answer필드만 공개; SDSS 미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AHV-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G208",
  "primary": [],
  "primary_candidates": [
    96,
    39
  ],
  "working_representative": 96,
  "auxiliary": [
    17
  ],
  "surface": [
    42,
    100
  ],
  "judgment_reason": "가정이라는 사고틀과 규범이라는 기준의 범위를 이탈한다는 문맥의미를 비교한다.96 의미판독과39 용례대조는 동일 작업으로 중첩.",
  "competing_codes": [
    {
      "code": 39,
      "verdict": "후보",
      "reason": "원문·선지의 벗어나다 용례 의미대조"
    },
    {
      "code": 42,
      "verdict": "표면",
      "reason": "밖으로 나감의 공간어감만으로 내부외부 관계를 핵심으로 삼으면 물리적①②와 추상⑤을 구별 못함"
    },
    {
      "code": 100,
      "verdict": "주 기각",
      "reason": "추상적 범위 이탈의 관용적 쓰임이며 새로운 비유의 대응관계를 추론하는 과제 아님"
    },
    {
      "code": 17,
      "verdict": "보조",
      "reason": "벗어나는 대상이 공간·줄·곤란상태·규범인지 분류하여 문맥뜻 구별"
    }
  ],
  "minimal_change_test": "가정의 뜻을 어려운 고통상태로 바꿔 읽어야만④가 가까워진다.그런 원문 의미변경 없이⑤을 선택한다.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
