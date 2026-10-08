

<!-- luna-raw:BOV-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G494",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2025/2025_answer_2025언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "①은3개 상한과 이식 예정 수량에 맞춘 수정 제한을 결합해 재진술한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BOV-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G494",
  "minimal_logic_without_codes": "한 주기의 수정·이식에는3개 상한이 있고 이식 예정 수보다 많이 수정할 수 없다.①은 이 제약들을 결합한다.",
  "primary": [
    {
      "code": 12,
      "reason": "주기·수량·예정 이식 수라는 규칙의 결합 조건을 적용한다."
    }
  ],
  "auxiliary": [
    {
      "code": 86,
      "reason": "최대3과 이식 예정 수 이하라는 두 수량 제한을 함께 유지한다."
    },
    {
      "code": 3,
      "reason": "착상 전 채취 제한을 착상 후 제거에 그대로 옮기지 않는다."
    },
    {
      "code": 24,
      "reason": "결함 배아 배제라는 예외를⑤의 어떤 경우에도라는 전칭에서 보존한다."
    },
    {
      "code": 17,
      "reason": "난자 채취와 난자 수정, 배아 이식을 구분한다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "수량은 있지만 실제 산술보다 상한·범위 판독이 중심이다."
    }
  ],
  "competing_codes": [
    {
      "code": 21,
      "rejection": "열거된 일부 요건을 충족하면 모든 법적 허용이 필요충분하게 결정된다는 정의를 새로 부여하지 않는다."
    },
    {
      "code": 4,
      "rejection": "⑤의 전칭 강화에는 작동하나①의 직접 수용은 여러 제한을 결합한 조건 적용이다."
    },
    {
      "code": 85,
      "rejection": "수정 수와 이식 수를 합계 일정의 경쟁 몫으로 읽지 않는다. 동일 과정의 상한 및 대응 조건이다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
