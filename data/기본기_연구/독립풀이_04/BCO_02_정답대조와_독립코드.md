

<!-- luna-raw:BCO-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G386",
  "selected_answer": 5,
  "official_answer": "⑤",
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "answer_verification_scope": "봉인 공식 정답 필드 대조; 원 정답표 독립 시각 확인 미실시",
  "logic_without_codes_fixed": "가열로 없어진 기능을 회복하는 성분은 원래 면역 혈청에 남은 항체가 아니라 보체이다.⑤는 파괴 성분과 보충 성분을 모두 항체로 바꾸었다.",
  "original_blind_preserved": true,
  "sdss_seen": false,
  "group_blind_barrier_verified": true,
  "remaining_uncertainty": "①의 감염 일반화는 문맥적 추론이며 개별 감염 실증으로 확대하지 않음"
}
```


<!-- luna-raw:BCO-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G386",
  "primary_codes": [
    17
  ],
  "auxiliary_codes": [
    19,
    10,
    46
  ],
  "surface_codes": [
    43
  ],
  "decisive_operation": "가열에 견디는 항체와 손실되는 보체를 분리하고 비면역 신선 혈청이 보충하는 성분을 정확히 귀속한다.",
  "competitor_refutations": [
    {
      "code": 19,
      "reason": "기능 상실을 외부 성분으로 보완하는 구조는 직접 적용된다. 그러나 무엇이 부족한지를 바꾼⑤를 배제하려면17 성분 귀속이 필요해 보조로 두며 유일 우선성은 유보한다."
    },
    {
      "code": 43,
      "reason": "정상/면역·가열/신선 비교는 실험 해석 배경이다. 정답은 이미 지문이 고정한 내열성 차이로 판단되므로 새 통제 실험 설계가 핵심은 아니다."
    },
    {
      "code": 10,
      "reason": "항체와 보체가 함께 필요하다는 결합요건은 중요하나 항체를 다시 넣어야 한다는⑤는 남은 성분/사라진 성분의 뒤바꿈으로 먼저 반증된다."
    }
  ],
  "boundary_note": "17/19는 성분 판독과 회복 과정 층위. 비면역 신선 혈청만으로도 특정 균의 용균이 항상 된다는 충분조건 확대 금지.",
  "confidence": 0.89,
  "sdss_seen": false,
  "group_answer_check_complete": true
}
```
