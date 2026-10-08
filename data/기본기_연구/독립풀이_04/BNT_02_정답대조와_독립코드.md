

<!-- luna-raw:BNT-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G485",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2024/2024_answer_2024언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "활성산소종의 작용 시간과 거리가 짧으므로 발생한 암세포에서 멀리 떨어진 정상세포에 대한 영향이 적다는④가 적절하다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "inference_limit_preserved": "기출 본문 모형에 한정"
}
```


<!-- luna-raw:BNT-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G485",
  "minimal_logic_without_codes": "활성산소종은 빨리 소멸하고 짧은 거리에서만 작용하므로 먼 정상세포에 대한 영향이 작다.",
  "primary": [
    {
      "code": 46,
      "reason": "수명·유효거리라는 물리적 작용 특성에서 공간적으로 제한된 손상 효과를 설명한다."
    }
  ],
  "auxiliary": [
    {
      "code": 45,
      "reason": "빛→감광제 활성→산소와 상호작용→세포 손상 경로의 입력·출력을 유지한다."
    },
    {
      "code": 17,
      "reason": "잔류 감광제 광손상·고농도 알레르기·항산화제 역할을 바꾸지 않는다."
    },
    {
      "code": 10,
      "reason": "빛·감광제·산소라는 필수 요건과 무광 저독성의 감광제 조건을 유지한다."
    }
  ],
  "surface": [
    {
      "code": 86,
      "reason": "반감기·유효거리 수치는 있으나 정확 계산 없이 작용 범위가 짧다는 근거로④를 판단한다."
    }
  ],
  "competing_codes": [
    {
      "code": 50,
      "rejection": "경로의 특정 지점을 인위적으로 차단하는 실험이 아니라 본래 유효거리의 한계를 적용한다."
    },
    {
      "code": 49,
      "rejection": "거리가 멀면 영향이 적다는 방향으로도 읽을 수 있지만 시간·거리의 작용 한계라는 설명 기제가 명시돼 있다.46과 국소 중첩 가능성을 보존한다."
    },
    {
      "code": 91,
      "rejection": "거리와 손상 정도 사이 정비례·반비례 법칙은 주어지지 않았다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false
}
```
