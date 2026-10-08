

<!-- luna-raw:BOS-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G493",
  "selected_answer": 1,
  "confidence": 0.97,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "정태상태 결정·수렴 설명",
      "evidence": "정태상태 자본량은 저축률·감가상각률·생산함수로 정해지고 비정태 경제는 시간에 따라 그 상태로 이동한다."
    },
    {
      "location": "공식 그래프",
      "evidence": "저축량은 아래로 굽은 증가곡선, 감가상각량은 원점을 지나는 직선이며 양의 자본에서 교차한다."
    }
  ],
  "minimal_logic_without_codes": "같은 기초 여건이면 본문이 다루는 같은 정태상태로 수렴하므로 초기 생산량이 달라도 소비 격차가 좁혀진다.①의 격차가 좁혀지지 않는다는 주장이 틀리다.",
  "intermediate_reasoning": [
    "② 현재 소비 손실과 미래 이익을 누릴 기간의 차이가 세대 반응에 영향을 준다.",
    "③ 감가상각률 상승은 직선을 가파르게 해 양의 교차점을 왼쪽으로 옮긴다.",
    "④ 저축률 상승은 저축곡선을 올려 양의 교차점을 오른쪽으로 옮긴다.",
    "⑤ 황금률 자본량은 소비 최대의 정태상태이므로 외생 변화가 없으면 생산도 일정하다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "최선의 자본량이라는 표현을 계속 성장하는 상태로 오인하면, 황금률도 정태상태의 한 종류라는 정의를 놓친다."
  },
  "source_restoration": {
    "crop": "data/기본기_연구/prepared_backlog/blind_sources/G493_official_graph_crop.png",
    "astra_direct_seen": true,
    "resolved_before_answer_disclosure": true
  },
  "scope_limit": "본문의 양의 정태상태 수렴을 적용한다. 자본0의 퇴화 경계처럼 별도 초기조건이 필요한 경우를 모두 다룬 전역 수학정리로 확대하지 않는다."
}
```
