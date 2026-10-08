

<!-- luna-raw:BPP-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G501",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "문과 초시·복시·전시 설명",
      "evidence": "초시·복시를 거쳐33명을 먼저 뽑고 전시는 그들의 등수와 품계를 정한다."
    },
    {
      "location": "현량과 시행",
      "evidence": "천거된 이들로 논술시험을 치러28명 합격자를 선발했다."
    }
  ],
  "minimal_logic_without_codes": "현량과 시험은 합격 총원을 선발하지만 전시는 이미 뽑힌 사람의 등수·품계를 정한다.③은 두 시험의 결정 기능을 같게 만든다.",
  "intermediate_reasoning": [
    "① 등급 때문에 다시 과거를 보기도 했다고 한다.",
    "② 학업의 재력과 급제 후 후원·인맥이 출세에 영향을 줬다.",
    "④ 현량과는 자파 세력 키우기라는 비판을 받았다.",
    "⑤ 훈구는 추천의 편파·특혜를 우려하며 기존 시험의 공정성을 내세웠다."
  ],
  "most_attractive_wrong": {
    "choice": 1,
    "exact_error": "과거는처음관직에들어갈사람만보는시험이라고가정하여, 더높은품계를위한재응시를배제한다."
  }
}
```
