

<!-- luna-raw:BDN-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G394",
  "selected_answer": 3,
  "official_answer": "③",
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "answer_verification_scope": "봉인 공식 정답 필드 대조; 원 정답표 독립 시각 확인 미실시",
  "logic_without_codes_fixed": "난소에서 부족해진 여성 호르몬 작용을ㄱ으로 보완하고 과도한 황체 형성 호르몬 분비를ㄷ으로 낮추는 방향이 제시된 장애를 줄인다.ㄴ은 난소에서 이미 낮은 전환 작용을 더 억제하여 불리하다.",
  "original_blind_preserved": true,
  "sdss_seen": false,
  "group_blind_barrier_verified": true,
  "remaining_uncertainty": "③은 난소의 직접 장애 개선 방향과 일치.ㄱ의 뇌하수체 되먹임 및ㄴ의 지방세포 간접경로를 포함한 전신 순효과와 정답 유일성은 미해결."
}
```


<!-- luna-raw:BDN-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G394",
  "primary_codes": [
    46
  ],
  "auxiliary_codes": [
    19,
    50,
    44
  ],
  "surface_codes": [
    49,
    52
  ],
  "decisive_operation": "난소의 남성호르몬 과다·여성호르몬 작용 부족 경로를 복원하여 부족한 작용 보완과 상위과다 신호 억제를 후보로 고른다.",
  "competitor_refutations": [
    {
      "code": 19,
      "reason": "ㄱ은 부족한 여성호르몬 작용 보완.하지만 되먹임 다른 경로가 있어 보충=전체기능개선이라는 충분성은 자동 성립하지 않는다."
    },
    {
      "code": 52,
      "reason": "ㄷ의 과다 신호 억제는 억제를 억제해촉진하는 이중부호와 다르다.경로부호를 실제로 적어야52를 붙일 수 있다.보조 후보로 남기되 필수성은 부정."
    },
    {
      "code": 49,
      "reason": "ㄱㄴㄷ의 국소증감만 합치면 난소와지방세포·뇌하수체 경로를 섞는다.46의 장소별경로 복원이 선행한다."
    }
  ],
  "boundary_note": "주46은 국소 인과 경로 판단.후속 전신 순효과 유보를 포함한다.의약적 사용 권고나 실제 치료효과 단정이 아니라 시험 내 인과관계 연구다.",
  "confidence": 0.78,
  "sdss_seen": false,
  "group_answer_check_complete": true
}
```
