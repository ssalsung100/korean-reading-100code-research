

<!-- luna-raw:BRA-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G513",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/표/2017/2017_answer/table_001.md 홀수형35",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "미국의 계약 위반 배상과 한국의 손해배상 처리가 공통된다.이익 충돌/불성실 유형 및 사실/필자 제안을 구별한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BRA-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G513",
  "sdss_seen": false,
  "primary": [
    {
      "code": 39,
      "reason": "불성실 변호에 대한 손해배상이라는 동일 비교축에서 한국·미국의 공통점을 확인한다."
    }
  ],
  "auxiliary": [
    {
      "code": 83,
      "reason": "한국에서 유죄 판결을 파기해야 한다는 필자 제안을 실제 파기 사례와 구별한다."
    },
    {
      "code": 25,
      "reason": "이익 충돌 유형과 불충분·불성실 유형을 나누어①⑤의 판결 처리를 검증한다."
    },
    {
      "code": 17,
      "reason": "기소 전 피의자와 기소된 피고인이라는 조력 대상 범위를 구별한다."
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "권리와 의무가 주제이지만② 직접 확인은 국가 간 동일 배상 규칙이다."
    }
  ],
  "competing_codes": [
    {
      "code": 23,
      "rejection": "공통점 교집합으로39와 동일 구간을 기술할 수 있다.집합 연산을 별도 필수 행동으로 늘리지 않는다."
    },
    {
      "code": 3,
      "rejection": "사실/향후 제안 구별과 시간이 겹치나 미래시제만으로 규범적 제안을 실현 사실로 볼 수는 없다."
    },
    {
      "code": 75,
      "rejection": "국가별 법제의 귀속은 관점 유지와 닮았지만②는 경쟁 견해의 논증 비교가 아니라 제시 제도 공통성 확인이다."
    }
  ],
  "confidence": 0.94
}
```
