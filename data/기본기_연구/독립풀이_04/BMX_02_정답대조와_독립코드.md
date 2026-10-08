

<!-- luna-raw:BMX-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G477",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2021/2021_answer_2021_LEET_언어이해_정답표_배포용.hwp",
  "minimal_logic_without_codes": "산소 감소로 단위 포도당당 ATP 수율이 낮아지는 조건에서 같은 ATP 양을 만들려면 포도당 유입을 늘려야 하므로 유도체 축적도 늘어난다는③이 맞는다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BMX-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G477",
  "minimal_logic_without_codes": "산소 감소가 산화적 인산화를 제한하고 수율을 낮출 때 같은 ATP 목표량을 유지하려면 포도당 유입이 더 필요하며 유도체 축적도 증가한다.",
  "primary": [
    {
      "code": 46,
      "reason": "산소→경로 의존→단위 수율→필요 포도당→추적 물질 축적의 연결을 복원한다."
    }
  ],
  "auxiliary": [
    {
      "code": 43,
      "reason": "③의 동일한 ATP 생성량을 고정해 수율 변화의 효과를 비교한다."
    },
    {
      "code": 84,
      "reason": "필요 포도당=고정 ATP 목표량/단위 포도당 수율이라는 분모 변화 관계를 적용한다."
    },
    {
      "code": 45,
      "reason": "포도당 수송과 유사체의 축적이라는 측정 지표의 대응을 연결한다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "정확한 ATP나 포도당 양을 수치로 계산하지 않고 방향만 판정한다."
    }
  ],
  "competing_codes": [
    {
      "code": 49,
      "rejection": "최종 방향을 요약할 수 있으나 어느 조건을 고정하고 어떤 경로를 거치는지 생략하면 효율 증가와 흡수 증가를 같은 방향으로 오독할 수 있다."
    },
    {
      "code": 85,
      "rejection": "입력량×수율=고정 산출량이라는 곱 일정 표상은84와 같은 국소 관계다. 별개 필수 연산으로 중복 계수하지 않는다."
    },
    {
      "code": 54,
      "rejection": "유도체 축적의 증가를 암이라는 질병의 충분한 확정 원인·조건으로 바꾸지 않는다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false
}
```
