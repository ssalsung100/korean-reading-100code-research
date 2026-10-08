

<!-- luna-raw:ATT-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G312",
  "selected_answer": 5,
  "confidence": 0.98,
  "exposure": {
    "prior_exposure": "이 세션에서 기존 풀이·정답·태그 노출 없음; 과거 세션 노출은 확인 불가",
    "official_answer_seen": false,
    "sdss_seen": false,
    "source": "blind_only"
  },
  "strict_blind_eligible": "과거 노출 미확인으로 잠정; 확정 성과 집계 보류",
  "needed_information_and_location": [
    "1문단: 연속 외부 변화에 불규칙·갑작스러운 유도 전류",
    "2문단: 역방향 정렬 전환은 군집으로 진행하며 효과 발생 자기장이 임계 자기장",
    "3문단: 통계적 접근 및 실험 증명"
  ],
  "minimal_logic_without_code": "초기 정렬 상태에서 반대 방향의 외부 조건을 바꾸면 군집 전환이 일어나고 그 현상이 관찰되는 조건값을 임계값이라 부른다.",
  "intermediate_reasoning": [
    "① 독립적 전이는 본문의 군집 전이와 반대",
    "② 불규칙 관측을 일정 검출값으로 바꿈",
    "③ 실험 증명을 부정",
    "④ 해석적 방법 가능으로 반전",
    "⑤ 역방향 조건과 임계값 정의를 결합"
  ],
  "most_attractive_wrong_answer_and_error": "④: 코발트라는 대상은 맞으나 해석적 설명이라는 뒷절은 거의 불가능하다는 본문과 충돌한다."
}
```
