

<!-- luna-raw:BEE-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G400",
  "selected_answer": 5,
  "confidence": 0.97,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "3문단 지역별 산출차→경지분산→위험감소, 생산감소는 보험료",
    "4문단 다른 위험 대비 방법 가능",
    "보기 ㄱ~ㄹ"
  ],
  "minimal_logic_without_codes": "보험 설명의 핵심 전제, 현상 분포 설명력, 대안 대비 효율성을 각각 검사한다. ㄱ·ㄷ·ㄹ은 설명을 약화하지만 ㄴ은 지속 자체와 양립한다.",
  "intermediate_reasoning": [
    "ㄱ 곡물 위험만으로 설명하면 공동 방목 유무에 따른 분포 차이를 추가 설명해야 한다. 방목 있는 곳에 주로 나타나는 증거는 설명을 약화할 수 있다.",
    "ㄴ 교환·매매가 가능해도 보험 이익이 있다면 흩어진 땅을 유지할 수 있어 반박이 아니다.",
    "ㄷ 좁은 지역의 산출 편차가 작다면 분산으로 얻는 보험 이익의 전제가 약해진다.",
    "ㄹ 통합 생산과 영주의 재분배가 더 효율적이면 비효율적 생산을 감수하는 분산 경작의 선택 이유가 약해진다."
  ],
  "attractive_wrong": {
    "choice": 3,
    "exact_error": "ㄱ이 보험 설명과 논리적 모순은 아니라는 이유로 제외한다. 발문은 반증만이 아니라 비판도 묻기 때문에 설명력의 약화가 포함된다."
  },
  "uncertainty": "ㄱ에는 지역 간 다른 조건 통제가 없으므로 단독 결정적 반증으로 강화하지 않는다."
}
```
