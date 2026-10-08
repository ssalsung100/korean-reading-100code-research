

<!-- luna-raw:ARH-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G290",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "법을 감정으로 거부하는 행위와 구체 조항 부재에서 일반 조항 해석에 감정을 쓰며 판결하는 행위는 다르다. 가장 가까운 견해 판정으로 보존한다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ARF",
    "ARG",
    "ARH"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ARH-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G290",
  "primary": [
    75
  ],
  "auxiliary": [
    8,
    24,
    17
  ],
  "surface": [
    79,
    78
  ],
  "decisive_operation": "질서 확보를 위한 판결 우선 입장을 유지하면서 명시 법조항 거부와 조항 부재에서의 일반조항 해석을 구별해 가장 가까운 견해를 고른다.",
  "competing_codes": [
    {
      "code": 79,
      "rebuttal": "법관의 직무상 당위가 내용이지만 모든 당위가 글쓴이 입장과 맞는 것은 아니다. 규범 귀속과 우선 기준을 확인해야 한다."
    },
    {
      "code": 24,
      "rebuttal": "감정 희생 원칙과 조항 부재에서의 해석 허용은 조건 범위가 다르다. 본문이 명시적 예외 조문을 준 것으로 과장하지 않고 보조 관점으로 둔다."
    },
    {
      "code": 78,
      "rebuttal": "법관의 개인 감정을 말하지만 선택의 핵심은 개인 심리 원인보다 제도적 직무와 글쓴이의 법이념 우선성이다."
    },
    {
      "code": 46,
      "rebuttal": "④의 잘못된 이유 연결을 배제하는 데 쓰이지만⑤의 입장 적합성 전체를 결정하지 않는다."
    }
  ],
  "boundary_note": "⑤의 어떠한 경우에도를 현행 법률의 보편 규정으로 검증한 것이 아니다. 글쓴이 견해에 가장 가깝다는 상대 비교이며 절대 금지의 외부 법적 진실로 확장하지 않는다.",
  "confidence": 0.87,
  "sdss_seen": false
}
```
