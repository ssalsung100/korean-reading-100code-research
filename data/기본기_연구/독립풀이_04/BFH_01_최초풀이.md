

<!-- luna-raw:BFH-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G410",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "1문단 혈액 지속 공급은 정상 기능의 필요 배경",
    "2문단 역류 열전달은 들어오는 혈액의 냉각 설명",
    "3·4문단 표면 방열·근육 움직임·생산량"
  ],
  "minimal_logic_without_codes": "혈액이 공급되는 사실을 전제로 그 혈액의 열이 어떻게 낮아지는지 설명한 이론이지 혈액 공급을 지속시키는 기제를 설명한 것이 아니다.",
  "intermediate_reasoning": [
    "① 근육으로 정소가 몸에서 가까워지거나 멀어진다.",
    "② 온도 상승 시 정자 생산 감소를 말한다.",
    "③ 망사 열교환과 표면 방열에 전도가 쓰인다.",
    "④ 설명의 전제인 혈액 공급과 설명 대상인 온도 유지의 기제를 혼동한다.",
    "⑤ 스칸단의 설명은 정낭 표면 방열이 중심이다."
  ],
  "attractive_wrong": {
    "choice": 5,
    "exact_error": "정소가 열을 생성한다는 사실만 보고 열을 밖으로 배출하는 정낭의 핵심 조절 역할을 놓친다."
  },
  "scope": "기관 명칭과 기능은 제공된 기출 전사 안의 표현으로 취급한다."
}
```
