

<!-- luna-raw:BRI-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G517",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "data/meet_answer_keys.json keys.2007.29/30; status=official_verified, 공식2007언어추론정답표.hwp table1 추출·odd_or_single",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "일상 결정이 눈에 드러나지 않는 구조의 영향으로 이루어진다는 구속성이다.조정 가능성 제한을 절대 불가능이나 운명으로 강화하지 않는다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "verification_scope": "공식 HWP에서 검증 추출된 정답key를 대조.이번 원HWP 재렌더링 검증은 하지 않음."
}
```


<!-- luna-raw:BRI-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G517",
  "sdss_seen": false,
  "primary": [
    {
      "code": 100,
      "reason": "등 뒤라는 공간 비유를 보이지 않는 구조의 일상 구속이라는 추상 의미로 복원한다."
    }
  ],
  "auxiliary": [
    {
      "code": 2,
      "reason": "조정 가능성의 극단적 제한을 절대적 저항 불가로 강화하지 않는다."
    },
    {
      "code": 46,
      "reason": "기술·사회구조가 일상에 작용하는 방향을 문맥 근거로 삼는다."
    }
  ],
  "surface": [
    {
      "code": 42,
      "reason": "등 뒤라는 위치가 있으나 실제 내부/외부 공간 소속 문제는 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 99,
      "rejection": "특정 앞말을 지시하는 대용표현 찾기에 그치지 않고 구속이 작동하는 양식을 비유로 해석해야 한다."
    },
    {
      "code": 80,
      "rejection": "감지 여부가 의미 일부지만 주된 요구는 표현의 함축 복원이다."
    },
    {
      "code": 54,
      "rejection": "구조의 제약을 모든 행위를 충분하게 결정하는 단일 원인으로 확대하면 자율의 제한적 여지를 지운다."
    }
  ],
  "confidence": 0.95
}
```
