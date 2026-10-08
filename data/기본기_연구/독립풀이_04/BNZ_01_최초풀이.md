

<!-- luna-raw:BNZ-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G487",
  "selected_answer": 2,
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
      "location": "전담기관 지원 문단 첫 문장",
      "evidence": "재판에서 승소하여 강제집행 절차까지 마쳐야 자녀를 반환시킬 수 있다고 한다."
    },
    {
      "location": "전담기관·재판제도 설명",
      "evidence": "두 제도 모두 효과적이며 합의가 성립해도 실행을 지원하고 외국 기관에 직접 지원을 신청할 수 있다."
    }
  ],
  "minimal_logic_without_codes": "재판상 승소와 실제 반환 집행은 다른 단계다. 승소만으로 반환이 실현되지 않는다는②가 본문에 맞는다.",
  "intermediate_reasoning": [
    "① 둘 다 효과적이라는 본문을 한 제도만 효과적이라고 바꾼다.",
    "③ 반환재판에서 양육권 적합성을 판단하지 못한다는 제한을 원래 나라에서도 변경 불가능하다는 말로 확대했다.",
    "④ 합의 성립 후에도 실행을 지원한다.",
    "⑤ 외국 전담기관에 직접 신청할 수도 있으므로 국적이 다르다는 이유의 지원 배제가 아니다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "외국의 반환재판이 양육권 본안을 판단하지 않는다는 절차상 범위를 원래 법원의 양육권 판단까지 영구 불변이라고 확대한다."
  },
  "scope_limit": "기출이 제시한 협약 모형만 판독하며 현행 법률 자문으로 확대하지 않는다."
}
```
