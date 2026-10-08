

<!-- luna-raw:BNB-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G479",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2024/2024_answer_2024언어이해정답.pdf",
  "minimal_logic_without_codes": "②는 식별자·준식별자의 처리 방법을 민감속성에 옮기므로 본문의 모형과 일치하지 않는다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BNB-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G479",
  "minimal_logic_without_codes": "식별자·준식별자에 적용하는 마스킹·범주화를 민감속성에 그대로 옮긴②를 배제한다.",
  "primary": [
    {
      "code": 17,
      "reason": "처리 기법이 적용되는 속성의 종류를 구분한다."
    }
  ],
  "auxiliary": [
    {
      "code": 45,
      "reason": "준식별자 값의 변환과 민감값 다양성 검사에 따른 집합 삭제라는 다른 처리를 나눈다."
    },
    {
      "code": 16,
      "reason": "식별자·준식별자·민감속성의 본문 정의를 각 선지에 적용한다."
    },
    {
      "code": 40,
      "reason": "데이터 집합·레코드·속성이라는 구성 층위를 유지한다."
    }
  ],
  "surface": [
    {
      "code": 49,
      "reason": "③의 유사도와 식별 가능성 방향은 다른 선지의 근거이나②는 적용 대상 교환이다."
    }
  ],
  "competing_codes": [
    {
      "code": 4,
      "rejection": "모든 속성에 같은 처리를 한다는 일반화로도 표현 가능하지만 구체 오류는 서로 다른 속성 유형과 작업의 혼동이다."
    },
    {
      "code": 19,
      "rejection": "민감정보 유출 문제를 보완한다는 목적이 곧 모든 속성에 같은 변환을 추가한다는 뜻은 아니다."
    },
    {
      "code": 25,
      "rejection": "속성 분류 자체보다 분류별 처리의 연결이 결정적이다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
