

<!-- luna-raw:AFE-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G193",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "sdss_linkage_absence_disclosed_before_blind": true,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "마지막문단노드수증가시성능저하,노드수감소시탈중앙성저하.",
    "보기A는노드10고정·더빠른승인알고리즘, B는노드수제한없음·현재200·A보다위조불가능성향상."
  ],
  "minimal_logic_without_codes": "B의노드수가감소할때본문의변수관계를적용하면성능은높아지고탈중앙성은낮아진다.③.",
  "intermediate_reasoning": [
    "①A승인시간감소는보안성저하방향이므로둘다상승아님.",
    "②노드증가가확장성의자동증가를뜻하지않음. 성능저하가문제.",
    "④제한있는A가비공개형, 제한없는B가공개형으로유형이뒤집힘.",
    "⑤B가위조불가능성을향상시켰다고했으므로A무결성이더높다는결론반대."
  ],
  "most_attractive_wrong_answer": 2,
  "exact_error": "노드수를확대할수있다는말과노드증가를감당하면서성능을유지한다는확장성의조건을혼동한다. 단순노드수증가가확장성향상자체는아니다.",
  "scope_limit": "본문이정의한변화방향과보기조건만적용하며실제시스템설계·공격실행으로확장하지않는다.",
  "strict_blind_qualification": "사이트연결부재사전노출보존",
  "quota_status": "unavailable"
}
```
