

<!-- luna-raw:BNM-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G482",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "본문 계정 계산법",
      "evidence": "이해관계자 편익을 합하고 비용 보전된 지원금을 비용으로 차감하여 미회수 순편익을 구한다."
    },
    {
      "location": "보기",
      "evidence": "정상 진료10, 본인부담2, 지자체3. 2021년100회; 2022년150회에 주민1·기업3 추가. 다른 조건 불변."
    }
  ],
  "minimal_logic_without_codes": "2021년 편익1000, 비용(2+3)×100=500, 순편익500. 2022년 편익1500, 비용(2+3+1+3)×150=1350, 순편익150. 두 해 비용 합은1850이므로1350이라고 한③이 틀린다. 단위는 만원.",
  "intermediate_reasoning": [
    "① 총 진료 편익은1500-1000=500 증가. 본인부담을 뺀 순편익과 다르다.",
    "② 가격을 통한 본인부담금 회수는300-200=100 증가. 후원금은 가격을 통한 회수와 별도다.",
    "③ 1350은2022년 단년 비용이며2021년500을 누락했다.",
    "④ 사회성과는150-500=-350이다. 활동 횟수가 늘어도 이미 보전된 비용이 더 커지면 잔여 성과는 줄 수 있다.",
    "⑤ 2021년 미회수 잔여는1000-200-300=500이므로 보상액500이다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "진료 제공 횟수와 총편익이 늘면 미회수 순편익도 반드시 늘 것이라고 생각한다. 신규 지원금이 비용으로 차감됨을 놓친다."
  },
  "source_limit": "시각자료1 원그림은 placeholder이나 예제 계산식이 본문에 있고 보기의 수치가 완전하다. 그림 배치 자체는 연구 근거로 주장하지 않는다."
}
```
