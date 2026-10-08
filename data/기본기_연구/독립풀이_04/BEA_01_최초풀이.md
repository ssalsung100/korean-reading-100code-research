

<!-- luna-raw:BEA-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G399",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "1문단 도리 좌우·보 전후",
    "2문단 종도리와 처마도리 높이 차",
    "3문단 대공→보→기둥 및 감주의 안정성 감소",
    "4문단 서까래 하중 한계와 중도리 삽입"
  ],
  "minimal_logic_without_codes": "넓힌 지붕의 서까래를 중도리로 추가 지지하므로 하중을 나누어 받는다. 중간 전달 부재와 방향·효과를 보존하여 진술을 대조한다.",
  "intermediate_reasoning": [
    "① 기울기는 두 도리의 높이 차로 설명된다. 도리 길이를 원인으로 제시하지 않는다.",
    "② 대공은 보를 거쳐 기둥으로 하중을 전달한다.",
    "③ 서까래 지지 한계 때문에 중도리와 나뉜 서까래가 필요하므로 하중 분산 진술이 맞다.",
    "④ 좌우 방향 도리는 전후 방향인 측면과 평행하지 않다.",
    "⑤ 감주는 공간 활용도를 높이지만 역학적 안정성은 낮춘다."
  ],
  "attractive_wrong": {
    "choice": 2,
    "exact_error": "하중의 최종 도달점이 기둥이라는 사실을 직접 전달로 바꾸어 보라는 중간 부재를 삭제했다."
  },
  "quota_status": "unavailable"
}
```
