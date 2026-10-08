

<!-- luna-raw:BDR-blind-20261002-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G396",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "needed_information_and_location": [
    "3문단 응집 대부분 비가역·쉽게 못 벗어남",
    "리폴딩은 응집체 형성 전에 샤페론 도움,실험에서는 샤페론 없이도 재현",
    "마지막 품질관리 실패 시 세포사멸"
  ],
  "minimal_logic_without_codes": "세포 안에서 이미 응집한 폴리펩티드가 자발적으로 원구조를 회복한다는④는 응집 전 리폴딩과 실험적 재현의 조건을 지운다.",
  "intermediate_reasoning": [
    "①품질관리실패→사멸가능.②리보솜서열정보사용.③열스트레스에구조변화.⑤특정입체구조필요."
  ],
  "most_attractive_wrong_answer": 3,
  "exact_error": "정상 폴딩의 내부 기제가 있다고 외부 열에 독립적인 것은 아니다.본문은 폴딩 중인 단백질에도 열 스트레스가 영향을 준다고 한다.",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BDR.json",
  "quota_status": "unavailable"
}
```
