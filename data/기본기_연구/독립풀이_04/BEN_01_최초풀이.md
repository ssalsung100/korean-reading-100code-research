

<!-- luna-raw:BEN-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G403",
  "selected_answer": 4,
  "confidence": 0.97,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "4문단 시간분할 채널수와 대기",
    "5·6문단 데이터분할 채널당 재생률의2배 이상",
    "7문단 적은 사용자일 때 NVOD 비효율"
  ],
  "minimal_logic_without_codes": "같은 총 전송 능력을 나눌 때 데이터분할 채널당 전송률이2배 이상이면 사용 채널수는 절반 이하일 수 있다. 예시의 정확히2배를 모든 경우의 고정2배로 바꿀 수 없다.",
  "intermediate_reasoning": [
    "① 같은 콘텐츠의 채널수가 늘면 시작 대기를 줄일 수 있다.",
    "② 공동 채널에 개인이 개입하면 다른 수신자에게 영향을 주므로 개인별 제어가 어렵다.",
    "③ 시간분할 채널수n, 수신자u일 때 총 전송은 각각n과u에 비례하므로 감소에는u>n이 필요하다.",
    "④ 데이터분할의 채널 전송률은2배 이상이므로 3배면 채널수는1/3까지 달라질 수 있다. 절반 고정은 불가.",
    "⑤ 적어도 전체의 절반 저장이 필요하다는 제약 때문에 고정 저장 공간에 너무 큰 콘텐츠는 부적합하다."
  ],
  "attractive_wrong": {
    "choice": 3,
    "exact_error": "NVOD는 사용자 수 제한을 극복한다는 장점만 보고 소수 사용자일 때 고정 채널 비용을 빠뜨린다. 데이터양 감소는 이용자가 채널수보다 많아야 한다."
  },
  "uncertainty": "④는 동일한 총 대역을 실제 사용하는 비교를 전제해도 하한2를 등호2로 바꾸는 오류다."
}
```
