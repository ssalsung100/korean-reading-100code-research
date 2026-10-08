

<!-- luna-raw:AKG-blind-20260926-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G227",
  "selected_answer": 2,
  "confidence": 0.97,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가; 엄격한 무노출 성과 확정 제외"
  },
  "needed_information_and_location": [
    "본문 마지막: 개체 사이 위계 관계가 있으면 계층법 효과적",
    "보기: 거주지·성별·나이·소득·생활양식의 고객 정보로 유사 고객 묶기",
    "본문2·품질 문단: 범주형 수치 변환·정규화·각자집단시 거리0"
  ],
  "minimal_logic_without_codes": "계통도를 산출할 수 있다는 결과 표현만으로 해당 고객 자료에 계층법이 효과적이라는 결론이 보장되지 않는다. 본문의 근거는 개체 간 위계 관계인데 보기에 고객 사이 위계가 제시되지 않아②의 효과성 근거가 부적절하다.",
  "intermediate_inferences": [
    "① 성별 등 범주형은 수치형으로 바꿔 거리를 적용.",
    "③ K는 사전 결정할 클러스터 수이므로 시장 개수 먼저 정함.",
    "④ 나이·소득은 단위가 달라 정규화.",
    "⑤ 각 고객이 한 집단이면 개체=중심점으로 거리 평균0. 마케팅 효용까지 좋다는 뜻은 아님."
  ],
  "most_attractive_wrong_answer": {
    "choice": 5,
    "attraction": "본문이 개체별 분리를 유용하지 않다고 하므로⑤도 틀린 것처럼 보인다.",
    "error": "⑤는 지표 값0만 말한다. 지표 계산과 실제 목적상 유용성은 다르다."
  },
  "quota_status": "unavailable"
}
```
