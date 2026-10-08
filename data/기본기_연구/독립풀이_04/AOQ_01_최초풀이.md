

<!-- luna-raw:AOQ-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G267",
  "selected_answer": 1,
  "confidence": 0.98,
  "exposure": {
    "current_session": "blind-only,답·태그미열람",
    "historical": "unknown;기존참조0"
  },
  "required_information": [
    "3~5문단:정부주범론은지역재투자법→대출완화→거품/위기;규제실패론이반박."
  ],
  "minimal_logic_without_codes": "①의 저소득층 높은 담보대출 한도는 법이 위험한 대출을 유발했다는 정부주범론을 지지하는 방향이다. 반박 논거로 보기 어렵다.",
  "intermediate_reasoning": [
    "①법에대출완화유도조항있음은정부원인설에유리",
    "②소득과무관한서브프라임연체는저소득층집중원인설에불리한단서",
    "③상업부동산주요거품이면주택자금법중심설명불리",
    "④법적용대출의서브프라임비중낮음은주된연계주장약화",
    "⑤유사법없는나라위기는해당법없이도위기가능함을시사"
  ],
  "attractive_wrong_answer": 2,
  "exact_error": "정부주범론이지역재투자법밖대출완화파급도주장하므로②가결정적반증은아니다.그러나①은반박과반대방향의가장명확한지지근거.",
  "limitation": "②⑤의비교는미국내법의기여가0임을입증하지않는다.⑤만으로다른나라와동일원인을확정할수도없음.발문은반박논거의가능한방향판정."
}
```
