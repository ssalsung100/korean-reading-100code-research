

<!-- luna-raw:BBR-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G379",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "answer_source": "sealed/answer_sdss.jsonl official_answer; data/meet_questions.jsonl 정본전사",
  "verification_limit": "원 정답표 이번 세션 독립 재확인 없음",
  "all_group_blind_records_before_any_group_answer_check": true,
  "minimal_logic_without_codes": "12년 주기의 목성 위치는 어느 해인지 표시하는 수단. 한 해 안의 계절을 가장 잘 표시한다는③은 기능·시간 단위·최상 비교를 바꿈.",
  "original_blind_preserved": true,
  "sdss_seen": false
}
```


<!-- luna-raw:BBR-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G379",
  "primary": [
    {
      "code": 44,
      "reason": "세성기년법이라는 수단의 목적은 연도 식별인데③은 계절 변화 표시로 바꾼다."
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "12년 주기 내 어느 해인지와 한 해 내 계절이라는 시간 범주 구분"
    },
    {
      "code": 45,
      "reason": "목성 위치→연도 대응을 계절 대응으로 교환"
    }
  ],
  "surface": [
    {
      "code": 9,
      "reason": "③ 가장 잘이라는 서열은 근거 없는 추가지만 기능 오류가 선행"
    }
  ],
  "competitors_rejected": [
    {
      "code": 3,
      "reason": "연/계절이라는 시간 말이 있지만 사건 선후 순서 판단 아님."
    },
    {
      "code": 92,
      "reason": "⑤ 0.25×4 계산은 국소 타당 선지이며③의 결정 연산 아님."
    },
    {
      "code": 80,
      "reason": "천의 감지는④의 맥락이고③은 달력 표기의 기능·목적 오류."
    }
  ],
  "boundary_note": "44와45는 수단의 이용 목적과 위치-출력 대응이라는 층위로 중첩.식별 목적 없는 단순 대응표는45로 재분할 가능.",
  "confidence": 0.91,
  "sdss_seen": false
}
```
