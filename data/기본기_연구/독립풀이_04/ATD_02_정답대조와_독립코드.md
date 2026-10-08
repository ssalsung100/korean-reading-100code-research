

<!-- luna-raw:ATD-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G306",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "strict_blind_eligible": false,
  "logic_without_codes": "각 하위 중산층의 동일시율이50%미만이라 전체 중산층도 과반이 비동일시한다. 객관 증가와 주관 감소를 분리한다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ATB",
    "ATC",
    "ATD"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ATD-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G306",
  "primary": [
    17
  ],
  "auxiliary": [
    80,
    86,
    12
  ],
  "surface": [
    84,
    46
  ],
  "decisive_operation": "객관 계층과 주관적 동일시의 집단·지표를 구분하고 두 하위집단의 비동일시 과반을 결합해 본문의 박탈감 해석을 적용한다.",
  "competing_codes": [
    {
      "code": 84,
      "rebuttal": "가중 비율 계산이 가능하지만 두 하위집단 모두50%미만이라는 부등식만으로 충분하다."
    },
    {
      "code": 46,
      "rebuttal": "①은 평균소득 상승을 중산층 증가의 원인으로 새로 추정한다. 분류 입력 변화와 실제 사회 변화 원인을 같게 보지 않는다."
    },
    {
      "code": 80,
      "rebuttal": "자기 계층 인식이 핵심 내용이나 객관/주관·중간/중산·하층의 대상 구분이 선지 전체를 결정한다."
    }
  ],
  "independence_limit": "기준문서의 점수표 함수/인과 예시 사전 노출을 보존.",
  "confidence": 0.96,
  "sdss_seen": false
}
```
