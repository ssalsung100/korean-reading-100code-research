

<!-- luna-raw:AFF-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G194",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "음악적 아름다움을 질문하고 소리의 물리적 성질을 분석한 뒤 음악 요소의 형식적 조직과 연결하여 답하므로④.",
  "official_answer_source": "sealed canonical answer 기계 연결; 이번stage에서공식배포답표직접대조아님.",
  "group_barrier": "G194 전체 유효blindraw저장확인후 answer필드만공개. 원문범위·그림·밑줄hold는후속직접확인으로해소하고최초기록보존.",
  "sdss_seen": false,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "source_boundary_residue": "같은 group AFK 선택지 말미에 ##2018학년도 잔재를 읽음. 해당group의 시험 식별로 확정하지 않음."
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFF-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G194",
  "logic_without_codes_fixed": "음악미의성립을묻고소리의과학적성질을설명한뒤요소들의조직형식과연결한다. 소리종류분류를음악형식분류로옮기지않는다.",
  "primary": [],
  "primary_candidates": [
    64,
    17
  ],
  "working_representative": 64,
  "auxiliary": [
    56
  ],
  "surface": [
    25,
    39
  ],
  "evidence": [
    "도입음악적아름다움의구현질문→파형·스펙트럼·음정→음악요소와조직형식.",
    "③은소리를구분했다는사실을음악형식분류로확장."
  ],
  "competing_codes": [
    {
      "code": 17,
      "reason": "무엇에대한설명인가를글전체에귀속한다는행동은64와국소중첩. 후보로보존하며유일주우위유보."
    },
    {
      "code": 25,
      "reason": "전반부에소리분류가있지만후반은음악형식종류의분류가아니다. 부분구조를전체구성으로확대하면③오독."
    },
    {
      "code": 39,
      "reason": "과학적탐색과음악적탐색이라는별개의두견해를같은축에서대조하지않는다. 두내용을관련짓는것과비교하는것은다름."
    }
  ],
  "auxiliary_scope": "56은소리분석이음악미탐구의설명내용으로쓰이는방식을기술. 주제귀속과독립증거로중복계수하지않음.",
  "confidence": 0.96,
  "sdss_seen": false,
  "exposure_qualification": "역사적노출확인불가,AFK말미경계잔재보존",
  "quota_status": "unavailable"
}
```
