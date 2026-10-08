

<!-- luna-raw:BIG-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G437",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BIG.json",
  "necessary_information": [
    {
      "location": "㉡의ⓐ전후",
      "evidence": "주주는부채상환후잔여가치청구,파산손실은자기투자액까지.성공시이익확대와실패시추가손실제한이비대칭유인."
    }
  ],
  "minimal_logic_without_codes": "주주가위험사업을선호하는것은자산-부채차이의상방증대가능성과하방손실제한때문이다.차이가줄어들가능성을높이기때문이라는⑤는선호이유를반대로붙인다.",
  "intermediate_reasoning": [
    "①유한책임,②양의잔여분은주주몫으로본문에명시된다.",
    "③자산이이미부채미만이면주주몫은0이고추가부족액에대한책임도투자액범위밖으로늘어나지않는본문모형이므로일치.현실의평판등추가이해를임의투입하지않는다.",
    "④고위험고수익은성공상방과실패하방가능성이라는본문의선호구조에맞는다.",
    "⑤사업위험이큰것과주주가회사의잔여가치를줄이고싶어하는것은다르다.위험수용동기와추구결과를분리한다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "못갚는부채가커질수록주주의손실도계속커진다고읽으면유한책임으로이미투자액손실이상한에달한다는조건을놓친다."
  },
  "unresolved": "③은본문의유한책임·잔여재산모형범위이다.파산부족액이현실주주의모든비재산적이해와무관하다는확장은하지않는다."
}
```
