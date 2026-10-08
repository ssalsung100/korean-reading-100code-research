

<!-- luna-raw:ALB-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G234",
  "official_answer": 3,
  "blind_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2023/2023_answer_언어이해정답.pdf",
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "logic_without_codes": "실험 결론의 대상과 조작을 보존하여 지지 여부를 판단한다.a는 부착 효과에 제거 효과를 보강하고 c는 결합 이동의 구체 사례이다.b는 핵 유입 신호 대상을 소포체 계통 분비 실험과 섞고 세포 종류별 차이도 보이지 않는다.",
  "correction": "없음",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:ALB-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    63
  ],
  "primary_candidates": [
    63,
    64,
    17
  ],
  "working_primary": 63,
  "unique_primary_confirmed": false,
  "auxiliary": [
    43,
    12
  ],
  "surface": [
    54
  ],
  "judgment_reason": "a와c는 각각 신호 조작 효과·결합 수송의 예측에 맞아 결론을 강화한다.b는 독립 리보솜의NLS 단백질을 소포체 리보솜 유래 단백질의 세포종류별 분비 신호 실험과 바꾸므로㉡ 강화 아님.",
  "competing_codes": [
    {
      "code": 64,
      "verdict": "공동 주 후보",
      "reason": "정답 조합을 가르는b의 논의 대상·결론 범위 일탈이 핵심."
    },
    {
      "code": 17,
      "verdict": "공동 주 후보",
      "reason": "NLS 대상의 합성 계통 귀속을 유지하면b의 연결이 차단된다.64와 국소 중첩."
    },
    {
      "code": 43,
      "verdict": "보조",
      "reason": "a는 해당 단백질의 신호 제거 조작이 이동에 미치는 결과를 비교한다.실험의 모든 잠재 교란을 통제했다고 덧붙이지 않는다."
    },
    {
      "code": 54,
      "verdict": "표면",
      "reason": "본문에 결정이라는 말이 있지만 개별 강화 사례를 보편적 결정 증명으로 올리지 않는다."
    }
  ],
  "minimal_change_test": "b의NLS 제거만으로 세포 종류에 따라 다르다는㉡ 결론을 지지할 수 없다.같은 소포체 계통을 대상으로 종류별 신호 유무 차이를 비교한 결과여야 직접 연결된다.",
  "confidence": 0.94,
  "passage_group": "G234",
  "sdss_seen": false,
  "all_group_answer_check_complete": true,
  "quota_status": "unavailable"
}
```
