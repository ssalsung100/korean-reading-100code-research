

<!-- luna-raw:ATE-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G307",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "정치 상황의 변화에 따른 신화 이미지 변형이 전체 시기를 관통한다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ATE",
    "ATF",
    "ATG"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ATE-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G307",
  "primary": [
    5
  ],
  "auxiliary": [
    46,
    64
  ],
  "surface": [
    3
  ],
  "decisive_operation": "여러 시대의 신화 이미지 변화를 정치 상황과 연결하여 전체를 포괄하는 중심 명제를 선택한다.",
  "competing_codes": [
    {
      "code": 3,
      "rebuttal": "시간 순서는 제시 틀이며 핵심은 시기에 따른 해석 변화와 그 조건이다."
    },
    {
      "code": 46,
      "rebuttal": "정치 상황의 영향은 핵심 내용으로5와 중첩되며 변화를 단순 나열로만 읽지 않는다."
    },
    {
      "code": 44,
      "rebuttal": "선전 목적은 후반의 일부 구현이고 독재 비판까지 모두 건국 정당화 수단으로 축소할 수 없다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
