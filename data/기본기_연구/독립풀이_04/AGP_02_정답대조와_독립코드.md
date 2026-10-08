

<!-- luna-raw:AGP-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G200",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "병원성소실과분리생존불가능은개체성상실·소기관화를보장하지않는다. 오히려자체복제가남아있어①의이미소기관변화확정은근거부족.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조 미수행.",
  "group_barrier": "전체6 blindraw저장후answer필드만공개.",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AGP-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G200",
  "logic_without_codes_fixed": "박테리아제거시아메바사망이라는생존의존성이있어도박테리아는자체복제하고있으며개체성상실수준의통합이입증되지않음. 비병원성·의존성만으로소기관화결론을내린①의충분성이없다.",
  "primary": [
    62
  ],
  "auxiliary": [
    15,
    17,
    2
  ],
  "evidence": [
    "본문분리생존불가능해도개체성잃을정도상호작용아니면공생. 소기관근거는숙주복제조절·공동증식·유전자이동.",
    "보기생존박테리아는자체복제,제거시숙주도사망."
  ],
  "competing_codes": [
    {
      "code": 10,
      "reason": "박테리아가아메바생존의필요조건일수있다는것을그관계가개체성상실의충분조건으로바꾸면안된다. 필요성이성립하는대상명제자체가다름."
    },
    {
      "code": 40,
      "reason": "세포안에있다는위치만으로하나의생명체의소기관부분이되었다고확정할수없다. 구조적포함과독립개체성상실의조건을구별."
    },
    {
      "code": 63,
      "reason": "추론결론의지지가충분한지평가하는넓은강화약화기술가능. 이문항은새외부증거보다현재전건이소기관화결론을보장하지못한다는관계부족을62로대표."
    }
  ],
  "falsification_probe": "분리생존불가이면서자체증식하는공생관계를본문이허용하므로의존성→소기관화는반증된다. 반대로병원성소실이나무해함도증식조절·유전통합의증거를대신하지못한다.",
  "scope_limit": "④는본문모형을개체성상실이라는가정에적용한것으로읽고실제박테리아DNA가줄었다는관측확정으로승격하지않음.",
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
