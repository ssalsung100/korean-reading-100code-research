

<!-- luna-raw:ASE-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G298",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "구조 유지와 기능·외관 변화를 결합하여 상동기관의 동일성과 차이를 설명한다. 구조 중시는 기능 단독 결정과 다르다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ASD",
    "ASE",
    "ASF"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ASE-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G298",
  "primary": [
    60
  ],
  "auxiliary": [
    5,
    10,
    23
  ],
  "surface": [
    54
  ],
  "decisive_operation": "상동기관의 같은 구조/다른 기능이라는 두 성질을 각각 설명하는 구조 지속과 환경별 변화의 논거를 결합한다.",
  "competing_codes": [
    {
      "code": 5,
      "rebuttal": "유지/변화의 대상 구분이 결정 내용이며60의 논거 결합 과업과 중첩된다."
    },
    {
      "code": 10,
      "rebuttal": "설명에 필요한 논거를 찾는 과업으로 유효하나 그 필요성을 형식적 유일 필수조건으로 과장하지 않고 본문 설명 구조에 제한한다."
    },
    {
      "code": 54,
      "rebuttal": "구조 중시를 기능의 충분한 결정 원인으로 바꾼ㄴ은 오답이다. 우선성은 단독 결정성이 아니다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
