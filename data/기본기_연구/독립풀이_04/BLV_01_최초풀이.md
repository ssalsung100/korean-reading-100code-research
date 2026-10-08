

<!-- luna-raw:BLV-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G468",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "2005년수목과대들보예시문단",
      "evidence": "1643→1628년에넓음5·좁음5·넓음6.대들보가장자리7개째부터대응,1650년벌목·1318년생육시작명시."
    }
  ],
  "minimal_logic_without_codes": "가장자리7번째를패턴시작으로두면7~11은넓고12~16은좁으며17~22는다시넓다.20번째가좁다는③이틀리다.",
  "intermediate_reasoning": [
    "① 2005-400=1605년경.",
    "② 10번째는첫넓은5개구간안이다.",
    "④ 본문이제시한1650년경벌목과층위차감관례에따르면15번째는1635년경이다.",
    "⑤ 대들보의생육기록범위1318~1650과기둥기록이겹치는구간에서패턴을대조해야한다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "원문이사용하는벌목연도와층위차감관례를달리세어1년을교정하려하면,문항이명시한근사연대표현과모형을바꾸게된다."
  },
  "source_limit": "예시문단의모든수치·패턴문구는공식HWP텍스트대조부록에서확인했다.[A]범위가첫5문단인지예시문단인지의주장은이미지재검증중이나해당예시문단은양범위에포함되어이계산판정은영향받지않는다.부록범위주장을확정사실로승격하지않는다.",
  "original_hold_preserved": true
}
```
