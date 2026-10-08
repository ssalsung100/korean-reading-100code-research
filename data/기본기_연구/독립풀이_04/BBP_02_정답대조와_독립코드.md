

<!-- luna-raw:BBP-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G378",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "answer_source": "sealed/answer_sdss.jsonl official_answer; data/meet_questions.jsonl 정본전사",
  "verification_limit": "원 정답표 이번 세션 독립 재확인 없음",
  "all_group_blind_records_before_any_group_answer_check": true,
  "minimal_logic_without_codes": "무대의 연출가는 자신의 몸을 해석 대상으로 제공한다. 이를 다층 해석의 통합 해설자 역할로 바꾸는③이 오류.",
  "original_blind_preserved": true,
  "sdss_seen": false
}
```


<!-- luna-raw:BBP-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G378",
  "primary": [
    {
      "code": 80,
      "reason": "연출가가 성찰 주체이면서 해석 대상이 되는 중첩 역할을 단일 해설 전달자로 오독한③ 배제"
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "연출가 몸/자기 성찰/해설자 역할의 귀속 구별"
    },
    {
      "code": 2,
      "reason": "열린 다층 해석을 한 몸에 통합한 해설로 강화함"
    }
  ],
  "surface": [
    {
      "code": 93,
      "reason": "③ 전달하는 해설자라는 잘못된 소통 모형은 오답 장치"
    },
    {
      "code": 100,
      "reason": "자기를 비추는 거울은 성찰을 설명하는 비유지만③ 결정 자체는 역할 오독"
    }
  ],
  "competitors_rejected": [
    {
      "code": 97,
      "reason": "연출 의도의 정답을 찾는 문제보다 연출가가 해석 대상으로 놓인다는 행위 관계 판단."
    },
    {
      "code": 9,
      "reason": "② 위계 변화는 국소 타당 선지이고③ 정답 핵심 아님."
    },
    {
      "code": 44,
      "reason": "관객에게 몸을 제공하는 목적은 배경. 구체적인 수단 성공/목적 일치 판정 없이도③ 역할 오류 식별."
    }
  ],
  "boundary_note": "80/17의 주체와 대상 역할 보존은 이 사례에서 중첩. 구별이 필요한 조건은 해석 작용이 없이 행위 역할만 교환되는 후속 사례.",
  "confidence": 0.91,
  "sdss_seen": false
}
```
