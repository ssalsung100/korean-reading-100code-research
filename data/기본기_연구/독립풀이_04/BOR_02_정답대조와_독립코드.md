

<!-- luna-raw:BOR-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G493",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2025/2025_answer_2025언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "생산함수가 정태상태에 영향을 준다는 명시 문장을 부정한①이 틀리다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BOR-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G493",
  "minimal_logic_without_codes": "정태상태 자본량을 결정하는 기초 여건에 생산함수가 포함된다는 본문과①의 영향 없음이 충돌한다.",
  "primary": [
    {
      "code": 45,
      "reason": "생산함수·저축률·감가상각률을 정태상태를 결정하는 입력으로 유지한다."
    }
  ],
  "auxiliary": [
    {
      "code": 92,
      "reason": "투자-감가상각=자본 변화의 식과 저축=투자의 항등식을 판독한다."
    },
    {
      "code": 43,
      "reason": "인구·기술을 고정한 단순 모형의 조건 안에서 판단한다."
    },
    {
      "code": 87,
      "reason": "⑤에서 자본의 증가에 대한 생산 증가폭의 감소를 수준 감소와 구별한다."
    }
  ],
  "surface": [
    {
      "code": 49,
      "reason": "자본과생산의증가방향은③에있으나①의결정오류는함수의영향을삭제한것이다."
    }
  ],
  "competing_codes": [
    {
      "code": 46,
      "rejection": "현실경제의새로운 인과를실증하는것이아니라주어진모형의결정요인을확인한다."
    },
    {
      "code": 91,
      "rejection": "생산은증가함수이지만한계효과가감소하므로일정비율의정비례로보면안된다."
    },
    {
      "code": 85,
      "rejection": "생산의소비/투자배분은있지만①의정태상태결정은고정총합배분만으로설명되지않는다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
