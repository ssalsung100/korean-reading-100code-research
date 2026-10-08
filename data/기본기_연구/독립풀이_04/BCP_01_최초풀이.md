

<!-- luna-raw:BCP-blind-20261002-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G386",
  "selected_answer": 5,
  "confidence": 0.89,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "needed_information_and_location": [
    "보기 항체가 태반을 넘어 태아 혈구를 파괴",
    "4문단 용균성 반응은 독소 중화 아닌 표적 파괴",
    "5문단 보체는 정상 동물에 존재하고 면역 반응으로 양 증가 안 함",
    "2문단 약한 균 접촉 뒤 재접촉 저항성"
  ],
  "minimal_logic_without_codes": "항원을 먼저 만난 엄마가 항체를 만들고 이 항체가 태아의 표적 혈구를 파괴한다. 반복 노출의 원인을 태아 보체 증가로 돌릴 수 없다. 이전 혈액 노출이 있으면 첫 임신도 최초 항원 노출이 아니다.",
  "intermediate_reasoning": [
    "ㄱ은 균 자체와 혈구의 차이를 유지하면서 항체에 의한 표적 파괴라는 방식에서 일종의 용균성으로 대응한다.ㄴ 보체 증가설은 마지막 문단과 충돌.ㄷ Rh 인자가 항체 생성을 유발하는 표적이다.ㄹ 임신 횟수가 아니라 이전 항원 노출 경험이 조건이다."
  ],
  "most_attractive_wrong_answer": 3,
  "exact_error": "ㄱ의 대상이 세균이 아니라는 이유만으로 제외하면 일종이라는 기능적 대응을 놓친다. 다만 원문 용균성 범주를 혈구로 확대하는 것은 비유적 적용이며 동일 생물학적 대상이라는 뜻이 아니다.",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BCP.json",
  "quota_status": "unavailable"
}
```
