

<!-- luna-raw:BPC-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G497",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2025/2025_answer_2025언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "볼거리는 플롯과 함께 비극의 요소이지 플롯의 구성 부분으로 제시된 것이 아니다.③은 같은 전체에 속하는 두 요소를 부분-전체로 바꾼다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "confidence_after_check": 0.99,
  "remaining_uncertainty": "추가 없음"
}
```


<!-- luna-raw:BPC-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G497",
  "minimal_logic_without_codes": "플롯과 볼거리는 비극이라는 전체의 다른 요소인데③은 볼거리를 플롯의 부분으로 바꾼다.",
  "primary": [
    {
      "code": 40,
      "reason": "같은 전체에 속한 동위 요소 사이에 없는 부분-전체 관계를 삽입한 오류다."
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "볼거리가 비극에 귀속됨과 플롯에 귀속됨을 구분한다."
    },
    {
      "code": 75,
      "reason": "아리스토텔레스·아르토·바르트의 관점을 유지한다."
    },
    {
      "code": 16,
      "reason": "연극성·창작술·플롯이라는 개념 범위를 나눈다."
    }
  ],
  "surface": [
    {
      "code": 9,
      "reason": "희곡과 공연의 위계가 지문 주제지만③은 그 우선순위보다 구성 단위의 혼동이다."
    }
  ],
  "competing_codes": [
    {
      "code": 29,
      "rejection": "집합 포함으로 표상할 수 있어도 비극의 구성요소라는 원문 관계를 먼저 보존한다. 개념 외연 포함과 물리·기능적 구성의 전역 동치를 주장하지 않는다."
    },
    {
      "code": 41,
      "rejection": "부분의 속성을 전체에 합산한 오류가 아니라 동위 부분을 다른 부분 내부로 옮긴 경우다."
    },
    {
      "code": 13,
      "rejection": "플롯과 볼거리가 다르다는 것만으로 함께 존재할 수 없는 요소가 되는 것은 아니다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
