

<!-- luna-raw:BPN-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G500",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2026/2026_answer_2026_LEET_언어이해_정답표.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "이념상 양극단 비중이 커지고 중도 비중이 크게 줄어 민주주의 손실을 감수하며 이념 효용을 택하는 경향이 설명된다.④는L승리를 그 유권자가 감소한 결과라고 하여 모형의 설명 방향을 뒤집는다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BPN-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G500",
  "minimal_logic_without_codes": "중도 비중이 줄고 이념상 양극단 비중이 커진 그림을 스볼릭의 효용 비교에 연결하면④의 감소한 결과라는 설명 방향은 맞지 않는다.",
  "primary": [
    {
      "code": 49,
      "reason": "분포 변화와 모형이 예상하는 조작 비용·이념 선택의 변화 방향을 연결한다."
    }
  ],
  "auxiliary": [
    {
      "code": 88,
      "reason": "각 가상 유권자의 이념 효용과 민주주의 훼손 손실을 함께 비교한다."
    },
    {
      "code": 86,
      "reason": "중도48→10 등 집단 비중과 좌표상의 상대 거리를 구분한다."
    },
    {
      "code": 43,
      "reason": "③은 조작의 수준을 같게 둔 상태에서 분포만 달라진 비교다."
    },
    {
      "code": 2,
      "reason": "모형상 가능성이 커짐과 실제 승리의 필연·단독 인과를 구분한다."
    }
  ],
  "surface": [
    {
      "code": 91,
      "reason": "본문에 비례·반비례 표현이 있어도 그림만으로 정확한 효용 배율을 계산할 수는 없다."
    }
  ],
  "competing_codes": [
    {
      "code": 46,
      "rejection": "정치 모형의 설명 경로를 적용할 수 있지만 그림의 분포만으로 실제 선거 인과를 새로 식별한 것으로 보지 않는다."
    },
    {
      "code": 84,
      "rejection": "비율 자료지만 분모 변화에 의한 착시를 계산하는 문항이 아니다."
    },
    {
      "code": 85,
      "rejection": "합100인 분포여도 특정 집단 증가량을 다른 단일 집단 감소량과 같은 것으로 놓지 않는다. 전체 분포를 읽는다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false,
  "scope_limit": "가상 자료의 독해에 한정하며 특정 실제 집단을 설득하거나 선거 조작을 최적화하는 방법을 만들지 않는다."
}
```
