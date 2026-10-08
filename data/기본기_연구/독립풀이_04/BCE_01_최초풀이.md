

<!-- luna-raw:BCE-blind-20261002-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G383",
  "selected_answer": 3,
  "confidence": 0.89,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BCE.json",
  "needed_information_and_location": [
    "5문단 인공 전파의 패턴·세기와항성 주위 탐사",
    "6문단 H/OH의 물 형성 및사용 대역",
    "7문단 반복성·지역·세기 후보선정"
  ],
  "minimal_logic_without_codes": "탐사의 가정은 신호 형태·강도·발생 지역·물 관련 대역에 관한 것이다.물 형성 물질과 관련된 대역을 생명체의 주성분 원소가 방출하는 주파수 일반으로 바꿀 근거는 없다.",
  "intermediate_reasoning": [
    "① 생명은 항성 주위 행성에 있다는 지문 조건과 부합.",
    "② 인공 신호와 무작위 자연 전파를 구분하는 탐사 근거.",
    "③ 특정 H/OH 대역 선택을 자신의 주성분 원소라는 별도 기준으로 바꾸며 OH도 단일 원소가 아님.",
    "④ 강한 전파 사용 가능성과세기를 후보 기준으로 삼는 탐사 가정에 대응.다만 강도가 커질수록 사후 확률이 단조 증가한다는 엄밀한 정량 법칙은 본문 미제시.",
    "⑤ 우리가 성간 물질을 관측하는 대역과 외계 생명이 쓸 것으로 가정하는 대역이 연결됨."
  ],
  "most_attractive_wrong_answer": {
    "choice": 4,
    "exact_error": "④의 엄밀한 확률 강도는 유보할 수 있으나 본문이 강한 전파의 사용 가능성과세기 고려를 직접 명시하므로 탐사 가정의 후보에는 해당한다.③은 대역 선택 근거 자체를 교환한다."
  },
  "residual_uncertainty": "④ 강도-발신자 확률의 역추론/단조관계 강도는 추후 반례검토 필요.",
  "quota_status": "unavailable"
}
```
