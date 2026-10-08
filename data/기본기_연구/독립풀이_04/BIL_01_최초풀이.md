

<!-- luna-raw:BIL-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G439",
  "selected_answer": 2,
  "confidence": 0.97,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BIL.json",
  "necessary_information": [
    {
      "location": "㉢의구법인용",
      "evidence": "세번시집간자의아들·손자는과거응시와현관제수제한."
    },
    {
      "location": "성종명령과수정대전",
      "evidence": "재가한여자의아들·손자는과거응시와모든관직임용제한."
    },
    {
      "location": "마지막문단",
      "evidence": "조씨·김주는예를갖추지않은혼인등으로대명률화간조항처벌.재가남성처벌논의는없음."
    }
  ],
  "minimal_logic_without_codes": "수정법은대상을세번째혼인에서재가로넓혔을뿐아니라제한관직도현관에서모든관직으로넓혔다.기존제재를그대로적용했다는②가틀리다.",
  "intermediate_reasoning": [
    "①다른법률인대명률을적용한처벌이있다.③관직자격이원래없는신분에는관직진출제한이라는제재의실효성이약하거나없다는조건부추론.",
    "④유자광소수의견의재가제재방향을성종이수용.⑤구법의세번째혼인자손불이익이명시됨.",
    "여성재가의일반적금지와혼인절차위반에대한남성처벌을혼동하지않는다.남성이한번처벌됐다는사실은재혼남성처벌규정이있다는증거가아니다."
  ],
  "most_attractive_wrong": {
    "choice": 1,
    "exact_error": "경국대전수정전재가가전면금지되지않았다는사실에서어떠한법률로도처벌할수없었다고확대한다.본문은별개의예절위반을다른법률로처벌한사실을준다."
  },
  "unresolved": "③은관직제한이라는명시제재에관한실효성추론이며사회적낙인등모든효과의부재로확장하지않는다."
}
```
