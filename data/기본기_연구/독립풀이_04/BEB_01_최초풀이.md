

<!-- luna-raw:BEB-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G399",
  "selected_answer": 4,
  "confidence": 0.88,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "2문단 도리마다 기둥, 칸은 기둥 사이 공간",
    "3문단 보로 내부 기둥을 대공으로 대체",
    "4문단 5량가의 종도리1·중도리2·처마도리2"
  ],
  "minimal_logic_without_codes": "다섯 도리의 기본 지지점은 다섯 개이므로 네 칸·내부 기둥 세 개다. 보를 도입하여 하나 이상 내부 기둥을 대체하는 구조에서는 내부 기둥은 최대 두 개 남는다.",
  "intermediate_reasoning": [
    "① 중도리·중대공이 추가되어 보 위 구조는 복잡해진다.",
    "② 보 없이 도리마다 기둥이면 다섯 기둥 사이 네 칸이다.",
    "③ 중간 지지점 높이·위치 변화는 종도리-중도리 및 중도리-처마도리 구간의 경사를 변화시킬 수 있다.",
    "④ 보의 감주 기능을 실제 사용하는 조건에서는 세 내부 기둥을 모두 유지하는 상한 3이 부적절하다. 가능한 수는 0~2로 읽는다.",
    "⑤ 중도리로 지붕을 넓히고 보로 내부 기둥을 제거하면 더 넓은 연속 공간이 가능하다."
  ],
  "attractive_wrong": {
    "choice": 3,
    "exact_error": "종도리와 처마도리의 전체 높이 차만 생각하면 중간 지지점을 움직여 구간별 경사 모양을 바꿀 가능성을 누락한다."
  },
  "uncertainty": "④ 반증은 본문의 보 사용을 감주를 실현하는 기능적 사용으로 읽는다. 내부 기둥을 모두 유지하면서 보만 추가하는 가상 구조를 원문이 물리적으로 금지하는 것은 아니므로 원문 범위 밖 절대 불가능으로 확대하지 않는다."
}
```
