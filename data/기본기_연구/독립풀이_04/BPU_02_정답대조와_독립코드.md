

<!-- luna-raw:BPU-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G503",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2026/2026_answer_2026_LEET_언어이해_정답표.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "관측 기울기가0이 아니어도 역인과·누락요인·측정오차 가능성이 있어 원인 효과를 확정하지 못한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "scope_limit": "원 blind의 반비례 해석·기술 경로의 중요성·교란 설명의 방향에 관한 제한을 그대로 보존한다."
}
```


<!-- luna-raw:BPU-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G503",
  "minimal_logic_without_codes": "一緒に変わる証拠だけでは向きのある効果の証拠にならない。",
  "primary": [
    {
      "code": 49,
      "reason": "관측된 동반 변화와 인과 효과를 구별하는 것이④의 정오를 가른다."
    }
  ],
  "auxiliary": [
    {
      "code": 46,
      "reason": "확정하려는 대상은x 변화에 따른y의 원인 효과다."
    },
    {
      "code": 62,
      "reason": "0 아닌 기울기를 인과의 충분한 근거로 삼는 연결을 부정한다."
    },
    {
      "code": 47,
      "reason": "제3요인에 의한 관련성은 직접 인과 추론의 반례 후보 중 하나다."
    }
  ],
  "surface": [
    {
      "code": 87,
      "reason": "기울기의 수치 계산이나 변화율 비교가 아니라0 아닌 기울기의 증거 지위가 핵심이다."
    }
  ],
  "competing_codes": [
    {
      "code": 43,
      "rejection": "교란 배제는 해결 방법이지만④ 자체는 통제 실험을 실행하거나 통제 변수를 정하는 문제가 아니다."
    },
    {
      "code": 91,
      "rejection": "②의 반비례는 경향의 표현으로 읽으며 정확한 역비례 수식 도출이④ 판단의 요건이 아니다."
    },
    {
      "code": 54,
      "rejection": "일반 인과 효과의 식별 문제를 충분조건적 결정론 문제로 좁히지 않는다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false,
  "scope_limit": "공통원인은 가능한 실패 경로 중 하나다. 본문은 역인과와 측정오차도 별도로 들므로47 하나로 전체를 축소하지 않는다."
}
```


<!-- luna-raw:BPU-independent_code-20261004-02 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G503",
  "minimal_logic_without_codes": "두 변수가 함께 변한다는 증거만으로 한 변수의 변화가 다른 변수를 변화시킨다는 방향 있는 효과를 입증하지 못한다.",
  "primary": [
    {
      "code": 49,
      "reason": "관측된 동반 변화와 인과 효과를 구별하는 것이④의 정오를 가른다."
    }
  ],
  "auxiliary": [
    {
      "code": 46,
      "reason": "확정하려는 대상은x 변화에 따른y의 원인 효과다."
    },
    {
      "code": 62,
      "reason": "0 아닌 기울기를 인과의 충분한 근거로 삼는 연결을 부정한다."
    },
    {
      "code": 47,
      "reason": "제3요인에 의한 관련성은 직접 인과 추론의 반례 후보 중 하나다."
    }
  ],
  "surface": [
    {
      "code": 87,
      "reason": "기울기의 수치 계산이나 변화율 비교가 아니라0 아닌 기울기의 증거 지위가 핵심이다."
    }
  ],
  "competing_codes": [
    {
      "code": 43,
      "rejection": "교란 배제는 해결 방법이지만④ 자체는 통제 실험을 실행하거나 통제 변수를 정하는 문제가 아니다."
    },
    {
      "code": 91,
      "rejection": "②의 반비례는 경향의 표현으로 읽으며 정확한 역비례 수식 도출이④ 판단의 요건이 아니다."
    },
    {
      "code": 54,
      "rejection": "일반 인과 효과의 식별 문제를 충분조건적 결정론 문제로 좁히지 않는다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false,
  "scope_limit": "공통원인은 가능한 실패 경로 중 하나다. 본문은 역인과와 측정오차도 별도로 들므로47 하나로 전체를 축소하지 않는다.",
  "correction_of": "BPU-independent_code-20261004-01",
  "correction_reason": "최소 논리 구조 필드에 잘못 입력된 비한국어 문장을 한국어로 정정한다. 최초 raw는 불변 보존하며 코드 판정과 의미는 바꾸지 않는다."
}
```
