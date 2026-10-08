

<!-- luna-raw:AHT-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G208",
  "blind_answer": 3,
  "official_answer": 3,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "미디어가 유권자에게 직접 미치는 영향이 작았던 결과를 관계망 속 정보제공자의 매개 영향으로 설명한다.③이 해당 설명이다.",
  "official_answer_source": "canonical answer field 기계 연결; 공식 정답표 직접 검증 아님",
  "barrier_verified": "G208 전체 blind4 저장 후 answer필드만 공개; SDSS 미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AHT-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G208",
  "primary": [],
  "primary_candidates": [
    56,
    46
  ],
  "working_representative": 56,
  "auxiliary": [
    17,
    3
  ],
  "surface": [
    93
  ],
  "judgment_reason": "미디어의 직접영향 미미라는 관측을 사회관계에 기반한 매개자의 영향으로 설명한다.설명항/피설명항56과 원인경로46이 같은 설명을 기술해 유일주 유보.",
  "competing_codes": [
    {
      "code": 46,
      "verdict": "후보",
      "reason": "관계망속 정보제공자가 미디어 효과에 영향을 미친 경로가 관측이유"
    },
    {
      "code": 93,
      "verdict": "표면",
      "reason": "커뮤니케이션 소재이나 화자·메시지·수신자의 표현의도 왜곡을 따로 판정하지 않음"
    },
    {
      "code": 3,
      "verdict": "특정오답 보조",
      "reason": "② 오늘날 공론장 역할을 과거 이유로 쓰는 시점전이 기각"
    },
    {
      "code": 63,
      "verdict": "주 기각",
      "reason": "새 증거가 이론을 얼마나 강화하는지보다 이미 주어진 관측의 이유를 복원"
    }
  ],
  "minimal_change_test": "매개자의 존재를 제거한⑤는 관측설명을 부정한다. 전문가라는 신분만 넣고 정보매개를 빼면④처럼 원인연결이 확보되지 않는다.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
