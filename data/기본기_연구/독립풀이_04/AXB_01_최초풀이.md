

<!-- luna-raw:AXB-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G340",
  "selected_answer": 3,
  "confidence": 0.98,
  "resolved_hold": "AXB-hold-20260928-01",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "source_restoration": "공식문제지의가정만기계복원후blind-only에서직접읽음"
  },
  "needed_information_locations": [
    "복원가정:C/MR²증가,Cm감소,ρm증가,M/R불변",
    "본문정규관성↑핵반경비율↑",
    "경도칭동∝1/Cm",
    "높은외곽밀도설명하는고밀도반지각"
  ],
  "minimal_logic_without_codes": "정규관성증가는핵비율증가,외곽관성감소는경도칭동증가,높은외곽밀도는고밀도반지각비중증가로모델수정한다.",
  "intermediate_reasoning": [
    "ㄱ참:전체반지름고정이므로핵비율증가가핵반경증가",
    "ㄴ거짓:Cm감소면반비례하는칭동은더큼",
    "ㄷ참:다른성분가정을유지한모델에서고밀도반지각을늘려외곽평균밀도증가설명",
    "ㄱㄷ=③"
  ],
  "attractive_wrong_answer_and_error": "⑤:전체정규관성과외곽층관성의변화방향을합쳐칭동을작다고읽기쉽다.칭동에들어가는것은Cm이다.",
  "quota_status": "unavailable"
}
```
