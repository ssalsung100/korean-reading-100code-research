

<!-- luna-raw:BIX-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G443",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BIX.json",
  "necessary_information": [
    {
      "location": "1문단",
      "evidence": "차별금지의취지는인권보호이며그취지에부합하지않으면정당성상실."
    },
    {
      "location": "2~4문단",
      "evidence": "장애속성에따라보호효과다름.성별과연령보호정도차이.소극수정에도약한보호적용."
    }
  ],
  "minimal_logic_without_codes": "인권보호취지에부합하지않으면정당하지않다는진술에서정당하면인권보호취지에부합한다는①을확인한다.",
  "intermediate_reasoning": [
    "②장애속성과업무관련성이효과를달리할수있다는본문과충돌.③헌법이사회적신분차별금지가치를명시하므로틀림.",
    "④연령등은성별보다보호정도가약하다고명시.⑤소극적수정은적용부재가아니라상대적으로약한보호이다.",
    "①을인권보호취지가있으면어떤법규든무조건정당하다는역방향으로확장하지않는다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "보호정도가약함을보호가전혀적용되지않음으로바꾼다.본문은소극수정도차별금지원칙의적용국면으로설명한다."
  }
}
```
