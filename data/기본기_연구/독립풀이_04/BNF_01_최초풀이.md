

<!-- luna-raw:BNF-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G480",
  "selected_answer": 2,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "정보 비용·대리지표·기회비용 문단",
      "evidence": "후보 정보 처리에 비용이 들고 주의 최대 도시 강수량은 주 전체 날씨의 대리지표이며, 일하지 못해 잃는 소득은 투표의 기회비용이다."
    }
  ],
  "minimal_logic_without_codes": "ㄱ은 다른 조건을 고정한 재선 후보 정보 축적,ㄴ은 넓은 지역에서 한 도시의 대표성 한계로 가능하다.시간당 임금과 투표율의 음의 관계는 기회비용 설명과 부합하므로 그 필요가 줄어든다는ㄷ은 맞지 않는다.②이다.",
  "intermediate_reasoning": [
    "ㄱ 이미 알려진 현역 후보에 관한 추가 정보 비용이 더 작을 수 있어 참여가 높아질 가능성이 있다.",
    "ㄴ 큰 주의 다양한 지역 날씨를 한 도시가 대표하지 못할 가능성이 더 커질 수 있다.면적만으로 실제 왜곡을 확정하지 않는다.",
    "ㄷ 같은 시간을 비울 때 임금이 높을수록 포기 소득이 커져 낮은 참여와 연결되는 설명이 가능하다.이 상관만으로 인과가 확정된다는 뜻은 아니다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "관측된 임금-투표율 관계가 설명할 수 있는 기회비용 기제와 같은 방향임에도, 그 관계가 발견되면 기제 검토가 불필요해진다고 읽는다."
  }
}
```
