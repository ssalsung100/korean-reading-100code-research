

<!-- luna-raw:AWL-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G335",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "incidental_adjacent_passage": "G335_visual02.png공식전체페이지우측LEET2023 Q28~30 벤야민 폭력/법지문일부사전노출.해당후속사례strict제외필요.정답·SDSS미노출."
  },
  "needed_information_locations": [
    "길이변화시간에따라빛세기변화",
    "M5반사→재활용광자증가",
    "공간일정비율변형"
  ],
  "minimal_logic_without_codes": "각개입이광자수와경로길이에미치는방향을연결한다.",
  "intermediate_reasoning": [
    "ㄱ검출은시간적세기변화를보는것이므로거짓",
    "ㄴ반사율감소→재활용N감소→요동감소→복사압잡음감소",
    "ㄷ길이증가→같은변형비율에서변화량증가",
    "ㄴㄷ=⑤"
  ],
  "attractive_wrong_answer_and_error": "ㄴ: 복사압잡음절대량감소와산탄신호대잡음비개선은같은것이아니다.",
  "visuals_reviewed": [
    "G335_visual01.png",
    "G335_visual02.png"
  ],
  "quota_status": "unavailable"
}
```
