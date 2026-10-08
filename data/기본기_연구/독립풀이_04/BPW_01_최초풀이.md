

<!-- luna-raw:BPW-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G503",
  "selected_answer": 4,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "보기 전반",
      "evidence": "당시 폭동 수준이 높을수록 현재 소득이 낮은 관측 관계."
    },
    {
      "location": "보기 후반",
      "evidence": "당시 소득이 낮은 도시에서 폭동이 더 심했던 데서 비롯되는 인과 추론 문제를 강우량 도구변수로 검토."
    },
    {
      "location": "본문2문단",
      "evidence": "도구변수는 설명 변수와 연관되고 그 외의 결과 영향 요인과 무관해야 한다."
    }
  ],
  "minimal_logic_without_codes": "당시 낮은 소득이 높은 폭동과 현재 낮은 소득 모두에 연결되는 것이 관측된 음의 관계를 흉내 낸다는 우려다.④처럼 과거와 현재 소득의 높은 음의 관계를 가정하면 이 우려의 방향과 어긋난다.",
  "intermediate_reasoning": [
    "① 강우량과 폭동의 관련성은 도구변수의 첫 요건이다.",
    "② 폭동과 현재 소득 사이 관측된 음의 관계를 방향만 바꾸어 읽은 것으로 시간 역행 인과를 주장하지 않는다.",
    "③ 강우량이 폭동을 거치는 경로 외에는 현재 소득과 연관되지 않는다는 배제 조건이다.",
    "⑤ 강우량에서 예측한 폭동 수준과 현재 소득의 관계를 검토한다는 방법과 맞는다."
  ],
  "most_attractive_wrong": {
    "choice": 2,
    "exact_error": "현재 소득이 낮은 곳에서 과거 폭동 수준이 높았다는 관측상의 결합을 현재 소득이 과거 폭동을 일으켰다는 시간 역행 인과로 오독할 수 있다."
  },
  "scope_limit": "과거/현재 소득의 양의 지속성은 연구자가 검토하는 잠재적 교란 설명의 방향이다. 원문에 수치가 없으므로 실제 상관계수나 보편 법칙은 계산·확정하지 않는다."
}
```
