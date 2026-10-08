

<!-- luna-raw:AGA-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G197",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "2011.9 X재무악화,2012.12.30 X지급능력이2011.8보다개선;다른요인변화없음.",
    "2013.9 Z채권AAA→AA+,프리미엄은매월1일갱신.",
    "본문Z는보장매도자로기초채권부도손실을부담."
  ],
  "minimal_logic_without_codes": "2011.10은재무악화후라기초채권위험이높고,2013.1은지급능력개선이반영된뒤라위험이낮다. 따라서Z가부도손실을입을가능성이작아진다는③이맞다.",
  "intermediate_reasoning": [
    "① CDS로위험을부담하는주체는X발행자가아니라Z보장매도자.",
    "② 악화후2011.11등급이A-보다높다고할수없음.",
    "④ 2013.3은Z등급하락전AAA상태,10월은AA+상태이므로다른조건같은이전프리미엄은100bp보다높은쪽.",
    "⑤ 2012.12개선이2011.8보다높은지급능력을의미하므로2013.4기초채권등급이BB-보다낮다는방향은맞지않음."
  ],
  "most_attractive_wrong_answer": 4,
  "exact_error": "2013.9Z의지급능력평가가낮아진것을기초자산위험상승처럼읽으면프리미엄변화방향을반대로판정한다. 2012.12의X개선과2013.9의Z하락은서로다른주체·변수.",
  "scope_limit": "구체등급몇단계나프리미엄정확금액은주어지지않았으므로순서·방향만판정.",
  "quota_status": "unavailable"
}
```
