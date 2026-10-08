

<!-- luna-raw:BLT-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G467",
  "selected_answer": 4,
  "confidence": 0.97,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "궤도그림",
      "evidence": "A는후방분사로진입하는외측큰타원,B는전방분사의내측작은타원.Y는원궤도유지,질량은같음."
    },
    {
      "location": "본문·복원수식",
      "evidence": "같은E에서r이작으면U가작고K가커진다.큰타원의최근점과작은타원의최원점은분사점r0이다."
    }
  ],
  "minimal_logic_without_codes": "A궤도에서K는최근점에서Y보다크고최원점에서Y보다작다.같은중간거리의대칭두지점에서같은K를가지므로Y와같은운동에너지의지점은하나가아닌둘이다.④가부적절하다.",
  "intermediate_reasoning": [
    "① B에서는더가까이내려가며최대속력이Y보다커지고질량이같아최대K도더크다.",
    "② A의최소U는r0에서,B의최소U는더작은r에서이므로Umin(A)>Umin(B).",
    "③ A의최근점은분사점r0여서Umin(A)=U(Y).",
    "⑤ 가능한거리의기하학적상한을비교하면외측A의최대반경이내측B의최대반경보다크다.실제특정시각에서상한이반드시실현된다고추가하지않는다."
  ],
  "most_attractive_wrong": {
    "choice": 2,
    "exact_error": "중력위치에너지가음수라는점을놓쳐가까워질수록수치가작아진다는순서를절댓값의크기와뒤바꾼다."
  },
  "background_knowledge_used": "큰타원최원점속력이기존원궤도속력보다작다는기본궤도역학과중심력타원의대칭성을보조사용했다.복원된본문수식은K,U,E뿐이며원문이궤도속력공식전체를명시했다고주장하지않는다.",
  "source_restoration": {
    "appendix": "data/기본기_연구/prepared_backlog/blind_sources/BLR-hold-source-20261003-appendix.md",
    "resolved_before_answer_disclosure": true
  },
  "scope_limit": "같은운동에너지지점둘은공간적지점수이다.두우주선이동시에그지점에있다는뜻이나충돌횟수아님."
}
```
