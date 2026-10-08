

<!-- luna-raw:BOZ-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G495",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2025/2025_answer_2025언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "행위의 부정의를 거부하되 그로 인한 처벌을 감수하는 갑의 결정은 유벤이 말한 도덕적 저항과 맞으므로⑤다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BOZ-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G495",
  "minimal_logic_without_codes": "부정의한 행위를 거부하면서 불이익을 감수하는 것은 도덕적 저항일 수 있다. 갑의 납세 거부와 구류 수용을 유벤의 해석에 대응한다.",
  "primary": [
    {
      "code": 75,
      "reason": "각 해석자가 보기의 갑과 을을 어떻게 평가할지 관점을 적용한다."
    }
  ],
  "auxiliary": [
    {
      "code": 16,
      "reason": "부정의를 저지름과 부정의를 감수함, 명령 불복과 처벌 수용을 구분한다."
    },
    {
      "code": 69,
      "reason": "소크라테스의 사형 감수와 갑의 구류 감수에서 행위·피해·저항의 관계를 대응한다."
    },
    {
      "code": 17,
      "reason": "플라톤의 저술 동기를 소크라테스의 행동 동기로 바꾸지 않는다."
    },
    {
      "code": 78,
      "reason": "경제적 손해 감수의 목적을 이익 계산이 아닌 도덕적 일관성의 맥락에서 읽는다."
    }
  ],
  "surface": [
    {
      "code": 88,
      "reason": "손해가 세금보다 크다는 비교가 있으나⑤는 순이익 최대화의 선택을 묻지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 13,
      "rejection": "처벌 수용과 부당 권력에 대한 저항은 유벤의 해석에서 양립하므로 무조건 배타로 볼 수 없다."
    },
    {
      "code": 97,
      "rejection": "을의 애국적 변호 발화가 있으나⑤ 직접 판단은 갑의 행위 평가다."
    },
    {
      "code": 53,
      "rejection": "두 사례의 차이로 인과 효과를 식별하는 실험이 아니라 공통 구조를 관점에 적용한다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
