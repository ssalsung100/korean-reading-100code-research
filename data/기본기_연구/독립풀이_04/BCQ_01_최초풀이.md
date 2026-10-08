

<!-- luna-raw:BCQ-blind-20261002-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G386",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "needed_information_and_location": [
    "보기 수동 면역: 다른 개체에서 생성된 항체 주입",
    "㉡ 말 혈액 항디프테리아 혈청",
    "㉣ 면역화 쥐 혈액의 면역 혈청",
    "㉠·㉢ 약한 균 접종으로 개체 스스로 면역화"
  ],
  "minimal_logic_without_codes": "받는 개체에 외부의 이미 만들어진 항체가 들어오는 경우를 찾으면㉡㉣이다. 균을 주입해 자기 항체 생성을 유도하는㉠㉢과 구별한다.",
  "intermediate_reasoning": [
    "㉠ 수탉은 약화 균으로 면역화된다.㉢ 쥐도 약화 균으로 면역화된다.㉡과㉣은 다른 개체 혈청 성분을 받는다."
  ],
  "most_attractive_wrong_answer": 3,
  "exact_error": "인위적으로 주사를 맞는다는 공통 행동으로 수동을 판정하면㉠도 넣는다. 수동의 기준은 시술의 수동성 대신 항체 생성 개체와 수혜 개체의 차이다.",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BCQ.json",
  "quota_status": "unavailable"
}
```
