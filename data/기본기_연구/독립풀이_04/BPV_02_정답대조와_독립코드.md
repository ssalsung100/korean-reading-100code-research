

<!-- luna-raw:BPV-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G503",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2026/2026_answer_2026_LEET_언어이해_정답표.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "사망률→이주→기술→소득의 제도 밖 경로를 중요한 것으로 인정하면 사용한 도구변수의 배제 조건에 충돌한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "scope_limit": "원 blind의 반비례 해석·기술 경로의 중요성·교란 설명의 방향에 관한 제한을 그대로 보존한다."
}
```


<!-- luna-raw:BPV-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G503",
  "minimal_logic_without_codes": "선택한 지표가 제도를 거치지 않고 기술 진보를 통해 소득과 연결된다면 그 지표로 제도의 효과만 분리할 수 없다. 저자는 그러한 경로를 중요하게 인정하지 않을 것이다.",
  "primary": [
    {
      "code": 10,
      "reason": "유효한 도구변수의 필요조건인 제도 외 경로와의 무관성을⑤의 가상 경로에 적용한다."
    }
  ],
  "auxiliary": [
    {
      "code": 46,
      "reason": "사망률→이주→기술→소득이라는 대안 경로가 제도를 거치는 경로와 다른지 추적한다."
    },
    {
      "code": 43,
      "reason": "다른 영향 요인을 배제해야 제도 효과를 식별한다는 통제 목적을 확인한다."
    },
    {
      "code": 63,
      "reason": "대안 경로가 인정되면 제시 증거의 설득력이 약해지는 방향을 검사한다."
    }
  ],
  "surface": [
    {
      "code": 68,
      "reason": "끝 문단이 비판과 재반박 형식이나⑤는 재반론 문장의 강도 자체보다 도구변수 요건을 묻는다."
    }
  ],
  "competing_codes": [
    {
      "code": 50,
      "rejection": "이미 차단된 경로에서 효과가 멈추는 상황이 아니라 제외해야 할 우회 경로의 유무를 평가한다.경로 표상은 겹칠 수 있으나 같은 연산으로 확정하지 않는다."
    },
    {
      "code": 54,
      "rejection": "③은 지속적 영향을 완전 결정으로 과장한 오답이다.⑤는 기술 진보가 소득을 반드시 결정한다는 주장이 아니다."
    },
    {
      "code": 47,
      "rejection": "핵심은 도구변수에서 결과로 가는 제도 밖 경로의 배제다. 제3의 공통원인이 반드시 있어야만 조건이 깨지는 것은 아니다."
    }
  ],
  "confidence": 0.93,
  "sdss_seen": false,
  "scope_limit": "10과43의 주/보조는 중첩 여지가 있다. 필요조건 위반을 판정하는 단계와 그 조건을 두는 인과식별 목적을 구분해 보존한다."
}
```
