

<!-- luna-raw:BKR-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G458",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2019/2019_answer_2019_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "ㄱ은 한 온톨로지를 공통으로 표현 가능하다고 언어 전체 표현력이 같을 필요는 없어 거짓.ㄴ의 모든 빵은 장미는 빵이 하위·장미가 상위인데 뒤집어 거짓.ㄷ은 계산 보장보다 최대 표현력을 원하면Full을 선택하므로 참.따라서③.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BKR-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G458",
  "minimal_logic_without_codes": "빵이면 장미라는 조건은 빵 집합이 장미 집합에 포함됨을 뜻한다.공통 온톨로지 표현 가능성은 언어 전체 표현력 동등을 필요로 하지 않으며,표현력 최대화를 원하면Full을 택한다.",
  "primary": [
    {
      "code": 12,
      "reason": "ㄴ에서 모든 x에 대해 빵(x)→장미(x)의 포함 방향과 상속 방향을 맞춘다."
    }
  ],
  "auxiliary": [
    {
      "code": 29,
      "reason": "Lite의 표현 가능 집합은DL·Full에 포함되므로 공통 표현 가능성을 동등 집합으로 바꾸지 않는다."
    },
    {
      "code": 10,
      "reason": "ㄱ은 특정 온톨로지의 공통 표현에 전체 언어 표현력 동등을 필요조건으로 잘못 부과한다."
    },
    {
      "code": 88,
      "reason": "ㄷ은 계산 보장보다 표현력 최대화를 우선하는 사용자의 선택 조건에 맞춘다."
    }
  ],
  "surface": [
    {
      "code": 4,
      "reason": "ㄴ의 모든이 전칭 포함을 나타내지만 오류는 수량 강도보다 상하 방향의 역전이다."
    }
  ],
  "competing_codes": [
    {
      "code": 11,
      "rejection": "빵이면 장미에서 역까지 보장하지 않는다.동일성·동치 관계로 강화할 수 없다."
    },
    {
      "code": 27,
      "rejection": "개념 외연-내포의 경쟁을 직접 계산하지 않는다.언어가 표현하는 문장 집합의 포함과 개념 간 포함 방향이 핵심이다."
    },
    {
      "code": 2,
      "rejection": "Full에 계산 보장이 없다는 것이 실패 필연이라는 뜻은 아니며 양상 구분은 보조가 될 수 있으나ㄴ의 핵심 방향 오류를 대체하지 않는다."
    }
  ],
  "boundary_note": "서로 다른 표현력의 언어도 같은 단순 온톨로지를 표현할 수 있다는Lite/Full 반모형을 유지한다.본문 OWL 버전 설명을 현재 기술 사양으로 일반화하지 않는다.",
  "confidence": 0.93,
  "sdss_seen": false
}
```
