

<!-- luna-raw:BHD-blind-20261002-r5-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G427",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BHD.json",
  "necessary_information": [
    {
      "location": "2문단 ㉠/㉡",
      "evidence": "㉠은 민형사만 사법권, 의회 자율의 위헌 판단.㉡은 모든 법 적용이 사법권, 판사 법리적 객관 심사."
    },
    {
      "location": "3문단 ㉢",
      "evidence": "위헌 법률의 헌법 통제는 필요하지만 정치성이 강하고 비선출 대법관 심사는 위험. 국가 과제 해결 중시."
    }
  ],
  "minimal_logic_without_codes": "세 입장의 심사 필요 여부·담당 기관·판단 성격·우선 가치를 각각 분리한다.㉡은 법리적 객관 심사,㉢은 정치적 성격을 강조하므로③이 맞다.",
  "intermediate_reasoning": [
    "①㉠민형사는㉡모든 법보다 좁다.②㉠의회 자율과㉢별도 헌법위원회는 다르다.",
    "④㉡/㉢ 모두 법률의 헌법 적합성 검증 필요성은 공유한다.⑤㉢은 국가 과제의 시급한 해결을 중시하므로 우선순위가 반대다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "심사 기관과 방식에 대한 반대를 심사 자체의 필요성에 대한 반대로 바꾼다.㉢도 국회의 위헌 법률이 통제받아야 한다고 명시한다."
  }
}
```
