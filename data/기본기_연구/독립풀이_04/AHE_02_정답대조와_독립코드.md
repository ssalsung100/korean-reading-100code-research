

<!-- luna-raw:AHE-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G204",
  "blind_answer": 3,
  "official_answer": 3,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "허위 광고의 의도를 알기 어렵다는 본문을 쉽게 파악한다로 뒤집은③을 기각한다.",
  "official_answer_source": "canonical answer field 기계 연결; 공식 정답표 직접 검증 아님",
  "barrier_verified": "G204 전체 blind4 저장 후 answer필드만 공개; SDSS 미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AHE-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G204",
  "primary": [],
  "primary_candidates": [
    96,
    39
  ],
  "working_representative": 96,
  "auxiliary": [
    46
  ],
  "surface": [
    43,
    40
  ],
  "judgment_reason": "정답③은 의도 파악이 어렵다를 쉽다로 바꾼 국소 의미 반전이다. 일상 표현의 정도/극성 판독96과 원문·선지 비교39는 여기서 중첩된다.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "주 기각",
      "reason": "주체는 이용자, 대상은 허위 광고 의도로 동일하고 술어 극성이 바뀐다. 대상 교환으로 설명할 필요 없음"
    },
    {
      "code": 46,
      "verdict": "보조",
      "reason": "역선택의 원인 연결은①,③ 후반에도 있지만 의도 파악의 반전만으로③ 기각 가능"
    },
    {
      "code": 43,
      "verdict": "표면",
      "reason": "비용의 차이가 있다는 정보만 있으며 통제 설계의 타당성 평가 없음"
    },
    {
      "code": 18,
      "verdict": "주 기각",
      "reason": "원문과 어긋남을 모두 모순 코드로 부르면 판독 행동을 구별하지 못한다. 선지 집합의 일관성 검증이 아님"
    }
  ],
  "minimal_change_test": "쉽게 파악되므로를 파악하기 어려우므로로 바꾸면 해당 불일치가 사라진다.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
