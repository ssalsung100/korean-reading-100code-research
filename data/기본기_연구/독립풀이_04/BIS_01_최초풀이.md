

<!-- luna-raw:BIS-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G441",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BIS.json",
  "necessary_information": [
    {
      "location": "1문단비개념주의",
      "evidence": "비개념적감각이먼저주어지고개념적판단이뒤따름."
    },
    {
      "location": "그림설명",
      "evidence": "멀리서사람으로인지하지만확대하면얼룩·물감이드러남.개념주의는감각에해석이내재한다고설명."
    }
  ],
  "minimal_logic_without_codes": "비개념주의라면사람이라는해석판단전에해석되지않은감각이있어야한다.③이그선행조건을적용한다.",
  "intermediate_reasoning": [
    "①확대해도사람으로보인다는결과는관찰서술과맞지않고이론의필연예측도아니다.",
    "②인지/판단자체를비개념적으로해야한다고말하면감각과개념적판단의구분을지운다.",
    "④근거리·원거리차이를실제대조해야사람을인지한다는추가조건은없다.⑤물감·얼룩구성에대한개념적깨달음이사람인지의필수조건도아니다.",
    "비개념주의를적용하는것이지본문의그림설명을개념주의그대로반복하지않는다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "재료가먼저감각된다는것과재료가물감방울·얼룩이라고개념적으로알아차려야한다는것을혼동한다.후자를사람인지의필수조건으로추가할수없다."
  }
}
```
