

<!-- luna-raw:BDT-blind-20261002-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G396",
  "selected_answer": 4,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "needed_information_and_location": [
    "ㄱA50도응집·ㄴB50안정70응집·ㄷ혼합50A정상",
    "ㄹ세제로응집체용해후세제제거에도A정상",
    "3문단 표면소수성 상호작용이응집유발"
  ],
  "minimal_logic_without_codes": "세제 처리로 응집체가 해체되고 제거 후 A가 정상기능을 회복했으므로 세제가 응집을 유지하는 단백질 사이 소수성 상호작용을 끊는다고 분석한다.",
  "intermediate_reasoning": [
    "①응집원인은소수성잔기의표면노출.②B70도응집은구조변성.③A가보호받고B가보호하는방향이다.⑤ㄹ의최종A정상기능은입체구조회복,즉리폴딩과부합."
  ],
  "most_attractive_wrong_answer": 3,
  "exact_error": "혼합으로 응집이 억제된 표적은 50도에서 단독 응집하던 A이다. B는 그 온도에서 원래 안정하므로 역할 방향은 B가A를 돕는 것이다.",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BDT.json",
  "quota_status": "unavailable"
}
```
