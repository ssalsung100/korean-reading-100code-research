

<!-- luna-raw:AFG-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G194",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "①은 리듬이 음높이를 가진다고 하여 본문의 음고 없음을 반대로 바꿨으므로 부적절하다. 활용에 관한 뒷절이 맞아도 앞절의 오류는 사라지지 않는다.",
  "official_answer_source": "sealed canonical answer 기계 연결; 이번stage에서공식배포답표직접대조아님.",
  "group_barrier": "G194 전체 유효blindraw저장확인후 answer필드만공개. 원문범위·그림·밑줄hold는후속직접확인으로해소하고최초기록보존.",
  "sdss_seen": false,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "source_boundary_residue": "AFK말미 ##2018학년도 잔재; group식별미확정"
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFG-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G194",
  "logic_without_codes_fixed": "리듬의정의에는음고없음이포함된다.①은그성질을음높이있음으로교체했으므로활용설명이맞아도전체진술은틀린다.",
  "primary": [],
  "primary_candidates": [
    16,
    1
  ],
  "working_representative": 16,
  "auxiliary": [
    17
  ],
  "surface": [
    18,
    23
  ],
  "evidence": [
    "본문리듬은음고없이장단·강약반복. 가락은음높이가있고지속시간을가지는음흐름.",
    "①은음높이를가지는리듬이라고진술."
  ],
  "competing_codes": [
    {
      "code": 1,
      "reason": "음고유무의반전으로동일오류를정확히기술할수있으므로16의유일주우위를강제하지않고중첩후보로보존."
    },
    {
      "code": 17,
      "reason": "가락의속성을리듬에옮긴것으로도기술가능하나①을기각하는데가락과실제교환되었다는가정은필요없다. 리듬정의와직접대조하면됨."
    },
    {
      "code": 18,
      "reason": "정의와선지가양립불가한것은판정결과이지만모든틀린진술에모순을추가주로붙이면오류내용을잃는다. 구체적음고유무보존이우선."
    }
  ],
  "falsification_probe": "①의음높이를가지는을음높이없이로바꾸면정의오류가사라진다. 정의전체의모든항목분석을추가로수행했다고과장하지않는다.",
  "confidence": 0.95,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
