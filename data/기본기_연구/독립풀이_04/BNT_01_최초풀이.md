

<!-- luna-raw:BNT-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G485",
  "selected_answer": 4,
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
      "location": "활성산소종 반감기·유효거리 문단",
      "evidence": "반감기 약0.05μs 이하, 발생점 약20nm 안에서 국소 반응한다."
    },
    {
      "location": "감광제 조건·잔류·암세포 축적 문단",
      "evidence": "무광 독성은 낮아야 하고 고농도 감광제는 알레르기를 유발할 수 있다. LDL 수용체가 많은 암세포에 축적된다."
    }
  ],
  "minimal_logic_without_codes": "활성산소종의 작용 시간과 거리가 짧으므로 발생한 암세포에서 멀리 떨어진 정상세포에 대한 영향이 적다는④가 적절하다.",
  "intermediate_reasoning": [
    "① 여드름균의 포르피린에 특정 파장 빛을 쪼여야 하며 빛 차단은 잔류 부작용 관리의 조건이다.",
    "② 빛 없을 때 독성이 낮아야 한다는 감광제 요건을 반대로 썼다.",
    "③ 알레르기는 높은 농도와 관련되고 외부 빛의 깊은 투과 여부가 발생하지 않을 충분조건이라고 제시되지 않았다.",
    "⑤ 선택적 축적은 LDL 수용체와 관련하며 항산화제 병행이 필수라는 말은 없다. 활성산소 제거는 치료 기제를 약화할 수도 있다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "광노출로 생기는 잔류 피부 손상과 고농도에 의한 알레르기를 하나의 원인으로 합치고 빛 투과 차단만으로 알레르기까지 부정한다."
  },
  "scope_limit": "기출 본문 모형의 독해이며 실제 의료 권고로 확장하지 않는다."
}
```
