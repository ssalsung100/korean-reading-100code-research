

<!-- luna-raw:BOB-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G487",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2024/2024_answer_2024언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "면접교섭권 침해에도 기관 지원은 받을 수 있다. 재판제도가 없다는 한계를 지원 자체 불가능으로 바꾼④가 틀리다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BOB-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G487",
  "minimal_logic_without_codes": "면접교섭권에는 기관 지원이 가능하되 협약상 재판 구제만 없다는 제한이다.④는 후자의 부재를 전자의 부재로 옮긴다.",
  "primary": [
    {
      "code": 17,
      "reason": "지원 제도와 재판 제도라는 서로 다른 구제 수단의 범위를 교환하지 않는다."
    }
  ],
  "auxiliary": [
    {
      "code": 12,
      "reason": "③의1년 이상 체류와 적응을 함께 요구하는 조건을 적용한다."
    },
    {
      "code": 2,
      "reason": "⑤ 중대한 위험이 인정돼도 보호조치와 반환 인용이 가능하다는 양태를 보존한다."
    },
    {
      "code": 24,
      "reason": "통상 반환 원칙과 예외 인정 가능성을 구분한다."
    },
    {
      "code": 10,
      "reason": "16세 미만과 양 본국 가입 요건을 확인한다.③에서는13세라 연령 요건을 충족한다."
    }
  ],
  "surface": [
    {
      "code": 3,
      "reason": "3년 뒤라는 시간은 연령 계산·체류 요건에 쓰이지만④ 직접 오류는 제도 범위의 교환이다."
    }
  ],
  "competing_codes": [
    {
      "code": 4,
      "rejection": "일부 구제수단 부재를 전부 부재로 바꾸는 범위 기술도 가능하다. 다만 구체 교환 대상인 지원/재판을17로 대표하며 배타 경계를 강제하지 않는다."
    },
    {
      "code": 21,
      "rejection": "지원과 재판이 서로 정의상 동치라는 근거는 없으며 정의의 필요충분성 문제가 아니다."
    },
    {
      "code": 8,
      "rejection": "두 수단 중 어느 것을 우선할지 정하는 것이 아니라 하나가 없더라도 다른 하나가 가능함을 확인한다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
