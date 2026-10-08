

<!-- luna-raw:BKC-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G453",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2019/2019_answer_2019_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "빛과 전자의 관찰 매체는 다르지만 둘 다 산란된 파동을 모아 상을 얻으므로 ⑤가 공통 원리에 맞는다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_limit_preserved": "새로운 원문 제한 없음"
}
```


<!-- luna-raw:BKC-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G453",
  "minimal_logic_without_codes": "광학과 전자 현미경의 서로 다른 매체에 공통되는 산란 파동의 집속·상 형성 원리를 대응한다.",
  "primary": [
    {
      "code": 39,
      "reason": "비교 항목을 파동 산란과 상 형성으로 고정하여 두 장치의 공통점을 확인한다."
    }
  ],
  "auxiliary": [
    {
      "code": 45,
      "reason": "매체 종류의 차이에도 시료 산란→집속→상 형성이라는 입력·처리·출력 대응을 보존한다."
    },
    {
      "code": 49,
      "reason": "②④ 배제에서 기압·전하 축적 증가와 상의 왜곡·선명도 방향을 확인한다."
    },
    {
      "code": 2,
      "reason": "③은 한 점에 집속하기 어렵다는 성능 한계를 제거하고 실제 동일점 도달을 단정한다."
    }
  ],
  "surface": [
    {
      "code": 23,
      "reason": "공통점이라는 집합식 표현은 가능하나 39와 동일한 비교 행동을 중복 계수하지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 46,
      "rejection": "충돌·전하 축적의 인과는 오답 근거지만 정답의 직접 선택은 두 장치 공통 원리의 대응이다."
    },
    {
      "code": 23,
      "rejection": "교집합 표상으로 재기술할 수 있으나 새로운 집합 연산은 필요하지 않아 유일 주를 두 코드 사이에서 확정할 근거는 약하다."
    },
    {
      "code": 40,
      "rejection": "렌즈·검출기가 등장한다는 부품 목록만으로는 파동 매체의 공통성을 판정하지 못한다."
    }
  ],
  "boundary_note": "39는 작업 대표이며 23과의 전역 통합은 유보. 산란 파동 공통성과 검출 방식 동일성을 혼동하지 않는다.",
  "confidence": 0.91,
  "sdss_seen": false
}
```
