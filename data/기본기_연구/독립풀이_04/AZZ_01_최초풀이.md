

<!-- luna-raw:AZZ-blind-20261001-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "selected_answer": 2,
  "confidence": 0.97,
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가; 이번 세션에서 사전 노출 없음. 엄격 blind 성과 자동 확정 안 함"
  },
  "source_read": [
    "AZZ.json",
    "G365_visual01.md"
  ],
  "source_quality": "판단에 필요한 본문·발문·5선지 확인. 보충자료는 BAB의 보기이며 누락 징후 없음.",
  "required_information_and_location": [
    "1문단: 프랑스는 판례로 도입, 여러 나라는 법률 또는 판례로 인정",
    "2문단: 사실관계 파악도 법관의 직무",
    "3문단: 당사자 불복이 없으면 판결 확정 가능",
    "5문단: 독일은 법률상 제한, 한국은 명문 제한 없음; 불복 미경유에도 법관 귀책 등 특별사정 예외"
  ],
  "minimal_logic_without_codes": "하급심도 불복 없이 확정될 수 있고, 불복을 거치지 않은 데 법관 귀책이 있는 특별사정이면 배상 청구가 허용될 수 있다. 따라서 최하위 법원 판결이 배상 대상이 될 가능성을 배제할 수 없다.",
  "intermediate_reasoning": [
    "②는 모든 최하위 판결의 배상책임을 주장하지 않고 대상이 될 가능성만 말한다. 법원 등급 자체를 제외 조건으로 정한 문장이 없다. 확정·위법성·불복 요건을 만족하거나 예외가 성립하는 경로가 남는다.",
    "① 프랑스 도입 방식인 판례를 법률로 바꾼다. ③ 사실관계 파악을 직무에서 제외해 본문과 반대다. ④ 독일의 법률상 제한을 판례만으로 바꾼다. ⑤ 한국에 없다는 별도 제한 규정을 있다고 한다."
  ],
  "most_attractive_wrong_answer": {
    "choice": 1,
    "why_attractive": "여러 나라에서 법률로 인정했다는 구절과 한국의 국가배상법이 눈에 띈다.",
    "exact_error": "여러 나라의 법률 또는 판례라는 분기를 프랑스까지 법률 도입으로 일괄 확장함. 프랑스의 도입 근거는 판례로 명시되어 있다."
  },
  "passage_group": "G365",
  "quota_status": "unavailable"
}
```
