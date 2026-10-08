

<!-- luna-raw:AGF-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G198",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "벌금만의단속으로목적을달성할수있다면추가무효의강한개입은최소제한원칙에맞지않는다. 따라서계약무효까지판결한것은벌금만으로목적실현이부족하다고고려한③으로이해된다.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조는 이번 stage에서 수행하지 않음.",
  "group_barrier": "AGD공식[A]확인뒤5문항전체blindraw저장검증. answer필드만공개.",
  "sdss_seen": false,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AGF-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G198",
  "logic_without_codes_fixed": "본문비례원칙에따라정당한개입으로이해하는조건에서,벌금만으로입법목적을달성할수있다면계약무효라는추가제한은필요하지않다. 계약무효까지정당화하려면벌금만으로는부족해야한다.③이그필요성을복원.",
  "primary": [],
  "primary_candidates": [
    20,
    10,
    12
  ],
  "working_representative": 20,
  "auxiliary": [
    44,
    24
  ],
  "equivalent_forms": {
    "20": "약한수단이충분하면추가강한수단이필요하지않다.",
    "10": "추가강한제한을정당화하기위해약한수단의불충분성이필요.",
    "12": "W=벌금만으로목적달성가능,S=강한제한정당화라면W→¬S의대우S→¬W. 같은본문최소제한명제의방향표현."
  },
  "evidence": [
    "마지막문단계약자유를필요한만큼만최소제한.",
    "보기벌금뿐아니라계약무효를판결.",
    "단속위반은계약유효와벌금양립,강행위반은무효와불이익;반사회적급부반환불인정예외."
  ],
  "competing_codes": [
    {
      "code": 10,
      "reason": "20과다른추론이라고억지분리하지않는다. 강한수단정당화의필요조건복원으로같은연산을기술가능해주후보보존."
    },
    {
      "code": 19,
      "reason": "약한제한으로부족하면무엇인가보완해야한다는관점과관련되지만부족함만으로이특정추가제한이항상충분하거나정당하다는역은성립하지않는다.③은필요성복원이며충분성보장아님."
    },
    {
      "code": 46,
      "reason": "②는벌금과무효라는병존효과를무효→벌금의인과로잘못연결한다.③의추론은사건발생메커니즘이아니라본문의규범적정당화조건적용이다."
    }
  ],
  "falsification_probe": "현실에서강한판결이존재한다는사실만으로약한수단이실제로부족했다고항상증명되는것은아니다. 이문항은본문비례원칙에따라판결의이유를이해하는전제를쓴다. 반대로약한수단불충분만으로어떤강한제한도자동정당화되지않음.",
  "scope_limit": "최소제한원칙이주어진기출의논리분석이며실제판례의모든정당성에대한법률판단으로확대하지않음.",
  "confidence": 0.96,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
