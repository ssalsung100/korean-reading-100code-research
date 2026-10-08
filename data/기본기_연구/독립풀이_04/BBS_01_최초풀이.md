

<!-- luna-raw:BBS-blind-20261002-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G379",
  "selected_answer": 2,
  "confidence": 0.88,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BBS.json",
  "needed_information_and_location": [
    "1문단 삭망월과 월초 설정의 구분",
    "2문단 황도12등분-중기 배당 및29.53/30.44 차이의 누적"
  ],
  "minimal_logic_without_codes": "윤달을 놓는 달의 판별은 달의 월 길이와 황도에 배당된 중기의 간격을 비교해 중기가 없는 달을 찾는 것이다. 월초를 정하는 상대 위치와 윤달을 고르는 규칙을 구별한다.",
  "intermediate_reasoning": [
    "ㄱ 달력상 한 달 길이가 삭망월이므로 고려.",
    "ㄷ 황도12등분에 절기·중기를 배당하여 무중월 식별하므로 고려.",
    "ㄴ 본문은 연 주기/평균 월 길이를 사용하며 운행 속도나 속도 변화를 직접 판별 요소로 제시하지 않음. 다만 평균 각속도와 주기의 수학적 연결까지 부정하지는 않음.",
    "ㄹ 해/달 상대 위치는 첫 문단의 매월1일 설정 조건. 특정 달의 중기 유무 판별과 분리."
  ],
  "most_attractive_wrong_answer": {
    "choice": 5,
    "exact_error": "ㄹ 월초 설정의 근거를 무중치윤법의 직접 고려 요소로 올리고, 달의 월 길이인ㄱ을 빠뜨린다. 상위 달력 제작과 하위 윤달 선정의 범위를 구분해야 한다."
  },
  "quota_status": "unavailable"
}
```
