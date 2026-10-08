

<!-- luna-raw:AFE-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G193",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "노드수감소에따른성능상승·탈중앙성저하의본문방향적용.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식배포답표직접대조아님",
  "group_barrier": "AFB/AFC/AFD/AFE 전체 blind raw 저장 후 answer 필드만 공개",
  "sdss_seen": false,
  "sdss_linkage_absence_disclosed_before_blind": true,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFE-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G193",
  "logic_without_codes_fixed": "기술의 다른 조건을 바꾼다는 정보 없이 B의 노드 수만 줄이는 상황에 본문의 변화 방향을 적용한다. 노드 증가에 따른 성능 저하 관계에서 노드 감소는 성능 상승 방향이고, 노드 감소에 따른 탈중앙성 저하는 직접 명시되어③이다.",
  "primary": [
    {
      "code": 49,
      "name": "상관관계",
      "reason": "본문에서 제시한 노드 수와 두 성질의 증감 방향을 보존·적용한다. 통계자료에서 인과를 추정하는 의미로 한정하지 않고 원표의 넓은 방향 관계 용례를 따른다."
    }
  ],
  "auxiliary": [
    {
      "code": 16,
      "name": "개념분석",
      "scope": "② 배제",
      "reason": "확장성은 단순히 노드를 늘리는 일이 아니라 노드 증가에도 성능 저하가 크지 않고 서비스를 유지하는 성질이다."
    },
    {
      "code": 15,
      "name": "기준",
      "scope": "④ 배제",
      "reason": "노드 수 제한 유무로 A/B의 비공개형/공개형을 대응한다."
    },
    {
      "code": 17,
      "name": "대상범주",
      "scope": "⑤ 배제",
      "reason": "보기의 위조 불가능성 향상 귀속은 B이다. A에 더 높은 무결성을 귀속하면 비교 주체를 뒤집는다."
    }
  ],
  "surface": [
    {
      "code": 70,
      "name": "딜레마",
      "reason": "본문 전체는 세 성질을 함께 높이기 어렵다고 설명하지만③은 최적 선택이나 손익 비교를 요구하지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 46,
      "name": "인과관계",
      "rebuttal": "원문에 노드 수가 성능에 영향을 준다는 기술이 있어 배제할 수 없는 넓은 설명이다. 다만③을 판정할 때 미제시 중간 원인 경로를 추가 복원할 필요가 없어 방향 적용을 대표49로 기록한다."
    },
    {
      "code": 43,
      "name": "타변수통제",
      "rebuttal": "B 자체의 노드 수만 바꾼다는 비교 조건은 유지해야 한다. 그러나 실험집단의 교란을 제거하거나 효과를 별도로 식별하는 문제는 아니므로 정답 주로 올리지 않는다. 새 알고리즘 등 다른 조건까지 변화하면 이 단순 방향 적용은 보장되지 않는다."
    },
    {
      "code": 45,
      "name": "함수",
      "rebuttal": "노드 수를 두 결과에 대응시키므로 넓게 함수로 표현 가능하지만 별도의 처리 단계·입출력 교환을 복원하지 않는다. 국소 중첩은 인정하되 추가 독립 연산으로 계수하지 않는다."
    }
  ],
  "evidence": [
    "마지막 문단: 노드 수 증가→성능 저하; 노드 수 감소→탈중앙성 저하.",
    "보기 B는 노드 수 제한이 없고 현재200개이며③은 그 수의 감소만 가정."
  ],
  "falsification_probe": "일반 명제 P이면Q의 역으로 성능 상승을 도출한다고 기록하지 않는다. 지문이 제시한 수량 변화 관계를 동일 기술의 비교 방향으로 읽는 것이다. 비단조 관계나 동시 기술 변경이 주어지면 반대 방향의 자동 적용은 금지한다.",
  "confidence": 0.95,
  "exposure": {
    "actual_sdss_tags_seen": false,
    "sdss_linkage_absence_preexposed": true,
    "strict_blind_eligible": false
  },
  "scope_limit": "주어진 지문·보기의 변수 관계만 분석. 실제 기술의 보편 성능 법칙이나 공격 방법으로 일반화하지 않는다.",
  "quota_status": "unavailable"
}
```
