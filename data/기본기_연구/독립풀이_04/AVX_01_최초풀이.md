

<!-- luna-raw:AVX-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G330",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_locations": [
    "사진B복잡깃털·C완만한밝기·A중간질감",
    "4문단 주파수삽입은전영역분산·일부잘라도추출가능",
    "5문단 고주파압축취약"
  ],
  "minimal_logic_without_codes": "주파수 영역에 넣은 정보는 한영역에만국한되지않으므로C를잘라도남은부분에서추출가능하다. 비가시성과압축후잔존은별개다.",
  "intermediate_reasoning": [
    "① B의복잡질감에서비가시성이더낮다고할근거없음",
    "② 매끈한C에고주파패턴추가하면도드라짐",
    "③ 저주파정보도분산돼일부영역손실에잔여정보존재",
    "④ 중간대역정보가매끈한C에더집중된다는방향아님",
    "⑤ B가복잡해도고주파제거압축의정보손실을복구하지못함"
  ],
  "attractive_wrong_answer_and_error": "⑤: 고주파성분이많은영역이라는사실이압축으로제거된식별자를보존해주지않는다.",
  "visuals_reviewed": [
    "G330_visual01.jpeg"
  ],
  "source_scope": "원문속워터마크특성·독해판정만분석;외부기술절차추가없음",
  "quota_status": "unavailable"
}
```
