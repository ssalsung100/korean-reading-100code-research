

<!-- luna-raw:BJH-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G446",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BJH.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G446_visual02.md"
  ],
  "necessary_information": [
    {
      "location": "㉠설명과자수예시",
      "evidence": "가벌성·규정적용·요건수·시민자유등기준에따라축소확장방향이달라짐."
    },
    {
      "location": "보기",
      "evidence": "공익·진실적시의비처벌규정이언론에서일반시민까지적용확대."
    }
  ],
  "minimal_logic_without_codes": "비처벌혜택이일반시민으로확대되면처벌대상은줄고표현의자유는넓어진다.시민자유를제한한다는②가반대방향이어서틀린다.",
  "intermediate_reasoning": [
    "①가벌성기준은비처벌대상증가로축소.③규정적용대상은언론→일반시민으로확장.",
    "④입법자가처음보호하려던외연보다보호대상이늘어확장.⑤언론이어야한다는명시되지않은부가조건이제거되어요건수기준으로축소.",
    "축소/확장이라는명칭을하나로고정하지않고무엇의크기·범위·제약이달라지는지를각선지에서바꿔읽는다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "보호받는사람이늘었으니모든기준에서확장이라고단정하면요건수가줄었다는별도비교축을놓친다."
  }
}
```
