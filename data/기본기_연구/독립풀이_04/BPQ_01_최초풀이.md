

<!-- luna-raw:BPQ-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G501",
  "selected_answer": 1,
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
      "location": "보기 중종 발언",
      "evidence": "별도 시험 방안을 제시하되 추천에서 명과 실이 어긋날 우려를 명심하라고 한다."
    },
    {
      "location": "보기 김정·정광필·남곤 발언",
      "evidence": "김정은 폐단에 얽매이지 말고 교화를 이루자고 하며, 정광필·남곤은 천거의 한계와 기존 제도 변경을 경계한다."
    }
  ],
  "minimal_logic_without_codes": "중종은 새 방식 마련을 지시하면서 추천의 폐단도 경계하므로①이 맞는다.",
  "intermediate_reasoning": [
    "② 김정은 현량과 반대자가 아니라 조광조 쪽 도입 취지를 지지한다.",
    "③ 조광조의 보완 도입을 기존 시험의 전면 대체로 바꿨다.",
    "④ 남곤은 과거 실패와 책임 묻기 어려움을 들어 도입에 반대한다.",
    "⑤ 김정이 가볍게 보는 폐단은 천거의 문제이지 경전 학습 편중이 아니다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "천거제 도입이라는 말을 기존 과거제의 폐지·대체로 읽으면, 본문의 보완 관계와중종의선왕제도유지발언을놓친다."
  }
}
```
