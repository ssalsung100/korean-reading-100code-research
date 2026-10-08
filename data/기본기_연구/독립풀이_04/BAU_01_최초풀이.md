

<!-- luna-raw:BAU-blind-20261001-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "necessary_information_locations": [
    "3문단 여러 대부모 가능, 사람형/물건형 비성사 구분",
    "4문단 친족 내 선택도 가능하나 관계 성립은 개별 조건에 따름",
    "보기 호세-이달리아,호세-라울,이달리아-로라의 각각 다른 매개"
  ],
  "minimal_logic_without_codes": "이달리아와 로라가 친척이고 각각 다른 상대와 후원 관계를 맺었다고 해서 호세와 로라의 관계가 자동 성립하지 않는다. 관계망의 확장 가능성과 모든 연결의 전이를 구분한다.",
  "intermediate_reasoning": [
    "①루이스 세례 대모이므로 성사 대부자 관계.",
    "②카르멘 졸업이라는 사람 매개 비성사 관계.",
    "③세례 부분을 나눠 여러 대부모를 둘 수 있으므로 외아들이어도 다른 대부모 가능.",
    "④로라-호세 관계의 매개·성립 사실은 주어지지 않음.",
    "⑤물건형은 후원 여부에 지속 기간이 달림."
  ],
  "most_attractive_wrong_answer": 3,
  "exact_error": "외아들이라는 자녀 수 제한을 대부모 수도 한 명이라는 제한으로 옮긴다. 세례의 여러 부분을 나누어 후원하는 복수 대부모가 가능하다.",
  "passage_group": "G371",
  "selected_answer": 4,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BAU.json",
  "quota_status": "unavailable"
}
```
