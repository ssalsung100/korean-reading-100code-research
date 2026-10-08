

<!-- luna-raw:BFJ-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G410",
  "selected_answer": 5,
  "confidence": 0.94,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "스칸단:정자 생산 열→정낭 전도·방출→정낭 표면 온도 상승",
    "동면 중 생산 감소·정소복부,동면후정낭",
    "번식력 성체는 지속 세포 분열",
    "박쥐 번식 계절에 정소정낭 이동"
  ],
  "minimal_logic_without_codes": "정자 생산·정소 위치로 정낭에 전달되는 열이 달라질 조건을 비교해 표면 온도를 관측하면 가설의 예측을 시험할 수 있다. 세 비교 모두 관련이 있다.",
  "intermediate_reasoning": [
    "ㄱ 동면 중보다 후에 생산·외부 정소 방열이 늘어나는 조건을 비교한다.",
    "ㄴ 번식력 있는 성체와 새끼는 정자 생산에 따른 열 발생 차이를 비교한다.",
    "ㄷ 번식기와 이후는 정소 위치·생산 상태가 달라 방열 표면 온도 예측을 비교한다.",
    "표면온도라는 종속 지표가 가설의 마지막 예측과 직접 연결되므로 모두 선택."
  ],
  "attractive_wrong": {
    "choice": 3,
    "exact_error": "ㄴ에는 계절별 정소 이동이 없다는 이유로 배제하면 가설의 또 다른 핵심 원인인 정자 생산 과정의 열 발생을 놓친다."
  },
  "uncertainty": "계절·연령 비교는 외기 온도·체격·대사 등 통제 필요. 단순 관찰만으로 가설을 유일하게 입증한다는 뜻은 아니고 시험 가능한 비교라는 관련성 판정."
}
```
