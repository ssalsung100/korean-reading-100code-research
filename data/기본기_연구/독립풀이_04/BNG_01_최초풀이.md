

<!-- luna-raw:BNG-blind-20261003-01 -->
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
      "location": "공식 보기 수식",
      "evidence": "R맑음-R비=(DC비-DC맑음)+(OC비-OC맑음),③의 부등호는>0."
    },
    {
      "location": "본문 후반",
      "evidence": "우천으로 인한 참여 감소는 비용 지불 의지·능력이 약한 주변부 유권자의 기권에 주로 기인한다고 설명한다."
    }
  ],
  "minimal_logic_without_codes": "본문은 주변부 집단에게 우천 비용 장벽이 크게 작용한다고 설명하므로⑤의 비용 증가를 더 작게 느낀다는 방향은 맞지 않는다.",
  "intermediate_reasoning": [
    "① 기존 연구의 우천 불편은 직접비용 차이를 양으로 만든다.",
    "② 가까운 투표소는 비가 오는 상황의 이동 직접비용도 낮출 수 있다.",
    "③ R맑음>R비이면 보기의 단조 관계에 따라 비가 올 때 참여 가능성이 더 낮다.",
    "④ 공휴일의 야외활동이 비로 취소되는 경우에는 OC비<OC맑음이 가능하다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "비가 직접비용을 높인다는 사실을 모든 비용 항이 증가한다는 말로 바꾸어 기회비용의 반대 방향 가능성을 지운다."
  },
  "source_restoration": {
    "appendix": "data/기본기_연구/prepared_backlog/blind_sources/BNG-hold-source-20261003-appendix.md",
    "crop": "data/기본기_연구/prepared_backlog/blind_sources/BNG_official_view_choices_crop.png",
    "resolved_before_answer_disclosure": true,
    "original_hold_preserved": true
  },
  "incidental_future_source_exposure": "공식crop의오른쪽및아래에다음10~12번진리개념지문일부가포함되어우연히보였다.해당지문의공식답·SDSS·선지전체는읽지않았다.다음관련그룹시작시이부분본문노출을추가로기록하고strictblind성과에서제외한다.",
  "scope_limit": "기출이 제시한 집단별 비용 모형을 판독한 것이며 실제 유권자 집단의 성향을 새로 추정하거나 선거 전략을 설계하지 않는다."
}
```
