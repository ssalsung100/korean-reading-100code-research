

<!-- luna-raw:ATU-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G312",
  "initial_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "prepared_backlog/sealed/answer_sdss.jsonl; 공식 페이지 검증 정본 기반",
  "original_blind_preserved": true,
  "code_free_logic": "최초 blind 논리 구조 유지. ATU①⑤의 엄밀 함축 한계 및 ATV②의 대응 수준 차이는 정답 일치로 해소된 것으로 취급하지 않는다.",
  "barrier": "all_group_blind_records_before_any_group_answer_check 충족"
}
```


<!-- luna-raw:ATU-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    46
  ],
  "auxiliary": [
    17,
    18
  ],
  "surface": [
    49,
    40,
    5
  ],
  "decisive_operation": "통계 특성이 거시적 특징에 의존한다는 관계에서 주체·대상·조건을 보존하고, 척도가 사라진다는 조건과 척도 의존을 대조한다.",
  "code_evidence": {
    "46": "의존 관계의 방향과 조건 복원",
    "17": "통계 특성/거시 특성/상관 길이 척도의 역할 교체",
    "18": "특정 척도 소실과 그 척도 의존의 충돌"
  },
  "competitor_refutations": [
    {
      "code": 49,
      "reason": "상관 길이는 이름일 뿐 두 변수의 증감 상관을 구하는 문항이 아니다."
    },
    {
      "code": 12,
      "reason": "①⑤를 단순 조건문 대우로 정당화할 수 없다. 주 결정은②의 의존 구조 왜곡이다."
    },
    {
      "code": 86,
      "reason": "길이나 질서도의 수치 크기를 비교하지 않는다."
    },
    {
      "code": 77,
      "reason": "서로 다른 물리계 일반화는③의 근거이며 정답②를 고르는 핵심은 아니다."
    }
  ],
  "unresolved": "①의 질서도는 질적 상태 변화로 수용,⑤는 규칙·주기/척도의 대비로 수용한 한계. 엄밀 연역으로 과장 금지.",
  "confidence": 0.87,
  "passage_group": "G312",
  "sdss_seen": false
}
```
