

<!-- luna-raw:BJI-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G447",
  "selected_answer": 4,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BJI.json",
  "necessary_information": [
    {
      "location": "4~마지막문단",
      "evidence": "Y성결정유전자→고환→테스토스테론→볼프관유지발달.적절시점신호없으면볼프관퇴화."
    }
  ],
  "minimal_logic_without_codes": "Y성결정유전자가없으면본문정상경로의고환·호르몬신호가이어지지않아볼프관이퇴화한다는④가맞다.",
  "intermediate_reasoning": [
    "①수컷을X없음으로규정한근거가없고사람남성은XY이다.②고환과난소의기원은공통단일성선이다.",
    "③항뮐러관인자는고환이먼저분비하며테스토스테론이이를촉진한다는관계는없다.⑤고환형성이뮐러관퇴화보다선행한다.",
    "④는외부호르몬투여등본문에없는우회개입을넣지않는정상발달경로의조건부추론이다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "두호르몬모두고환에서분비된다는공통기원을앞호르몬이뒤호르몬을촉진하는직접인과로바꾼다."
  }
}
```
