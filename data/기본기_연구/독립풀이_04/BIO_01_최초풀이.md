

<!-- luna-raw:BIO-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G440",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BIO.json",
  "necessary_information": [
    {
      "location": "2~5문단",
      "evidence": "경계불분명,민간기업관여,원인다양,비공식재원.네트워크전은수평적조정,게릴라전은전선불분명하지만정교하게조직."
    }
  ],
  "minimal_logic_without_codes": "전선이나위계가불명확하다는것은조직이없다는것과다르다.본문은정교한조직과수평적조정을명시하므로비조직적이라는⑤가틀리다.",
  "intermediate_reasoning": [
    "①민간기업이다양한군사서비스제공.②전투원·민간인구분소멸과원인다양성.③시작과끝의불명확성은전후국제법질서와다르다는서술에맞는다.④공식경제외재원방식이열거된다.",
    "네트워크라는표현을위계명령의부재와연결하더라도그것이모든조정·조직의부재를뜻하지않는다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "전쟁의시작과끝이불명확하다는특징에서전후국제법적평화정착이어렵다는본문상비교를놓치면③을배제하게된다.국제법이아예존재하지않는다는강한해석은필요없다."
  }
}
```
