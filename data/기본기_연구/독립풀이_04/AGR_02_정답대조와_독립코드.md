

<!-- luna-raw:AGR-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G201",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "장갑의 두 방향은 아바타 쪽 설정 감각→사용자와 사용자 움직임→아바타다. 사용자와아바타가서로감각반응을주고받는다는⑤는움직임전달을감각전달로바꿨다.",
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


<!-- luna-raw:AGR-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G201",
  "logic_without_codes_fixed": "장갑은 가상 물체의 감각을 사용자에게, 사용자의 손·팔 움직임을 아바타에게 전달한다. 두 방향이 있다는 사실을 동일한 감각 정보가 양방향 전달된다고 바꾸지 않는다.",
  "primary": [],
  "primary_candidates": [
    45,
    17
  ],
  "working_representative": 45,
  "auxiliary": [
    39
  ],
  "surface": [
    93,
    80
  ],
  "evidence": [
    "2문단 크기·형태·온도 등 가상 감각→사용자; 손가락·팔 움직임→아바타.",
    "⑤ 서로 감각 반응을 주고받는다는 진술."
  ],
  "competing_codes": [
    {
      "code": 17,
      "reason": "정보 종류를 각 전달 방향에 귀속하는 행동으로45의 입출력 대응과 국소 중첩한다. 후보로 남기고 유일 주 우위는 확정하지 않는다."
    },
    {
      "code": 93,
      "reason": "전달·주고받음이라는 표면은 있으나 발화·의미·의도 소통을 분석하는 문제가 아니다. 장치의 입력·출력과 전달 내용의 역할을 보존해야 한다."
    },
    {
      "code": 80,
      "reason": "사용자의 감각 체험이 소재지만 지각의 성립이나 믿음의 정당화를 따지는 것이 아니라 장치가 어느 정보를 어느 쪽에 전달하는지를 묻는다."
    }
  ],
  "falsification_probe": "⑤의 사용자→아바타 쪽 감각 반응을 동작 정보로 바꾸면 본문의 두 방향 관계가 회복된다. 양방향이라는 말 자체가 오류인 것이 아니다.",
  "generation_principle": "정보 흐름의 방향과 정보 종류를 별도 칸으로 고정한 뒤 한 칸만 교환하여 오답의 정확한 위치를 기록한다.",
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
