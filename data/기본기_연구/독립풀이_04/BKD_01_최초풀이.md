

<!-- luna-raw:BKD-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G453",
  "selected_answer": 2,
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
      "evidence": "물질파 파장은 운동량에 반비례, 가속 전압 증가→속도 증가. 최소 해상도는 파장·초점 거리에 비례."
    },
    {
      "location": "3문단",
      "evidence": "전자에 작용하는 힘은 속도·자기장에 비례, 코일 전류 증가→자기장 증가→힘 증가→초점 거리 감소."
    }
  ],
  "minimal_logic_without_codes": "ㄱ은 파장 증가→속도 감소→힘 감소여서 거짓. ㄴ은 전압 증가→속도 증가→파장 감소→회절 원반 감소가 가능하여 참. ㄷ은 전류 감소→초점 거리 증가→최소 해상도 수치 증가여서 거짓. ㄴ만 선택한다.",
  "intermediate_reasoning": [
    "ㄱ의 비교에서 전자 질량과 자기장을 고정한다. 파장과 힘의 방향은 반대다.",
    "ㄴ에서 다른 렌즈 조건을 고정한 파장 효과를 본다.",
    "ㄷ은 해상도가 작다는 것이 더 세밀한 구분이라는 본문 정의를 유지해야 한다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "해상도 수치가 작은 것을 나쁜 성능으로 읽거나 전류 감소를 회절 감소로 곧바로 연결하면 ㄷ을 잘못 수용한다. 본문은 전류와 초점 거리의 역방향 경로를 준다."
  }
}
```
