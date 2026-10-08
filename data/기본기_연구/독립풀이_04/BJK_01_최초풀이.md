

<!-- luna-raw:BJK-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G447",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BJK.json",
  "necessary_information": [
    {
      "location": "㉠및그전후",
      "evidence": "기본모델아닌성은성염색체유전자지령의추가단계로개체발생중기본모델에서파생.포유류는암컷기본."
    },
    {
      "location": "선지④",
      "evidence": "포유류암컷수정란에수컷결정유전자삽입후고환·음경수컷발달."
    }
  ],
  "minimal_logic_without_codes": "④는기본인암컷발생조건에수컷결정유전자를추가하여비기본수컷기관발달이일어난다는관찰로㉠의유전자·발생단계설명을직접지지한다.",
  "intermediate_reasoning": [
    "①물고기의성체성전환은발생중성염색체유전자추가단계와직접맞지않는다.②온도결정은성염색체유전자지령을직접검증하지않는다.",
    "③성체개구리의화학물질노출후호르몬전환은기본모델과성염색체발생지령의직접근거가아니다.⑤호르몬투여에따른노래행동변화는성전체발생·기관분화와다르다.",
    "가설과양립가능한사례와핵심기제에직접개입한강화사례를구분한다.다른선지를모두㉠의결정적반례라고부르지는않는다."
  ],
  "most_attractive_wrong": {
    "choice": 1,
    "exact_error": "유전자발현감소로수컷이된다는표현에끌리지만성체의환경변화후성전환과성염색체결정유전자에의한개체발생이라는시점·기제조건이다르다."
  }
}
```
