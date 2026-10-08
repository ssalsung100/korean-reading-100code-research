

<!-- luna-raw:ATD-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G306",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": true,
    "strict_blind_eligible": false,
    "prior_exposure_detail": "핵심8코드 기준문서의 중산층 점수표 판단 예시 사전 노출.",
    "supplement_seen": "G306_visual01.md"
  },
  "needed_information_locations": [
    "객관중산층인데동일시안하는집단상대박탈예상",
    "핵심중35%/주변중12%만동일시",
    "객관중산층증가·주관귀속감소"
  ],
  "minimal_logic_without_codes": "핵심과 주변 모두 절반 미만만 동일시하므로 합친 중산층에서도 과반이 동일시하지 않는다. 본문 기준상 상대적 박탈감을 예상할 수 있다.",
  "intermediate_reasoning": [
    "①평균소득증가가분류증가원인이라는자료없음.②낮은중산층귀속은주관기준이높기때문이지객관기준아님.③주관감소가객관붕괴아니며객관은증가.④각집단비율로과반불일치확인.⑤하층의6%중산층동일시는오히려작은불일치."
  ],
  "attractive_wrong_answer": 3,
  "exact_error": "주관적 귀속 의식 감소를 객관적 중산층 비율 감소와 동일시한다.",
  "optional_check": "0.35×0.35+0.32×0.12=0.1609, 이를 객관중산층0.67로 나누면 약24%만 동일시. 정확 계산 없이 양쪽 모두50%미만인 점으로 판정 가능.",
  "quota_status": "unavailable"
}
```
