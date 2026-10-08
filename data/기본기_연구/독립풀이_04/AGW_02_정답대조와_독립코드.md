

<!-- luna-raw:AGW-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G202",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "본문은충전양초과의수명영향을말하며허용전류초과라는전류세기조건의수명영향은제시하지않는다.②는원문근거를찾을수없다.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조 미수행.",
  "group_barrier": "AGW5선지표복원후전체5 blindraw저장검증. answer필드만공개.",
  "sdss_seen": false,
  "source_qualification": "2022학년도예시문항;실제시행기출과구분. 문제지전재본시각검증과공식배포호스트직접검증을구별.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AGW-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G202",
  "logic_without_codes_fixed": "본문은충전량초과와수명감소를연결하나허용전류세기초과의수명영향은제시하지않는다. 누적량과유입률을바꾼②는본문근거가없다.",
  "primary": [
    64
  ],
  "auxiliary": [
    17,
    92
  ],
  "surface": [
    46,
    2
  ],
  "evidence": [
    "과충전정의는최대용량초과. 전류적산은전류×시간간격의합으로충전양을추정하여두량을구분.",
    "원문②는충전허용전류보다센전류의수명영향을주장."
  ],
  "competing_codes": [
    {
      "code": 46,
      "reason": "선지는인과주장이지만그주장의현실적진위를검증하는것이아니라본문이그인과를제공했는지확인한다. 실제수명영향이없다고반대인과를새로단정하지않음."
    },
    {
      "code": 17,
      "reason": "본문효과의대상인충전량을전류세기로교환한것으로기술가능하여64의증거범위검사와국소중첩. 독점코드기여로확대하지않음."
    },
    {
      "code": 2,
      "reason": "정보부재를불가능성으로승격하지않는다. 답②는원문에서근거를못찾는다는판정이지현실에서일어날수없다는판정아님."
    }
  ],
  "falsification_probe": "같은전류세기라도흐른시간이다르면총충전량이달라진다. 따라서충전량초과효과를전류한변수의초과효과로즉시치환못함.",
  "confidence": 0.98,
  "sdss_seen": false,
  "source_qualification": "예시문항·문제지전재본검증한계보존.",
  "quota_status": "unavailable"
}
```
