

<!-- luna-raw:AZB-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G357",
  "first_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "구조조정으로퇴직한근로자에게전직제한부담이추가되므로권리형량은효력부정쪽으로움직인다.",
  "group_barrier": "전체blind저장후정답공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AZB-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G357",
  "primary": [
    88,
    63
  ],
  "auxiliary": [
    15,
    39,
    2
  ],
  "surface": [
    79,
    46
  ],
  "decisive_operation": "근로자 권리와 기업이익의 형량에서 일방구조조정이라는 사실이 어느쪽 무게를 키우는지 판정한다. 약화방향이지 최종무효의 확정이 아니다.",
  "competing_codes": [
    {
      "code": 63,
      "rejection": "주어진 사실이 유효성을 약화하는지 평가하므로88의형량방향과 상위행동이 겹친다."
    },
    {
      "code": 46,
      "rejection": "퇴직경위가불이익을키우는연결은있지만 효과발생량을구하거나기제를검증하는문항아님."
    },
    {
      "code": 10,
      "rejection": "단일사실을무효필요충분조건으로만들지않는다.종합고려중어느방향인가가질문."
    },
    {
      "code": 2,
      "rejection": "부정적영향을반드시무효로강화하지않는제한에필요."
    }
  ],
  "sdss_seen": false,
  "confidence": 0.92,
  "quota_status": "unavailable"
}
```
