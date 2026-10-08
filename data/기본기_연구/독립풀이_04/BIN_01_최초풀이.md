

<!-- luna-raw:BIN-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G439",
  "selected_answer": 4,
  "confidence": 0.97,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BIN.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G439_visual01.md"
  ],
  "necessary_information": [
    {
      "location": "수정대전문단",
      "evidence": "재가한여자의아들·손자는과거와관직제한.나이·생계형편에따른예외가제시되지않음."
    },
    {
      "location": "보기",
      "evidence": "목씨는첫남편사후오빠중매로남예건과혼례.부모는사망."
    },
    {
      "location": "마지막문단",
      "evidence": "조씨는친척주선없는혼인,김주는예미준수혼인으로처벌.재가상대남성일반처벌은논의없음."
    }
  ],
  "minimal_logic_without_codes": "수정후규정은재가에나이·형편예외를두지않으므로그사정을살펴유죄를가린다는④가본문의확대제재방향과맞지않는다.",
  "intermediate_reasoning": [
    "①오빠의중매가있어조씨의친척주선없는재가죄목과는다르다.②두번째혼인이므로구법의세번혼인자손제재는적용되지않는다.③수정후손자는과거응시금지에포함된다.",
    "⑤남예건은예갖춘혼례를치렀고재가상대남성자체를제재하는규정은본문에추가되지않는다.남녀혼인행위모두동일하게처벌된다고확대하지않는다.",
    "④의유죄라는표현을여성본인에대한정확한형벌까지새로확정하는근거로쓰지않는다.핵심은나이·빈곤사정에대한예외조건을새규정에임의추가했다는점이다."
  ],
  "most_attractive_wrong": {
    "choice": 1,
    "exact_error": "모두과부가재혼했다는표면만보고죄목도같다고판단한다.조씨사건은중매·혼례절차문제가따로있고목씨는오빠중매를거쳤다."
  },
  "unresolved": "수정규정이명시한것은자손의자격제재이다.④로부터목씨본인의구체적형벌이나현실판결절차를새로확정하지않는다."
}
```
