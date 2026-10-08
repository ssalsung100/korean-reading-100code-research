

<!-- luna-raw:AXH-blind-20260928-02 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G342",
  "selected_answer": 4,
  "confidence": 0.99,
  "resolved_hold": "AXH-hold-20260928-01",
  "original_hold_preserved": true,
  "source_read": [
    "AXH.json",
    "G342_visual01.tif 직접 렌더",
    "자료/LEET_언어이해/HWP_홀수형_페이지_렌더링/2014/page_003.png 직접 확인"
  ],
  "source_path_deviation": "복원 helper가 전달한 공식 문제지 렌더를 blind_sources 복사본 생성 전 직접 열었다. 정답·해설 없는 G342 문제지만 포함하나 blind_sources 경로 제한을 준수한 것으로 소급하지 않는다.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "helper_answer_and_sdss_exposure": true
  },
  "strict_blind_eligible": false,
  "required_information_and_location": [
    "그림2 α는 왼쪽 저→고 전이 경계,β는 오른쪽 고→저 전이 경계",
    "원문 선지④ α,⑤ β 직접 판독"
  ],
  "minimal_logic_without_codes": "기존 상태를 유지하며 제재 강도를 증감시키는 방향으로 곡선을 따라가야 한다. 고범죄에서 제재를 강화하여 저범죄로 넘어가는 오른쪽 경계는 β이므로 이를 α에 귀속한④는 틀리다.",
  "intermediate_reasoning": [
    "① E의 오른쪽 실선 기울기는 작아 미미한 감소.",
    "② F 오른쪽은 점선 급락 구간.",
    "③ G 왼쪽은 α에 가까워져 급증 가능.",
    "④ α는 고→저 전이 경계가 아니라 저→고 전이 경계.",
    "⑤ β보다 강한 제재에서는 낮은 범죄율 상태만 남는다."
  ],
  "most_attractive_wrong_answer": 3,
  "exact_error": "제재 약화가 범죄율 증가 방향이라는 사실만 보거나 완만 구간만 연장하면 임계점 접근에 따른 급증 가능성을 놓친다.",
  "quota_status": "unavailable"
}
```
