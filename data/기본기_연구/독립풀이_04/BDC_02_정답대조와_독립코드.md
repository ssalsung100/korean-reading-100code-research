

<!-- luna-raw:BDC-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G390",
  "selected_answer": 2,
  "official_answer": "②",
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "answer_verification_scope": "봉인 공식 정답 필드 대조; 원 정답표 독립 시각 확인 미실시",
  "logic_without_codes_fixed": "카밀라 파워는 여기서 다른 사람과 닮았다는 비교 기준이 아니라 해당 주장을 하는 이론가 부류의 예이다. 첫 대항목 둘째 뜻풀이에 해당한다.",
  "original_blind_preserved": true,
  "sdss_seen": false,
  "group_blind_barrier_verified": true,
  "remaining_uncertainty": null
}
```


<!-- luna-raw:BDC-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G390",
  "primary_codes": [
    96
  ],
  "auxiliary_codes": [
    25,
    38
  ],
  "surface_codes": [
    39,
    69
  ],
  "decisive_operation": "같은의 문맥 기능을 비교 유사성 대신 이론가 부류의 구성원 예시로 판정해 사전 풀이와 대응한다.",
  "competitor_refutations": [
    {
      "code": 39,
      "reason": "다른 것과 다르지 않다는①은 가능한 뜻이지만 이 문맥은 두 대상의 공통 속성을 비교하지 않는다."
    },
    {
      "code": 69,
      "reason": "비유나 유추는 의미의 표면 가능성일 뿐, 카밀라 파워는 예시된 실제 이론가로 제시된다."
    },
    {
      "code": 38,
      "reason": "개체가 부류에 속한다는 뜻풀이의 내용을 직접 드러낸다. 주96의 문맥 의미 판독과 동일 근거를 공유하는 국소 공동 후보."
    }
  ],
  "boundary_note": "96/38/25는 어휘 판독·개체 귀속·분류 출력의 층위. 문장 끝의같다 추정 양상2와도 다름.",
  "confidence": 0.89,
  "sdss_seen": false,
  "group_answer_check_complete": true
}
```
