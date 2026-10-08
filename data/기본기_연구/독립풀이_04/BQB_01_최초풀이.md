

<!-- luna-raw:BQB-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G505",
  "selected_answer": 1,
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
      "location": "사례1~2 해설",
      "evidence": "사례1은 대안가능성이 없어도 책임이 있고 사례2는 대안가능성이 없어 죽음의 책임이 없다."
    },
    {
      "location": "사례3 논증 소개",
      "evidence": "구조 결과를 바꿀 수 없지만 결심했다면 구하려고 할 수 있었다는 구분."
    }
  ],
  "minimal_logic_without_codes": "사례1과2 모두 대안가능성이 없으므로 그 유무의 차이가 책임 판단 차이의 이유가 될 수 없다.①이 틀린다.",
  "intermediate_reasoning": [
    "② 행위와 무위에 책임을 묻는 논증을 각각 제시하는 사례 역할이다.",
    "③ 신경과학자의 개입은 결심이 흔들리는 경우의 가정이고 실제 결심은 유지됐다.",
    "④ 사례3의 제안자는 죽음을 자신의 결심과 연결하려 한다.이는 사토리오까지 최종적으로 인정했다는 말이 아니다.",
    "⑤ 자신의 실제 결심은 자유롭고, 대안 경로에서의 방해 가능성과 다르다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "사토리오가 논박한 주장이라는 이유로 그 주장을 보이려는 사례3의 논증상 목적까지 부정하면 안 된다."
  },
  "scope_limit": "책임의 대상이 결심인지 아이의 죽음인지 구별한다.결심의 자유와 결과의 대안가능성을 동일시하지 않는다."
}
```
