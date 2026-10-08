

<!-- luna-raw:BNM-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G482",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2024/2024_answer_2024언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "2021년 편익1000, 비용(2+3)×100=500, 순편익500. 2022년 편익1500, 비용(2+3+1+3)×150=1350, 순편익150. 두 해 비용 합은1850이므로1350이라고 한③이 틀린다. 단위는 만원.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BNM-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G482",
  "minimal_logic_without_codes": "각 연도 비용은 환자 지급액과 모든 지원금의 합이다.2021년500과2022년1350을 합한1850이 두 해 비용인데③은2022년 단년1350으로 바꾼다.",
  "primary": [
    {
      "code": 92,
      "reason": "회당 금액×횟수, 계정 합산, 두 연도 합계와 순편익 차감 계산이 필요하다."
    }
  ],
  "auxiliary": [
    {
      "code": 88,
      "reason": "총편익에서 회수·보전 비용을 빼 잔여 사회성과를 구한다."
    },
    {
      "code": 3,
      "reason": "③의2022년 단년 값과2021년부터 두 해 누적 범위를 구분한다."
    },
    {
      "code": 17,
      "reason": "가격을 통한 회수, 정부·주민·기업 지원, 총편익, 순성과 항목을 섞지 않는다."
    },
    {
      "code": 43,
      "reason": "다른 조건 불변에 의해2022년도 본인부담2와 지자체3을 유지한다."
    }
  ],
  "surface": [
    {
      "code": 86,
      "reason": "연도별 증가·감소 비교가 있지만 결정적 오답은 비용 총액의 산출과 기간 누락이다."
    }
  ],
  "competing_codes": [
    {
      "code": 85,
      "rejection": "총합이 고정된 자원 몫을 나누는 문제가 아니다. 횟수와 지원액이 동시에 바뀐다."
    },
    {
      "code": 84,
      "rejection": "회당 단가가 있지만 분모 변동에 따른 비율 왜곡이 핵심은 아니다."
    },
    {
      "code": 46,
      "rejection": "추가 지원과 활동 증가를 인과로 해석할 수 있어도 계산은 보기의 주어진 수량과 회계 규칙만으로 한다."
    }
  ],
  "numeric_evidence": {
    "unit": "만원",
    "2021": {
      "benefit": 1000,
      "patient_payment": 200,
      "government": 300,
      "cost": 500,
      "impact": 500
    },
    "2022": {
      "benefit": 1500,
      "patient_payment": 300,
      "government": 450,
      "citizen": 150,
      "business": 450,
      "cost": 1350,
      "impact": 150
    },
    "two_year_cost": 1850
  },
  "confidence": 0.96,
  "sdss_seen": false
}
```
