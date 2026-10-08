

<!-- luna-raw:BAL-answer_check-20261001-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G368",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2016/2016_answer_2016학년도_법학적성시험_언어이해_정답표.hwp",
  "answer_access": "sealed 공식 정답 필드 대조; 정답표 원본 별도 재검증 아님",
  "code_free_logic_fixed": "리튬의 작은 질량은 원자 운동량 감소와 관련되지만 짧은 공명 파장은 광자 운동량 증가와 관련된다.",
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "sdss_seen": false,
  "source_repair_provenance": "공식 HWP question-only 등록 렌더13~14 직접 확인. 선행 hold와 불완전crop 기록 보존."
}
```


<!-- luna-raw:BAL-independent_code-20261001-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    91
  ],
  "auxiliary": [
    17,
    84,
    39
  ],
  "surface": [
    92
  ],
  "decisive_operation": "파장과 진동수·광자 운동량의 반비례 방향을 적용하면서 원자 질량에 따른 원자 운동량과 구분한다.",
  "evidence": [
    "리튬670nm<루비듐780nm→공명f와광자p는리튬이큼",
    "질량6.94<85.47→같은v의원자p는리튬이작음",
    "광원f를낮추면파장은공명값보다길어짐"
  ],
  "competing_codes": [
    {
      "code": 84,
      "rebuttal": "반비례를분수식으로표현가능하나정확한비율계산없이방향으로결정.91과국소동치적기술을허용하되번호별별도연산계수안함."
    },
    {
      "code": 17,
      "rebuttal": "원자/광자대상고정은필수보조지만반비례방향을계산하지않으면②의참거짓을결정할수없다."
    },
    {
      "code": 86,
      "rebuttal": "단순양의대소확인에서끝나지않고파장작음→운동량큼이라는역방향변환이필요하다."
    },
    {
      "code": 43,
      "rebuttal": "③같은속도는조건이지만비교실험으로원인효과를식별하는문항은아니다."
    }
  ],
  "boundary_note": "같은 운동량 명칭 아래에도 원자 p=mv와 광자 p∝1/파장은 입력·대상이 다르다.",
  "confidence": 0.94,
  "passage_group": "G368",
  "sdss_seen": false,
  "code_free_logic_preserved": true,
  "source_repair_provenance_preserved": true
}
```
