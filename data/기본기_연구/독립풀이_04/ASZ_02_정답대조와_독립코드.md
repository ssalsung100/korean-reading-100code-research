

<!-- luna-raw:ASZ-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G305",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "A는 성분, B는 투여 경로를 바꾼 비교이며 가설상 증가 원인 제거에 따른 감소를 예측한다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ASY",
    "ASZ",
    "ATA"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ASZ-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G305",
  "primary": [
    46
  ],
  "auxiliary": [
    43,
    50,
    49
  ],
  "surface": [
    74
  ],
  "decisive_operation": "성분 추가와 경구 대사의 두 증가 경로를 각각 제거했을 때 지정 질환 위험이 감소한다는 가설 예측을 적용한다.",
  "competing_codes": [
    {
      "code": 43,
      "rebuttal": "A와B의 고정·변경 조건은 중요하지만 결과 방향은 제거되는 인과 경로를 알아야 정해진다."
    },
    {
      "code": 49,
      "rebuttal": "증감 방향은 결과 표현이고 무엇을 바꾸어 어떤 경로를 끊는지가 결정 근거다."
    },
    {
      "code": 74,
      "rebuttal": "여러 원인 후보가 있으나 새 결과로 경쟁 가설 승패를 선택하기보다 가설이 맞다는 조건 아래 예측한다."
    }
  ],
  "confidence": 0.97,
  "sdss_seen": false
}
```
