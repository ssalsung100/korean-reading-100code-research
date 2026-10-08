

<!-- luna-raw:BJJ-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G447",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BJJ.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G447_visual01.md"
  ],
  "necessary_information": [
    {
      "location": "보기",
      "evidence": "XY,항뮐러관인자·테스토스테론생산가능,테스토스테론·DHT수용체결함,음경·음낭없음,외부성징여성."
    },
    {
      "location": "본문4~5문단",
      "evidence": "Y신호로고환형성,고환에서호르몬분비.항뮐러관인자로뮐러관제거.음낭이고환을감쌈."
    }
  ],
  "minimal_logic_without_codes": "고환생성과호르몬생산은있으나말단수용체반응이없어음낭이형성되지않는다.따라서몸내부의고환을가진다는①.외부형태만으로난소나뮐러관유래기관을추론하지않는다.",
  "intermediate_reasoning": [
    "②테스토스테론수용체반응이없어볼프관의부고환·정관·정낭발달이이어지지않는다.",
    "③고환으로분화했고외부여성형이난소·배란을보장하지않는다.④Y유전자작용은고환·호르몬생산근거로이미일어난것으로읽는다.",
    "⑤항뮐러관인자생산은정상이며그수용체장애는보기에서없으므로뮐러관제거경로는남는다.",
    "수용체결함은명시된테스토스테론·DHT의경로에한정한다.모든호르몬신호가없다고확대하지않는다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "외부성징여성이라는결과를여성내부기관의존재로옮긴다.항뮐러관인자에의한뮐러관제거는테스토스테론/DHT불감성과별개경로다."
  }
}
```
