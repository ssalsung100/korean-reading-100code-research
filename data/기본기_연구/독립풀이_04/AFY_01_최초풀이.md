

<!-- luna-raw:AFY-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G197",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "공식[A]는가령은행갑은으로시작해기초자산은을발행채권이라는끝까지의예시문단.",
    "앞문단정의:보장매입자는기초채권보유·위험이전,매도자는위험부담·손실보상."
  ],
  "minimal_logic_without_codes": "갑은을채권을매입한보장매입자이고병과CDS를체결해위험을이전한다. 따라서보험회사병이신용위험을부담하는보장매도자여서④.",
  "intermediate_reasoning": [
    "① 갑은기초자산을보유.",
    "② 손실보상역할은갑이아니라병.",
    "③ 을은투자자가아니라채권발행자.",
    "⑤ 병은위험부담대가의프리미엄을받으며부도발생해야만이득인것은아님. 부도시에는손실보상의무."
  ],
  "most_attractive_wrong_answer": 5,
  "exact_error": "보장이부도시작동한다는사실과보험회사가이득을보는조건을뒤섞는다. 보험료수입은부도발생을필수조건으로하지않는다.",
  "visual_verification": "AFY_A_range_official_crop_20260920.png의[A]상하단·㉠갑㉡을㉢병직접확인. AFZ_table_official_crop_20260920.png도동시에직접확인하여앞서읽은XML5행등급·선지대응이원표와일치함을확인.",
  "quota_status": "unavailable"
}
```
