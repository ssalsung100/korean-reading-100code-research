

<!-- luna-raw:AVW-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G330",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_locations": [
    "3문단 특정방향으로명암변화가자주있을수록그방향주파수높음"
  ],
  "minimal_logic_without_codes": "수평으로 뻗은 줄무늬가조밀하면 줄을 가로지르는 수직방향에서 밝기변화가빈번하다. 선의방향과변화가일어나는방향을구분한다.",
  "intermediate_reasoning": [
    "① 밝기데이터변경→스펙트럼변경",
    "② 흑백교대는인접최대차",
    "③ 고주파시각둔감",
    "④ 변환정의",
    "⑤ 줄방향수평을주파수측정방향으로오인"
  ],
  "attractive_wrong_answer_and_error": "③: 고주파에서가시적왜곡작음은압축강인성이크다는뜻과다르다.",
  "visuals_reviewed": [
    "G330_visual01.jpeg"
  ],
  "source_scope": "원문속워터마크특성·독해판정만분석;외부기술절차추가없음",
  "quota_status": "unavailable"
}
```
