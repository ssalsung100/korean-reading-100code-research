

<!-- luna-raw:BEM-answer_check-20261002-r2-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G403",
  "all_group_blind_records_before_any_group_answer_check": true,
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "fixed_logic_without_codes": "같은 전송률에서 블록크기2배→전송 반복주기2배.",
  "unresolved": "공식답 일치와 모든 채널의 동일 전송률이 본문에 명시됐는지는 별개. 이질 전송률까지 허용한 보편 진술은 유보.",
  "sdss_disclosed": false
}
```


<!-- luna-raw:BEM-independent_code-20261002-r2-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G403",
  "primary": [
    {
      "code": 91,
      "reason": "전송률 동일 조건에서 블록 크기와 반복주기의 비례관계를 적용한다."
    }
  ],
  "auxiliary": [
    {
      "code": 43,
      "reason": "블록 크기 효과를 주기로 옮길 때 채널별 전송률을 고정해야 한다."
    },
    {
      "code": 92,
      "reason": "주기=블록크기/전송률 관계가 근거다."
    }
  ],
  "surface": [
    {
      "code": 3,
      "reason": "재생 순서는 시간 소재지만 정답의 직접 연산은 크기·주기 비례다."
    }
  ],
  "competing_codes": [
    {
      "code": 45,
      "rejection": "입출력 함수라는 포괄 표현보다 동일률에서2배 관계를 좁혀 기술할 수 있다."
    },
    {
      "code": 17,
      "rejection": "①②③은 방식 속성의 혼동이지만 정답⑤는 수량 관계가 직접 근거다."
    },
    {
      "code": 2,
      "rejection": "④의 무관하게 결정 가능 여부에도 쓰이지만⑤의 동일 전송률 전제가 먼저다."
    }
  ],
  "confidence": 0.87,
  "sdss_disclosed": false
}
```
