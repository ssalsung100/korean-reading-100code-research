

<!-- luna-raw:BBJ-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G376",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "answer_source": "prepared_backlog/sealed/answer_sdss.jsonl의 official_answer; data/meet_questions.jsonl official-page-verified canonical transcript",
  "verification_limit": "원 정답표를 이번 세션에서 독립 재확인하지 않음",
  "all_group_blind_records_before_any_group_answer_check": true,
  "minimal_logic_without_codes": "가속 팽창→냉각의 정성 관계를 적용하되 밀도와 총량을 혼동하지 않는다. ㄱ의 가속적 감소라는 엄밀한 변화율 주장은 답 일치만으로 검증된 것으로 보지 않는다.",
  "original_blind_preserved": true,
  "sdss_seen": false,
  "incidental_exposure": "answer 필드 필터가 site_marked_answer도 표시함. SDSS 코드 태그는 미열람."
}
```


<!-- luna-raw:BBJ-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G376",
  "primary": [
    {
      "code": 46,
      "name": "인과관계",
      "reason": "암흑 에너지→팽창 가속→냉각의 경로를 적용하여 ㄱ을 선택하고 밀도·물질량 증가의 잘못된 연결을 배제"
    }
  ],
  "auxiliary": [
    {
      "code": 49,
      "reason": "팽창과 냉각의 증감 방향 적용;46의 경로 서술과 국소 중첩"
    },
    {
      "code": 84,
      "reason": "ㄴ 공간 부피 확대와 질량/부피인 밀도의 방향 구별"
    },
    {
      "code": 86,
      "reason": "ㄷ 전체 질량과 밀도·공간 크기를 구별"
    }
  ],
  "surface": [
    {
      "code": 87,
      "reason": "가속적이라는 문구는 있으나 변화율 정량식·곡선 부재. 수학적 가속 확정 코드는 보류"
    }
  ],
  "competitors_rejected": [
    {
      "code": 85,
      "reason": "합이 고정된 비중 경쟁을 푸는 문제가 아님. 70/20 퍼센트는 배경."
    },
    {
      "code": 91,
      "reason": "정성적 방향을 정확한 비례법칙으로 승격할 근거 없음."
    },
    {
      "code": 43,
      "reason": "변수 통제 실험이나 동일 조건 비교 설계가 주어지지 않음."
    }
  ],
  "boundary_note": "방향만으로 읽으면49, 매개 경로 복원이 필요하면46. 이 사례는 두 행동이 겹쳐 유일 주 코드의 강한 배타성은 주장하지 않는다. ㄱ 가속적 감소의 엄밀성은 미해결로 유지.",
  "confidence": 0.8,
  "sdss_seen": false
}
```
