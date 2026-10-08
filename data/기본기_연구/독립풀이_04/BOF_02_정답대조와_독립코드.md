

<!-- luna-raw:BOF-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G489",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2025/2025_answer_2025언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "④는 흡혈귀 공통 증세의 질환을 선천성 조혈기성에서 혼합 포르피린증으로 바꾸어 귀속한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "confidence_after_check": 0.99,
  "remaining_uncertainty": "추가 없음",
  "source_restoration_before_disclosure": false
}
```


<!-- luna-raw:BOF-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G489",
  "minimal_logic_without_codes": "흡혈귀 공통 증세의 선천성 조혈기성 질환과 조지3세에게 가설로 제기된 혼합 질환을 바꾸어 귀속한④를 배제한다.",
  "primary": [
    {
      "code": 17,
      "reason": "같은 포르피린증 상위 이름 안에서 특정 증상이 어느 하위 질환에 귀속되는지 유지한다."
    }
  ],
  "auxiliary": [
    {
      "code": 25,
      "reason": "결함 효소가 다른 포르피린증 하위 종류를 분류한다."
    },
    {
      "code": 45,
      "reason": "유로포르피리노젠I의 발생과 그 다음 효소를 통한 원인물질 생성의 단계를 구별한다."
    },
    {
      "code": 46,
      "reason": "앞 단계 효소 결함의 결과와 뒷 단계 효소 정상 작용의 결과를 나눈다."
    }
  ],
  "surface": [
    {
      "code": 19,
      "reason": "헴 보철그룹의 기능 보완 설명은 있지만④의 결정 행동은 질환 귀속이다."
    }
  ],
  "competing_codes": [
    {
      "code": 4,
      "rejection": "하위 질환의 증상을 상위 포르피린증 전부에 확대하는 범위 오류로도 기술할 수 있으나④는 특정 하위 종류를 다른 종류로 교환한다."
    },
    {
      "code": 13,
      "rejection": "서로 다른 종류라는 사실만으로 현실의 동시 발병이나 모든 증상의 공유 불가능을 주장하지 않는다."
    },
    {
      "code": 40,
      "rejection": "헤모글로빈 안의 헴 구성 관계는 배경이며④의 하위 질환은 한 질환의 물리적 구성 부분이 아니다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
