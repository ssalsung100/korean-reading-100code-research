

<!-- luna-raw:BOC-answer_check-20261003-01 -->
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
  "minimal_logic_without_codes": "②는 뉴게이트소설이 맞섰던 범죄 담론을 오히려 강화했다고 뒤집고 새커리의 개인 병증 관점을 그 장르 전체에 옮긴다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BOC-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G488",
  "minimal_logic_without_codes": "뉴게이트소설이 대항했던 지배 담론을 오히려 강화했다고 쓰고, 새커리의 개인 병증 설명을 앞선 작가들의 사회경제적 원인 설명으로 바꾸어 귀속한②를 배제한다.",
  "primary": [
    {
      "code": 17,
      "reason": "개인 병증·타고난 악함이라는 설명을 어느 작가·문학 흐름에 귀속하는지 유지한다."
    }
  ],
  "auxiliary": [
    {
      "code": 75,
      "reason": "사회경제적 원인과 개인적 병증·악함이라는 경쟁 관점을 비교한다."
    },
    {
      "code": 63,
      "reason": "대항 담론과 지배 담론의 강화라는 반대 관계를 구분한다."
    },
    {
      "code": 46,
      "reason": "① 개혁운동→소설→개혁 촉진이라는 시간 단계별 상호작용을 유지한다."
    },
    {
      "code": 78,
      "reason": "⑤ 생존 압박과 개인 통제력이라는 인물 행동 설명을 나눈다."
    }
  ],
  "surface": [
    {
      "code": 55,
      "reason": "②가 틀린 인과 설명이라고 볼 수 있지만 외부 현실의 실제 범죄 원인을 새로 검증하는 문제가 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 18,
      "rejection": "개혁운동이 계기이자 성과라는 것은 동일 시점의 명제 모순이 아니라 시간 단계가 다른 순환적 상호작용이다."
    },
    {
      "code": 4,
      "rejection": "일부 작가 관점을 전체로 확대하는 범위 기술도 가능하나 구체적으로 어떤 흐름과 관점을 뒤바꿨는지 보존해야 한다."
    },
    {
      "code": 74,
      "rejection": "가설 검증의 예측 차이를 새 자료와 대조하기보다 서술된 작가별 원인관을 귀속한다.75와 전역 분리를 강제하지 않는다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false
}
```
