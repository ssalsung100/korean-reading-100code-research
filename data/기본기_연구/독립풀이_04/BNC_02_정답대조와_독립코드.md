

<!-- luna-raw:BNC-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G479",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2024/2024_answer_2024언어이해정답.pdf",
  "minimal_logic_without_codes": "같은 분류에서k만 바꿔 잔존율이 증가했다면 문턱을 낮춰 이전에 탈락한 더 작은 동질집합을 추가로 남긴 것이다.남아 있는 집합 크기의 최솟값은 낮아지므로⑤가 맞는다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BNC-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G479",
  "minimal_logic_without_codes": "전처리 집합을 고정하면k의 변화는 집합의 내부 크기를 바꾸지 않고 통과·삭제 여부만 바꾼다.잔존율의 엄격한 증가에는 더 작은 집합의 추가 통과가 필요하다.",
  "primary": [
    {
      "code": 45,
      "reason": "문턱k를 입력으로 받아 고정된 집합들을 필터링하는 과정과 그 산출 통계의 변화를 추적한다."
    }
  ],
  "auxiliary": [
    {
      "code": 43,
      "reason": "원본과 범주화·마스킹 및 그룹 구성을 고정하고k만 바뀌는 조건을 유지한다."
    },
    {
      "code": 49,
      "reason": "잔존율 증가와 새 최소 집합 크기 감소의 방향을 연결한다."
    },
    {
      "code": 86,
      "reason": "추가된 집합은 이전k보다 작아 기존에 남은 집합들의 최솟값보다도 작다는 대소 관계를 쓴다."
    },
    {
      "code": 17,
      "reason": "집합 전체의 삭제와 개별 집합 내부 레코드 삭제를 구분한다."
    }
  ],
  "surface": [
    {
      "code": 84,
      "reason": "잔존율은 분수지만 분모인 원본 레코드 수가 고정되어 분자 변화와 같은 방향이다."
    }
  ],
  "competing_codes": [
    {
      "code": 91,
      "rejection": "k와 최솟값·잔존율의 관계는 계단식일 수 있어 일정 비율의 정비례·반비례가 아니다."
    },
    {
      "code": 15,
      "rejection": "통과 기준 적용은 포함되지만⑤는 관측된 결과 증가에서 문턱 변화와 새 최솟값을 추적하는 단계까지 요구한다."
    },
    {
      "code": 85,
      "rejection": "남은 집합들 사이에 총합을 일정하게 나누는 경쟁 관계가 아니다.삭제에 따라 총 잔존수가 바뀐다."
    }
  ],
  "scope_limit": "기존 집합이 비어 있지 않아 최솟값이 정의되는 비교다.k를 낮추기만 하면 항상 잔존율이 엄격히 증가한다는 역명제는 주장하지 않는다.",
  "confidence": 0.94,
  "sdss_seen": false
}
```
