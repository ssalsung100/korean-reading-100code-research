

<!-- luna-raw:AHO-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G207",
  "blind_answer": 2,
  "official_answer": 2,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "스위치의 온오프는 변압기에 필요한 전압 변화를 만들며 평활 회로가 변동을 억제한다.②은 스위치에 반대 기능을 부여한다.",
  "official_answer_source": "canonical answer field 기계 연결; 공식 정답표 직접 검증 아님",
  "barrier_verified": "G207 전체 blind4 저장 후 answer필드만 공개; SDSS 미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AHO-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G207",
  "primary": [],
  "primary_candidates": [
    45,
    17
  ],
  "working_representative": 45,
  "auxiliary": [
    46,
    49
  ],
  "surface": [
    40
  ],
  "judgment_reason": "스위치의 입출력 변화 기능을 억제로 바꾼② 오류. 기능 대응45와 억제 기능의 잘못된 장치 귀속17이 같은 위치를 검출. 부품이 많다는40으로 대체하지 않음.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "후보",
      "reason": "평활회로의 억제기능을 스위치에 옮김으로 설명 가능"
    },
    {
      "code": 49,
      "verdict": "보조",
      "reason": "변동 증가를 억제로 바꾼 방향 반전이나 그 방향은 국소 스위치 입출력에 한정"
    },
    {
      "code": 46,
      "verdict": "보조",
      "reason": "변압기 작동을 위한 변동 생성의 경로가 뒷받침하지만②은 직접 기능문 대조로 기각 가능"
    },
    {
      "code": 40,
      "verdict": "표면",
      "reason": "부품 구성 존재만 알면 어떤 부품이 억제하는지 결정 못함"
    }
  ],
  "minimal_change_test": "스위치라는 주체를 평활회로로 바꾸거나 억제를 생성으로 고치면 기능 오류 해소. 전체 전원의 안정화를 개별 스위치의 국소 작용으로 옮기지 않는다.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
