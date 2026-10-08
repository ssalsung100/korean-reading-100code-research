

<!-- luna-raw:AFD-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G193",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "sdss_linkage_absence_disclosed_before_blind": true,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "1문단여러컴퓨터에블록체인중복저장.",
    "3문단일부데이터가삭제돼도승인된원래데이터복원에는승인과정불필요."
  ],
  "minimal_logic_without_codes": "일부가삭제되어도다른노드에중복저장된원래내용을확인할수있고원래의승인된데이터복원은새승인이필요없다.②가복원이쉬운이유를제공한다.",
  "intermediate_reasoning": [
    "①변경이쉽다는것은본문무결성설명과반대.",
    "③노드수제한은비공개형의설정일뿐일반복원이유아님.",
    "④최초포함의승인필요를원래내용복원과혼동.",
    "⑤다른노드에같은체인을저장하는것과같은체인여러블록에동일내용이중포함을혼동."
  ],
  "most_attractive_wrong_answer": 5,
  "exact_error": "중복저장이라는단어만보고저장단위인노드와블록의위치를바꾼다. 본문은전자를활용하지만후자는검증으로방지한다.",
  "scope_limit": "복구방법의구체절차를새로만들지않고본문의복제위치와승인여부만연결한다.",
  "strict_blind_qualification": "사이트연결부재사전노출보존",
  "quota_status": "unavailable"
}
```
