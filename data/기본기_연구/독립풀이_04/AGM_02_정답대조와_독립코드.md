

<!-- luna-raw:AGM-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G200",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "미토콘드리아에서사용할단백질을외부의세포핵DNA정보에따라얻으므로미토내부로전달되어야한다.④는미토에서세포질밖으로나가는방향으로바꿔부적절.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조 미수행.",
  "group_barrier": "전체6 blindraw저장후answer필드만공개.",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AGM-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G200",
  "logic_without_codes_fixed": "세포핵DNA정보에따라생산된미토대사필요단백질의사용처는미토내부다.④는필요한수송을미토→세포질방향으로역전한다.",
  "primary": [],
  "primary_candidates": [
    45,
    17
  ],
  "working_representative": 45,
  "auxiliary": [
    42,
    10
  ],
  "auxiliary_scope": "42는막안팎방향,10은③기존미토이분분열이유일생성원천이라는필요조건확인.",
  "evidence": [
    "마지막문단미토대사단백질은세포핵DNA로부터합성. 새미토는기존미토의이분분열로만생성."
  ],
  "competing_codes": [
    {
      "code": 17,
      "reason": "생산정보출처와사용처를서로다른장소에귀속하는행동은45의전달대응과국소중첩해후보유지."
    },
    {
      "code": 40,
      "reason": "부분기관구조를알아야하지만틀린것은부분/전체성질전이가아니라물질이동방향이다."
    },
    {
      "code": 46,
      "reason": "단백질이대사에필요하다는작용관계는배경. 특정생산기구·수송메커니즘을추가추론하지않고본문의출처/용도대응만따름."
    }
  ],
  "scope_limit": "정보출처가단백질의정확한합성소기관위치와동일하다고단정하지않음. 원문밖번역·수송기구세부는추가하지않는다.",
  "confidence": 0.96,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
