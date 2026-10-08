

<!-- luna-raw:ATW-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G313",
  "initial_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "official_answer_source": "prepared_backlog/sealed/answer_sdss.jsonl의 공식 페이지 검증 정본",
  "code_free_logic": "최초 blind에 고정한 세포별 작용 경로/용량과 작용 종류 구분/질환별 목적 구분을 유지한다.",
  "barrier": "group 전체 blind raw 3건 저장 후 공개"
}
```


<!-- luna-raw:ATW-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    46
  ],
  "auxiliary": [
    45,
    17,
    50
  ],
  "surface": [
    52
  ],
  "decisive_operation": "세포별 효소→산물→기능을 연결한 뒤 억제의 효과를 끝까지 추적한다. 위 점막의 COX1 억제→프로스타글란딘 감소→보호 약화.",
  "competitor_refutations": [
    {
      "code": 52,
      "reason": "정답은 보호 촉진 경로를 억제하므로 보호 약화다. 억제의 억제로 최종 촉진되는 경로는 이 정답이 아니다."
    },
    {
      "code": 16,
      "reason": "정의 회수보다 다단계 작용 경로와 세포별 대상 보존이 필요하다."
    },
    {
      "code": 43,
      "reason": "실험 집단 비교에서 타변수 통제를 요구하지 않는다."
    }
  ],
  "boundary_note": "45는 경로의 단계 합성,46은 방향 추적이라는 관점 차이가 커 이번 사례만으로 분리 확정하지 않는다. 50은 효소 억제로 하류 산물 감소하는 개입 경로 보조.",
  "confidence": 0.94,
  "passage_group": "G313",
  "sdss_seen": false
}
```
