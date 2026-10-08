

<!-- luna-raw:BGX-answer_check-20261002-r4-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G425",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2011/2011_answer_2011_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "자연법은 상위 정당화 이론, 실제 합리적 소송 규칙은 제도 절차. 이 역할을 서로 귀속시키지 않는다.",
  "limitations": [
    "봉인 공식 전사 답과 대조. 원정답표 독립 시각 대조 미실시. 과거노출unknown 유지."
  ]
}
```


<!-- luna-raw:BGX-independent_code-20261002-r4-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G425",
  "sdss_seen": false,
  "general_task": "제도와 이론의 속성 귀속 확인",
  "decisive_relation": "소송 규칙의 소재를 실제 재판 제도에서 기독교적 자연법 이론으로 옮긴 오류",
  "primary": {
    "code": 17,
    "scope": "정답④",
    "reason": "절차 규칙과 상위 정당화 이론의 서로 다른 범주를 구분한다."
  },
  "auxiliary": [
    {
      "code": 98,
      "scope": "정답④",
      "reason": "어느 법/제도의 규칙인지 귀속 주체를 복원한다.17과 같은 국소 오류의 구체 표현."
    },
    {
      "code": 60,
      "scope": "정답④ 및⑤",
      "reason": "정당화 근거와 시행 절차의 역할을 논증 안에서 구분한다."
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "법과 처벌의 규범이 등장하나 정답은 허용/금지 판단이 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 9,
      "verdict": "본문 보조, 주로는 기각",
      "refutation": "법의 위계는 있지만 상위법이 하위법의 모든 절차를 포함한다는 상속은 성립하지 않는다.④를 고르는 직접 행동은 귀속 확인이다."
    },
    {
      "code": 46,
      "verdict": "③한정 보조",
      "refutation": "공권력 강화→동물 소송 가능이라는 인과는 참인③을 확인하지만④의 절차 귀속 오류를 대신하지 못한다."
    },
    {
      "code": 22,
      "verdict": "주로는 기각",
      "refutation": "상위/하위법의 효력 관계를 개체-범주의 속성 상속 관계로 보아 절차 규칙을 전파하면 오히려 오류를 만든다."
    }
  ],
  "countermodel": "어떤 규범이 하위 규칙의 유효성을 제한하더라도 하위 규칙의 상세 절차를 모두 직접 규정할 필요는 없다. 효력 제한과 내용 포함의 차이.",
  "confidence": 0.97
}
```
