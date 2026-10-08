

<!-- luna-raw:BDS-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G396",
  "selected_answer": 3,
  "official_answer": "③",
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "answer_verification_scope": "봉인 공식 정답 필드 대조; 원 정답표 독립 시각 확인 미실시",
  "logic_without_codes_fixed": "분해 장치를 잃으면 제거 경로,샤페론이 줄면 재생 경로가 약해져 스트레스 해소를 방해한다. XBP-1 활성과 개시인자 불활성화는 각각 분해 촉진·새로운 부담 생산 감소로 해소에 기여한다.",
  "original_blind_preserved": true,
  "sdss_seen": false,
  "group_blind_barrier_verified": true,
  "remaining_uncertainty": "BDS는 각 해소 경로를 저해하는 원인 방향 판단이며 하나의 경로 손실이 모든 경우 전체 해소 실패를 보장한다고 읽지 않음."
}
```


<!-- luna-raw:BDS-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G396",
  "primary_codes": [
    46
  ],
  "auxiliary_codes": [
    50,
    44,
    49
  ],
  "surface_codes": [
    52
  ],
  "decisive_operation": "재생·분해·생산억제의 세 경로를 고정한 뒤 각각의 개입이 변성 축적을 늘리는지 줄이는지 판단한다.",
  "competitor_refutations": [
    {
      "code": 50,
      "reason": "ㄴ분해경로 장치 손실은 뒤의 제거 작용을 막고ㄷ샤페론감소는재생을약화하므로46의구체경로단절형."
    },
    {
      "code": 44,
      "reason": "목표가스트레스해소임을고정해야ㄹ합성억제의효과를뒤집지않는다.단백질총량증가가목적이아님."
    },
    {
      "code": 52,
      "reason": "ㄹ은개시인자불활성으로합성감소→변성부담감소.생물체의좋고나쁨을부호로바꾸어억제의억제라는이름만붙이면경로가불명확하다."
    }
  ],
  "boundary_note": "각경로방해의기여원인과다른경로보상에도불구한전체실패의충분조건을구별.",
  "confidence": 0.9,
  "sdss_seen": false,
  "group_answer_check_complete": true
}
```
