

<!-- luna-raw:BQF-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G506",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2026/2026_answer_2026_LEET_언어이해_정답표.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "분몰부피 변화는 몰수로 가중되어 상쇄되며 희석R과 다수S의 변화량이 같지 않다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "scope_limit": "원blind의 비교기준·절단축 수치유보·G507일부노출을 유지한다."
}
```


<!-- luna-raw:BQF-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G506",
  "minimal_logic_without_codes": "총부피곡선의기울기를R분몰부피로읽고,nR dVR+nS dVS=0에서다른성분의변화를추론한다.몰수가크게다르면반대방향변화의크기도다르다.",
  "primary": [
    {
      "code": 92,
      "reason": "③의변화량동일주장을몰수로가중된관계식에대입해배제한다."
    }
  ],
  "auxiliary": [
    {
      "code": 87,
      "reason": "곡선높이·접선기울기·기울기변화를구별해①②④⑤를판정한다."
    },
    {
      "code": 84,
      "reason": "dVS=-(nR/nS)dVR로희석성분과다수성분변화의크기를비교한다."
    },
    {
      "code": 43,
      "reason": "온도·압력·S몰수고정,첨가R몰수변경의조건을유지한다."
    },
    {
      "code": 49,
      "reason": "양성분분몰부피변화의반대방향을적용한다."
    }
  ],
  "surface": [
    {
      "code": 85,
      "reason": "가중변화합0이라는경쟁제약은있으나두분몰부피자체의단순합이항상일정한것은아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 1,
      "rejection": "총부피의증가/감소만읽으면분몰부피의변화량을묻는③을놓친다."
    },
    {
      "code": 46,
      "rejection": "분자작용이배경이지만③의차이를증명하는직접근거는정량적제약식이다."
    },
    {
      "code": 91,
      "rejection": "가중변화관계를분몰부피자체의고정비례함수로확장할수없다.몰수비도R첨가에따라바뀐다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false,
  "scope_limit": "a에서nR/nS=10^-6.절단축뒤의정확몰수와함수꼴은미상이며수치보간하지않는다."
}
```
