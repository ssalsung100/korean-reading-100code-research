

<!-- luna-raw:BHL-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G430",
  "selected_answer": 2,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BHL.json",
  "necessary_information": [
    {
      "location": "1문단",
      "evidence": "지방세포 분비 리파아제는 모세혈관 막에서 혈액 중성지방을 분해해 지방세포 흡수를 돕는다."
    },
    {
      "location": "2~3문단",
      "evidence": "세포 내 호르몬-민감 리파아제는 저장 지방 분해·분비에 관여.성장호르몬은 자극 민감도를 높이고 외부 리파아제 활성을 낮춘다."
    }
  ],
  "minimal_logic_without_codes": "효소의 이름이 같아도 분비 주체·작용 장소·처리하는 지방이 다르다.지방세포가 분비한 외부 효소의 흡수 기능을 저장 지방의 분비 감소로 옮긴②는 근거가 없다.",
  "intermediate_reasoning": [
    "①성장호르몬→카테콜아민 자극 민감도 증가→호르몬-민감 리파아제 활성 증가로 연결.④많은 에너지 요구시 같은 자극 분해가 활성화.",
    "③췌장 효소 억제는 작은창자 흡수 전 분해를 줄여 흡수·저장 경로를 감소시키는 본문 내 예측.다른 생리 효과를 임의 추가하지 않는다.",
    "⑤혈관 막 효소가 공급하는 지방산·글리세롤 흡수가 증가하면 에스테르화 저장 원료가 늘어난다.",
    "②흡수 촉진과 분비 억제는 동의가 아니며 해당 외부 효소가 세포 내부 분해·분비를 억제한다는 근거가 없다."
  ],
  "most_attractive_wrong": {
    "choice": 1,
    "exact_error": "성장호르몬이 지방세포 분비 리파아제의 활성을 감소시킨다는 문장만 보고 내부 호르몬-민감 효소에도 같은 감소를 적용한다.작용 위치와 기능이 다르다."
  }
}
```
