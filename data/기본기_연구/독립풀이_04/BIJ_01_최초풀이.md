

<!-- luna-raw:BIJ-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G438",
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
    "data/기본기_연구/prepared_backlog/blind_sources/BIJ.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G438_visual03.md"
  ],
  "necessary_information": [
    {
      "location": "1/마지막문단",
      "evidence": "고유밝기와겉보기밝기비교로거리측정.세페이드주기로고유밝기를추정."
    },
    {
      "location": "3문단/보기",
      "evidence": "세페이드는비대칭밝기변화.대칭은쌍성.성운모양은정체가설근거이지밝기거리측정의근거가아님."
    }
  ],
  "minimal_logic_without_codes": "주기→고유밝기와관측겉보기밝기의차이를거리효과로연결하므로ㄴ이필요하다.원반모양ㄱ과대칭변광성ㄷ은그측정경로에들어가지않는다.ㄴ만인②.",
  "intermediate_reasoning": [
    "ㄱ은성운을독립은하로보는형태유사성논거이나해당거리산출의변수는아니다.",
    "ㄷ은세페이드가아닌쌍성의특징이므로그주기에서세페이드고유밝기관계를적용할수없다.",
    "ㄴ의거리와겉보기밝기관계는고유밝기를이미추정한동일대상에대한비교로적용한다.고유밝기가다른모든별을관측밝기만으로거리정렬하지않는다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "모든변광성의주기에같은고유밝기관계가성립한다고보고대칭변광성ㄷ까지포함한다.본문은세페이드라는대상조건을분리한다."
  }
}
```
