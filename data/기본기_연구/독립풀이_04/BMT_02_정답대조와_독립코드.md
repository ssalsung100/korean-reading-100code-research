

<!-- luna-raw:BMT-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G476",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2021/2021_answer_2021_LEET_언어이해_정답표_배포용.hwp",
  "minimal_logic_without_codes": "정책 전체에 대한 입장은 달라도 가난한 사람의 수요를 고려해야 한다는 점에서는 이스털리와 배너지·뒤플로가 일치하므로②가 맞는다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BMT-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G476",
  "minimal_logic_without_codes": "정책·지원에 관한 전반적 입장이 달라도 가난한 사람의 수요를 중시한다는 비교 항목에서 두 입장이 일치한다.",
  "primary": [
    {
      "code": 39,
      "reason": "비교 축을 수요의 고려 여부로 고정해②의 국소 공통점을 확인한다."
    }
  ],
  "auxiliary": [
    {
      "code": 75,
      "reason": "정책 우선성·외국 개입·부패에 대한 견해를 다른 학자에게 옮기지 않는다."
    },
    {
      "code": 17,
      "reason": "한 비교 항목의 일치를 전체 정책론의 동일성과 구분한다."
    },
    {
      "code": 14,
      "reason": "정부 지원에 대한 다른 태도와 수요 중시의 공통성은 함께 성립할 수 있다."
    }
  ],
  "surface": [
    {
      "code": 43,
      "reason": "배너지·뒤플로의 통제 비교 방법은 제시돼 있으나②를 선택하는 직접 관계는 수요의 공통점이다."
    }
  ],
  "competing_codes": [
    {
      "code": 23,
      "rejection": "공통점을 교집합으로 재기술할 수 있어39와 같은 행동에 중첩한다. 별도 필수 집합 연산으로 세지 않는다."
    },
    {
      "code": 74,
      "rejection": "관측 결과를 통해 이론의 예측을 경쟁시키는 검증 단계가 아니다."
    },
    {
      "code": 58,
      "rejection": "수요 중시라는 공통 요소를 모든 주장의 공통 전제라고 확대하지 않는다. 서로 다른 처방이 남아 있다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false
}
```
