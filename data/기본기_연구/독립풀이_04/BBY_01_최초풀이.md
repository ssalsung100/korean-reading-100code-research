

<!-- luna-raw:BBY-blind-20261002-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G381",
  "selected_answer": 1,
  "confidence": 0.95,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BBY.json",
  "needed_information_and_location": [
    "㉠ 유전자가 운반자 주변 환경을 조종해 자기 복제 기회 확대",
    "보기 ㄱ 뇌충 유전자→개미 행동→소 숙주 도달",
    "ㄴ 운반자 질병저항·ㄷ 정자 운동성 및장기 성비"
  ],
  "minimal_logic_without_codes": "어느 유전자의 운반자인지 기준을 고정한 뒤 자기 운반자 밖의 생물학적 환경을 바꿔 복제에 유리하게 만드는 경로를 찾는다.",
  "intermediate_reasoning": [
    "ㄱ 뇌충의 유전자에 대해 운반자는 뇌충,개미는 그 외부 환경/중간 숙주.개미 행동 변경→최종 숙주 소에게 이동.",
    "ㄴ 운반자 자체의 헤모글로빈 형질이 저항성을 줌.환경 조종이 아님.",
    "ㄷ 정자의 내부 운동성 증대가 직접 이득이며 장기 성비 불균형은 불리한 결과.주변 환경 통제로 복제 기회를 넓힌㉠과 다름."
  ],
  "most_attractive_wrong_answer": {
    "choice": 4,
    "exact_error": "ㄴ이 말라리아라는 외부 환경에서 이롭다는 것과 말라리아 환경 자체를 조종하는 것은 다르다.운반자 내부 형질의 적응과 외부 조종 경로 혼동."
  },
  "quota_status": "unavailable"
}
```
