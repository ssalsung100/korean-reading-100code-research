

<!-- luna-raw:BPW-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G503",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2026/2026_answer_2026_LEET_언어이해_정답표.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "과거 저소득이 높은 폭동과 현재 저소득에 함께 연결되는 교란 우려에 과거/현재 소득의 음의 관계는 맞지 않는다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "scope_limit": "원 blind의 반비례 해석·기술 경로의 중요성·교란 설명의 방향에 관한 제한을 그대로 보존한다."
}
```


<!-- luna-raw:BPW-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G503",
  "minimal_logic_without_codes": "과거 소득이 낮을수록 폭동이 높았고 현재 소득이 낮은 경향이 이어진다면, 폭동 자체의 효과가 없어도 관측된 음의 관계를 설명할 수 있다. 과거와 현재 소득의 강한 음의 관계는 이 설명의 방향과 맞지 않는다.",
  "primary": [
    {
      "code": 47,
      "reason": "과거 소득이 폭동과 현재 소득의 관계를 교란하는 대안 설명의 방향을 재구성한다."
    }
  ],
  "auxiliary": [
    {
      "code": 49,
      "reason": "폭동/현재 소득의 음의 관계와 과거/현재 소득의 관계를 구별한다."
    },
    {
      "code": 3,
      "reason": "당시 소득·당시 폭동·현재 소득의 시점을 고정하여 현재가 과거를 일으킨다는 오독을 피한다."
    },
    {
      "code": 10,
      "reason": "강우량의 관련성과 배제 조건으로①③⑤를 검토한다."
    },
    {
      "code": 46,
      "reason": "폭동 자체의 원인 효과와 과거 소득에 따른 결합 관계를 구분한다."
    }
  ],
  "surface": [
    {
      "code": 87,
      "reason": "기울기는 음이라는 방향 표시에 쓰이며 실제 값 계산을 요구하지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 52,
      "rejection": "두 음의 관계를 곱해 촉진을 확정하는 인과 사슬이 아니다. 공유된 요인에 대한 관련성 방향을 검토한다."
    },
    {
      "code": 48,
      "rejection": "공통 결과를 조건으로 선별해 두 원인을 연결하는 구조가 아니다."
    },
    {
      "code": 92,
      "rejection": "회귀계수나 함수가 없어 수치 연산을 수행할 수 없고 필요하지도 않다."
    }
  ],
  "confidence": 0.93,
  "sdss_seen": false,
  "scope_limit": "상관계수 부호는 일반적으로 단순히 곱해 추론할 수 없다. 여기서는 본문이 지목한 교란 설명이 관측 관계를 흉내 내는 방향을 검사하며 실제 세계의 과거/현재 소득 상관을 증명하지 않는다."
}
```
