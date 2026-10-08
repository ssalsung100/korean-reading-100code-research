

<!-- luna-raw:BQD-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G506",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2026/2026_answer_2026_LEET_언어이해_정답표.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "반발력으로 혼합부피가 팽창해도 구성 성분의 비율에 따라 증가 정도가 달라진다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "scope_limit": "원blind의 비교기준·절단축 수치유보·G507일부노출을 유지한다."
}
```


<!-- luna-raw:BQD-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G506",
  "minimal_logic_without_codes": "부피변화는 이종분자 힘의 방향뿐 아니라 구성비율에도 의존한다.반발력인 경우 비율 영향을 제거할 수 없다.",
  "primary": [
    {
      "code": 45,
      "reason": "분몰부피라는 결과가 구성비라는 입력에 의존함을⑤가 삭제한다."
    }
  ],
  "auxiliary": [
    {
      "code": 46,
      "reason": "인력·반발력이 혼합부피에 미치는 경로를 구별한다."
    },
    {
      "code": 16,
      "reason": "분몰부피는 고정조건하 첨가몰수에 대한 총부피 변화라는 정의다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "기호식이 등장하지만⑤의 정오는 계산없이 본문의 비율의존 진술로 결정된다."
    }
  ],
  "competing_codes": [
    {
      "code": 85,
      "rejection": "비율이라는 낱말만으로 일정한 합 아래 비중경쟁이 주연산이 되는 것은 아니다."
    },
    {
      "code": 54,
      "rejection": "구성비만 주어지면 모든 조건과 무관하게 분몰부피가 결정된다는 주장이 아니다.온도·압력·성분종류를 유지한다."
    },
    {
      "code": 43,
      "rejection": "정의의 고정조건은 필요하나⑤는 통제조건과 변경조건을 바꾼 것보다 비율의존 자체를 부정했다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
