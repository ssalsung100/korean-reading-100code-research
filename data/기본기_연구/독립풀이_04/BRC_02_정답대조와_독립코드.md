

<!-- luna-raw:BRC-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G514",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/표/2018/2018_answer/table_001.md 홀수형13~15(공식 HWP 추출 표)",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "헤겔이 칸트에게 부족하다고 보는 구체적 형성과정을 칸트가 지나치게 논한다고 한④가 비판 표적을 바꾼다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BRC-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G514",
  "sdss_seen": false,
  "primary": [
    {
      "code": 75,
      "cluster": "C074_075",
      "reason": "헤겔의 윤리적 형성과정과 칸트의 자기완결적 이성 주체를 분리해 비판 내용을 귀속한다."
    }
  ],
  "auxiliary": [
    {
      "code": 65,
      "reason": "④는 칸트가 논증하지 않은 구체적 함양과정에 편중되었다고 공격하는 왜곡된 표적을 만든다."
    },
    {
      "code": 60,
      "reason": "비판의 논거인 실질 내용·권리·공동체 형성의 부재를 논증 구조로 복원한다."
    }
  ],
  "surface": [
    {
      "code": 82,
      "reason": "헤겔의 발전단계가 있으나 정반합 형식을 조립하지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 63,
      "rejection": "새 증거의 약화 효과보다 해당 비판이 실제 두 견해의 차이에 맞는지 확인한다."
    },
    {
      "code": 73,
      "rejection": "비판들이 출발 전제를 문제 삼을 수 있으나④ 결정은 틀린 표적 귀속이다.어느 전제가 거짓인지 입증하는 별도 과제가 아니다."
    },
    {
      "code": 19,
      "rejection": "칸트의 부족을 헤겔이 보완하는 전체 서술로는 가능하지만④의 과도함/부재 교환을 직접 구별하지 못한다."
    }
  ],
  "confidence": 0.94,
  "scope_limit": "65는 단순 오귀속을 넘어④가 왜곡한 대상을 편중·불균형이라고 공격하므로 실제 논박 표적 검토로 인정한다."
}
```
