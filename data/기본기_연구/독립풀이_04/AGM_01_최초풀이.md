

<!-- luna-raw:AGM-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G200",
  "selected_answer": 4,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "마지막문단미토대사단백질은세포핵DNA로부터합성,사용처는미토콘드리아.",
    "새미토는기존미토의이분분열로만생성. 고세균이진핵세포로전환·원생미토는소기관으로전환."
  ],
  "minimal_logic_without_codes": "미토콘드리아에서사용할단백질을외부의세포핵DNA정보에따라얻으므로미토내부로전달되어야한다.④는미토에서세포질밖으로나가는방향으로바꿔부적절.",
  "intermediate_reasoning": [
    "① 쌍둥이사례가유사성만으로개체성판정불가임을보임.",
    "② 바닷물에는한개체의강한유기적상호작용조건이부족.",
    "③ 기존미토의분열로만생기므로복제하려면기존미토필요.",
    "⑤ 고세균이진핵세포로바뀐전체계승관계는원생미토의부분소기관편입보다강한연결."
  ],
  "most_attractive_wrong_answer": 3,
  "exact_error": "진핵세포가미토증식을조절한다는것을미토없이도새미토를만든다는뜻으로확대하면이분분열의필수원천을놓친다.",
  "scope_limit": "단백질세부합성위치·수송기구를원문밖지식으로추가하지않고정보출처와미토대사사용방향만기록.",
  "quota_status": "unavailable"
}
```
