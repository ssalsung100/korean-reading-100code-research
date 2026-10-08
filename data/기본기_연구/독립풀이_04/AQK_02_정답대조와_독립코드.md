

<!-- luna-raw:AQK-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G283",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "역할 준비를 위한 연구와 평소 기자직 동경은 다르며 후자는 근거 없다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "AQK",
    "AQL",
    "AQM"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:AQK-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G283",
  "primary": [
    78
  ],
  "auxiliary": [
    3
  ],
  "surface": [
    93
  ],
  "decisive_operation": "지시받아 이번 역할을 준비했다는 행동의 계기에서 평소 기자직 동경이라는 지속적 동기를 부당하게 추론했는지 확인한다.",
  "competing_codes": [
    {
      "code": 80,
      "rebuttal": "동경은 정신적 태도지만 지식·믿음의 내용보다 행동 이유에 무근거 동기를 부가한 점이 직접적이다. 정신 태도의 넓은 분류에서는 중첩 가능하다."
    },
    {
      "code": 3,
      "rebuttal": "평소/오늘의 시간 차이는 보조다. 단순히 시점만 바꾸어도 기자직 동경이라는 내용 근거 부재가 남는다."
    },
    {
      "code": 93,
      "rebuttal": "언론과 보도는 소재이며 전달자-수신자 경로를 복원해야 정답이 갈리는 문항은 아니다."
    }
  ],
  "boundary_note": "명시 동기가 없다고 반대 동기가 확정되는 것은 아니다. ④는 동경하지 않았다는 반대 사실이 아니라 추론 근거 부재로 배제한다.",
  "confidence": 0.9,
  "sdss_seen": false
}
```
