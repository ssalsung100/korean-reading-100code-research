

<!-- luna-raw:BLR-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G467",
  "selected_answer": 2,
  "confidence": 0.97,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "2문단",
      "evidence": "작용반작용의힘은같고같은힘에서질량과가속도는반비례.기체질량이우주선보다작음."
    },
    {
      "location": "3문단·복원수식",
      "evidence": "원궤도에서중력이클수록속력이빠름.K=mv²/2,U=-GMm/r,E=K+U.중력만작용하면E보존."
    },
    {
      "location": "마지막문단",
      "evidence": "전방분사로일시감속하면작은타원으로진입해주기가짧아짐."
    }
  ],
  "minimal_logic_without_codes": "큰원궤도는지구에서멀고중력이약해원궤도속력이더느리므로지름이클수록빠르다는②가부적절하다.",
  "intermediate_reasoning": [
    "① 추진은작용반작용원리와일치한다.",
    "③ 추가분사없이중력만작용하는타원운동에서는E가보존된다.",
    "④ 같은힘에더작은질량인기체의가속도가더크다.",
    "⑤ 처음감속과나중궤도의짧은공전주기는양립하며본문이명시한다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "처음느려졌으므로이후한바퀴도는시간도반드시길다고직관적으로읽고궤도자체가작아지는효과를제외한다."
  },
  "background_knowledge_used": "거리증가에따른중력약화라는기존물리지식을원궤도중력-속력문장에연결했다.본문의복원식에는힘의역제곱법칙이나원궤도속력식이명시돼있지않으므로그식이원문에있었다고기록하지않는다.",
  "source_restoration": {
    "appendix": "data/기본기_연구/prepared_backlog/blind_sources/BLR-hold-source-20261003-appendix.md",
    "resolved_before_answer_disclosure": true,
    "original_hold_preserved": true
  }
}
```
