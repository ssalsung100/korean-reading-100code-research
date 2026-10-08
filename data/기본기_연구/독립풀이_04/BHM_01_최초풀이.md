

<!-- luna-raw:BHM-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G430",
  "selected_answer": 1,
  "confidence": 0.91,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BHM.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G430_visual01.md",
    "data/기본기_연구/prepared_backlog/blind_sources/G430_visual02.md"
  ],
  "necessary_information": [
    {
      "location": "3문단",
      "evidence": "성장호르몬은 자극 분해 증가와 저장 감소 양쪽으로 지방 축적을 줄임."
    },
    {
      "location": "5문단 및 보기",
      "evidence": "여성은 대퇴부 에스테르화 많고 자극분해 느림.남성은 내장 외부 효소 활성 높고 자극분해 느림.기초분해 고정,다른 조직 매개 효과 제외."
    }
  ],
  "minimal_logic_without_codes": "보기의 투여 호르몬을 관련된 성별·부위 특성에 대응해 저장과 분해 방향을 결합한다.여성호르몬-대퇴부와 남성호르몬-내장은 증가,성장호르몬-내장과 여성호르몬-내장은 감소로 예상하므로ㄱㄴ인①.",
  "intermediate_reasoning": [
    "ㄱ남성 대퇴부에 여성호르몬:여성형 특성의 저장 증가·분해 감소에 따라 지방 증가 예상.",
    "ㄴ낮은 여성호르몬 농도의 여성 내장에 남성호르몬:남성형 저장 증가·분해 감소 방향으로 증가 예상.",
    "ㄷ성장호르몬 보충은 자극 분해를 촉진하고 흡수를 위한 외부 효소를 억제하므로 감소.",
    "ㄹ여성호르몬 보충은 내장 지방 자극 분해가 빠른 여성형 방향으로 감소 예상.",
    "성별 관측 차이만으로 모든 투여량·개인의 결과를 인과적으로 확정할 수 없다.본문의 성호르몬 기능 설명 시도와 문항의 예상 요구 아래 정성 예측이며 기전 미확정이라는 한계를 유지한다."
  ],
  "most_attractive_wrong": {
    "choice": 2,
    "exact_error": "ㄷ에서 호르몬-민감 리파아제 활성화를 저장용 외부 리파아제 활성화로 오인하면 성장호르몬이 축적을 늘린다고 보게 된다.본문은 분해 촉진과 저장 억제를 함께 명시한다."
  },
  "unresolved": "성별 차이의 정성 설명을 약물 효과로 전이하는 문항이다.여성/남성 호르몬의 용량별 작용과 개별 반응은 제시되지 않아 임상·현실 일반화 불가."
}
```
