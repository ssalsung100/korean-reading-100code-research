

<!-- luna-raw:ATB-blind-20260928-01 -->
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
    "prior_exposure_detail": "초기 읽은 핵심8코드 기준문서의 중산층 점수표 함수/인과 예시와 소재가 일치함. 동일 기출 여부는 아직 미확정이나 보수적으로 strict 성과 제외.",
    "strict_blind_eligible": false,
    "supplement_seen": "G306_visual01.md"
  },
  "needed_information_locations": [
    "합계3이상핵심/2주변",
    "직업최대2,소득·자산·교육각1"
  ],
  "minimal_logic_without_codes": "주택 점수0이어도 직업2와 소득1 또는 교육1로3점을 만들어 핵심 중산층이 될 수 있다.",
  "intermediate_reasoning": [
    "①소득없이도직업2로중산층.②고졸이어도직업2+다른1로핵심가능.③직업최대2/자산1로가중치다름.④반례구성가능.⑤직업의두행은택일이므로최대5점이지6아님."
  ],
  "attractive_wrong_answer": 5,
  "exact_error": "같은 직업 지표의 대체 범주2점과1점을 동시에 더한다.",
  "quota_status": "unavailable"
}
```
