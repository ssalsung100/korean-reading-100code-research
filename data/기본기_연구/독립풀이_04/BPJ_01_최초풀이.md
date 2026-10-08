

<!-- luna-raw:BPJ-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G499",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "적중정책 정의",
      "evidence": "기본값 유일 정책은 오버랩을 허용하지 않고 한번에 하나의 규칙만 만족하도록 관리한다."
    },
    {
      "location": "DRD 및 규칙 조건 정의",
      "evidence": "조건 열은AND로 결합하며 하위노드 출력은 상위노드 입력으로 전달된다."
    }
  ],
  "minimal_logic_without_codes": "같은 입력으로 여러 규칙이 동시에 만족될 수 있으면 오버랩을 금지하는 기본 유일 정책을 사용할 수 없으므로①이 맞는다.",
  "intermediate_reasoning": [
    "② AND를OR로바꿨다.",
    "③ 같은입력을다른로직이함께활용할수없다는독점조건은없다.",
    "④ 하위입력이중간노드출력을거쳐간접적으로상위결정에영향을줄수있다.",
    "⑤ 본문의상향출력전달방향을뒤집었다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "직접연결부재를간접영향경로의부재로바꾸어, 하위출력이상위입력이되는합성경로를놓친다."
  },
  "source_limit": "공통DRD그림복원전이지만정답유일정책및상향전달·AND정의는본문에명시돼있다."
}
```
