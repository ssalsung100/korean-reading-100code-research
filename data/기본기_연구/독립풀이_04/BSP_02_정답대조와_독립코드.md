

<!-- luna-raw:BSP-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G529",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/표/2011/2011_answer/table_001.md Q27~29 공식HWP추출",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "국가적직무필요에는동의하지만동등한문무반처우에는반대입장이다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BSP-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G529",
  "sdss_seen": false,
  "primary": [
    {
      "code": 75,
      "cluster": "C074_075",
      "reason": "잡학의기능필요와처우입장을두주체에각각귀속한다."
    }
  ],
  "auxiliary": [
    {
      "code": 39,
      "reason": "공통된직무필요축과다른신분대우축을구분한다."
    },
    {
      "code": 9,
      "reason": "보기의신분위계가차별적처우근거임을확인한다."
    }
  ],
  "surface": [
    {
      "code": 13,
      "reason": "처우에는반대라도직무필요에동의하므로모든명제에서배타가아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 23,
      "rejection": "일부공통점은있지만그교집합만으로처우차이를판정하지못한다."
    },
    {
      "code": 63,
      "rejection": "새근거로신분관점을강화/약화하는것이아니라명시입장비교다."
    }
  ],
  "confidence": 0.96
}
```
