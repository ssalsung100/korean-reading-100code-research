

<!-- luna-raw:AGR-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G201",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "1문단 아바타가 보고만지는것으로설정된감각→사용자전달.",
    "2문단 장갑은가상물체의크기·형태·온도등을사용자에게전달하고사용자의손가락·팔움직임에따라아바타를움직임."
  ],
  "minimal_logic_without_codes": "장갑의 두 방향은 아바타 쪽 설정 감각→사용자와 사용자 움직임→아바타다. 사용자와아바타가서로감각반응을주고받는다는⑤는움직임전달을감각전달로바꿨다.",
  "intermediate_reasoning": [
    "① 감각·공간이동장치모두몰입을돕는다고명시.",
    "② 사용자움직임을아바타에게전달.",
    "③ HMD는시차영상을뇌에서조합해입체감을제공.",
    "④ 감각전달장치정의와일치."
  ],
  "most_attractive_wrong_answer": 2,
  "exact_error": "장갑에서가상감각이사용자에게전달되는방향과공간이동장치의움직임전달방향을섞으면사용자→아바타를잘못부정한다. 장치와전달정보의종류를함께유지해야한다.",
  "quota_status": "unavailable"
}
```
