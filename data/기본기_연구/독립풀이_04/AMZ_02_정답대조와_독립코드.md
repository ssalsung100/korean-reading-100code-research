

<!-- luna-raw:AMZ-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G252",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2009/2009_answer_2009_법학적성시험_언어이해_정답표.hwp",
  "barrier": "all_group_blind_records_before_any_group_answer_check 확인",
  "original_blind_preserved": true,
  "fixed_logic_without_codes": "형식적 요건의 유무로 소권을 가르는 ㉠을 내용에 따른 판단으로 바꾼 것이 오류다. ㉠과 ㉡의 기능상 공통점은 유지된다.",
  "sdss_disclosed": false
}
```


<!-- luna-raw:AMZ-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G252",
  "primary": [
    {
      "code": 15,
      "reason": "형식과 내용 중 어느 조건이 구속력·소권 판단의 기준인지 확인"
    }
  ],
  "auxiliary": [
    {
      "code": 10,
      "scope": "②",
      "reason": "형식 없는 합의만으로 불충분하므로 추가 요건을 복원"
    },
    {
      "code": 23,
      "scope": "⑤",
      "reason": "판단 기준의 내용 차이와 기준 제공이라는 공통 기능을 구분"
    },
    {
      "code": 3,
      "scope": "③",
      "reason": "19세기에도 준수 원칙이 유지되는지 시기 연결"
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "규범 명제이나 당위 여부 자체가 오류 축은 아님"
    }
  ],
  "competitors": [
    {
      "code": 17,
      "refutation": "내용/형식 속성의 귀속 교환으로 기술 가능하지만 단순 대상 이름 교환을 넘어 법적 판단에 투입되는 조건이 바뀐다. 15와 국소 중첩 가능성 유지"
    },
    {
      "code": 21,
      "refutation": "원문은 개념의 완전 정의가 아니라 소권 성립의 부족 조건을 말하므로 필요충분 정의로 강화 불가"
    },
    {
      "code": 12,
      "refutation": "②의 함축 방향 해석에는 유효하나 정답①을 가르는 중심은 어느 조건을 썼는지이며 조건문 일반만으로는 부족"
    },
    {
      "code": 75,
      "refutation": "견해 대립을 외워도 ⑤의 기능상 공통점을 배제하면 실패. 대립 자체가 아니라 각 기준의 역할을 유지해야 함"
    }
  ],
  "counterfactual_probe": "①의 내용을 형식으로 바꾸면 ㉠의 원칙에 가까워지며 ⑤는 그대로 참이다. 단 형식만 갖추면 어떤 합의든 소권 성립한다고 추가하면 본문 이상의 충분성 강화다.",
  "boundary_status": "15/17의 국소 중첩 및 15를 필요충분조건과 일괄 동일시할 수 없는 점 보존",
  "confidence": 0.93,
  "sdss_disclosed": false
}
```
