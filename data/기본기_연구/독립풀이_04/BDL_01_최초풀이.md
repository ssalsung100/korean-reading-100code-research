

<!-- luna-raw:BDL-blind-20261002-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G394",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "needed_information_and_location": [
    "2문단 난포막 세포의 남성 호르몬 합성",
    "2·5문단 아로마타제는 남성→여성 호르몬 전환",
    "1·3문단 남성 호르몬과 뇌하수체 조절"
  ],
  "minimal_logic_without_codes": "아로마타제는 이미 합성된 남성 호르몬을 여성 호르몬으로 바꾼다.②는 전환의 입력을 산출물로 바꿔 남성 호르몬 합성에 필요하다고 했다.",
  "intermediate_reasoning": [
    "①부고환에서정자활동성.③상위호르몬분비로성호르몬조절.④간질/난포막세포모두합성.⑤황체형성호르몬이간질세포활성화."
  ],
  "most_attractive_wrong_answer": 3,
  "exact_error": "뇌하수체가 여성 호르몬을 직접 만들지 않는다고 조절도 못 하는 것은 아니다.생식샘 자극 호르몬을 통한 간접조절 경로가 있다.",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BDL.json",
  "quota_status": "unavailable"
}
```
