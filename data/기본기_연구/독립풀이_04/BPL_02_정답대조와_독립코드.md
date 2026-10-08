

<!-- luna-raw:BPL-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G500",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2026/2026_answer_2026_LEET_언어이해_정답표.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "두 역할 모두 서로 다른 결과의 득실을 고려하는 선택 상황에 놓일 수 있으므로②가 적절하다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BPL-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G500",
  "minimal_logic_without_codes": "유권자와 집권자 모두 선택에 따른 여러 효용과 손실을 비교하는 상황에 놓일 수 있다는 공통점을 읽는다.",
  "primary": [
    {
      "code": 88,
      "reason": "각 행위자가 얻는 이익과 감수하는 손실의 비교가 전략적 선택의 내용이다."
    }
  ],
  "auxiliary": [
    {
      "code": 39,
      "reason": "다른 역할의 행위자를 득실 비교라는 같은 축에서 비교한다."
    },
    {
      "code": 75,
      "reason": "민주주의의 내재적 가치와 도구적 교체 능력이라는 모델별 가정을 구분한다."
    },
    {
      "code": 17,
      "reason": "높은 매력의 집권자와 도전자, 지지 속 퇴행과 반대 속 퇴행을 바꾸지 않는다."
    },
    {
      "code": 2,
      "reason": "선택 상황에 직면할 수 있다는 가능성이지 모든 상황의 동일 선택을 뜻하지 않는다."
    }
  ],
  "surface": [
    {
      "code": 91,
      "reason": "첫 모델의 이념 거리 관계는 있지만②의 공통 요약에 정확 비례 계산이 필요하지 않다."
    }
  ],
  "competing_codes": [
    {
      "code": 79,
      "rejection": "민주적 가치가 소재여도 독자가 새로운 정치적 당위를 제안하는 것이 아니라 모델의 선택 구조를 읽는다."
    },
    {
      "code": 4,
      "rejection": "모든 모델에 내재적 가치를 공통 가정으로 확대하면 두번째 모델을 왜곡한다."
    },
    {
      "code": 90,
      "rejection": "선택 대안이 여럿이라는 것과 가능한 경우의 수를 계산하는 것은 다르다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
