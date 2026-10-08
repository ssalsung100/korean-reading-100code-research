

<!-- luna-raw:AWM-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G335",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "incidental_adjacent_passage": "G335_visual02.png공식전체페이지우측LEET2023 Q28~30 벤야민 폭력/법지문일부사전노출.해당후속사례strict제외필요.정답·SDSS미노출."
  },
  "needed_information_locations": [
    "그래프점선은저·고진동수양쪽에서민감도역수감소",
    "저주파복사압·고주파산탄지배",
    "거울질량증가→요동감소,출력증가→산탄비개선"
  ],
  "minimal_logic_without_codes": "세로값은1/신호대잡음비여서낮아짐이개선이다. 저진동수복사압은거울질량증가로,고진동수산탄은출력증가로개선하는조합을고른다.",
  "intermediate_reasoning": [
    "ㄱ질량↑복사압감소",
    "ㄴ출력↑산탄비↑;복사압악화는질량증가와함께조정",
    "ㄷ투과율↑이면반사재활용↓로N감소하여산탄비악화",
    "ㄱㄴ=③"
  ],
  "attractive_wrong_answer_and_error": "①: 질량만바꾸면복사압쪽은개선하지만점선의고주파산탄쪽개선을설명못한다.",
  "visuals_reviewed": [
    "G335_visual01.png",
    "G335_visual02.png"
  ],
  "quota_status": "unavailable"
}
```
