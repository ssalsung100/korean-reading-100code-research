

<!-- luna-raw:BED-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G400",
  "selected_answer": 4,
  "confidence": 0.98,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "2·3문단 매클로스키 생산 비효율/위험 분산",
    "4문단 페노알티아 노동 배분 효율",
    "5문단 달만 공동 방목 규모 경제",
    "6문단 스미스 소규모 경작/대규모 목축"
  ],
  "minimal_logic_without_codes": "개별 농지보다 큰 규모의 공동 목축이 효율적이라는 전제를 달만과 스미스가 공유한다. 이를 스미스만의 입장으로 만들면 틀린다.",
  "intermediate_reasoning": [
    "① 생산량 감소를 보험료로 해석하므로 맞다.",
    "② 두 사람의 설명은 곡물 생산·위험·저장·노동 배분에 관한 것이다.",
    "③ 페노알티아 생산 효율과 달만 목축 규모 경제에 각각 부합한다.",
    "④ 달만도 개별 울타리가 공동 방목의 규모 경제를 방해한다고 설명하므로 작은 개별 경지의 한계를 전제한다.",
    "⑤ 이 세 사람이 해당 제도의 지속을 효율적 선택으로 해석한다는 문맥 요약은 가능. 모든 지속 제도가 항상 합리적이라는 보편 명제로 확대하면 근거가 부족하다."
  ],
  "attractive_wrong": {
    "choice": 5,
    "exact_error": "해당 논의의 해석 태도 요약을 모든 역사적 제도에 관한 엄밀한 전칭 명제로만 읽으면 ⑤를 고르게 된다. 명확한 내용 반대는④의 차이 부여다."
  },
  "uncertainty": "⑤ 일반화의 허용 범위는 문맥적이며 모든 제도에 대한 보편 명제로 확정하지 않는다."
}
```
