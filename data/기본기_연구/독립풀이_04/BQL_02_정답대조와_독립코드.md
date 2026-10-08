

<!-- luna-raw:BQL-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G508",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "data/기본기_연구/prepared_backlog/sealed/G086_official_provenance/2016_KICE_Korean_B_odd_answer_table.pdf",
  "official_exam": "2016학년도 수능 국어 B형 홀수형",
  "question_number": 23,
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "문서 매뉴얼에서 반복 숙련으로 감각적 지식을 얻는 명시→암묵 변환이다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_hold_resolved": "sealed의 기존null을공식정답표연결로복원.예상답으로대체하지않음.",
  "scope_limit": "BQL⑤의완전한과정유보와BQM②의국소부적합판정을원blind대로보존."
}
```


<!-- luna-raw:BQL-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G508",
  "minimal_logic_without_codes": "각 사례의 출발 지식과 도착 지식을 찾아 변환쌍에 대응한다.③은 문서 명시지에서 감각적 암묵지로 간다.",
  "primary": [
    {
      "code": 45,
      "reason": "명시/암묵의 입력과 출력 방향을 추적하여 내면화에 대응한다."
    }
  ],
  "auxiliary": [
    {
      "code": 16,
      "reason": "각 유형의 정의 조건을 보존한다."
    },
    {
      "code": 25,
      "reason": "입출력 쌍으로 네 유형을 분류한다."
    },
    {
      "code": 37,
      "reason": "유형 정의에 부합하는 실제 사례를 찾는다."
    }
  ],
  "surface": [
    {
      "code": 40,
      "reason": "여러 매뉴얼이나 기술 요소가 등장해도 부분들의 단순 결합 여부가 모든 변환을 결정하지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 46,
      "rejection": "연습이 숙련을 낳는 인과가 있지만 정답을 가르는 직접 기준은 앞뒤 지식의 유형이다."
    },
    {
      "code": 3,
      "rejection": "입력과 출력의 순서는 필요하지만 네 변환이 반드시 이어지는 고정 단계라는 근거는 없다."
    },
    {
      "code": 100,
      "rejection": "⑤의 동물 형상은 소재이며 모든 사례를 비유의 유무로 분류할 수 없다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
