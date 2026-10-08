

<!-- luna-raw:AGF-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G198",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "보기벌금+계약무효+쌍방부당이득반환.",
    "본문비례원칙은목적달성에필요한최소제한만허용.",
    "강행위반시반환원칙,급부가비도덕·반사회적이면반환권도부정하는예외."
  ],
  "minimal_logic_without_codes": "벌금만의단속으로목적을달성할수있다면추가무효의강한개입은최소제한원칙에맞지않는다. 따라서계약무효까지판결한것은벌금만으로목적실현이부족하다고고려한③으로이해된다.",
  "intermediate_reasoning": [
    "① 개인간농지임대차는사법관계. 위반했다고사법적용이사라지지않음.",
    "② 벌금은법률위반에따른불이익이며계약무효라서만부과하는것아님.",
    "④ 반사회적급부라면반환권을부정하는원칙인데보기는반환을명함.",
    "⑤ 반환은부당이득에해당하기때문이지해당하지않아서가아님."
  ],
  "most_attractive_wrong_answer": 2,
  "exact_error": "벌금과무효가함께나타난것을무효가벌금의원인인것처럼연결한다. 단속법규에서는계약유효와벌금이함께가능하므로그인과는보장되지않음.",
  "scope_limit": "판결이본문의비례원칙에따른다는문항의전제안에서이유를복원. 모든현실판결이자동으로완전한최소침해증명을했다는일반명제아님.",
  "quota_status": "unavailable"
}
```
