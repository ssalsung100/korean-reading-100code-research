

<!-- luna-raw:AIC-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G211",
  "blind_answer": 3,
  "official_answer": 3,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "제원들은태보가목숨걸고간한충을인정하며자신들의책임을말하고,태보는가족에게뜻이변하지않고죽어서도왕비복위를간하겠다고한다.③ 강직함의평가와다짐이대응한다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2022__국어_1교시_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조. AIC 공식PDF범위직접검증과정답셀직접대조는구별",
  "barrier_verified": "AICscope해소후유효blind4개모두저장한다음G211첫answer공개; SDSS미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIC-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G211",
  "primary": [],
  "primary_candidates": [
    39,
    17
  ],
  "working_representative": 39,
  "auxiliary": [
    80,
    5
  ],
  "surface": [
    46,
    63
  ],
  "judgment_reason": "[A] 제원의 평가와[B] 태보의 직접 다짐에서 같은 강직함을 확인한다. 발화 간 성격대응39와 각발화에 성격속성을 귀속17이 같은 최소확인에 겹친다.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "후보",
      "reason": "죽기를각오한간언과뜻불변을 태보의강직함에 각각귀속"
    },
    {
      "code": 80,
      "verdict": "보조",
      "reason": "죽음에도뜻을유지하는태도를 판독하나 다른인물의평가와 직접발화대응까지 확인"
    },
    {
      "code": 46,
      "verdict": "특정오답 기각",
      "reason": "② 제원의위로가생존도모결심의원인이라는연결은없음"
    },
    {
      "code": 63,
      "verdict": "표면",
      "reason": "칭송이라는긍정평가가논증을강화하는증거평가과제라는뜻은아님"
    }
  ],
  "minimal_change_test": "[B]가간언을후회하고뜻을포기하는말이라면[A]의강직함이[B]에서확인된다는③은깨진다.반복속성의확인이지위로로태도가변했다는인과아님.",
  "sdss_seen": false,
  "confidence": 0.96,
  "quota_status": "unavailable"
}
```
