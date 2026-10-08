

<!-- luna-raw:AFJ-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G194",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "source_boundary_residue": "AFK말미##2018학년도잔재보존;group식별미확정"
  },
  "required_information_and_location": [
    "공식[A]는두음의협화도·음정설명부터차를리노의협화음정기준까지.",
    "공식보기표P440,Q550,R660,S880Hz의전체숫자행·하단선직접확인.",
    "본문현악기부분음은기본음진동수의정수배."
  ],
  "minimal_logic_without_codes": "음정은진동수의차가아니라높은값/낮은값이다. P-Q=550/440=5/4, Q-R=660/550=6/5이며1.25>1.2이므로P-Q가더넓다.②의더좁다는틀림.",
  "intermediate_reasoning": [
    "① 5/4이므로장3도.",
    "③ P-R=660/440=3/2이고약분분자·분모모두1~6안이므로협화음정.",
    "④ P의2배부분음880Hz와S의기본음880Hz가일치.",
    "⑤ P-S=2/1옥타브는Q-R=6/5단3도보다본문상협화도가큼."
  ],
  "most_attractive_wrong_answer": 4,
  "exact_error": "기본음440과880이다르다는것만보고모든부분음이서로다르다고확대하면틀린다. 기본음은각복합음의부분음중하나이고정수배성분은겹칠수있다.",
  "visual_verification": [
    "AFJ_A_range_official_crop_20260920.png의이어지는열을포함한실제[A]범위확인.",
    "AFJ_PQRS_official_crop_20260920_v2.png의P/Q/R/S=440/550/660/880전체값확인. v1하단잘림hold와원장보존."
  ],
  "quota_status": "unavailable"
}
```
