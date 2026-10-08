

<!-- luna-raw:BPN-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G500",
  "selected_answer": 4,
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
      "location": "공식 그림1",
      "evidence": "L은좌측·낮은민주주의신념, R은온건우측·더높은신념. V2는V3보다중도에가깝고민주주의신념도높다. V4는R과가까운우측·높은신념, V1은중도·가장높은신념이다."
    },
    {
      "location": "공식 그림2",
      "evidence": "2015→2026 비율: 좌파5→20, 중도좌파22→22, 중도48→10, 중도우파20→33, 우파5→15."
    }
  ],
  "minimal_logic_without_codes": "이념상 양극단 비중이 커지고 중도 비중이 크게 줄어 민주주의 손실을 감수하며 이념 효용을 택하는 경향이 설명된다.④는L승리를 그 유권자가 감소한 결과라고 하여 모형의 설명 방향을 뒤집는다.",
  "intermediate_reasoning": [
    "① V2는V3보다L과의이념친밀도에덜얽매이고민주주의훼손손실을더크게평가하는위치라R지지가능성이높다.",
    "② V4는R에정책상가깝고L의낮은민주주의신념과도차이가커두축모두L재집권에불리하다.",
    "③ 같은조작에이탈하는중도집단비중감소로집권자의감표손실이작아지는방향이다.",
    "⑤ V1에해당하는중도비율감소는본문모형에서조작의감표비용이줄어드는요인이다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "2026년우파가증가했다는한범주만보고, 조작에따른추가손실을평가할때중도비중감소가가지는역할을놓친다."
  },
  "source_restoration": {
    "crop": "data/기본기_연구/prepared_backlog/blind_sources/BPN_official_graphs_crop.png",
    "astra_direct_seen": true,
    "resolved_before_answer_disclosure": true,
    "original_hold_preserved": true
  },
  "scope_limit": "기출의가상X국모형과그림만해석한다. 실제선거결과의단독원인이나실제집단을대상으로한전략을추론하지않는다. 승리를보장하는정확효용계산식도주어지지않았다."
}
```
