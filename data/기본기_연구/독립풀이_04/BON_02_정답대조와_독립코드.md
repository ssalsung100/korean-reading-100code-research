

<!-- luna-raw:BON-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G491",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2025/2025_answer_2025언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "(가)의 법 개정 반대 증가60→80은 위헌 판결과 같은 방향이다. 법 개정에 반대한다고 위헌 결정에 반발한 것이 아니므로②가 틀리다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BON-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G491",
  "minimal_logic_without_codes": "위헌 판결 뒤 개정법 반대가60에서80으로 늘어난 것은 판결과 같은 방향의 변화다. 개정법에 반대하는 대중을 법원 결정에 반발한 대중으로 바꾼②를 배제한다.",
  "primary": [
    {
      "code": 17,
      "reason": "반대의 대상이 개정법인지 그 법을 무효화한 판결인지 구별한다."
    }
  ],
  "auxiliary": [
    {
      "code": 15,
      "reason": "관측된 여론 변화 패턴을 네 모델의 기준과 대조한다."
    },
    {
      "code": 86,
      "reason": "찬반·모름 비율 및 결정 전후 변화의 크기를 비교한다."
    },
    {
      "code": 3,
      "reason": "입법 전·입법 후·판결 후의 시점을 구분한다."
    },
    {
      "code": 49,
      "reason": "국기법 보도 증가와 모름 비율 감소의 같은 시기 변화를 읽되 인과 확정으로 확대하지 않는다."
    }
  ],
  "surface": [
    {
      "code": 33,
      "reason": "반대 대상이 부정된다는 구조를 이중부정처럼 표상할 수 있으나 법 정책에 대한 선호와 합헌성 판단은 논리적으로 같은 명제가 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 46,
      "rejection": "그래프의 비율 변화만으로 법원 신뢰나 언론 보도의 단독 인과효과를 식별한 것은 아니다. 문항은 모델과 관측 양상의 부합을 판단한다."
    },
    {
      "code": 43,
      "rejection": "두 법안의 사전 관심과 보도 시점이 다르며 타변수 통제를 통해 같은 조건의 인과를 비교한 실험이 아니다."
    },
    {
      "code": 41,
      "rejection": "집계 비율을 모든 개인의 동일한 이동 경로로 전이하지 않는다. 개별 무응답자가 어느 쪽으로 갔는지 확정할 수 없다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false,
  "numeric_evidence": {
    "election": {
      "before": [
        30,
        60,
        10
      ],
      "after_law": [
        30,
        60,
        10
      ],
      "after_court": [
        10,
        80,
        10
      ]
    },
    "flag": {
      "before": [
        25,
        15,
        60
      ],
      "after_law": [
        15,
        25,
        60
      ],
      "after_court": [
        45,
        45,
        10
      ]
    },
    "order": "찬성,반대,모름및무응답"
  }
}
```
