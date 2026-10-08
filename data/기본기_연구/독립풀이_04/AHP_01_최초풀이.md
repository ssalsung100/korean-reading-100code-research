

<!-- luna-raw:AHP-blind-20260921-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G207",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_and_location": [
    "3문단 선형의 손실·발열·크기 단점과 특별 사용",
    "4문단 끝 스위칭 노이즈 잔류"
  ],
  "minimal_logic_without_codes": "선형의 효율·크기·발열상 단점에도 스위칭의 잔류노이즈가 성능을 해치는 경우에는 선형을 쓸 이유가 있다.⑤은 대안의 단점을 회피하는 필요와 연결된다.",
  "intermediate_inferences": [
    "① 고효율·② 소형화·③ 낮은손실·④ 발열손상 방지는 모두 선형 단점과 어긋나 선택 이유가 안 됨",
    "⑤은 최종 출력 변동에 민감하다는 특별 조건"
  ],
  "most_attractive_wrong_answer": {
    "choice": 4,
    "attraction": "안정적인 전원이라는 선형의 정전압 특성",
    "error": "발열손상 방지는 열소모가 큰 선형 선택의 적절한 이유가 아니다. 결합된 조건 전체를 봐야 한다."
  },
  "quota_status": "unavailable"
}
```
