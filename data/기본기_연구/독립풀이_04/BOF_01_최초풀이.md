

<!-- luna-raw:BOF-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G489",
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
      "location": "선천성 조혈기성 포르피린증 문단·조지3세 문단",
      "evidence": "흡혈귀 공통 증세와 연결되는 것은 선천성 조혈기성, 조지3세 가설은 혼합 포르피린증이다."
    },
    {
      "location": "생성 경로 설명",
      "evidence": "앞 효소 결함으로 유로포르피리노젠I이 생기고 다음 효소의 작용으로 원인물질 코프로포르피리노젠I이 만들어진다."
    }
  ],
  "minimal_logic_without_codes": "④는 흡혈귀 공통 증세의 질환을 선천성 조혈기성에서 혼합 포르피린증으로 바꾸어 귀속한다.",
  "intermediate_reasoning": [
    "① 헴 합성 중간물질·부산물을 통칭하는 포르피린 범위에 포함된다.",
    "② 미오글로빈·시토크롬 모두 헴 보철그룹을 가진 단백질이다.",
    "③ 두 단백질 모두 산소 결합 기능이 있다.",
    "⑤ 유로포르피리노젠I을 원인물질로 전환하는 다음 효소는 작동하는 단계이며 그 효소 결함이 해당 원인물질을 생성한 원인이라고 읽지 않는다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "원인물질을 만드는 효소의 정상 작용과 그보다 앞 단계 효소의 결함을 혼동하여, 경로에 등장하는 모든 효소 결함을 같은 발병 원인으로 취급한다."
  },
  "scope_limit": "기출의 질환 설명과 경로를 판독하며 실제 진단·치료 지침으로 확장하지 않는다."
}
```
