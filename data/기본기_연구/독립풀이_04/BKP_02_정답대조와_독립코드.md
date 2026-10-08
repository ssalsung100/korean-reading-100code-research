

<!-- luna-raw:BKP-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G457",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2019/2019_answer_2019_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "논박 성공 측에서는 느낌이 뒤집혀도 말과 행동이 같아 빨간 온수 꼭지를 틀어야 한다. 따라서 양측 모두 빨간 꼭지를 틀지 않는다고 한 ④는 틀리다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BKP-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G457",
  "minimal_logic_without_codes": "성공 측은 색의 느낌이 바뀌어도 온수를 얻는 행동과 색 이름의 발화는 같다고 본다.따라서 양측 모두 빨간 꼭지를 틀지 않는다는④의 공통 귀속은 성공 측에 맞지 않는다.",
  "primary": [
    {
      "code": 45,
      "reason": "같은 상황 입력에서 사적 느낌과 발화·행동 출력을 분리하고 기능 동일이라는 성공 측 조건을 적용한다."
    }
  ],
  "auxiliary": [
    {
      "code": 74,
      "reason": "같은 빨간 꼭지 사례를 두고 사고 실험 성공/실패 설명이 예측하는 기능 변화를 구분한다."
    },
    {
      "code": 4,
      "reason": "양측 모두의 공통 판단이라는④를 한쪽의 반대 예측으로 배제한다."
    },
    {
      "code": 17,
      "reason": "실제 꼭지의 색·느껴지는 색·입으로 말하는 색을 서로 다른 귀속 항목으로 유지한다."
    }
  ],
  "surface": [
    {
      "code": 86,
      "reason": "빨강·초록·파랑의 구별은 양적 크기 비교가 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 75,
      "rejection": "입장별 귀속은74와 겹친다.본 문항은 동일 상황에서 기능 출력의 같고 다름이 구체 판단이므로45를 작업 대표로 둔다."
    },
    {
      "code": 80,
      "rejection": "주관적 경험 내용은 중요하지만 그 느낌에서 명명·행동까지 같은 방향으로 바뀐다고 결론 내리지 않는 것이 관건이다.인식 내용 비교만으로는 부족하다."
    },
    {
      "code": 69,
      "rejection": "본문의 규정된 기능 조건을 새 온수 사례에 적용한다.별도 유사성을 근거로 미확인 속성을 투사하는 유비와는 구별한다."
    }
  ],
  "boundary_note": "실패 측의 정확한 대체 행동을 몰라도 성공 측의 빨간 꼭지 사용만으로④를 배제할 수 있다.정답 결정에 불필요한 행동 예측을 추가하지 않는다.",
  "confidence": 0.93,
  "sdss_seen": false
}
```
