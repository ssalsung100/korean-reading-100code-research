

<!-- luna-raw:BNA-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G478",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2024/2024_answer_2024언어이해정답.pdf",
  "minimal_logic_without_codes": "ㄱ과ㄷ은 사비니의 학문성 옹호와 해석 제안권에 맞고,ㄴ은 법률 바깥이라는 부분 관계를 법체계 바깥으로 확대하므로 틀리다.③이다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BNA-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G478",
  "minimal_logic_without_codes": "법체계가 법률과 규범적 교의를 함께 포함하므로 법률의 바깥에 있는 교의도 전체 체계의 안에 있을 수 있다.ㄴ의 전체 범위 확대를 배제한다.",
  "primary": [
    {
      "code": 40,
      "reason": "법체계 전체와 그 구성 요소인 법률·교의를 구분한다."
    }
  ],
  "auxiliary": [
    {
      "code": 42,
      "reason": "안과 밖의 기준 대상을 법률에서 법체계로 바꾸지 않는다."
    },
    {
      "code": 17,
      "reason": "법률 바깥이라는 속성을 법체계 바깥으로 옮긴 지시 범위 오류를 판독한다."
    },
    {
      "code": 97,
      "reason": "ㄷ의 해석 제안권을 왜 박탈해야 하느냐는 반문을 그 권한을 옹호하는 발화로 읽는다."
    }
  ],
  "surface": [
    {
      "code": 25,
      "reason": "두 구성 영역을 분류할 수 있지만 단순 명칭 분류보다 전체·부분의 관계가 결정적이다."
    }
  ],
  "competing_codes": [
    {
      "code": 29,
      "rejection": "집합 포함으로도 법률∪교의라는 전체를 표상할 수 있어40과 국소 중첩한다. 번호 차이를 별개 연산으로 세지 않는다."
    },
    {
      "code": 41,
      "rejection": "구성원의 속성을 전체에 옮기는 전형적 결합 오류보다는 부분의 외부를 전체의 외부로 확대하는 경계 오류다."
    },
    {
      "code": 13,
      "rejection": "법률 밖에 있으면서 법체계 안에 있는 것은 기준 범위가 달라 양립 가능하다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
