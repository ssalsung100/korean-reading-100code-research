

<!-- luna-raw:AGS-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G201",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "아바타가경사로를만나는환경변화에따라트레드밀기울기가변경될수있다는③은본문허용가능성을적용한다.",
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


<!-- luna-raw:AGS-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G201",
  "logic_without_codes_fixed": "가상 환경 변화에 따라 트레드밀의 기울기도 변경될 수 있다는 명시 관계에 경사로 사례를 적용한다. 센서의 측정 기능과 컴퓨터의 제어 기능 및 HMD 표시 결과를 서로 교환하지 않는다.",
  "primary": [
    12
  ],
  "auxiliary": [
    45,
    2
  ],
  "primary_scope": "가상 환경 변화라는 조건과 트레드밀 기울기 변경 가능이라는 결과를 경사로에 적용.",
  "auxiliary_scope": {
    "45": "①측정 대상,②제어 주체/표시 결과,④동기화 방향,⑤입력 종류를 보존하여 오답 배제.",
    "2": "③의 변경될 수 있음을 필연적 변경으로 높이지 않음. 조건의 후건 자체가 가능성이다."
  },
  "surface": [
    46
  ],
  "evidence": [
    "공식[A] 가상 환경 변화에 따라 바닥 진행 속도·방향·기울기 변경되기도 함.",
    "관성 센서=속도변화율·회전속도; 압력 센서=뛰는힘; 컴퓨터=바닥제어."
  ],
  "competing_codes": [
    {
      "code": 45,
      "reason": "환경을 입력, 기울기를 출력으로 기술하면③의 같은 관계와 중첩한다.12는 사례 조건의 적용을 드러내는 대표이며 코드 전체의 독점 경계는 주장하지 않는다. 오답별 장치 역할은 별도 보조 범위로 기록."
    },
    {
      "code": 46,
      "reason": "환경 변화의 효과라는 넓은 인과 기술은 가능하지만 중간 장치 작용을 새로 추론하지 않고 본문 관계를 그대로 적용한다. 실제 물리적 인과 메커니즘으로 확대하지 않음."
    },
    {
      "code": 10,
      "reason": "경사로가 기울기 변경의 필요조건이거나 가상 환경만이 변경 원인이라고 말하지 않는다. 본문에 사용자 움직임이라는 다른 입력도 있어 유일 요건화는 틀림."
    }
  ],
  "falsification_probe": "가능한 결과라는 진술을 경사로를 만나면 반드시 기울어진다고 바꾸면 근거보다 강하다. 여러 입력 경로를 하나의 배타적 필수 경로로 만들지 않는다.",
  "confidence": 0.97,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
