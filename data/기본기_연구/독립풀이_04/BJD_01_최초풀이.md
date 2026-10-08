

<!-- luna-raw:BJD-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G445",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BJD.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G445_visual01.jpg",
    "data/기본기_연구/prepared_backlog/blind_sources/G445_visual02.jpg"
  ],
  "necessary_information": [
    {
      "location": "그림2간선",
      "evidence": "0→1,0→2,1→2,1→3,2→3,3→4."
    },
    {
      "location": "코딩규칙및검사단계",
      "evidence": "출발뒤4+도착앞4의상보코드.1단계시작0끝4검사."
    }
  ],
  "minimal_logic_without_codes": "정점3개의경로를모든시작점에서열거하면012,013,023,123,134,234의6개다.4개라는④가틀리다.",
  "intermediate_reasoning": [
    "①1234는시작점1이라1단계에서이미탈락.정점수검사단계까지기다릴필요없다.",
    "②V3뒤AAGG+V4앞AATT=AAGGAATT의상보는TTCCTTAA로맞음.",
    "③혼성화로정점코드들을간선상보코드가연결하므로경로분자는이중가닥결합구조로표현된다.전체양끝의모든염기가빠짐없이쌍이라는추가주장은하지않는다.",
    "⑤5개정점을한번씩지나려면0→1→2→3→4뿐이다.0→2는1누락,1→3은2누락."
  ],
  "most_attractive_wrong": {
    "choice": 1,
    "exact_error": "정점이4개라는특징만보고2단계에서만탈락한다고생각한다.검사는순차적이므로시작점불일치가먼저걸러진다."
  }
}
```
