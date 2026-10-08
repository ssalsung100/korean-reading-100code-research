

<!-- luna-raw:BCZ-blind-20261002-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G389",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "needed_information_and_location": [
    "표의 첫 수 갑·둘째 수 을",
    "발송 고가격·자제 저가격",
    "2문단 변화하지 않으려는 균형과 상이 가격의 분리"
  ],
  "minimal_logic_without_codes": "을의 각 선택을 고정하면 갑은 자제가 더 유리하고, 갑의 각 선택을 고정하면 을은 발송이 더 유리하다. 갑 자제·을 발송에서 누구도 혼자 선택을 바꾸어 이익을 늘릴 수 없고 가격이 달라 분리 균형이다.",
  "intermediate_reasoning": [
    "을 발송: 갑5<7, 을 자제: 갑6<7. 갑 발송: 을10>8, 갑 자제: 을8>7. 안정 상태(7,8)에서 갑 변경은7→5, 을 변경은8→7로 불리하다. 둘 다 발송은 갑이 자제로, 둘 다 자제는 을이 발송으로 이탈한다."
  ],
  "most_attractive_wrong_answer": 1,
  "exact_error": "합산 이익15가 (7,8)의15와 같아도 합계가 균형 기준은 아니다. 둘 다 발송(5,10)에서 갑은 혼자 자제해7을 얻을 수 있다.",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BCZ.json",
  "visual_source": "G389_visual01.md 표를 직접 읽음",
  "quota_status": "unavailable"
}
```
