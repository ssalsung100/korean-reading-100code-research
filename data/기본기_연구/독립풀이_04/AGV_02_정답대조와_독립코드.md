

<!-- luna-raw:AGV-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G202",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "감소하는전압의일부값은평균보다낮을수있으므로②가맞다. 공칭전압은모든순간값의하한이아니다.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조 미수행.",
  "group_barrier": "AGW5선지표복원후전체5 blindraw저장검증. answer필드만공개.",
  "sdss_seen": false,
  "source_qualification": "2022학년도예시문항;실제시행기출과구분. 문제지전재본시각검증과공식배포호스트직접검증을구별.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AGV-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G202",
  "logic_without_codes_fixed": "방전중변하는순간단자전압의평균이공칭전압이므로일부순간값이그평균보다낮을수있다. 평균을하한이나고정값으로바꾸지않는다.",
  "primary": [
    86
  ],
  "auxiliary": [
    16,
    2
  ],
  "surface": [
    84,
    49
  ],
  "evidence": [
    "첫문단단자전압감소,그평균이공칭전압.②평균보다낮을수있음."
  ],
  "competing_codes": [
    {
      "code": 84,
      "reason": "평균을분수로계산할수있지만표본수·합계의실제계산은없다.평균과개별값의관계를이용한양적위치비교가결정적."
    },
    {
      "code": 49,
      "reason": "방전진행에따른전압감소방향만알아도평균의위치를생략하면②를확정못한다. 평균값의정의를함께보존해야함."
    },
    {
      "code": 15,
      "reason": "공칭전압은작동허용의최소기준이아니라관측값의평균이다. 기준값으로오인하면낮아질수없다는반대판정을하게됨."
    }
  ],
  "falsification_probe": "개별시점값이항상평균이상이며일부는더크다면그평균정의와맞지않는다. 정확시간별값계산없이도낮은값의가능성판정가능.",
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
