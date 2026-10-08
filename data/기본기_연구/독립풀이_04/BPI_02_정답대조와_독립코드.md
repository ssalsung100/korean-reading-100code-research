

<!-- luna-raw:BPI-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G499",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2026/2026_answer_2026_LEET_언어이해_정답표.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "②는 의사결정 로직을 애플리케이션과 분리하면 구현·유지보수가 쉬워진다는 효과를 재진술한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BPI-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G499",
  "minimal_logic_without_codes": "코드 안의 규칙 혼재와 변경 지연이라는 문제를 로직의 분리·명시적 모델링으로 줄인다는②를 수용한다.",
  "primary": [
    {
      "code": 59,
      "reason": "기존 방식의 가시성·유지보수 문제와 DMN의 해결 수단을 대응한다."
    }
  ],
  "auxiliary": [
    {
      "code": 44,
      "reason": "로직 분리는 업무 담당자의 빠른 규칙 변경을 위한 수단이다."
    },
    {
      "code": 17,
      "reason": "규칙 모델 변경과 애플리케이션 코드 변경을 구분한다."
    },
    {
      "code": 45,
      "reason": "BPMN이 DMN 테이블을 호출하는 방향을 유지한다."
    },
    {
      "code": 16,
      "reason": "전략적 의사결정과 운영 의사결정의 적용 범위를 나눈다."
    }
  ],
  "surface": [
    {
      "code": 19,
      "reason": "BPMN의 한계를 별도 표준이 보완하는 구조는 있으나②는 구현·유지보수의 문제 해결을 직접 재진술한다."
    }
  ],
  "competing_codes": [
    {
      "code": 46,
      "rejection": "모형 분리의 효과는 원문에 제시됐지만 실제 생산성을 새로 계측한 인과 실험은 아니다.59의 문제-대응을 대표로 삼았다."
    },
    {
      "code": 20,
      "rejection": "DMN이 BPMN의 모든 기능을 대체해 불필요하게 만든다는 주장은 없다. 두 표준은 연동된다."
    },
    {
      "code": 4,
      "rejection": "중요한 의사결정이면 모두 자동화할 수 있다는 범위 확대를 허용하지 않는다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
