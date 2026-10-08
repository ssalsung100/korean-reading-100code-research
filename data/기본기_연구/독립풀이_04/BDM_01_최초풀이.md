

<!-- luna-raw:BDM-blind-20261002-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G394",
  "selected_answer": 1,
  "confidence": 0.97,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "needed_information_and_location": [
    "5문단 지방세포는 유입 남성호르몬을 여성호르몬으로 전환",
    "6문단 남성 생식샘자극호르몬 억제·여성 난소 아로마타제 감소",
    "5문단 여성은 지방세포가 여성호르몬 흡수저장"
  ],
  "minimal_logic_without_codes": "지방세포는 남성 호르몬을 새로 합성하는 장소로 제시되지 않는다. 비만으로 커지는 것은 이를 여성 호르몬으로 바꾸는 작용이다.①은 입력 물질의 전환과 합성 증가를 혼동한다.",
  "intermediate_reasoning": [
    "②뇌하수체억제→황체형성호르몬감소→고환남성호르몬감소.③남성혈중여성호르몬상승,여성은흡수저장으로거의변화없음.④여성지방세포에생성과저장.⑤난소아로마타제감소로여성호르몬생산저하.단양적 농도는본문의 균형저하 설명을 따름."
  ],
  "most_attractive_wrong_answer": 5,
  "exact_error": "남성 호르몬 기질이 늘어도 전환 효소가 감소하면 여성 호르몬도 반드시 늘어난다고 할 수 없다. 본문은 난소 전환 저하와 난자 성숙 장애를 연결한다.",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BDM.json",
  "quota_status": "unavailable"
}
```
