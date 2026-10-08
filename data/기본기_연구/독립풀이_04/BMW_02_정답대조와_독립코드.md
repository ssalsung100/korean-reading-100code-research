

<!-- luna-raw:BMW-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G477",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2021/2021_answer_2021_LEET_언어이해_정답표_배포용.hwp",
  "minimal_logic_without_codes": "⑤의 비교값은 해당작용의 ATP2개와 NADH2개로 같으므로 전자가 더 많다는 주장이 틀리다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BMW-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G477",
  "minimal_logic_without_codes": "비교하는 두 수율은 각각 포도당1개당 해당작용 ATP2개와 NADH2개이므로 더 많다는⑤는 틀리다.",
  "primary": [
    {
      "code": 86,
      "reason": "동일 입력량을 기준으로 두 산물의 개수를 비교해 같은 값을 더 크다고 한 오류를 찾는다."
    }
  ],
  "auxiliary": [
    {
      "code": 92,
      "reason": "③의36/38-2=34/36과④의2+2×3=8을 계산한다."
    },
    {
      "code": 17,
      "reason": "세포질 직접ATP와 NADH의 미토콘드리아 전환ATP, 전체 산화수율을 서로 다른 범위로 유지한다."
    },
    {
      "code": 10,
      "reason": "①에서 미토콘드리아 기능이 해당 NADH-ATP 전환 경로에 필요한 조건임을 적용한다."
    }
  ],
  "surface": [
    {
      "code": 40,
      "reason": "전체 수율을 구성하는 항의 구분은 있지만⑤는 주어진 두 개수의 대소 비교다."
    }
  ],
  "competing_codes": [
    {
      "code": 84,
      "rejection": "분모가 다른 비율을 비교하는 것이 아니라 모두 포도당1개로 기준을 맞춘 두 수치다."
    },
    {
      "code": 49,
      "rejection": "조건 변화에 따른 두 변수의 방향을 묻지 않고 정해진 산물 수를 비교한다."
    },
    {
      "code": 45,
      "rejection": "전환 과정은 배경이며⑤의 직접 오류는 변환 구조가 아니라2와2를 부등관계로 놓은 것이다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
