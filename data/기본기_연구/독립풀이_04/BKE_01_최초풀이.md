

<!-- luna-raw:BKE-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G453",
  "selected_answer": 4,
  "confidence": 0.96,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "보기 이미지 (가)/(나)",
      "evidence": "(가)의 사각형 영역이 (나)에 확대되어 보이고 (가)에서 뭉친 점이 (나)에서 네 점으로 분리된다. (가) 30nm 눈금보다 짧은 간격의 점들이 구분된다."
    },
    {
      "location": "3문단",
      "evidence": "코일 전류 증가→초점 거리 감소→배율 증가."
    },
    {
      "location": "2·4문단",
      "evidence": "전자 물질파는 대략 0.01nm 수준이며 내부는 진공. 배율 변화는 전류 조절로 가능."
    }
  ],
  "minimal_logic_without_codes": "(나)는 같은 시료 영역을 더 큰 배율로 관찰한 상이다. 본문의 전류-초점 거리-배율 관계를 적용하면 (나)의 코일 전류가 더 큰 ④가 적절하다.",
  "intermediate_reasoning": [
    "① (가)에서도 30nm보다 가까운 점들이 구분되므로 해상도가 30nm보다 크다는 진술은 맞지 않는다.",
    "② 전자 현미경 내부 진공 조건과 반대다.",
    "③ 본문의 전자 파장 및 미세 구조 구분과 맞지 않는다. 관찰된 점 크기를 파장으로 동일시하지 않는다.",
    "⑤ 배율이 커졌다는 사실로 전자 속력을 3배 작다고 정할 수 없다. 본문은 전류로 배율을 바꾸는 경로를 제시한다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "확대 배율의 비를 전자의 속력 비로 직접 옮긴다. 두 양 사이에 그러한 정량 관계는 제시되지 않았다."
  },
  "source_limit": "visual02 아래쪽 눈금의 글자가 일부 잘려 있으나 사각형 대응과 배율 증가 및 visual01 30nm 눈금은 확인 가능하다. 잘린 눈금의 단위나 정확한 확대비를 추정해 답의 근거로 사용하지 않았다.",
  "scope_limit": "본문의 전자 렌즈 배율 조절 모형에 따른 선지 판정. 임의의 사후 디지털 확대 등 원문 밖 가정은 추가하지 않는다."
}
```
