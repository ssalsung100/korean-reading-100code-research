

<!-- luna-raw:BJC-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G445",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BJC.json",
  "necessary_information": [
    {
      "location": "4문단부호화예시",
      "evidence": "각정점8염기.간선은출발정점뒤절반4와도착정점앞절반4를이어상보화하므로8염기."
    },
    {
      "location": "DNA컴퓨팅전략과마지막문단",
      "evidence": "후보병렬생성후조건검사로선별.1994에이들먼방법."
    }
  ],
  "minimal_logic_without_codes": "정점두개전체를잇는것이아니라각각절반을잇기때문에간선염기수는4+4=8로정점과같다.두배라는⑤가틀리다.",
  "intermediate_reasoning": [
    "①②는창시자와정보표현·연산정의에직접부합.③은후보생성후선별전략.④는순차계산에서분자병렬반응으로접근한변화에부합.",
    "상보적치환은염기종류를바꿀뿐염기개수를늘리지않는다.두가닥구조전체염기수와간선한가닥코드길이도구별한다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "조건을하나씩검사한다는순차단계를보고모든후보를먼저생성하지않는다고오독할수있다.본문은대규모혼성화로후보를만들고그후필터링한다."
  },
  "source_limitations": [
    "본문4n표기는문맥상4의n승으로읽히나이문항판정에는그표현을사용하지않았다.정확한서식복원전외연수계산근거로쓰지않는다."
  ]
}
```
