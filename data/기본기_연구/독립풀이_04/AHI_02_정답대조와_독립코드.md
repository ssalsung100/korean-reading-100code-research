

<!-- luna-raw:AHI-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G205",
  "blind_answer": 4,
  "official_answer": 4,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "같은 물질의 기포가 합쳐져 반지름이 커지면 표면장력 조건을 유지한 압력차는 작아진다. 따라서 새 기포 압력차는 원래 큰 기포보다 작다는④.",
  "official_answer_source": "canonical answer field 기계 연결; 공식 정답표 직접 검증 아님",
  "barrier_verified": "G205 전체 blind4 저장 후 answer필드만 공개; SDSS 미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AHI-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G205",
  "primary": [
    91
  ],
  "auxiliary": [
    43,
    86,
    46
  ],
  "surface": [
    40
  ],
  "judgment_reason": "같은 구성 물질의 표면장력 조건에서 반지름 증가→압력차 감소의 반비례 방향을 적용하는 것이④ 결정 연산. 합쳐진 부피의 수치 계산은 필요 없다.",
  "competing_codes": [
    {
      "code": 84,
      "verdict": "대체 표상",
      "reason": "압력차를 표면장력/반지름 꼴로 표현 가능하나 원문 반비례 방향만으로 충분. 분수식 전체와91의 전역 동일성은 주장 안 함"
    },
    {
      "code": 43,
      "verdict": "보조",
      "reason": "표면장력 조건이 달라지면 반지름만으로 압력차 방향 결정 불가. 이 사례는 같은 물질 조건을 유지"
    },
    {
      "code": 46,
      "verdict": "특정 오답 보조",
      "reason": "① 공기 이동에는 압력차→이동 경로가 관여하나④은 두 상태의 압력차 비교로 충분"
    },
    {
      "code": 92,
      "verdict": "주 기각",
      "reason": "숫자를 넣은 압력·부피 계산이 없고 방향만 판단"
    }
  ],
  "minimal_change_test": "반지름 증가를 유지해도 표면장력이 그보다 더 크게 증가하도록 전제를 바꾸면 감소 결론은 보장 안 됨. 반비례 적용의 고정 조건을 보존해야 함.",
  "sdss_seen": false,
  "confidence": 0.96,
  "quota_status": "unavailable"
}
```
