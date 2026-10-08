

<!-- luna-raw:BEC-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G399",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "5문단 정치·감주·이주 정의 및 전열/후열 위치",
    "보기 ㄱ 앞 공간을 비우고 남은 네 기둥을 뒤로 이동",
    "보기 ㄴ 앞쪽 내부 기둥 두 개만 유지"
  ],
  "minimal_logic_without_codes": "정위치 격자의 내부 기둥을 기준으로 없앤 열과 옮긴 열을 따로 표시한다. ㄱ은 앞 열을 없애고 뒤 열을 이동, ㄴ은 뒤 열을 없애고 앞 열을 유지한다.",
  "intermediate_reasoning": [
    "ㄱ의 5×3칸은 내부 기둥 4×2=8개가 기본이다. 남은 4개는 불단이 놓인 후열이며 앞 열은 제거되었다.",
    "ㄱ 후열은 뒤로 이동하므로 후열이주도 적용된다.",
    "ㄴ의 3×3칸 기본 내부 기둥은 2×2=4개. 중앙 출입문 쪽 두 개만 남겨 후열감주다.",
    "②만 ㄱ 전열감주 유·ㄴ 무에 부합한다. ㄴ의 남은 전열 이동은 제시되지 않았다."
  ],
  "attractive_wrong": {
    "choice": 3,
    "exact_error": "불단·용상이 뒤에 있다는 물체 위치를 기둥 제거 위치로 오인한다. ㄱ은 뒤 기둥을 유지·이동했고 ㄴ이 뒤 기둥을 없앴다."
  }
}
```
