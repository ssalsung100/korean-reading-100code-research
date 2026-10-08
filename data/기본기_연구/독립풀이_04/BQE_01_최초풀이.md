

<!-- luna-raw:BQE-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G506",
  "selected_answer": 2,
  "confidence": 0.97,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "황산마그네슘 예시",
      "evidence": "많은 물에 소량 첨가하면 구조 수축으로 전체 부피 자체가 감소한다."
    },
    {
      "location": "물/에탄올 설명",
      "evidence": "이종분자 인력이 수소결합 네트워크를 깨 혼합 전 부피합보다 부피 증가가 덜하다."
    },
    {
      "location": "첫문단",
      "evidence": "깁스에너지 변화=혼합열-절대온도×엔트로피변화."
    }
  ],
  "minimal_logic_without_codes": "황산마그네슘은 첨가 후 물의 원래 부피보다도 작아지고 에탄올은 인력 때문에 산술적 부피합보다 작아지므로②가 공통 결과를 정확히 묶는다.",
  "intermediate_reasoning": [
    "① 질량 합은 보존되나 혼합 부피가 단순 합이 아니므로 같은 부피 두 물질의 밀도 평균이 혼합밀도라고 할 수 없다.",
    "③ 혼합에 따른 엔트로피 증가를 분몰부피 음수에만 한정할 수 없다.",
    "④ 인력 강화로 부피가 수축하는 설명과 반대로 거리가 커졌다고 한다.",
    "⑤ 엔트로피 단위는 에너지/온도이지 에너지×온도가 아니다."
  ],
  "most_attractive_wrong": {
    "choice": 1,
    "exact_error": "같은 부피로 섞을 때 질량은 합산해도 부피를2V로 둘 수 없으므로 밀도 산술평균이 성립하지 않는다."
  },
  "scope_limit": "②는 각 혼합물에서 혼합 전 부피합과 비교한 공통 방향이지 두 혼합물의 최종 부피나 수축량이 같다는 뜻이 아니다."
}
```
