

<!-- luna-raw:AHJ-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G205",
  "blind_answer": 3,
  "official_answer": 3,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "점도와 표면장력을 유지하고 밀도×지름을 2×1/2로 바꾸면 곱이 보존된다. 오네소르게 수를 결정하는 값들이 보존되어③이 참이다.",
  "official_answer_source": "canonical answer field 기계 연결; 공식 정답표 직접 검증 아님",
  "barrier_verified": "G205 전체 blind4 저장 후 answer필드만 공개; SDSS 미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AHJ-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G205",
  "primary": [
    85
  ],
  "auxiliary": [
    45,
    43,
    15
  ],
  "surface": [
    91
  ],
  "judgment_reason": "정답③은 밀도×노즐지름에서 두 배와 절반이 상쇄하여 곱이 일정함을 확인한다. 점도·표면장력도 유지되어 오네소르게 수 불변.85의 곱 일정 작업 대표를 사용한다.",
  "competing_codes": [
    {
      "code": 45,
      "verdict": "보조",
      "reason": "개별입력이 달라도 결정에 쓰이는 결합값이 같으면 출력 동일. 곱 불변을 확인하는 단계와 연결"
    },
    {
      "code": 43,
      "verdict": "보조",
      "reason": "점도와 표면장력을 유지했다는 조건은 상쇄 효과 해석에 필요하나 바뀐 두 변수의 곱 계산을 대체하지 않음"
    },
    {
      "code": 91,
      "verdict": "주 기각",
      "reason": "본문은 곱이 클수록 수가 작다라고 했을 뿐 정확한 역비례 거듭제곱을 주지 않음.③은 곱 자체가 같아 정확 수식 없이 성립"
    },
    {
      "code": 92,
      "verdict": "상위 기술",
      "reason": "2×1/2의 간단 계산으로도 기술 가능하나85의 곱 일정이라는 더 구체적 연산을 대표로 삼음. 배타적 코드 분리를 주장하지 않음"
    }
  ],
  "minimal_change_test": "밀도2배·지름1/2 대신 둘 다2배라면 곱 불변이 깨진다. 오네소르게 수의 정확 분모 지수는 몰라도 원래③의 불변 결론은 유지된다.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
