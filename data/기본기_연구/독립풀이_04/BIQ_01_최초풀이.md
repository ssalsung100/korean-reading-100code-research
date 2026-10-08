

<!-- luna-raw:BIQ-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G440",
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
    "data/기본기_연구/prepared_backlog/blind_sources/BIQ.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G440_visual01.md"
  ],
  "necessary_information": [
    {
      "location": "마지막문단[A]로추정",
      "evidence": "국민국가틀을넘는다중정체성·동등시민권·다층공동체의민주주의."
    },
    {
      "location": "보기",
      "evidence": "(가)출신묻지않는환대,(나)국가보편가치침해우려시종교관습표출금지,(다)지배문화아닌민주적헌정질서에충성."
    }
  ],
  "minimal_logic_without_codes": "[A]와(가)는정체성에따른차별을배제하는방향을공유하고,[A]와(다)는기존국민국가·지배문화중심의관점을바꾸려한다.④가맞다.",
  "intermediate_reasoning": [
    "①무조건환대는이주민정체성동화를조건으로삼지않는다.②[A]는다중정체성을긍정하고단일정체성을요구하지않는다.",
    "③(다)의민주헌정질서존중을기존정치질서무조건준수로옮긴다.[A]도민주주의보존을말하므로질서존중자체만으로대립하지않는다.",
    "⑤(나)는특정종교관습을제한할수있으며(다)는특정윤리지향과의결합을거부하므로차이불용으로읽을수없다.",
    "[A]와(가)의공통차별배제는(가)의적대에도지속되는절대환대모든조건을[A]가공유한다는뜻은아니다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "(다)의헌정가치·원리에대한충성을현재정치규범과질서를변경없이따라야한다는주장으로강화한다.기존지배문화와의결합을거부한다는한정도놓친다."
  },
  "source_limitations": [
    "blind전사에는[A]범위표지가없어새공동체가능성을논하는마지막문단으로추정했다.문단내용은완전하며정확범위는공식원문기계복원대기."
  ]
}
```
