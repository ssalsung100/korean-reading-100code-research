

<!-- luna-raw:ASV-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G304",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "현재 모임 속에 과거 인사와 분위기 변화가 회고되어 발생 순서만 따르지 않는다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ASV",
    "ASW",
    "ASX"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ASV-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G304",
  "primary": [
    3
  ],
  "auxiliary": [
    93
  ],
  "surface": [
    80
  ],
  "decisive_operation": "현재 대화 사이에 배치된 과거 회고를 확인해 사건 발생 순서와 서술 순서의 불일치를 판정한다.",
  "competing_codes": [
    {
      "code": 93,
      "rebuttal": "서술 전달 방식으로 포괄 가능하지만 결정 요소는 시간 배열이다."
    },
    {
      "code": 80,
      "rebuttal": "인물 내면 초점 이동은④의 근거이며 정답③의 순서 오류와 다르다."
    },
    {
      "code": 5,
      "rebuttal": "검사실 상황 변화 자체보다 그 변화가 현재 서술 중 회고되는 배치가 핵심이다."
    }
  ],
  "confidence": 0.97,
  "sdss_seen": false
}
```
