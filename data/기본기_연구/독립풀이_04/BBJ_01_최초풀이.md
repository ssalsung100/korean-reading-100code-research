

<!-- luna-raw:BBJ-blind-20261002-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G376",
  "selected_answer": 1,
  "confidence": 0.85,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BBJ.json",
  "needed_information_and_location": [
    "2문단 팽창에 따른 냉각·정상 물질 생성",
    "4문단 평균/임계 밀도와 팽창·수축",
    "7문단 암흑 에너지에 의한 팽창 가속"
  ],
  "minimal_logic_without_codes": "암흑 에너지는 공간 팽창을 가속한다. 팽창은 냉각과 연결되며, 공간 확대 자체는 정상 물질 총량 증가가 아니다.",
  "intermediate_reasoning": [
    "ㄱ 지문의 팽창→냉각 관계를 가속 팽창에 적용하면 관측 온도 감소를 예상. 가속적으로 감소라는 시간 미분의 엄밀한 강도는 지문만으로 확정되지 않아 정성적 연결로 한정.",
    "ㄴ 공간 확대에서 평균 밀도 증가를 도출할 수 없으며 임계값 초과 증가는 본문의 수축 분기와 연결되어 팽창 가속 설명과 맞지 않음.",
    "ㄷ 초기 생성된 정상 물질 총량이 팽창만으로 늘어난다는 근거 없음. 밀도·부피·총량 구별."
  ],
  "most_attractive_wrong_answer": {
    "choice": 3,
    "exact_error": "ㄴ을 포함하여 팽창 규모나 암흑 에너지의 작용 증가를 평균 밀도 증가로 바꾼다. 평균/임계 관계와 공간 확대를 구분해야 한다."
  },
  "quota_status": "unavailable"
}
```
