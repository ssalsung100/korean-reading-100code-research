

<!-- luna-raw:BFV-blind-20261002-r3-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G415",
  "selected_answer": 3,
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
      "location": "거리 행렬 문단·표1/그림1,2",
      "evidence": "모든 형질의 차이 개수를 비율로 환산해 최소 거리끼리 묶음"
    },
    {
      "location": "분기론 및 확률방법 문단",
      "evidence": "파생 여부는 진화 정보 필요,컴퓨터 계산능력 향상으로 확률법 유용성 증가"
    }
  ],
  "minimal_logic_without_codes": "여러 형질을 하나의 거리값으로 합산한 계통수가 개별 형질 특성을 잘 드러낸다고 한③은 입력 정보와 산출 표상을 혼동한다.",
  "intermediate_inference": [
    "같은 거리값은 서로 다른 형질 조합에서도 나올 수 있다.계통수 가지 자체는 개별 형질을 표시하지 않는다.",
    "① 조류 위치 수정,② 분자/초미세 정보 확대,④ 파생성 판단의 선행 정보,⑤ 계산능력 향상은 근거가 있다."
  ],
  "attractive_wrong_answer": 4,
  "exact_error": "④의 이전 정보를 순환논증으로 오해할 수 있으나 화석에서 날개 출현을 알아야 파생형질을 판별한다는 절차가 명시된다.",
  "unresolved": null
}
```
