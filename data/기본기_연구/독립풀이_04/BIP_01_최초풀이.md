

<!-- luna-raw:BIP-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G440",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BIP.json",
  "necessary_information": [
    {
      "location": "㉠비판문단",
      "evidence": "새롭다고제시된현상은기존전쟁에도있었고미디어와선택적사례가부각했을뿐이라는주장."
    },
    {
      "location": "새로운양상설명",
      "evidence": "용병·민간참여,내전,게릴라,전투원/민간인구분불명확등."
    }
  ],
  "minimal_logic_without_codes": "비판을뒷받침하려면새로움의특징으로제시된현상이예전에도있었다는사실이어야한다.국가총력전의과거보편화는그특징이아니므로④는직접근거가아니다.",
  "intermediate_reasoning": [
    "①과거용병활용,②과거내전,③과거게릴라,⑤과거민간인/전투원무차별공격은새롭다는특징의과거존재를뒷받침한다.",
    "④가역사적으로오래되었다는형식은같지만내용이새로운전쟁론이내세운차이에대응하지않는다.",
    "선지의사례는주어진근거후보로취급하며실제역사사실전반을여기서별도로검증하거나공격절차로확장하지않는다."
  ],
  "most_attractive_wrong": {
    "choice": 2,
    "exact_error": "현재내전이줄었다는통계비판만읽고과거내전존재의관련성을놓치면안된다.㉠은새로운현상의신규성자체도비판하며내전의과거발생은그방향의근거가될수있다."
  }
}
```
