

<!-- luna-raw:AXN-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G344",
  "first_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "사법 집행 비용의 효율성과 시장 경제의 효율성은 다르다. 경제 효과를 덜 분석하는 원칙이 시장 효율을 더 고려한다고 결론낼 수 없다.",
  "group_barrier": "전체3개blind 저장 후 정답만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AXN-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G344",
  "primary": [
    17,
    98
  ],
  "auxiliary": [
    39,
    15
  ],
  "surface": [
    88,
    77
  ],
  "decisive_operation": "효율성의 귀속 대상을 사법 집행 자원과 시장 경제 효과로 나누고, 한쪽의 개선을 다른 쪽의 중시로 옮긴①을 배제한다.",
  "competing_codes": [
    {
      "code": 88,
      "rejection": "효율성이라는 어휘만으로 비용편익 계산으로 삼지 않는다. 비교 대상의 귀속이 먼저 틀렸다."
    },
    {
      "code": 46,
      "rejection": "새 인과 기제를 복원하지 않고 어떤 효율인가를 확인한다."
    },
    {
      "code": 2,
      "rejection": "④의 오류 가능성에는 관여하지만①의 직접 오류는 강도 아닌 대상 교환."
    },
    {
      "code": 98,
      "rejection": "A의 B라는 소유·수식관계를 정확히 추적한다는 점에서17과 국소 같은 역할. 번호별로 억지 분리하지 않는다."
    }
  ],
  "sdss_seen": false,
  "confidence": 0.9,
  "quota_status": "unavailable"
}
```
