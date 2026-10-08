

<!-- luna-raw:BMV-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G477",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "마지막문단 첫 설명",
      "evidence": "빠른 성장에 필요한 거대 분자를 만들기 위해 해당작용 중간 생성물을 동화작용 재료로 쓴다."
    },
    {
      "location": "3~4문단·마지막문장",
      "evidence": "NAD+→NADH, 발효는NAD+재생. 유전자 변이가 주된 원인이고 바르부르크 효과는 결과라는 서술."
    }
  ],
  "minimal_logic_without_codes": "④는 해당작용의 중간 생성물이 동화작용의 재료로 쓰인다는 설명에 맞는다.",
  "intermediate_reasoning": [
    "① NADH는 산화적 인산화를 통해 추가 ATP 생산에 쓰일 수 있다.",
    "② 소비·재생되는 NAD+와 생성되는 NADH를 바꾼다.",
    "③ 젖산 발효는 NAD+ 재생에 기여하므로 젖산 증가에서 NAD+ 감소를 곧바로 도출하지 못한다.",
    "⑤ 유전자 돌연변이와 대사 변화의 원인·결과 방향을 뒤집는다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "발효의 젖산 생성만 보고 같은 과정의 NAD+ 재생을 누락한다.재생 흐름이 있다는 것과 세포 전체의 순농도 변화는 구분한다."
  },
  "scope_limit": "지문이 제시한 대사 모형을 판독하며 현재 임상적 발암 원인·검사·치료 안내로 확장하지 않는다."
}
```
