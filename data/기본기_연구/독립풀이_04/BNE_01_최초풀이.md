

<!-- luna-raw:BNE-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G480",
  "selected_answer": 5,
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
      "location": "기회비용 문단",
      "evidence": "공휴일 지정·사전투표 도입은 근무나 다른 선택의 포기에서 생기는 기회비용을 낮추려는 제도로 설명된다."
    },
    {
      "location": "첫·후반문단",
      "evidence": "정보 비용과 소득별 참여 차이, 날씨에 따른 주변부·연령 집단의 다른 반응을 서술한다."
    }
  ],
  "minimal_logic_without_codes": "⑤는 사전투표의 본문상 도입 취지를 기회비용 감소에서 직접비용 감소로 바꾼다.",
  "intermediate_reasoning": [
    "① 미국의 우천이 공화당에 유리할 수 있다는 본문 설명에서는 투표율 증가가 민주당에 도움이 될 가능성을 읽을 수 있다.보편적 필연은 아니다.",
    "② 사회경제적 지위가 높을수록 정보 비용을 낮게 체감한다는 설명에 맞는다.",
    "③ 세대별 날씨 반응과 정치적 지지가 다르면 정당별 영향도 달라질 수 있다.",
    "④ 공약 비교 공개는 정보 획득·처리 비용을 낮출 수 있다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "한국에서 비가 일부 사람의 기회비용을 줄일 수 있다는 사실만으로 모든 집단·정당에 같은 효과가 난다고 생각한다."
  },
  "scope_limit": "기출 본문의 투표 비용 모형과 진술 범위를 판독하며 실제 선거 집단을 겨냥한 전략은 만들지 않는다."
}
```
