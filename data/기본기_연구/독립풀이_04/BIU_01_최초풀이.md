

<!-- luna-raw:BIU-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G442",
  "selected_answer": 4,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BIU.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G442_visual01.jpg"
  ],
  "necessary_information": [
    {
      "location": "1/마지막문단",
      "evidence": "소낭줄기세포가복제하거나상피세포로분화.분열산물이멀어지면Wnt감소·β카테닌감소로상피분화후융모채움."
    }
  ],
  "minimal_logic_without_codes": "융모상피는소낭성체장줄기세포의분화산물이므로④가맞다.원래줄기세포와밀려나분화한후손세포의정체성을구분한다.",
  "intermediate_reasoning": [
    "①융모는표면적을늘리므로반비례라는방향이틀리다.정확선형비례를추가주장할필요는없다.",
    "②이동하며분화하는것은분열로생긴세포이며소낭의줄기세포자체의위치가그대로옮겨진다는요약은정체성변화를빠뜨린다.",
    "③Wnt분비자는판네스세포,반응자는줄기세포.높은Wnt는자기복제를촉진하고분화는낮은자극에서일어난다.⑤이동방향도분화방향도반대."
  ],
  "most_attractive_wrong": {
    "choice": 2,
    "exact_error": "분열후생긴세포가밀려올라가는사실을분화하지않은원줄기세포의위치이동과동일시한다.본문은새세포의상피분화와공급을설명한다."
  }
}
```
