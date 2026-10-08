

<!-- luna-raw:BEU-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G405",
  "selected_answer": 3,
  "confidence": 0.97,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "지도 북중국판과 한반도 북부·남중국판과 남부 연결",
    "4문단 남중국판이 북중국판 아래로 섭입",
    "5문단 오대산2억5천만·홍성2억3천만년",
    "4문단 곤드와나 적도 부근·산둥 인장력 추정"
  ],
  "minimal_logic_without_codes": "충돌대가 이어졌다는 가정에서 중국 두 판의 위치·섭입 방향을 지도상의 한반도 남북에 대응한다. 남부가 북부 밑으로 들어가는 방향을③이 뒤집는다.",
  "intermediate_reasoning": [
    "① 동쪽 오대산 충돌 연대가 더 오래되므로 동쪽이 먼저라는 추정과 맞다.",
    "② 연결된 두 판은 적도 부근 곤드와나 일부였다는 설명과 이어진다.",
    "③ 지도상 남부=남중국, 북부=북중국이므로 남부가 북부 아래로 섭입하는 방향이 맞다.",
    "④ 두 대륙이 충돌 전에 떨어져 있었다는 해양 존재 과정과 부합.",
    "⑤ 산둥처럼 낮은 산지라는 유사성에 인장력 저하 설명을 적용할 수 있다."
  ],
  "attractive_wrong": {
    "choice": 1,
    "exact_error": "2억5천만이2억3천만보다 수가 크다는 것을 더 늦은 사건으로 오인한다. 과거 몇 년 전의 수가 클수록 앞선 사건이다."
  },
  "scope": "⑤는 유사 지형과 연결 가정에 근거한 추정으로 원문의 추정 양상을 유지한다."
}
```
