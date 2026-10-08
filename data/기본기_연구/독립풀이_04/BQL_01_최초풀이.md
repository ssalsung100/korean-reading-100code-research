

<!-- luna-raw:BQL-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G508",
  "selected_answer": 3,
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
      "location": "4문단",
      "evidence": "암묵→암묵 공동화,암묵→명시 표출화,명시→명시 연결화,명시→암묵 내면화."
    },
    {
      "location": "③",
      "evidence": "매뉴얼을 읽고 반복 사용하여 감각적 지식을 획득."
    }
  ],
  "minimal_logic_without_codes": "문서 지식을 반복 숙련해 감각적 지식으로 바꾸는③은 명시지→암묵지의 내면화다.",
  "intermediate_reasoning": [
    "① 대면 접촉으로 타자의 느낌을 포착하는 것은 공동화에 가깝고 명시지 결합이 아니다.",
    "② 특허 기술을 결합한 새 기술은 명시지 결합인 연결화다.",
    "④ 교재와 반복 시뮬레이션으로 조종 숙련을 얻으면 내면화다.",
    "⑤ 디자인에 대한 감지를 형상으로 완성하는 과정은 형식화 방향이며 타자 암묵지의 직접 모방·전달 근거가 없다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "교재와 시뮬레이션이라는 수단이 여러 개라는 이유로 연결화라고 하면 안 된다.최종 산출은 명시지의 결합이 아니라 숙련된 조종 능력이다."
  },
  "scope_limit": "⑤의 구체적 설계 전 과정을 알 수 없으므로 모든 단계가 표출화뿐이라고 단정하지 않는다.제시된 서술이 공동화 요건을 뒷받침하지 않는다는 점으로 배제한다."
}
```
