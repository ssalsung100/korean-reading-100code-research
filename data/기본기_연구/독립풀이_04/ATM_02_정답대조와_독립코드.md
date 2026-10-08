

<!-- luna-raw:ATM-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G309",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "선지에서 이미 주어진 채무 사실 아래의 의무 회피와 침해된 자기 권리 관철을 구분한다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ATK",
    "ATL",
    "ATM"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ATM-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G309",
  "primary": [
    37
  ],
  "auxiliary": [
    79,
    78,
    17
  ],
  "surface": [
    88
  ],
  "decisive_operation": "침해된 정당한 자기 권리의 관철이라는 요건을 사례에 적용하여 이미 가진 채무 의무의 회피를 제외한다.",
  "competing_codes": [
    {
      "code": 79,
      "rebuttal": "권리와 의무의 방향이 핵심 내용이며37의 사례 대응과 중첩된다."
    },
    {
      "code": 78,
      "rebuttal": "행동의 목적이 권리 관철인지 의무 회피인지 구별하는 보조다."
    },
    {
      "code": 88,
      "rebuttal": "소액 사건에도 투쟁할 수 있다는⑤는 금전 이익만으로 행동을 평가하지 않는다는 근거다."
    }
  ],
  "boundary_note": "채무자가 입증을 요구할 일반적 절차상 권리 자체를 부정하는 것으로 확대하지 않는다. 이미 돈을 빌렸다는 선지 설정과 필자 개념의 대응만 판단한다.",
  "confidence": 0.96,
  "sdss_seen": false
}
```
