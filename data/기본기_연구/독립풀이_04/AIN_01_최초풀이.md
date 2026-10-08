

<!-- luna-raw:AIN-blind-20260921-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G214",
  "selected_answer": 2,
  "confidence": 0.99,
  "resolved_hold_record": "AIN-hold-20260921-01",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_and_location": [
    "공식crop[A]첫두행,[B]함께썩어갈수록~흔들고,[C]이윽고~버섯피어남",
    "[D]서서히썩음~고통멈춤,[E]낙엽·바람두행,[F]덮을길없음~독기채움"
  ],
  "source_scope_verified": "AIN_poem_ABF_scope_official_pdf.png에서[A]~[F]여섯대괄호의양끝직접확인",
  "minimal_logic_without_codes": "바람이참나무를흔든뒤이윽고홀씨가일어나버섯이핀다.②의[B]→[C]순차관계가명시된연결에맞다.",
  "intermediate_inferences": [
    "①다시이전상태로되돌아오는순환아님",
    "③버섯생성과고통멈춤은대립이아니라연결",
    "④버섯생성이낙엽·바람의상황을일으킨인과없음",
    "⑤낙엽·바람은덮지못하고버섯은채우므로기능이같지않음"
  ],
  "most_attractive_wrong_answer": {
    "choice": 3,
    "attraction": "썩어감과피어남의대비를보고[C][D]전체도대립으로오독",
    "error": "[C]버섯생성과[D]고통멈춤은같은생명생성효과로연결되며대립축은나무의썩음과버섯의생성이다."
  },
  "quota_status": "unavailable"
}
```
