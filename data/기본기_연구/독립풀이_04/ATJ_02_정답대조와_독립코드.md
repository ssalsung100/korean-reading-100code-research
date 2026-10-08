

<!-- luna-raw:ATJ-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G308",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "범위 일반화·비용 누락·다른 원인 가능성은 유효한 비판이며 시장 대응을 간과한다는 주장은 본문 왜곡이다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ATH",
    "ATI",
    "ATJ"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ATJ-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G308",
  "primary": [
    63
  ],
  "auxiliary": [
    77,
    88,
    43,
    65
  ],
  "surface": [
    74
  ],
  "decisive_operation": "ㄱ의 외적 적용 한계,ㄷ의 비용편익,ㄹ의 교란 가능성을 각각 확인하고ㄴ의 본문 기능 삭제를 배제한다.",
  "competing_codes": [
    {
      "code": 43,
      "rebuttal": "ㄹ에 결정적이나ㄱ과ㄷ은 각각 적용 범위와 순이익 문제라 모두 통제 문제로 단일화하지 않는다."
    },
    {
      "code": 88,
      "rebuttal": "ㄷ의 실질 경로이며ㄹ의 원인 식별을 비용 문제로 대체할 수 없다."
    },
    {
      "code": 65,
      "rebuttal": "ㄴ 배제의 핵심인 상대 주장 왜곡이며 정답 세 항의 비판 유형과 구분한다."
    }
  ],
  "boundary_note": "유효한 비판이 모두 결론을 완전히 반증한다는 뜻은 아니다.ㄱ은 일반화 범위,ㄷ은 조건부 비용,ㄹ은 인과 단정의 강도를 제한한다.",
  "confidence": 0.98,
  "sdss_seen": false
}
```
