

<!-- luna-raw:BQF-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G506",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false,
    "visual_supplement_seen": true
  },
  "necessary_information": [
    {
      "location": "본문 분몰부피 정의",
      "evidence": "총부피 대 첨가몰수 그래프의 접선기울기가 첨가 성분의 분몰부피."
    },
    {
      "location": "깁스-뒤엠식",
      "evidence": "nR dVR+nS dVS=0.희석 성분의 분몰부피는 급격히,다수 성분은 완만히 변한다."
    },
    {
      "location": "보기 그래프",
      "evidence": "a→b는 양의 기울기가 커지고,c→d는 음의 기울기 절댓값이 작아진다.S는1000몰,a의R은0.001몰."
    }
  ],
  "minimal_logic_without_codes": "a 부근의 R은 S보다 극히 적으므로 같은 변화에서 S의 분몰부피 변화는 R보다 훨씬 작다.③의 같은 급격함은 몰수로 가중된 변화 제약을 무시한다.",
  "intermediate_reasoning": [
    "① b접선이 a보다 가파르므로 R분몰부피가 더 크다.",
    "② R분몰부피가 증가하면 S분몰부피는 감소한다.",
    "③ dVS=-(nR/nS)dVR이며 a에서 비는10^-6이다.두 변화량을 같은 크기로 둘 수 없다.",
    "④ b에서양의접선,c에서음의접선이므로그림의연속적곡선중간에0접선인지점이있다.",
    "⑤ c보다d의음의기울기가완만하여동일극소량첨가에따른부피감소가더작다."
  ],
  "most_attractive_wrong": {
    "choice": 2,
    "exact_error": "총부피가a→b에서증가한다는것을S분몰부피도증가한다는것으로바꾸면안된다.총부피기울기는R분몰부피이고S는가중관계식으로따로추론한다."
  },
  "scope_limit": "절단된x축너머의정확한몰수·최대부피값은추정하지않는다.a부근의희석조건과접선방향만사용한다."
}
```
