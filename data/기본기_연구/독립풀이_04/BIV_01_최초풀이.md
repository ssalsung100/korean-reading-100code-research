

<!-- luna-raw:BIV-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G442",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BIV.json",
  "necessary_information": [
    {
      "location": "3/마지막문단",
      "evidence": "GSK3β활성→β카테닌인산화→분해→낮은농도→자기복제유전자꺼짐→상피분화. Wnt자극은GSK3β억제."
    }
  ],
  "minimal_logic_without_codes": "상피분화에는β카테닌이낮아지는방향이필요하다.④의GSK3β억제는인산화·분해를줄여β카테닌을높이므로분화를유도하지않는다.",
  "intermediate_reasoning": [
    "①분비중단,②거리증가,⑤수용체결합실패는Wnt자극을줄여GSK3β활성억제를풀고β카테닌감소쪽이다.",
    "③인산화활발은분해를증가시켜β카테닌감소.④는이와반대이다.",
    "억제제라는단어가있다고언제나줄기세포복제도억제되는것이아니다.무엇의활성을억제하는지에따라최종부호가바뀐다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "수용체돌연변이가분화신호전달을막는다고뭉뚱그리면틀린다.이경로의높은Wnt자극은자기복제유지이고그자극감소가상피분화쪽이다."
  }
}
```
