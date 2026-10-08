

<!-- luna-raw:AWE-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G333",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "incidental_adjacent_passage": "G333_visual01.png가공식전체페이지여서오른쪽16~18이민선문학지문일부사전노출. 해당후속group은strict blind제외필요.정답·SDSS노출없음."
  },
  "needed_information_locations": [
    "생애주기단락:성별·거주지·교육수준별차이",
    "마지막 출생연도=조사연도-연령 식별문제"
  ],
  "minimal_logic_without_codes": "배경별 차이가 있다고 명시했는데②는 무관하다고 바꾼다. 식별문제의 임시우회와완전해결은구분한다.",
  "intermediate_reasoning": [
    "① 두정보로출생연도",
    "③④ 제약·대리변수명시",
    "⑤ 완전분리방법부재와특수조건우회는양립",
    "② 약간차이를무관으로반전"
  ],
  "attractive_wrong_answer_and_error": "⑤: 임시방편이있다는것이세효과의기술적완전분리가능을뜻하지않는다.",
  "visuals_reviewed": [
    "G333_visual01.png"
  ],
  "quota_status": "unavailable"
}
```
