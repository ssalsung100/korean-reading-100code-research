

<!-- luna-raw:BNB-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G479",
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
      "location": "k-익명성 설명",
      "evidence": "마스킹·범주화는 식별자와 준식별자에만 적용한다고 명시한다."
    },
    {
      "location": "ℓ-다양성 설명",
      "evidence": "민감속성의 서로 다른 값 개수를 검사하고 기준 미달 동질집합을 삭제한다."
    }
  ],
  "minimal_logic_without_codes": "②는 식별자·준식별자의 처리 방법을 민감속성에 옮기므로 본문의 모형과 일치하지 않는다.",
  "intermediate_reasoning": [
    "① 휴대전화번호는 일반적으로 직접 식별에 쓰이는 속성이다.",
    "③ 원본과 더 유사한 세부 정보가 보존될수록 식별 가능성을 낮추는 효과는 줄어드는 방향이다.",
    "④ 준식별자 조합의 유일성이 식별을 가능하게 하는 예가 명시된다.",
    "⑤ 레코드는 여러 속성의 조합으로 정의된다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "활용성 지표인 유사도가 높다는 것을 비식별 보호도 더 강해진다는 뜻으로 읽어, 정보 보존과 식별 가능성의 방향을 바꾼다."
  },
  "scope_limit": "기출문항이 정의한 비식별 모형의 적용 대상을 판독한다. 실제 개인의 재식별이나 외부 자료 결합은 수행하지 않는다."
}
```
