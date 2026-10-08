

<!-- luna-raw:AQH-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G282",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "sealed/answer_sdss.jsonl의 공식 정답 필드; official-page-verified canonical transcript",
  "original_blind_preserved": true,
  "logic_without_codes": "꿈속 그림의 출전을 알아본 사실만 있고 세속적 욕망의 근원을 소설에서 발견했다는 인식은 없다.",
  "group_blind_barrier_verified": [
    "AQG",
    "AQH",
    "AQI",
    "AQJ"
  ],
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AQH-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G282",
  "primary": [
    80
  ],
  "auxiliary": [
    98
  ],
  "surface": [
    78,
    51
  ],
  "decisive_operation": "인식 주체 나가 책에서 확인한 대상은 그림의 출전이다. 이를 욕망의 근원 인식으로 교체한 것을 판별한다.",
  "competing_codes": [
    {
      "code": 78,
      "rebuttal": "돈에 대한 욕망과 행동 동기는 다른 선지의 내용이지만 정답은 나가 무엇을 발견했는지에 관한 인식 내용 오류다."
    },
    {
      "code": 51,
      "rebuttal": "뿌리는 근원을 뜻하지만 실제 원인을 인과적으로 설명하거나 비교하는 과업이 아니다."
    },
    {
      "code": 100,
      "rebuttal": "뿌리의 비유를 풀어도 발견 대상 교체 오류가 남으므로 비유 해독만으로 충분하지 않다."
    }
  ],
  "boundary_note": "80은 주체-인식내용 귀속, 98은 그림의 출전/욕망의 근원의 수식 관계를 붙잡는 보조 표현이며 동일 오류를 중복 계수하지 않는다.",
  "confidence": 0.89,
  "sdss_seen": false
}
```
