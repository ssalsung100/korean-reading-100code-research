

<!-- luna-raw:ASY-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G305",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "무작위 배치가 치료군의 체계적 건강 선택 편향을 통제하는 차이를 적용한다. 모든 표본 특성이 정확히 같다는 뜻은 아니다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ASY",
    "ASZ",
    "ATA"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ASY-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G305",
  "primary": [
    43
  ],
  "auxiliary": [
    46
  ],
  "surface": [
    44,
    49
  ],
  "decisive_operation": "자기 선택·의사 선택으로 생긴 건강 차이와 무작위 배치의 차이를 확인하여 교란된 비교를 구별한다.",
  "competing_codes": [
    {
      "code": 46,
      "rebuttal": "기존 건강이 결과에 영향을 주는 인과가 있으나 치료 효과를 분리하는 설계 차이가 직접적이다."
    },
    {
      "code": 44,
      "rebuttal": "④의 눈가림과 월경 미재개는 수단/목적 방향 오류지만 정답②의 핵심은 편향 통제다."
    },
    {
      "code": 49,
      "rebuttal": "관찰된 좋은 결과의 동반 관계만으로 치료 인과를 확정하지 않는다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
