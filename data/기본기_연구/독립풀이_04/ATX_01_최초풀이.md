

<!-- luna-raw:ATX-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G313",
  "selected_answer": 4,
  "confidence": 0.98,
  "exposure": {
    "prior_exposure": "이 세션의 사전 해설·정답·SDSS 노출 없음; 과거 노출 미확인",
    "official_answer_seen": false,
    "sdss_seen": false
  },
  "strict_blind_eligible": "과거 노출 미확인으로 확정 집계 보류",
  "needed_information_and_location": [
    "2문단 저용량은 혈소판 활성 최고치만 감소·가벼운 출혈 지혈 영향 작음",
    "3문단 가역적 억제와 COX2 선택적 결합"
  ],
  "minimal_logic_without_code": "용량에 따른 작용 강도의 차이를 작용 종류의 배타적 전환으로 바꾸면 근거가 없다. 고용량에서 진통이 없어지고 응고 억제만 남는다는 결론은 제시되지 않았다.",
  "intermediate_reasoning": [
    "① COX2 선택은 전체 COX 억제보다 제한적",
    "② 세포별 산물·기능이 달라 같은 억제도 효과가 다름",
    "③ 가역성이 지속 억제 부작용 감소를 설명하는 문맥",
    "⑤ COX1 혈소판 트롬복산 경로 보존+COX2 내피 응고 억제 경로 차단 → 응고 촉진"
  ],
  "most_attractive_wrong_answer_and_error": "⑤: 응고를 억제하는 산물 생성을 차단하므로 응고 촉진이다. 억제 대상의 부호를 놓치면 거꾸로 읽게 된다.",
  "source_scope": "시험 원문 내부 독해; 현재 의료 판단으로 확장하지 않음"
}
```
