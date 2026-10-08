

<!-- luna-raw:AAJ-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G168",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "조정 시작의 요건인 합의가 없어 재판 절차를 따라야 한다. 조정위원회의 자료 수집 가능을 실제 이 분쟁 절차에 옮긴⑤는 적용 절차를 잘못 잡았다.",
  "official_answer_source": "sealed canonical answer 기계 연결. 이번 stage에서 공식 배포 답표 직접 대조한 것은 아님.",
  "strict_blind_eligible": false,
  "stage_qualification": "과거 원문·전체답표 노출 후 재구성 결과의 대조이며 strict blind 정답률에서 제외.",
  "group_barrier": "AAG 실제 범위 복원 후 여섯 사례 전체 코드 없는 재구성 raw 저장 확인을 거쳐 answer 필드만 공개.",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AAJ-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G168",
  "logic_without_codes_fixed": "당사자 합의가 있어야 조정 절차가 시작된다. 보기에서 갑의 거절로 합의가 없으므로 재판 절차를 따라야 한다. 조정위원회의 자료 수집 가능을 이 분쟁의 실제 절차에 붙인⑤가 틀리다.",
  "primary": [
    {
      "code": 10,
      "name": "필요조건",
      "reason": "조정 시작의 필요조건인 합의가 충족되지 않았다는 사실로 조정 절차 적용을 차단한다."
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "name": "대상범주",
      "reason": "자료 수집 주체·기능이 조정위원회에 귀속된다는 정보를 재판 절차로 옮기지 않는다."
    },
    {
      "code": 24,
      "name": "원칙/예외",
      "scope": "①·③·④ 배제",
      "reason": "갱신 요구 보호에는 실거주 사유 증명에 의한 거절이 가능하고, 상한 초과 상가에는 최단 기간이 적용되지 않으며 기간 미정이면 자유로운 종료가 가능하다."
    },
    {
      "code": 75,
      "name": "경쟁입장",
      "scope": "②·④ 배제",
      "reason": "기간 보호는 복지적 평등·연대, 계약에 따른 자유로운 종료는 자유 보장의 가치와 대응한다."
    }
  ],
  "surface": [
    {
      "code": 45,
      "name": "함수",
      "reason": "조건에 따른 절차 분기와 각 기관의 기능 대응으로도 표현 가능하지만 필요조건 차단과 동일 근거를 중복 계수하지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 12,
      "name": "조건문",
      "rebuttal": "조정→합의의 대우 및 불합의→재판이라는 본문 명제를 적용하므로10과 국소 동치다. 주10은 탈락한 진입 요건을 강조하는 대표 표기일 뿐 번호간 배타 경계가 아니다."
    },
    {
      "code": 50,
      "name": "길이막히면뒤로못간다",
      "rebuttal": "요건 부재로 절차 진입이 막힌다는 관점에서 중첩 가능하다. 물리적 작용 경로의 중단을 추가 복원하는 것은 아니며10/12와 별개의 필수 연산으로 늘리지 않는다."
    },
    {
      "code": 17,
      "name": "대상범주",
      "rebuttal": "자료 수집 주체 혼동만 알아도 의심할 수 있으나 현재 사건이 조정이 아닌 재판임을 확정하려면 합의 요건을 적용해야 한다. 귀속은 후속 보조로 유지한다."
    }
  ],
  "evidence": [
    "(나) 마지막 문단: 합의해야 시작, 합의가 없으면 재판; 자료 수집은 조정위원회 기능.",
    "보기: 을의 조정 제안에 갑 거절하여 합의가 이루어지지 않음."
  ],
  "scope_limit": "지문에 제시된 두 절차와 기능 범위의 판정이며 현실 법률 전체에서 다른 지원 가능성을 부정하지 않는다.",
  "confidence": 0.98,
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
