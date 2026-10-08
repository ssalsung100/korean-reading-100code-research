

<!-- luna-raw:BTF-blind-20261005-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G534",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "[가]㉠과㉡",
      "evidence": "㉠은C가B에도우선한다고하고㉡은A-C판결이제3자B에게불이익을주지못한다고반대한다."
    }
  ],
  "minimal_logic_without_codes": "③은판결의B에대한효력제한이라는㉡의근거를C우선을주장하는㉠에게옮겼다.",
  "intermediate_reasoning": [
    "① B는원래설정순서B<C를근거로우선주장가능.",
    "② C는C>A라는판결과A>B라는원순서를이어B보다앞선다고주장가능.",
    "④ 파울루스는소송당사자관계만확정됐다고본다.",
    "⑤ 둘다A-C판결을없애는것이아니라그것이B에미치는효과를다툰다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "판결효력의범위에반대하는것을당사자사이판결자체의무효주장으로혼동한다."
  },
  "scope_limit": "실제법원의판단이나현행저당법을검토하지않고제시된상반주장을재구성한다."
}
```
