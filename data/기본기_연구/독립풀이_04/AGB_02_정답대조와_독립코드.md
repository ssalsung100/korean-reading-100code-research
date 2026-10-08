

<!-- luna-raw:AGB-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G197",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "가격과기온이라는수량수준이낮아진다는용법이같아①. 몫이생김·욕구감퇴·닳아망가짐·명령이내려짐과는문맥행위가다르다.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조는 이번 stage에서 수행하지 않음.",
  "group_barrier": "AFY공식범위와AFZ원표직접확인후전체5 blindraw저장검증,answer필드만공개.",
  "sdss_seen": false,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "uncertainty_preserved": "AGB①/③근접문맥의미의최초불확실성은정답일치로삭제하지않음.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AGB-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G197",
  "logic_without_codes_fixed": "가격수준의하락과기온수준의하락이가장가까운용법이다. 입맛감퇴도감소의의미권을공유하지만같은수치수준의하락과는문맥대상·용법이덜직접적이다.",
  "primary": [],
  "primary_candidates": [
    96,
    39
  ],
  "working_representative": 96,
  "auxiliary": [],
  "surface": [
    1,
    49
  ],
  "evidence": [
    "원문채권가격이떨어진다/①기온이영하로떨어졌다.",
    "③입맛감퇴,②몫이생김,④신발이해짐,⑤말씀이내려짐."
  ],
  "competing_codes": [
    {
      "code": 39,
      "reason": "원문과선지의문맥의미를비교하는행동은96과국소중첩. 후보/대표구조로보존."
    },
    {
      "code": 49,
      "reason": "원문주변에는신용위험과가격의증감관계가있지만이문항은그관계를추론하는것이아니라떨어지다용법을찾는다. 소재의방향관계와어휘판정구분."
    },
    {
      "code": 1,
      "reason": "①과③모두감소라는넓은뜻으로요약가능해유무·증감만으로둘을완전히갈라낼수없다. 문맥에가장가까운수치수준하락의용례를선택한다."
    }
  ],
  "uncertainty_preserved": "최초blind의①/③근접의미가능성은남긴다. 공식답①일치를떨어지다의모든용례가상호배타라는사전적정의검증으로승격하지않음.",
  "generation_principle": "가장가까운의미문항에서는명백한다의어와근접용법오답의근거수준을구별하고보편적인배타정의를임의생성하지않는다.",
  "confidence": 0.94,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
