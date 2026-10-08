

<!-- luna-raw:BFI-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G410",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "그림 체내→정낭동맥→정소동맥→정소→정소정맥→정낭정맥",
    "혈액온도39→34→33→38.6",
    "3문단 낮게 유지하는 기제와 낮추는 기제 구별"
  ],
  "minimal_logic_without_codes": "망사에서 뜨거운 유입혈액과 차가운 유출혈액이 열을 교환하므로39→34와33→38.6을 설명한다. 정소 통과 중34→33은 그 교환 구간이 아니다.",
  "intermediate_reasoning": [
    "①39도는 체내에서 들어온 혈액이므로 체온에 가깝다.",
    "②⑤는 같은 열 전달을 주는 쪽과 받는 쪽에서 표현한다.",
    "③ 두 변화는 망사의 넓은 접촉 면적과 연결된다.",
    "④는 정소 통과 구간의 추가 냉각을 망사 교환만으로 설명하여 이론 범위를 넘는다."
  ],
  "attractive_wrong": {
    "choice": 5,
    "exact_error": "정맥이 혈액을 내보내므로 열도 무조건 밖으로 내보낸다고 생각한다. 망사 구간에서 상대적으로 차가운 정맥혈은 뜨거운 동맥혈의 열을 받는다."
  }
}
```
