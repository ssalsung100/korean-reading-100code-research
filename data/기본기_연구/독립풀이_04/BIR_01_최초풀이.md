

<!-- luna-raw:BIR-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G441",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BIR.json",
  "necessary_information": [
    {
      "location": "1문단",
      "evidence": "비개념주의도판단과추론은고차인지·개념적절차라고규정."
    },
    {
      "location": "3~4문단",
      "evidence": "개념주의는감각경험에이미판단·추론·해석이개입한다고주장."
    }
  ],
  "minimal_logic_without_codes": "갈리는것은감각과판단의분리여부이지판단이개념적인지여부가아니다.둘다판단과정에개념내용이들어간다는②에동의한다.",
  "intermediate_reasoning": [
    "①알아채지못하는감각불가능은개념주의,③감각선행은비개념주의의분리절차에해당한다.",
    "④판단·추론이무오류라는주장은어느쪽공통전제로제시되지않는다.감각특권논의와판단오류를구분해야한다.",
    "⑤감각에서판단으로전환할때손실된다는구조는개념주의의별개절차부정과맞지않는다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "감각을통해믿음을얻는일상서술에끌려양측이같은선후구조에동의한다고본다.개념주의는보는것자체에판단이개입한다고본다."
  }
}
```
