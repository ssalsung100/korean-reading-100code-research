

<!-- luna-raw:BSL-blind-20261005-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G528",
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
      "location": "네근본개념정의·단일권리관계",
      "evidence": "청구권자는상대방에게행위를요구하고그상대방이의무를진다.자유권은상대요구를따르지않아도됨이다."
    }
  ],
  "minimal_logic_without_codes": "권리를가진사람과그권리에대응한의무부담자를구별하면②처럼같은주체의의무를곧바로따르게할수없다.",
  "intermediate_reasoning": [
    "① A의청구권이면상대B의의무라는경우가있다.",
    "③ A의자유권이면B의청구권부재,또는A의형성권이면B의면제권부재다.",
    "④ 동일행위에따르지않을자유권이없는A는그행위의무를지는경우가된다.",
    "⑤ A가B에게행위를요구할청구권이없으면그권리관계의B의무도없다.",
    "④⑤는모든권리부재에대한일반명제가아니라특정권리유형을대입하는존재사례로확인한다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "권리없음에서의무를알수없다고모든권리유형을뭉뚱그리면,따르지않아도될자유의부재와따를의무의관계를놓친다."
  },
  "scope_limit": "단일관계·동일행위에한정한다.다른법률관계의추가의무나일반적권리의무동시보유를부정하지않는다."
}
```
