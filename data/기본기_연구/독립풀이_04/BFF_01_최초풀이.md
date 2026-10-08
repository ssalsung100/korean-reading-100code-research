

<!-- luna-raw:BFF-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G409",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "단순은 존재하는 정당 모두·이항은 의석과 내각 참여 가능성",
    "지수=1/각비율제곱합",
    "보기 전6·후3, 의석.4/.4/.2, 득표.4/.3/.2/나머지합.1"
  ],
  "minimal_logic_without_codes": "이항에서3당을 세고 의회 지수는1/(.16+.16+.04)=25/9로3보다 작다. 따라서③.",
  "intermediate_reasoning": [
    "① 해산으로 단순 정당수는6에서3으로 감소.",
    "② 선거 후 단순3과 이항3은 같다. 세 당은 의석 보유·내각 구성 관심을 가진다.",
    "③3>25/9.",
    "④ 소수3당의 득표제곱합은 최대.01이므로 선거 지수 분모는 최대.30이고 의회 분모.36보다 작다. 두 지수는 같지 않다.",
    "⑤25/9는3이 아니다."
  ],
  "attractive_wrong": {
    "choice": 5,
    "exact_error": "의석 가진 당이3개라는 원래 개수를 비율에 따라 가중한 유효 지수와 동일시한다."
  },
  "uncertainty": "내각 구성 관심을 참여 가능성과 연결하는 보기의 의도된 조건을 사용했다. 관심만으로 실제 정치적 가능성을 항상 보장하는 일반 명제는 아니다."
}
```
