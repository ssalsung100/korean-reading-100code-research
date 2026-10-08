

<!-- luna-raw:BSL-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G528",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/표/2011/2011_answer/table_001.md Q9~11 공식HWP추출",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "청구권의상대적의무자와권리자자신을바꾸지않고자유/비자유의동일행위조건을유지한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BSL-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G528",
  "sdss_seen": false,
  "primary": [
    {
      "code": 17,
      "reason": "권리자와상대의무자를구별하여같은그의의무로바뀐②를배제한다."
    }
  ],
  "auxiliary": [
    {
      "code": 16,
      "reason": "청구권·자유권의정의를같은행위에대입한다."
    },
    {
      "code": 12,
      "reason": "권리보유/부재에서누구의어떤지위가따르는지방향을유지한다."
    },
    {
      "code": 4,
      "reason": "경우가있다는존재명제를권리종류별구체예로검증한다."
    }
  ],
  "surface": [
    {
      "code": 13,
      "reason": "청구권/자유권양립불가가배경이나모든권리와모든의무가배타적이라는뜻은아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 11,
      "rejection": "정의에기초한양방향표상은16과중첩가능하나주체를바꾸는문제가별도로남는다."
    },
    {
      "code": 33,
      "rejection": "권리부재를단순이중부정제거로처리할수없고무슨권리의부재인지확인해야한다."
    }
  ],
  "confidence": 0.94,
  "scope_limit": "④⑤는동일관계의자유/의무·청구/의무정의에의한증인사례이다.관계밖의권리의무동시보유금지로확장하지않는다."
}
```
