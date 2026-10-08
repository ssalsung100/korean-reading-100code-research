

<!-- luna-raw:BQP-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G509",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2017/2017_answer_2017학년도_법학적성시험_언어이해_정답표.hwp",
  "answer_transcription_source": "자료/LEET_언어이해/텍스트/2017/2017_answer.md",
  "question_number": 3,
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "위법성을긍정해도책임이라는별도요건을검토해야하므로이사건의책임여부를따진다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_hold_resolved": "공식답정본과전사연결로null복원",
  "scope_limit": "제시문 내부 범죄정의에 한정하며 현실 법률의 일반 조언으로 확대하지 않는다."
}
```


<!-- luna-raw:BQP-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G509",
  "minimal_logic_without_codes": "구성요건 해당과 위법성만으로는 범죄가 확정되지 않아 책임을 따진다.위법성과 책임은 서로 다른 판단 대상과 기준을 갖는다.",
  "primary": [
    {
      "code": 10,
      "reason": "범죄 성립의 남은 필요요건인 책임을 검토하는③의 이유를 복원한다."
    }
  ],
  "auxiliary": [
    {
      "code": 16,
      "reason": "행위의 위법성과 행위자의 법적 비난가능성이라는 책임 개념을 구별한다."
    },
    {
      "code": 17,
      "reason": "법질서와 관계를 따지는 행위,개별 상황에서 비난하는 행위자의 대상을 나눈다."
    },
    {
      "code": 79,
      "reason": "기대가능성을 포함한 법적 책임과 윤리적 비난을 구별한다."
    }
  ],
  "surface": [
    {
      "code": 3,
      "reason": "구성요건·위법성·책임의 검토 순서가 있으나 단순 선후가 판단의 이유는 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 12,
      "rejection": "같은 필요조건 명제를 조건문으로 표상할 수 있지만 위법성→책임 또는 위법성→범죄라는 충분관계는 성립하지 않는다.12를 배타적 경쟁자로 폐기하지 않는다."
    },
    {
      "code": 2,
      "rejection": "다른 행동의 기대가능성은 책임 정의의 요소지만③은A의 물리적 행동 가능성을 새로 계산하는 문제가 아니다."
    },
    {
      "code": 38,
      "rejection": "두선원의대인관계보다범죄성립요건과평가기준의구별이중심이다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
