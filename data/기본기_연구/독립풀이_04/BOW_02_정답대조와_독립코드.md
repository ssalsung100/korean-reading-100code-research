

<!-- luna-raw:BOW-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G494",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2025/2025_answer_2025언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "독일법이 자기결정권을 제한한다는 사실은 배아 생성에 관한 어떤 선택도 행사할 수 없다는 뜻이 아니다.②는 제한을 전면 부정으로 바꾼다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BOW-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G494",
  "minimal_logic_without_codes": "독일법이 특정 생성·시술 방식을 제한한다는 사실을 생성에 관한 선택권 전부의 부재로 바꾼②를 배제한다.",
  "primary": [
    {
      "code": 4,
      "reason": "권리 행사 일부의 제한을 어떤 행사도 불가능하다는 전면 부정으로 확대한다."
    }
  ],
  "auxiliary": [
    {
      "code": 2,
      "reason": "조건 아래 선택 가능함과 전혀 행사할 수 없음의 강도를 나눈다."
    },
    {
      "code": 12,
      "reason": "정상 시술·무결함·한 번의 이식이라는 사례 조건을 일반 규칙에 결합한다."
    },
    {
      "code": 17,
      "reason": "보존할 수 있다는 법적 상태와 이 사례에 잔여가 실제 존재한다는 상태를 구분한다."
    },
    {
      "code": 24,
      "reason": "결함 예외가 보기에서 배제되었다는 점을 유지한다."
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "자기결정권이 소재지만②의 직접 조작은 권리 제한의 범위 확대다."
    }
  ],
  "competing_codes": [
    {
      "code": 34,
      "rejection": "전칭 부정으로도②의 과도한 결론을 표상할 수 있다.4와 국소 중첩하므로 별개 필수 연산으로 중복 계수하지 않는다."
    },
    {
      "code": 13,
      "rejection": "법적 제한과 일정 범위의 자기결정권은 함께 존재할 수 있어 양립 불가능으로 두지 않는다."
    },
    {
      "code": 95,
      "rejection": "잔여를 보존하려면 잔여가 있어야 한다는 존재 요건은③에 관련되지만②의 전면 권리 부정이 정답을 결정한다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
