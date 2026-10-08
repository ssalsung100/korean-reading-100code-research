

<!-- luna-raw:BGD-blind-20261002-r3-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G418",
  "selected_answer": 5,
  "confidence": 0.97,
  "exposure": {
    "prior_exposure": "unknown",
    "official_answer_read": false,
    "sdss_read": false,
    "existing_case_analysis_read": false,
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "순이론적 방법 설명",
      "evidence": "퍼텐셜 에너지 고려→방정식 세움→풀어 파동함수→계 상태 계산"
    },
    {
      "location": "보정 방법 문단",
      "evidence": "경험자료로 근사 선택,실험결과로 이론가정 수정"
    }
  ],
  "minimal_logic_without_codes": "⑤는 본문이 설명한 계산의 입력·산출 방향을 반대로 서술한다.퍼텐셜을 고려하여 파동함수를 구한다고 했다.",
  "intermediate_inference": [
    "① 보정도 이론도구 사용,② 정확해 대상이 좁아 근사보정 적용확대.",
    "③ 화학이 물리학 도구에 의존하는 방향을 가리키면 지지되나 전체관계가 일방적이라는 뜻이면 후반의 상호피드백과 맞지 않는다.",
    "④ 경험자료로 보정해야 예측정확성을 높이는 경로가 제시된다."
  ],
  "attractive_wrong_answer": 3,
  "exact_error": "③의 비대칭을 두 분야의 모든 영향이 영원히 한방향이라는 뜻으로 확대하면 안 된다.방법론적 도구 의존은 있으면서 경험자료·기법의 역방향 기여도 있다.",
  "unresolved": "수식 자체 전사 누락이 있으나 문장상의 입력/출력 순서로 판단했다.현실 수학에서 역문제가 불가능하다는 주장으로 확대하지 않음."
}
```
