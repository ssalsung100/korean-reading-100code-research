

<!-- luna-raw:BPM-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G500",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2026/2026_answer_2026_LEET_언어이해_정답표.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "③은 각 모델에서 유권자가 비교하는 두 효용을 정확히 구분하여 대응한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BPM-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G500",
  "minimal_logic_without_codes": "첫 모델의 이념/민주주의 효용과 두번째 모델의 현재 정부 매력/미래 교체 능력을 각각 짝지어③을 수용한다.",
  "primary": [
    {
      "code": 88,
      "reason": "각 모델에서 교환되는 효용 두 항의 내용을 정확히 유지한다."
    }
  ],
  "auxiliary": [
    {
      "code": 39,
      "reason": "두 모델을 유권자의 비교 기준이라는 공통 축에서 비교한다."
    },
    {
      "code": 17,
      "reason": "현재 집권자·미래 도전자와 이념·매력·프리미엄의 역할을 교환하지 않는다."
    },
    {
      "code": 3,
      "reason": "현재 정부의 질과 미래 교체 가능성이라는 시점을 나눈다."
    },
    {
      "code": 75,
      "reason": "모델별 가정을 한쪽의 계산 구조로 통일하지 않는다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "득표와 감표의 차이라는 표현은 있지만③의 비교는 수치 계산이 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 85,
      "rejection": "효용 사이의 트레이드오프가 있다고 합이나 곱이 일정한 수학식이 주어진 것은 아니다."
    },
    {
      "code": 53,
      "rejection": "두 모델의 차이가 관측 차이를 설명한다는 실험 검증을 하는 것이 아니라 가정된 선택 항을 대응한다."
    },
    {
      "code": 70,
      "rejection": "동시에 모두 최대로 얻기 어려운 선택 구조는 있지만 논리적으로 두 대안만이 가능하며 반드시 하나를 포기해야 한다는 형식 딜레마를 새로 부여하지 않는다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
