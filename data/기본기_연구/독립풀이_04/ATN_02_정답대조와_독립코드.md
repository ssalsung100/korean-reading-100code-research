

<!-- luna-raw:ATN-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G310",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "일부 군포 감축을 전면 면제로 바꾸고 서민의 찬성 동기로 단정했다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ATN",
    "ATO",
    "ATP"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ATN-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G310",
  "primary": [
    1
  ],
  "auxiliary": [
    78,
    2
  ],
  "surface": [
    59
  ],
  "decisive_operation": "군포 한 필 감축이라는 양적 감소를 부담의 완전 부재로 바꾼 것을 찾고 그 기대를 서민에게 새로 귀속한 점을 분리한다.",
  "competing_codes": [
    {
      "code": 78,
      "rebuttal": "서민의 찬성 동기를 근거 없이 부가한 것도 오류이나 그 내용의 출발점인 감축/면제 차이가 직접적이다."
    },
    {
      "code": 4,
      "rebuttal": "모든 서민이라는 수량 범위보다 부담량 일부와0의 차이가 핵심이다."
    },
    {
      "code": 59,
      "rebuttal": "개혁이라는 문제 해결 소재가 있으나 선택 오류는 해결 정도의 강화다."
    }
  ],
  "confidence": 0.97,
  "sdss_seen": false
}
```
