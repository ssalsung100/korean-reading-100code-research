

<!-- luna-raw:BLK-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G464",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2020/2020_answer_2020_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "X에서는덜유연한공급측으로부담이확산되고Y에서는수요비탄력적인소비자에게부담이집중된다.두세금이탄력도높은쪽에부담을준다는④는반대다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BLK-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G464",
  "minimal_logic_without_codes": "수요·공급의조정가능성을비교하면X는공급,Y는수요가상대적으로비탄력적이다.낮은탄력도쪽의부담이라는본문기준에반대한④를배제한다.",
  "primary": [
    {
      "code": 15,
      "reason": "탄력도가낮은쪽에더많은부담이라는기준을두세금사례에적용한다."
    }
  ],
  "auxiliary": [
    {
      "code": 49,
      "reason": "조정가능성의상대적크기와실제부담귀착방향을대응한다."
    },
    {
      "code": 17,
      "reason": "법정과세대상과실제부담을지는주체를구분한다."
    },
    {
      "code": 16,
      "reason": "②에서초과부담을세금자체가아닌의사결정왜곡의추가손실로해석한다."
    },
    {
      "code": 64,
      "reason": "⑤의정책목표는각기부유층부담·소비감소이지단순세수증가만이아니다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "탄력계수나세액을계산하지않고보기의변화양상으로상대적탄력성을판독한다."
    }
  ],
  "competing_codes": [
    {
      "code": 43,
      "rejection": "조건을일정하게둔외부실험비교가아니라각사례의명시적조정가능성을읽는다."
    },
    {
      "code": 46,
      "rejection": "부담전가의인과배경은있지만주어진판정규칙과탄력성자료의대응으로정답이결정된다."
    },
    {
      "code": 88,
      "rejection": "세금의사회적최적성을새로비용편익평가하는과제가아니다."
    }
  ],
  "scope_limit": "과세대상·실제부담·초과부담·정책성과를서로독립항목으로기록한다.",
  "confidence": 0.94,
  "sdss_seen": false
}
```
