

<!-- luna-raw:AVR-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G328",
  "selected_answer": 2,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_locations": [
    "보기(가) 적도접원통·경선간격고정",
    "본문정적원통:동서확대→남북축소",
    "(나)극중심평면에서북위38은중심밖"
  ],
  "minimal_logic_without_codes": "(가)는위도가있는위치의동서길이가늘어나는상태에서경선간격을고정하므로정적성을위해남북을줄인다. 원은동서로긴모양이된다.",
  "intermediate_reasoning": [
    "② 동서확대·남북축소",
    "① 정형은늘어난동서에남북도맞춰면적확대",
    "③ 정형은모양보존이지면적불변아님",
    "④ 정거는중심으로부터거리보존이지북위38원모양보장아님",
    "⑤ (나)의정적보존이남북연장을보장하지않음;극밖의접선방향확대는남북압축으로보정"
  ],
  "attractive_wrong_answer_and_error": "④: 중심은북극인데원을그린중심은북위38이다. 거리보존과모양보존을혼동하면틀린다.",
  "visuals_reviewed": [
    "G328_visual01.md",
    "G328_visual02.md",
    "G328_visual03.jpeg",
    "G328_visual04.jpeg",
    "G328_visual05.md"
  ],
  "quota_status": "unavailable"
}
```
