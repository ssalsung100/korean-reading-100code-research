

<!-- luna-raw:BMS-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G476",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2021/2021_answer_2021_LEET_언어이해_정답표_배포용.hwp",
  "minimal_logic_without_codes": "정치제도 변화가 성장의 선행조건이라는 주장은 애쓰모글루에게 제시된 것이며 제도를 중시하는 모든 학자에게 일반화할 수 없으므로③이 틀리다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BMS-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G476",
  "minimal_logic_without_codes": "제도를 중시하는 학자들 중 특정인에게만 제시된 정치제도 선행조건을 그 부류 전체의 공통 주장으로 넓힌③을 배제한다.",
  "primary": [
    {
      "code": 4,
      "reason": "일부 구성원의 주장을 모든 제도 중시 학자에게 일반화한 범위 확대다."
    }
  ],
  "auxiliary": [
    {
      "code": 75,
      "reason": "이스털리·애쓰모글루·로머·콜리어의 각각 다른 처방을 귀속한다."
    },
    {
      "code": 10,
      "reason": "정치제도 변화라는 필요조건이 어느 입장에 속하는지 범위를 유지한다."
    },
    {
      "code": 25,
      "reason": "지리/제도라는 큰 분류 안에도 서로 다른 하위 입장이 있음을 보존한다."
    }
  ],
  "surface": [
    {
      "code": 43,
      "reason": "마지막 입장의 통제 비교는 지문에 있으나③의 직접 판단은 견해 범위의 확대다."
    }
  ],
  "competing_codes": [
    {
      "code": 13,
      "rejection": "다른 원인 설명을 가진 학자도 특정 지원 필요나 수요 고려에 동의할 수 있으므로 모든 논점에서 배타로 두지 않는다."
    },
    {
      "code": 59,
      "rejection": "처방의 실효성을 새로 평가하는 것보다 어느 학자가 어떤 처방을 주장했는지 확인한다."
    },
    {
      "code": 74,
      "rejection": "가설 간 대체 설명은 배경이지만③의 오류는 새로운 증거 배분이 아닌 부분 주장 일반화다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
