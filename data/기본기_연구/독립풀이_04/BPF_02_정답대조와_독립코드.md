

<!-- luna-raw:BPF-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G498",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2026/2026_answer_2026_LEET_언어이해_정답표.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "④는 지구법학이 지리적 영역을 점하는 존재에도 권리 주체성을 인정한다는 본문 내용을 적용한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BPF-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G498",
  "minimal_logic_without_codes": "지구법학은 존재 자체에서 권리 주체성을 도출하므로 지리적 영역을 점하는 존재에도 권리를 인정한다.",
  "primary": [
    {
      "code": 12,
      "reason": "지구법학 내부의 존재 조건→권리 주체성이라는 규칙을④에 적용한다."
    }
  ],
  "auxiliary": [
    {
      "code": 83,
      "reason": "존재 사실에서 규범적 권리 결론을 얻는 논증이라는 층위를 확인한다."
    },
    {
      "code": 75,
      "reason": "인간중심적 전통과 지구법학의 권리 근거를 구별한다."
    },
    {
      "code": 17,
      "reason": "자연 보호의 목적이 인간의 이익인지 자연 자체의 권리인지 귀속한다."
    },
    {
      "code": 4,
      "reason": "권리를 널리 인정함과 모든 권리의 양태가 같음은 다르다."
    }
  ],
  "surface": [
    {
      "code": 81,
      "reason": "존재가 주제이지만④는 그 존재론의 참됨을 외부에서 입증하는 과제가 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 10,
      "rejection": "지리적 영역을 점하는 것만이 모든 권리의 필요조건이라는 역방향을 부여하지 않는다. 인간·새 등 다른 존재 방식도 있다."
    },
    {
      "code": 11,
      "rejection": "전체 권리론의 필요충분 정의가 명시된 것으로 확대하지 않는다."
    },
    {
      "code": 44,
      "rejection": "보전주의의 수단·목적과 지구법학의 권리 근거는 다르며④를 인간 이익의 도구적 보호로 읽지 않는다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
