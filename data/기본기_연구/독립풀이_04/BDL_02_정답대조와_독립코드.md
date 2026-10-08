

<!-- luna-raw:BDL-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G394",
  "selected_answer": 2,
  "official_answer": "②",
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "answer_verification_scope": "봉인 공식 정답 필드 대조; 원 정답표 독립 시각 확인 미실시",
  "logic_without_codes_fixed": "아로마타제는 이미 합성된 남성 호르몬을 여성 호르몬으로 바꾼다.②는 전환의 입력을 산출물로 바꿔 남성 호르몬 합성에 필요하다고 했다.",
  "original_blind_preserved": true,
  "sdss_seen": false,
  "group_blind_barrier_verified": true,
  "remaining_uncertainty": null
}
```


<!-- luna-raw:BDL-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G394",
  "primary_codes": [
    45
  ],
  "auxiliary_codes": [
    17,
    46,
    10
  ],
  "surface_codes": [
    49
  ],
  "decisive_operation": "아로마타제의 입력은 남성 호르몬,산출은 여성 호르몬임을 고정해 효소가 입력물질 합성에 필요하다는②를 반증한다.",
  "competitor_refutations": [
    {
      "code": 17,
      "reason": "합성 장소와 전환 물질의 역할을 구별하는 귀속 판독으로45와 공유.정답 입력/산출 뒤바꿈을45가 구체적으로 표시."
    },
    {
      "code": 10,
      "reason": "필요하다는 결론은 강하지만 단지 필요성 증거 없음보다 실제 반대 방향 전환이라는 양성 근거가 결정적이다."
    },
    {
      "code": 46,
      "reason": "생식샘 조절 인과가 배경이나 효소의 입력/산출을 확인하면②를 직접 배제할 수 있다.③은간접조절 경로에46필요."
    }
  ],
  "boundary_note": "효소 작용의 필요성 일반론이 아니라 어떤 산출에 필요한가를 보존한다.",
  "confidence": 0.92,
  "sdss_seen": false,
  "group_answer_check_complete": true
}
```
