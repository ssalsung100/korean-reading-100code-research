

<!-- luna-raw:AGT-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G201",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "키넥트센서가파악하는것은실제피사체사용자의입체·동작정보다. 가상공간물체들사이거리측정으로입체감을구현한다는①은측정대상과장치역할을바꿨다.",
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


<!-- luna-raw:AGT-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G201",
  "logic_without_codes_fixed": "키넥트의 카메라가 측정하는 것은 현실의 피사체·사용자 정보다.①은 이를 가상 공간 물체 사이 거리 측정으로 바꾸고 입체감 구현까지 연결한다.④는 센서 전체 정보가 아니라25점 골격 이미지의 표상 한계를 묻는다.",
  "primary": [
    17
  ],
  "auxiliary": [
    45,
    40
  ],
  "primary_scope": "측정 대상의 현실 사용자/가상 물체 귀속을 유지한다.",
  "auxiliary_scope": {
    "45": "적외선 저해상도 입체+RGB 고해상도 컬러→골격 이미지→사용자 동작이라는 처리 단계 및 HMD의 가상 영상 전달 역할 구분.",
    "40": "④골격 이미지의 연결점 위치·수에 얼굴 세부점이 없음을 원그림에서 확인. RGB 원영상의 모든 정보가 최종 골격에 보존된다고 확대하지 않음."
  },
  "surface": [
    42,
    80
  ],
  "evidence": [
    "보기 카메라는 피사체 표면 반사광·컬러를 포착하고 사용자 검출 시25점 골격을 제공.",
    "실제 그림의 머리 영역은 단일 연결점이며 눈·입 세부 표정점 없음."
  ],
  "competing_codes": [
    {
      "code": 45,
      "reason": "측정입력을 현실피사체에서 가상물체로 바꾼 오류로도 표현 가능해17과 국소 중첩한다. 주17은 대상 교환을 드러내는 대표이며45의 보조 역할은 다른 처리 단계 확인 범위와 구별."
    },
    {
      "code": 42,
      "reason": "현실/가상이라는 차이를 장치의 내부/외부 경계로 바꾸면 원문에 없는 공간 관계가 생긴다. 어떤 대상을 측정하는지 직접 기록하면 충분."
    },
    {
      "code": 80,
      "reason": "입체감이 언급되어도①오류는 인식 가능성의 일반 논증이 아니라 측정 대상과 장치 기능의 바꿔치기다. 단순 지각 소재만으로 주코드를 부여하지 않는다."
    }
  ],
  "falsification_probe": "골격 이미지에 얼굴 세부 연결점을 추가한다는 변경은④의 근거를 바꿀 수 있으나 RGB 원영상의 해상도만 높였다는 정보는 동일25점의 표정 한계를 자동 해소하지 못한다.",
  "boundary_note": "40의 구성 한계와 처리 과정45의 정보 보존 범위는 국소적으로 결합하며 번호별 독점 기여는 유보.",
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
