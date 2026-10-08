

<!-- luna-raw:BNV-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G485",
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
      "location": "보기 X·Y·Z 실험 조건",
      "evidence": "X는 녹색을 받아 적색 형광을 내고 자체 활성산소는 만들지 않으며 빛과 무관하게100%사멸. Y는 적색에서 활성산소를 생성하고 그때100%사멸. Z는 활성산소50%제거. 직접 상호작용은 지정 매개 외에 없음."
    }
  ],
  "minimal_logic_without_codes": "녹색광에서 YZ만 있으면 형광과 활성산소가 없지만 XYZ는 X의 적색 형광이Y를 활성화해 활성산소를 만든다. Z가절반을 없애도 나머지는 존재하므로②의 두 비교가 맞는다.",
  "intermediate_reasoning": [
    "① XZ녹색의 적색형광은 크지만 활성산소는0이므로 YZ적색보다 많다는 말은 틀린다.",
    "③ XZ녹색은 적색형광이 있고 활성산소0, XYZ적색은 형광 없고Y의활성산소가 있으므로 비교 방향이 둘 다 반대다.",
    "④ XZ는 빛과 무관한X로100%사멸하고 YZ녹색은Y가 활성화되지 않는다. 적게 사멸한다는 방향이 틀린다.",
    "⑤ XZ는이미100%사멸하므로 YZ적색이 이를 넘어 더 많이 사멸할 수 없다. Z가활성산소를50%없앤다고 세포사멸률도50%로 고정하지 않는다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "활성산소 제거비율을 세포 사멸비율에 선형으로 복사하거나 Y의 광독성만 보고 X의 무광100%사멸을 누락한다."
  },
  "scope_limit": "보기의 가상 실험 조건과 신호 전달만 판독한다."
}
```
