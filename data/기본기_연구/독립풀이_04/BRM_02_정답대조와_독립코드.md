

<!-- luna-raw:BRM-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G519",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "data/meet_answer_keys.json keys.2012.26/27; official_verified,2012_통합_정답표.pdf 1쪽 추출",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "이타적 동기에서 돕고 부수적으로 만족하는 관계를 유지한다.만족감 발생은 자기만족 목적의 증거로 충분하지 않다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BRM-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G519",
  "sdss_seen": false,
  "primary": [
    {
      "code": 78,
      "reason": "이타적도움의동기와행위뒤만족감을분리해행위의이기성귀속을판정한다."
    }
  ],
  "auxiliary": [
    {
      "code": 62,
      "reason": "만족감발생→만족감목적이라는추론의충분성을부정한다."
    },
    {
      "code": 46,
      "reason": "행위→만족의결과방향을유지한다."
    },
    {
      "code": 75,
      "cluster": "C074_075",
      "reason": "심리적이기주의와그비판자의입장을혼동하지않는다."
    }
  ],
  "surface": [
    {
      "code": 49,
      "reason": "동시발생도언급되지만결정적쟁점은목적·동기의귀속이다."
    }
  ],
  "competing_codes": [
    {
      "code": 55,
      "rejection": "잘못된원인연결로기술가능하나실제요구는어떤목적으로행위했는가의행위설명이다.배타경계로보지않는다."
    },
    {
      "code": 73,
      "rejection": "첫논증의욕구전제공격은③과관련되지만①의결정은이타적동기와행위평가의연결이다."
    },
    {
      "code": 36,
      "rejection": "의무감행위가욕구설명의반례지만이문항의①판정을단독설명하지못한다."
    }
  ],
  "confidence": 0.94
}
```
