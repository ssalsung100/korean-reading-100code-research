

<!-- luna-raw:AOY-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G270",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "current_session": "blind본문·visual01/02그림직접열람,답·태그미열람",
    "historical": "unknown;기존참조0"
  },
  "required_information": [
    "(가):평면에서옆으로비켜지나갈수없고바퀴에축을붙일수없음.그림의평면몸/팔다리."
  ],
  "minimal_logic_without_codes": "훌라후프는 몸통을 둘러싸는 고리를 몸의 진행축과 교차하지 않게 배치·회전시킬 추가 공간방향이 필요하다.한 평면의 몸에서 고리를 허리 주위로 돌리는 구성은 어렵다.",
  "intermediate_reasoning": [
    "①표면따라이동가능",
    "②위로올라넘기가명시",
    "③몸통과고리의배치/축문제",
    "④평면속팔다리로유체이동은차원제약만으로금지안됨",
    "⑤판위로미끄러짐은축달린바퀴필수아님"
  ],
  "attractive_wrong_answer": 5,
  "exact_error": "스노보드판을바퀴차량과혼동하면안됨.금지근거는판형이아니라바퀴축배치.",
  "limitation": "일반적인훌라후프동작의평면구현불가판정이지2차원에서모든원운동이불가능하다는뜻아님."
}
```
