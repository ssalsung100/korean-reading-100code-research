

<!-- luna-raw:BLD-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G462",
  "selected_answer": 2,
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
      "location": "5~6문단",
      "evidence": "단백질은아미노산서열로구분되고트립신은특정아미노산을인지해그서열의예측가능한지점을자른다."
    },
    {
      "location": "2~4문단",
      "evidence": "동일개체의세포는유전체정보가같고단백질체는기능과양차이를반영한다."
    }
  ],
  "minimal_logic_without_codes": "같은단백질에서잘라낸여러펩타이드는원서열의서로다른구간이므로모두동일서열이라는②는도출되지않는다.절단위치가규칙적이라는것과각조각의서열동일성은다르다.",
  "intermediate_reasoning": [
    "① 본문은동일인간시스템과그세포의유전체정보동일을전제하고분화는단백질조합변화로설명한다.",
    "③ 직접기능을수행하는단백질조합차이가기능차이에연결된다.",
    "④ 원서열·절단규칙·아미노산분자량이알려져있으므로조각분자량을예측가능하다.",
    "⑤ 동일처리조건에서특정유래펩타이드증가는원단백질양증가의지표가되어발암후보로분류가능하다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "펩타이드실측전에는어떤예측도못한다고생각하면이미알려진원서열·절단규칙·아미노산분자량의결합을놓친다."
  },
  "scope_limit": "단백질에따라우연히같은서열조각이반복될수없다고일반화하지않는다.②의일괄동일성주장을배제한다."
}
```
