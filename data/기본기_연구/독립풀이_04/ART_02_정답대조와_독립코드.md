

<!-- luna-raw:ART-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G294",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "해양이 없는 표면에서 같은 위도 지역 간 해류 영향 차이라는 요인이 사라짐을 적용한다. 다른 모든 기후 요인의 통제를 주장하지 않는다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ARR",
    "ARS",
    "ART"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ART-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G294",
  "primary": [
    46
  ],
  "auxiliary": [
    39,
    50
  ],
  "surface": [
    43,
    84
  ],
  "decisive_operation": "해양 부재라는 표 조건을 해류 영향의 지역 차이 경로에 적용하여 같은 위도 지역의 온도 차이 요인이 줄어듦을 추정한다.",
  "competing_codes": [
    {
      "code": 43,
      "rebuttal": "같은 위도 조건은 있지만 지구/화성의 모든 다른 변수가 통제된 실험이 아니다. 이를 통제 인과 추정으로 과장하지 않는다."
    },
    {
      "code": 50,
      "rebuttal": "해양 부재가 해류 효과 경로를 차단한다는 국소 설명으로 유효하다. 전체는 그 경로가 기온 비교에 주는 영향을 적용한다."
    },
    {
      "code": 84,
      "rebuttal": "표에 비율이 있지만 분모·분자 연산이나 수치 계산은 정답 결정에 필요하지 않다."
    }
  ],
  "boundary_note": "화성의 실제 지역 기후를 완전히 예측한 것이 아니라 원문의 특정 원인 요인 제거를 적용한 문항 내 추정이다.",
  "confidence": 0.92,
  "sdss_seen": false
}
```
