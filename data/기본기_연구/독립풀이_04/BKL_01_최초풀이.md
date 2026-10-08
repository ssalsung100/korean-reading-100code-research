

<!-- luna-raw:BKL-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G456",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "2문단",
      "evidence": "전통 경제학은 유동성 조달 제약을 금융 시장의 불완전성으로 설명한다."
    },
    {
      "location": "3~4문단",
      "evidence": "행동경제학은 마음속 계정 구분과 자발적 자기 통제 기제로 소비 제약을 설명한다."
    }
  ],
  "minimal_logic_without_codes": "동일한 소비·유동성 제약을 전통 경제학은 외부 금융 환경, 행동경제학은 개인의 심리적 선택으로 설명하므로 ③이 맞는다.",
  "intermediate_reasoning": [
    "① 전통 경제학의 불굴의 실행 의지와 행동경제학의 유혹 취약 가정을 같게 만든다.",
    "② 두 이론의 외부 제약/자발적 선택 귀속을 바꾼다.",
    "④ 유동성 제약이 소비를 어렵게 한다는 방향을 반대로 만든다.",
    "⑤ 금융적으로는 예금 인출이 낫다는 점을 두 이론이 부정한다고 할 근거가 없다. 비합리적 행동의 관찰·설명과 금융적 효율 평가는 다르다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "행동경제학이 저축 유지·고금리 차입을 설명한다는 사실을 그 행동이 금융적으로 최선이라고 평가한다는 뜻으로 바꾼다."
  }
}
```
