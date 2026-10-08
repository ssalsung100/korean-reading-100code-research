

<!-- luna-raw:AGU-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G201",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "외부에서주어진움직임의방향·속도를기준으로다른것의동작을그에따르게조절하는뜻이다.①노래를기준으로피아노연주를맞추는용법이가장가깝다.",
  "official_answer_source": "sealed canonical answer 기계 연결; 이번stage에서공식배포답표직접대조아님.",
  "group_barrier": "G201 전체 유효blindraw저장확인후 answer필드만공개. 원문범위·그림·밑줄hold는후속직접확인으로해소하고최초기록보존.",
  "sdss_seen": false,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AGU-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G201",
  "logic_without_codes_fixed": "사용자 움직임을 기준으로 바닥 동작을 그에 따르게 조절함과, 노래를 기준으로 피아노 연주를 그에 따르게 조절함이 같은 용법이다. 색 조화·협력·인원 충족·답 대조와 구별한다.",
  "primary": [],
  "primary_candidates": [
    96,
    39
  ],
  "working_representative": 96,
  "auxiliary": [],
  "surface": [
    45,
    93
  ],
  "evidence": [
    "ⓐ 사용자가 움직이는 방향과 속도에 맞춰 바닥 제어.",
    "① 피아노를 언니의 노래에 맞추어 침."
  ],
  "competing_codes": [
    {
      "code": 39,
      "reason": "두 용례의 문맥 의미를 비교하는 행동으로96과 국소 중첩한다. 양쪽을 대칭 재구성할 수 있어 유일 주 우위는 유보하고 후보로 보존."
    },
    {
      "code": 45,
      "reason": "원문은 장치 제어라는 입력·출력 소재이나 선택지의 용법 일치는 장치 작동을 추가 추론하지 않고 기준에 따른 행위 조절이라는 뜻을 비교하면 된다."
    },
    {
      "code": 93,
      "reason": "③의 손발을 맞추는 협력과⑤의 답 대조를 정답으로 고르는 문제가 아니다. 노래와 연주가 관련되었다는 사실만으로 의사소통 기능을 새로 부여하지 않는다."
    }
  ],
  "falsification_probe": "외부 진행 기준에 따름을 목표 인원수 충족으로 바꾸면 같은 맞추다라도④의 용법으로 달라진다. 대상 명사만이 아니라 조절 행위의 기준·방식을 보존해야 한다.",
  "confidence": 0.97,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
