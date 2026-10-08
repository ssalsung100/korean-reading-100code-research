

<!-- luna-raw:BRD-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G514",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/표/2018/2018_answer/table_001.md 홀수형13~15(공식 HWP 추출 표)",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "동등성의 비교축을 법적 권리에서 사회적 지위로 바꾸면 명시적 차이를 지운다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BRD-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G514",
  "sdss_seen": false,
  "primary": [
    {
      "code": 39,
      "reason": "법적 권리와 사회적 지위라는 비교축을 구별해②의 동등성 귀속을 배제한다."
    }
  ],
  "auxiliary": [
    {
      "code": 16,
      "reason": "권리와 지위의 개념을 동일시하지 않는다."
    },
    {
      "code": 9,
      "reason": "가족·시민사회·국가의 자유 실현 수준 차이를④에서 확인한다."
    }
  ],
  "surface": [
    {
      "code": 4,
      "reason": "모든 구성원이라는 표현이 있지만 오류는 대상 범위보다 동등하다는 성질의 비교축이다."
    }
  ],
  "competing_codes": [
    {
      "code": 86,
      "rejection": "동등이라는 말만으로 양적 수치 비교라 할 수 없다.법적 권리 동등은 수량 없이 제시된다."
    },
    {
      "code": 13,
      "rejection": "법적 권리 동등과 사회적 지위 차이는 양립하므로 양립불가 판정이 아니다."
    },
    {
      "code": 82,
      "rejection": "세 단계가 있다는 이유만으로 정반합 추론을 필요 연산으로 만들지 않는다."
    }
  ],
  "confidence": 0.95,
  "scope_limit": "39/16은 비교축 식별과 개념 구분으로 같은 결정 구간에서 중첩한다."
}
```
