

<!-- luna-raw:AHS-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G208",
  "blind_answer": 2,
  "official_answer": 2,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "기업 조직 내 관계에 주목하는 연구와 달리 오피니언 리더 연구는 비정형 환경의 리더에 주목한다.②은 대비한 연구대상을 옮겨 연구 출발점을 서술한다.",
  "official_answer_source": "canonical answer field 기계 연결; 공식 정답표 직접 검증 아님",
  "barrier_verified": "G208 전체 blind4 저장 후 answer필드만 공개; SDSS 미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AHS-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G208",
  "primary": [
    17
  ],
  "auxiliary": [
    39,
    64
  ],
  "surface": [
    3,
    75
  ],
  "judgment_reason": "정형적 기업관계 연구를 비정형 오피니언리더 연구의 출발로 옮긴②이다. 연구가 주목한 대상과 환경의 귀속을 유지하면 기각된다.",
  "competing_codes": [
    {
      "code": 39,
      "verdict": "보조",
      "reason": "두연구를 대비하여17 귀속을 복원하지만 비교 자체보다 어느 연구의 대상인가가 오류위치"
    },
    {
      "code": 3,
      "verdict": "표면",
      "reason": "시작이라는 표현이 있으나 사건의 선후를 뒤집은 오류가 아니라 기원의 연구범위 교환"
    },
    {
      "code": 75,
      "verdict": "주 기각",
      "reason": "서로 상반되는 두 견해의 논쟁이 아니라 연구대상 환경 구별"
    },
    {
      "code": 64,
      "verdict": "보조",
      "reason": "기업에서 시작되었다는 근거는 없지만 본문이 직접 대비한 범주교환이 더 구체적 근거"
    }
  ],
  "minimal_change_test": "기업내 리더구성원 관계를 비정형환경 리더로 고치면 오류해소. 시간표현만 고쳐서는 오귀속 남음.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
