

<!-- luna-raw:BRS-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G522",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/표/2009/2009_answer/table_001.md Q17~19, 공식 HWP 추출표",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "홍조와 금빛이라는 두 결과에서 사랑하는 한수를 공통 원인 대상으로 찾고 그를 등불로 비유한㉢에 대응한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BRS-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G522",
  "sdss_seen": false,
  "primary": [
    {
      "code": 47,
      "reason": "홍조·금빛이라는 두 결과의 공통 원인인 사랑하는 한수/그를 떠올림을 추적한다."
    }
  ],
  "auxiliary": [
    {
      "code": 100,
      "reason": "확인한 원인 대상을 비유한 표현인 등불㉢을 고른다."
    },
    {
      "code": 46,
      "reason": "대상 회상→내면 밝음→몸의 홍조·금빛이라는 인과 경로를 유지한다."
    }
  ],
  "surface": [
    {
      "code": 49,
      "reason": "두 현상이 같이 나타나지만 공변 통계로 공통 원인을 추정한 것은 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 48,
      "rejection": "두 원인이 한 결과로 모인 것이 아니라 같은 동인이 둘 이상의 표현을 낳는다."
    },
    {
      "code": 99,
      "rejection": "단순지시어의선행사찾기가아니라원인확인후비유대응이라는두관계가필요하다."
    },
    {
      "code": 39,
      "rejection": "두결과의공통외관을비교하는것만으로그공통원인표현을찾지못한다."
    }
  ],
  "confidence": 0.96,
  "scope_limit": "47과100은 원인 대상 발견과 그 대상의 비유 식별이라는 두 필수 층위.주체의 사랑을 한수의 객관적 인격으로 바꾸지 않는다."
}
```
