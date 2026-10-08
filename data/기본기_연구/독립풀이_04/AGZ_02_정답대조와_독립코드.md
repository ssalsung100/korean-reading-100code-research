

<!-- luna-raw:AGZ-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G202",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "실습이라는행위과정을통해이론습득,망원경이라는도구를통해내다봄이각원문용법을보존하므로⑤.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조 미수행.",
  "group_barrier": "AGW5선지표복원후전체5 blindraw저장검증. answer필드만공개.",
  "sdss_seen": false,
  "source_qualification": "2022학년도예시문항;실제시행기출과구분. 문제지전재본시각검증과공식배포호스트직접검증을구별.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AGZ-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G202",
  "logic_without_codes_fixed": "충방전이라는과정과충전기라는도구를수단으로쓴뜻을실습과망원경용례에각각대응한다. 흐름·연결·효력·상호이해등다른어의와구별.",
  "primary": [],
  "primary_candidates": [
    96,
    39
  ],
  "working_representative": 96,
  "auxiliary": [],
  "surface": [
    44,
    23
  ],
  "evidence": [
    "ⓐ충방전을통해반복사용/실습을통해이론습득.ⓑ충전기를통해충전/망원경을통해관측."
  ],
  "competing_codes": [
    {
      "code": 39,
      "reason": "각원용례와보기용례를비교하는행동으로96과국소중첩하여후보보존."
    },
    {
      "code": 44,
      "reason": "선택된어의가수단을나타내지만그수단이목적에효과적인지판정하는문제아님.단어용법확인을수단적절성추론으로확대하지않음."
    },
    {
      "code": 23,
      "reason": "두용례가함께맞아야하는선택형식일뿐별도공통속성교집합을구하는독립연산을수행했다고추가계수하지않음."
    }
  ],
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
