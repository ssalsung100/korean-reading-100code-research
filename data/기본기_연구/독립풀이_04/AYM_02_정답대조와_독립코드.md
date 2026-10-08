

<!-- luna-raw:AYM-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G352",
  "first_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "낮은융해량의대형표본을전체로외삽하여소형의큰D를놓친편향은전체와소형지표를낮추지만대형로스자체R의과소평가이유는아님.",
  "group_barrier": "전체3개blind 저장 후 정답만공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AYM-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G352",
  "primary": [
    77,
    84
  ],
  "auxiliary": [
    17,
    39,
    43
  ],
  "surface": [
    41,
    86
  ],
  "decisive_operation": "대형표본의낮은D/면적을전체에외삽한편향이전체와소형의D,R,S를낮추는방향을확인하되이미대형인로스에같은편향원인을귀속하지않는다.",
  "competing_codes": [
    {
      "code": 41,
      "rejection": "부분자료를전체에확대하지만부분의성질이항상전체로옮겨진다는논증보다비대표표본일반화와비율추정편향이다."
    },
    {
      "code": 49,
      "rejection": "D가줄면R,S가줄어드는방향에유효하나분모에D도포함된R의구조와편향적용범위가먼저필요."
    },
    {
      "code": 86,
      "rejection": "50%대50%등양비교는근거이지만면적91/9차이를고려하지않으면표본밀도편향을설명못함."
    },
    {
      "code": 43,
      "rejection": "C와총면적고정이라는비율변화조건은명시해야하나실험설계의원인식별은아님."
    }
  ],
  "sdss_seen": false,
  "confidence": 0.91,
  "quota_status": "unavailable"
}
```
