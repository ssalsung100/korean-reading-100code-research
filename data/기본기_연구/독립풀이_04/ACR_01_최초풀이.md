

<!-- luna-raw:ACR-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G180",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "5문단: 소리 크기와 차폐 문턱값의 차이가 클수록 비트 많이 할당, 문턱 미만 제거.",
    "보기 표: A 30/38, B 30/20, C 63/38, D 55/6 (소리 크기/문턱값)."
  ],
  "minimal_logic_without_codes": "C의 문턱 초과량은25, D는49이므로 실제 소리 크기는 C가 더 커도 비트는 D에 더 많이 할당한다. 따라서⑤.",
  "intermediate_reasoning": [
    "A는30<38이라 최소가청강도에도 못 미쳐 들리지 않음. 차폐 없음과 가청은 다르다.",
    "D는55>6이므로 문턱이 최소강도보다 높아졌더라도 들림.",
    "A/B 절대크기는30으로 같지만 A는제거, B는문턱초과10이라 동일 비트 할당이 아님.",
    "A/C 문턱값38의 일치로 주파수에 따른 대역 폭의 일치를 추론할 수 없음."
  ],
  "most_attractive_wrong_answer": 2,
  "exact_error": "차폐가 발생하여 문턱이 높아졌다는 사실을 해당 대역의 모든 소리가 안 들린다는 결론으로 확장한다. 실제 D의 크기는 높아진 문턱보다 크다.",
  "table_reading": "4개 소리 열과 주파수·크기·최소가청강도·차폐문턱값 4행이 완전하여 값 대응 가능. 각 소리가 서로 다른 대역이라는 조건을 유지.",
  "quota_status": "unavailable"
}
```
