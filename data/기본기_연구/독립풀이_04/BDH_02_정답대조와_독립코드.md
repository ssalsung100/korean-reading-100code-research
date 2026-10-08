

<!-- luna-raw:BDH-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G392",
  "selected_answer": 4,
  "official_answer": "④",
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "answer_verification_scope": "봉인 공식 정답 필드 대조; 원 정답표 독립 시각 확인 미실시",
  "logic_without_codes_fixed": "범패 연주를 포함했다는 사실에는 참석자 사이 우열·서열의 차등을 표현한다는 근거가 없다. 다른 보기는 자리·방향·역할·예를 받는자와 행하는자의 차이를 드러낸다.",
  "original_blind_preserved": true,
  "sdss_seen": false,
  "group_blind_barrier_verified": true,
  "remaining_uncertainty": "BDH⑤ 군신의 비대칭 행위에 대한 문맥적 해석을 사용. 단순 절차 존재만으로 모든 의례가 차등을 표상한다는 일반화는 금지."
}
```


<!-- luna-raw:BDH-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G392",
  "primary_codes": [
    37
  ],
  "auxiliary_codes": [
    9,
    100,
    10
  ],
  "surface_codes": [
    44
  ],
  "decisive_operation": "예를 받는자/행하는자,문무·관품 차이를 자리와 역할로 표상한 사례인지 확인한다.범패 수용 자체에는 그런 위계 대응이 제시되지 않는다.",
  "competitor_refutations": [
    {
      "code": 9,
      "reason": "보기의 기준 내용은 사회적 서열이다. 사례 적합성을 검사하는37과 같은 축의 경쟁이라기보다 대상 관계와 검사 행동의 차이."
    },
    {
      "code": 100,
      "reason": "자리·상징·행례가 질서의 우열을 나타낸다는 대응에서 적용. 모든 절차가 상징이라는 이유만으로 차등화 사례가 되는 것은 아니다."
    },
    {
      "code": 44,
      "reason": "통합과 통치라는 의례의 목적 전체로 넓히면 범패도 제도 일부라며 수용할 위험. 여기서는 지정된 차등화 기능의 사례를 찾는다."
    }
  ],
  "boundary_note": "37/10은 사례요건 국소 중첩. 공간이라는 말을 고정 좌표로만 제한하면③·⑤의 절차적 역할 차이를 놓친다.",
  "confidence": 0.89,
  "sdss_seen": false,
  "group_answer_check_complete": true
}
```
