

<!-- luna-raw:ANK-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G256",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2009예비/2009예비_answer_2009법학적성시험_예비_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "윤리 요구에서 벗어난 독자적 법 논리를 윤리 규범 이용으로 뒤집음.",
  "original_blind_preserved": true,
  "barrier": "group 전체 blind 저장 후 answer",
  "sdss_disclosed": false
}
```


<!-- luna-raw:ANK-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G256",
  "primary": [
    {
      "code": 42,
      "reason": "법의 독자적 논리 체계에서 외부 종교·윤리 요구를 분리하는 경계를 보존하는 작업 대표"
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "근대법에 속하는 특징과 속하지 않는 특징 대조"
    },
    {
      "code": 5,
      "reason": "윤리 요구에서 점차 벗어나는 변화의 방향"
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "윤리 규범 소재지만 당위 추론이 아님"
    }
  ],
  "competitors": [
    {
      "code": 13,
      "refutation": "독자적 법 논리와 모든 윤리 내용의 일치가 절대 불가능하다는 배타 명제를 세우면 과도. 외부 요구에 대한 추론 의존을 벗어났다는 문맥만 적용"
    },
    {
      "code": 23,
      "refutation": "영국도 예측가능성을 가진다는 공통점은① 수용에 유효하지만 정답②의 결정 연산은 분리 방향"
    },
    {
      "code": 16,
      "refutation": "근대법의 특징 묶음 확인으로 기술 가능하나 개념의 완전한 정의를 분석하는 단계는 없음"
    }
  ],
  "counterfactual_probe": "②를 종교·윤리 요구에서 독립한 추론 체계로 고치면 적절.①은 영국과 공유되더라도 근대법 특징이라는 지위가 소멸하지 않음.",
  "boundary_status": "42/17 분리 경계와 특징 귀속의 국소 중첩,42 유일주 미확정",
  "confidence": 0.89,
  "sdss_disclosed": false
}
```
