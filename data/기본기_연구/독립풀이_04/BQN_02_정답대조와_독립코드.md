

<!-- luna-raw:BQN-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G509",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2017/2017_answer_2017학년도_법학적성시험_언어이해_정답표.hwp",
  "answer_transcription_source": "자료/LEET_언어이해/텍스트/2017/2017_answer.md",
  "question_number": 1,
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "두사람의행위가현재의생명위난을피하려는목적이라는점을읽는다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_hold_resolved": "공식답정본과전사연결로null복원",
  "scope_limit": "제시문 내부 범죄정의에 한정하며 현실 법률의 일반 조언으로 확대하지 않는다."
}
```


<!-- luna-raw:BQN-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G509",
  "minimal_logic_without_codes": "둘의 행동은 생명 위난을 벗어나려는 목적에서 나왔다.그 목적이 같다는 사실은 각 행위가 적법하거나 도덕적으로 옳다는 평가와는 별개다.",
  "primary": [
    {
      "code": 78,
      "reason": "두 인물의 행위를 생존 목적과 연결하여①을 확인한다."
    }
  ],
  "auxiliary": [
    {
      "code": 44,
      "reason": "널판을 붙잡거나 상대를 밀어낸 행위가 위난 회피의 수단임을 읽는다."
    },
    {
      "code": 79,
      "reason": "④에서 도덕적 타당성과 법적 비난가능성을 구별한다."
    },
    {
      "code": 17,
      "reason": "A/B의 위치 교환으로 책임 기준이 달라진다고 할 근거가 없음을 확인한다."
    }
  ],
  "surface": [
    {
      "code": 46,
      "reason": "사망의 인과가 소재이나①의 핵심은 행위 목적의 공통성이다."
    }
  ],
  "competing_codes": [
    {
      "code": 13,
      "rejection": "두사람이한판에계속있으면살수없다는상황을모든행위목적의배타성으로확대하지않는다."
    },
    {
      "code": 10,
      "rejection": "범죄의요건검토는다른선지에중요하지만①을판정하려면목적서술을확인하면된다."
    },
    {
      "code": 83,
      "rejection": "법적판정과윤리적판정모두평가의틀이므로이를단순사실/가치의대립으로단정하지않는다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
