

<!-- luna-raw:AOC-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G262",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2013/2013_answer_2013_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "결과의 형량 변화는 공모 사실 신인정이 아니라 알고 숨겨 준 행위에 적용할 조문 변경.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:AOC-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 12,
      "reason": "모반/모반대역 각각의 공모·인지·은닉 조건에 따른 형량을 추적"
    }
  ],
  "auxiliary": [
    {
      "code": 15,
      "reason": "형량 산출에 쓰인 적용 기준 교체"
    },
    {
      "code": 45,
      "reason": "사실 입력과 적용 규칙이 결과 형량에 미치는 역할 구별"
    },
    {
      "code": 17,
      "reason": "막동·끝동만 조문 변경, 나머지 처분과 구분"
    }
  ],
  "surface": [
    {
      "code": 3,
      "reason": "진술의 시간 순서보다 변경된 변수가 핵심"
    }
  ],
  "competitors": [
    {
      "code": 46,
      "refutation": "형량 증가라는 결과를 새 사실의 인과적 증거로 읽으면 오류.법규칙 교체로도 결과 달라짐"
    },
    {
      "code": 10,
      "refutation": "사형에는 반드시 공모가 필요하다는 것은 모반대역 은닉 조항에서 성립 안 함"
    },
    {
      "code": 36,
      "refutation": "율문 자체를 반박하는 사례가 아니라 다른 율문에 따른 결과 적용"
    }
  ],
  "counterfactual_probe": "인지·은닉 사실을 고정하고 모반을 모반대역으로 바꾸면 유배에서 참형으로 바뀔 수 있다.따라서 결과 변화에서 공모 인정 추가를 역추론 못함.",
  "boundary_status": "12/15/45 조건적 규칙·기준·함수 표상이 동일 연산을 다른 관점으로 기술.번호 중복 계수 금지",
  "confidence": 0.96,
  "passage_group": "G262",
  "sdss_disclosed": false
}
```
