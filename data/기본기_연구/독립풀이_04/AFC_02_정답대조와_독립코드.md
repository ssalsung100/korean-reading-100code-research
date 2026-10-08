

<!-- luna-raw:AFC-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G193",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "본문상연결에앞서다른데이터와비교검증이필요.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식배포답표직접대조아님",
  "group_barrier": "AFB/AFC/AFD/AFE 전체 blind raw 저장 후 answer 필드만 공개",
  "sdss_seen": false,
  "sdss_linkage_absence_disclosed_before_blind": true,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFC-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G193",
  "logic_without_codes_fixed": "본문이 정한 절차에서 연결 완료에는 다른 블록 내용과의 비교 검증과 승인이 선행해야 한다. 연결되었다면 비교를 거쳤다는 방향은 성립하나 비교만 했다고 승인이 보장되지는 않는다.",
  "primary": [
    {
      "code": 10,
      "name": "필요조건",
      "reason": "⑤의 연결되기 위해서는 비교되어야 한다에서 결여할 수 없는 선행 요건을 복원한다."
    }
  ],
  "auxiliary": [
    {
      "code": 45,
      "name": "함수",
      "scope": "본문 단계 대응 및① 배제",
      "reason": "검증 대상은 내용이고 승인 결정 대상은 연결 여부다. 참여 노드 선정으로 처리 대상/출력을 바꾼①을 배제한다."
    },
    {
      "code": 4,
      "name": "양화",
      "scope": "② 배제",
      "reason": "특정 노드의 변경 블록 및 이후 블록을 전체 노드의 모든 블록으로 확장할 근거가 없다."
    },
    {
      "code": 84,
      "name": "분수식",
      "scope": "④ 배제",
      "reason": "성능=저장량/시간이므로 같은 양에 시간이 짧아지면 성능이 높다."
    }
  ],
  "surface": [
    {
      "code": 3,
      "name": "선후",
      "reason": "순서 자체가 보이지만⑤는 단순 시간 선후를 넘어 규정된 필수 단계를 묻는다."
    }
  ],
  "competing_codes": [
    {
      "code": 12,
      "name": "조건문",
      "rebuttal": "연결→비교로 같은 명제를 표현할 수 있어10과 국소 동치다. 대표10은 필요성을 질문하는 방향을 나타낼 뿐 전역 배타 경계를 새로 만들지 않는다."
    },
    {
      "code": 3,
      "name": "선후",
      "rebuttal": "앞서 일어났다는 사실만으로 반드시 거쳐야 하는 요건은 되지 않는다. 이 지문은 모든 연결이 검증·승인을 거치는 절차를 명시하기 때문에⑤가 성립한다."
    },
    {
      "code": 46,
      "name": "인과관계",
      "rebuttal": "비교가 연결을 자동 발생시킨다는 설명이 아니다. 검증 후 승인 단계가 남아 비교→연결 보장은 성립하지 않는다."
    }
  ],
  "evidence": [
    "1문단: 내용 상충/이중 포함 검증→검증이 끝난 블록 연결 여부 승인→승인 완료 블록 연결.",
    "⑤의 필요조건 표현을 최초 blind 논리에 재대조했다."
  ],
  "counterfactual_probe": "검증이 권장되지만 생략 가능한 절차로 바뀌면 단순 선후 기술을 유지해도⑤의 필요성은 깨진다. 비교 후 승인되지 않는 경우는⑤와 모순되지 않는다.",
  "confidence": 0.98,
  "exposure": {
    "actual_sdss_tags_seen": false,
    "sdss_linkage_absence_preexposed": true,
    "strict_blind_eligible": false
  },
  "quota_status": "unavailable"
}
```
