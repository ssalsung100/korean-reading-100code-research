

<!-- luna-raw:AAK-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G168",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "ⓐ의 보호를 존립 이유로 설정함과① 기사를 주장의 근거로 설정함이 같은 용법이다.",
  "official_answer_source": "sealed canonical answer 기계 연결. 이번 stage에서 공식 배포 답표 직접 대조한 것은 아님.",
  "strict_blind_eligible": false,
  "stage_qualification": "과거 원문·전체답표 노출 후 재구성 결과의 대조이며 strict blind 정답률에서 제외.",
  "group_barrier": "AAG 실제 범위 복원 후 여섯 사례 전체 코드 없는 재구성 raw 저장 확인을 거쳐 answer 필드만 공개.",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AAK-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G168",
  "logic_without_codes_fixed": "시민 보호를 국가의 존립 이유로 삼음과 신문 기사를 주장의 근거로 삼음은 대상을 어떤 역할·근거로 설정하는 같은 용법이다. 다른 선지는 같은 어형이어도 추상적 직면/물리적 충돌, 실현·유지 곤란/이해 난도, 잔존/이익 발생, 제시/장소 이동으로 뜻이 달라진다.",
  "primary": [
    {
      "code": 96,
      "name": "일상언어",
      "reason": "문맥과 논항 역할을 보존하여 동일 어형의 실제 의미를 비교한다."
    }
  ],
  "auxiliary": [
    {
      "code": 39,
      "name": "비교대상",
      "reason": "원문 용례와 선택지 용례를 한 쌍씩 대응해 의미가 같거나 다른 지점을 확인한다. 의미 비교 안의 절차이며 별도 독립 연산으로 중복 계수하지 않는다."
    }
  ],
  "surface": [
    {
      "code": 100,
      "name": "비유",
      "reason": "부딪히다·내놓다의 물리/추상 차이가 일부 오답에 보이지만 모든 용례를 비유 하나로 판정하지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 16,
      "name": "개념분석",
      "rebuttal": "본문이 새 전문 개념을 정의하고 그 조건을 적용하는 것이 아니다. 일상어의 문맥 의미를 파악하는 데 정의형 표현을 쓸 수 있지만 그것만으로16 주를 부여하지 않는다."
    },
    {
      "code": 100,
      "name": "비유",
      "rebuttal": "②·⑤의 문자적/확장된 의미 대비에는 도움이 되나①의 역할 설정 일치나③의 곤란 대상 차이를 전부 설명하지 않는다."
    },
    {
      "code": 39,
      "name": "비교대상",
      "rebuttal": "두 용례 비교는 필수이나96의 실제 풀이 행동을 넓게 기술한 것과 중첩한다. 번호가 다르다는 이유로 독립 경계를 만들지 않고 작업 대표96을 유지한다."
    }
  ],
  "evidence": [
    "ⓐ 보호하는 것을 일차적 존립 이유로 삼았다 /① 기사를 주장의 근거로 삼았다.",
    "ⓒ 기본 원리 유지가 어렵다 /③ 전문 용어가 어렵다."
  ],
  "generation_note": "단순 물리/추상 이분법만으로 풀리지 않도록 같은 곤란 표현의 대상·행위 차이도 오답 근거로 보존한다.",
  "confidence": 0.98,
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
