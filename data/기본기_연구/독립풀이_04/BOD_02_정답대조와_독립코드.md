

<!-- luna-raw:BOD-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G488",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2025/2025_answer_2025언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "㉡은 살아남기 위한 선택의 맥락이지 기존 계급적 역할에 순응해야 하는 운명이 아니다.②가 생존을 위한 범법과 계급 순응을 바꾼다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BOD-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G488",
  "minimal_logic_without_codes": "자연의 제일법칙은 생존의 막다른 상황에서 살아남기 위해 선택하는 맥락이다. 기존 계급 역할에 순응하는 운명이라는②의 뜻풀이로 바꿀 수 없다.",
  "primary": [
    {
      "code": 16,
      "reason": "추상적 표현의 문맥상 의미를 주변의 생존 압박·교수형 서술로 복원한다."
    }
  ],
  "auxiliary": [
    {
      "code": 78,
      "reason": "범죄 선택의 동기를 생존이라는 필요에서 이해한다."
    },
    {
      "code": 100,
      "reason": "피에 굶주림·공범자·봉쇄 등 비유 표현을 실제 법률적 주체나 물리적 행위로 오독하지 않는다."
    },
    {
      "code": 44,
      "reason": "⑤의 감정이입 차단이라는 작가의 목적과 실제 독자 반응을 나눈다."
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "법칙이라는 단어가 있지만②의 생존 맥락을 기존 법질서 순응의 당위로 읽으면 안 된다."
    }
  ],
  "competing_codes": [
    {
      "code": 97,
      "rejection": "글쓴이의 표현 의도도 관련되지만 이 문항의 직접 행동은 지시 표현의 뜻풀이와 문맥 대응이다.16과의 배타 경계는 주장하지 않는다."
    },
    {
      "code": 99,
      "rejection": "지시어가 가리키는 명사 하나를 찾는 수준을 넘어 비유적·추상적 표현의 의미를 복원해야 한다."
    },
    {
      "code": 8,
      "rejection": "사회적 위계에서 우선할 지위를 묻는 것이 아니며 생존 동기를 계급 순응 원칙으로 바꾸지 않는다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false
}
```
