

<!-- luna-raw:BGC-blind-20261002-r3-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G417",
  "selected_answer": 2,
  "confidence": 0.98,
  "exposure": {
    "prior_exposure": "unknown",
    "official_answer_read": false,
    "sdss_read": false,
    "existing_case_analysis_read": false,
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "슬로비치 문단",
      "evidence": "보도된 위험을 해석하여 보도대상 신뢰훼손·관련업체 인식 및 소송파장"
    },
    {
      "location": "점화·부정편향 설명 및visual01",
      "evidence": "과거 이미지 연상,부정정보에 큰 비중"
    }
  ],
  "minimal_logic_without_codes": "모델들은 위험 보도를 받아들여 위험과 대상에 대한 인식을 증폭시키는 경로다.②는 보도내용 자체를 믿지 않아 정정을 요구하므로 이 경로의 대상·방향이 다르다.",
  "intermediate_inference": [
    "① 대응실패에서 공포확대,③ 관련업체 책임과 소송은 증폭파장.",
    "④ 과거 조류독감 연상은 점화,⑤ 긍정 신약보다 부정사고에 주목은 부정편향.",
    "②를 실제로 설명하는 다른 심리가 없다는 뜻이 아니라 이 글이 제시한 기제만으로는 그 불신이 도출되지 않는다는 한정이다."
  ],
  "attractive_wrong_answer": 3,
  "exact_error": "③의분뇨→발병 인과가 과학적으로 입증됐는지는 묻지 않는다.의혹이 확산되어 관련기업 소송으로 이어지는 인지·사회파장은 본문 모델이 설명한다.",
  "unresolved": null
}
```
