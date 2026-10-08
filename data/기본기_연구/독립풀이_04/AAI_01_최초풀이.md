

<!-- luna-raw:AAI-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G168",
  "selected_answer": 4,
  "confidence": 0.99,
  "strict_blind_eligible": false,
  "stage_qualification": "사전답 노출 후 코드 없는 원문 재구성",
  "exposure": {
    "official_answer_seen": true,
    "official_source_seen": true,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "required_information_and_location": [
    "(나) 임차물 사용권 소멸 또는 충분한 경제력일 때 특별 보호 필요 없음.",
    "㉮는 계약 종료 후 반환시 원상회복 의무를 계약으로 정하는 경우."
  ],
  "minimal_logic_without_codes": "반환하는 임차물은 더 이상 생활·생업의 사용 근거가 아니므로 이 대상에 대해 계약보다 법이 우선하여 보호할 이유가 사라진다.④가 해당 사례의 이유를 붙인다.",
  "intermediate_reasoning": [
    "① 충분한 경제력은 다른 보호 불필요 조건이지만㉮에 그런 정보 없음.",
    "② 변경 불가는 법 우선 경우의 설명이며㉮의 계약 우선과 반대.",
    "③ 자유 보장의 원칙은 계약 존중이지 항상 법률로 내용 정하기가 아님.",
    "⑤ 조건에 따라 법/계약 적용이 달라지는데 무관하다고 함."
  ],
  "most_attractive_wrong_answer": 1,
  "exact_error": "본문에 있는 참된 일반 이유라도 현재 사례에 전건이 주어지지 않으면 해당 이유로 채택할 수 없다. 종료·반환은 사용권 소멸과 연결되지만 경제력을 말하지 않는다.",
  "quota_status": "unavailable"
}
```
