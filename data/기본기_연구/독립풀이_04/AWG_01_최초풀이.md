

<!-- luna-raw:AWG-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G333",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "incidental_adjacent_passage": "G333_visual01.png가공식전체페이지여서오른쪽16~18이민선문학지문일부사전노출. 해당후속group은strict blind제외필요.정답·SDSS노출없음."
  },
  "needed_information_locations": [
    "도식 B(t1)=중년,A(t2)=중년",
    "동일코호트종단/동시점횡단/동일연령시차",
    "정보하나부족으로효과분리불가"
  ],
  "minimal_logic_without_codes": "B(t1)/A(t2)는 연령만 같고 조사연도와출생코호트가함께바뀌어기간·코호트합성효과를얻는시차연구다.",
  "intermediate_reasoning": [
    "① 코호트고정이면남은것은연령+기간",
    "② 동일시점횡단임",
    "③ t2고정해도연령차이남음",
    "④ 동일연령의시차비교",
    "⑤ 같은B의시간변화는종단"
  ],
  "attractive_wrong_answer_and_error": "③: 조사시점을고정했다고생애주기차이까지통제되는것은아니다.",
  "visuals_reviewed": [
    "G333_visual01.png"
  ],
  "quota_status": "unavailable"
}
```
