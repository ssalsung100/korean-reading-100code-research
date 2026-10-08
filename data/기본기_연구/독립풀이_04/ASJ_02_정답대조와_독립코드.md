

<!-- luna-raw:ASJ-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G300",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "암석 형성 연대와 모천체를 떠난 이후의 우주 체류 기간은 다른 측정 대상이다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ASJ",
    "ASK",
    "ASL"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ASJ-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G300",
  "primary": [
    3
  ],
  "auxiliary": [
    17,
    98
  ],
  "surface": [
    92
  ],
  "decisive_operation": "암석 형성·모행성 이탈·지구 도달의 서로 다른 시점을 고정해 한 연대를 다른 구간의 길이로 바꾼 오류를 찾는다.",
  "competing_codes": [
    {
      "code": 98,
      "rebuttal": "무엇의 연대인가라는 수식 관계가 중요하지만 시간 구간의 시작·끝을3으로 구체화한다."
    },
    {
      "code": 92,
      "rebuttal": "10억년 수치가 있어도 계산 오류가 아니라 측정하는 기간의 교체다."
    },
    {
      "code": 46,
      "rebuttal": "동위원소 생성 경로는 자료의 기원 설명이며 정답은 연대 지표의 시간적 대상 차이다."
    }
  ],
  "confidence": 0.97,
  "sdss_seen": false
}
```


후속 depth_backfill raw: `AUDIT84-depth_backfill-20260927-01` — [원장 기록](../../../분석/기본기_연구/독립연구_04_절차와_진행기록.md)
