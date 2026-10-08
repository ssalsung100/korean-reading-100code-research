

<!-- luna-raw:BQK-answer_check-20261004-01 -->
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
  "question_number": 22,
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "명시지가 더 공유하기 쉽다는 비교의 방향을③이 뒤집는다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_hold_resolved": "sealed의 기존null을공식정답표연결로복원.예상답으로대체하지않음.",
  "scope_limit": "BQL⑤의완전한과정유보와BQM②의국소부적합판정을원blind대로보존."
}
```


<!-- luna-raw:BQK-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G508",
  "minimal_logic_without_codes": "같은 공유가능성 기준에서 명시지와 암묵지의 상대적 우열을 고정하면③의 방향이 반대임을 알 수 있다.",
  "primary": [
    {
      "code": 39,
      "reason": "비교 기준과 두 대상을 고정하여 상대적 순서를 뒤집은 오류를 찾는다."
    }
  ],
  "auxiliary": [
    {
      "code": 16,
      "reason": "객관적으로 형식화된 명시지와 표현하기 어려운 암묵지의 속성을 구분한다."
    },
    {
      "code": 17,
      "reason": "폴라니와 노나카의 주장을 서로 바꿔 귀속하지 않는다."
    }
  ],
  "surface": [
    {
      "code": 2,
      "reason": "공유가능성이라는 말이 있지만 가능/필연 강도 교환이 아니라 두 대상의 비교 방향 역전이다."
    }
  ],
  "competing_codes": [
    {
      "code": 86,
      "rejection": "정량적 크기나 상대량/절대량 변환이 제시되지 않아 일반적인 비교축 고정39가 더 직접적이다.숫자 없는 우열도86에 포함할지는 유보한다."
    },
    {
      "code": 13,
      "rejection": "암묵지와 명시지가 함께 쓰일 수 없다는 배타성 판정이 아니다."
    },
    {
      "code": 4,
      "rejection": "명시지가 모두 공유된다고 전칭으로 확대한 선지가 아니라 두 지식의 상대 순서를 뒤집었다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
