

<!-- luna-raw:BKQ-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G458",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2019/2019_answer_2019_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "④는 상위 개념과 하위 개념 사이의 상속 관계를 개념과 소속 개체 사이에 옮긴다.두 관계의 항목 유형이 다르므로 부적절하다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BKQ-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G458",
  "minimal_logic_without_codes": "개념-개체의 소속 관계와 상위 개념-하위 개념의 상속 관계는 양 끝의 대상 유형이 다르다.④는 이를 교환한다.",
  "primary": [
    {
      "code": 38,
      "reason": "구체 개체가 개념 집합에 속하는 관계를 개념 사이의 계층 관계와 구분한다."
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "상속 관계의 양 끝이 개념인지 개체인지 대상 범주를 고정한다.38과 국소 중첩."
    },
    {
      "code": 22,
      "reason": "하위 개념이 상위 개념의 속성을 물려받는 본문의 상속 정의를 유지한다."
    },
    {
      "code": 16,
      "reason": "개념·개체·상속의 정의를 각 선지에 적용한다."
    }
  ],
  "surface": [
    {
      "code": 31,
      "reason": "개체와 집합의 수를 세는 것이 아니므로 별칭의 유사성만으로 수량 혼동으로 기록하지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 25,
      "rejection": "전체는 분류 구조지만④의 구체 오류는 분류 항목 간 상하 관계를 소속 관계와 바꾸는 유형 오류다."
    },
    {
      "code": 40,
      "rejection": "개체 소속을 부분-전체로 읽지 않는다.본문은 부분-전체 관계를 상속과 별도로 제시한다."
    },
    {
      "code": 17,
      "rejection": "38과 같은 국소 판독을 포괄하므로 유일 주 분리는 유보한다.38은 개체/개념 관계를 드러내는 작업 대표."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false
}
```
