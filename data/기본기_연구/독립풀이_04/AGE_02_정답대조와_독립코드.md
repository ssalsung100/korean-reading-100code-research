

<!-- luna-raw:AGE-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G198",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "둘다위법계약에법적불이익이있다는점은같지만계약효력과급부의무는다르다.①이공통.",
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


<!-- luna-raw:AGE-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G198",
  "logic_without_codes_fixed": "단속위반과강행위반은둘다법적불이익이있지만계약효력·급부의무·반환은서로다르다. 공통속성은불이익이어서①.",
  "primary": [
    23
  ],
  "auxiliary": [
    17,
    12
  ],
  "surface": [
    13,
    4
  ],
  "evidence": [
    "㉠벌금/유효/급부의무존속.㉡불이익/무효/급부의무부정/이미준자금반환가능."
  ],
  "competing_codes": [
    {
      "code": 17,
      "reason": "각효과를각유형에귀속하는것은공통항목계산의보조이며국소중첩한다. 이문항은두유형의공통성을명시적으로선택하므로23을작업대표."
    },
    {
      "code": 13,
      "reason": "유효와무효는서로배타적인결과지만두유형전체가모든속성에서반대인것은아니다. 불이익이라는공유속성을배제하면정답놓침."
    },
    {
      "code": 4,
      "reason": "둘모두라는양화범위는있으나핵심은무슨속성을공유하는가다. 단순히법위반범주전체로무효를확장하는④의오류를실제효과표로기각."
    }
  ],
  "falsification_probe": "법규위반→항상무효라는규칙에는본문㉠이직접반례다. 벌금이있음과계약유효는양립하므로불이익/효력을하나의축으로합치지않는다.",
  "confidence": 0.99,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
