

<!-- luna-raw:AZI-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G359",
  "first_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "④는예방수단시행만제시되고그수단이실패했다는증거가없다.",
  "group_barrier": "전체blind저장후정답공개",
  "sdss_seen": false,
  "blind_record_quality_note": {
    "error": "most_attractive_wrong_answer에 선택답④를 입력하고 정답을 놓칠 위험을 적은 오류. AYP와 같은 형식 오류 재발. 원raw 보존.",
    "retrospective_wrong_analysis": "공식답 확인 후 보충:①을 고르기 쉽지만 격리 이전 보도에 이미 노출돼 예단을 가졌을 수 있으므로 격리조치의 실효성 의심에 부합한다.",
    "not_counted_as_original_wrong_option_analysis": true,
    "prevention": "앞으로 임시 raw append helper가 blind 선택답과 매력적오답 번호 동일시를 저장 전에 거부하도록 설정. 과거원장은수정안함."
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AZI-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G359",
  "primary": [
    63,
    44
  ],
  "auxiliary": [
    64,
    2,
    46
  ],
  "surface": [
    59
  ],
  "decisive_operation": "예방수단을 썼음에도 그 목적이 달성되지 않은 증거와 수단을 시행했다는 사실만 있는 경우를 구별한다.",
  "competing_codes": [
    {
      "code": 64,
      "rejection": "표현의자유침해라는다른쟁점을끌어오면실효성평가영역에서벗어난다."
    },
    {
      "code": 2,
      "rejection": "실패증거가없음은성공보장이아니므로④를효과확정사례로강화하지않음."
    },
    {
      "code": 46,
      "rejection": "①~③⑤에서수단효과가막히는경로는근거지만상위행동은실효성의심을지지하는지의평가."
    },
    {
      "code": 36,
      "rejection": "각실패사례는항상예방된다는주장의반례로도쓸수있으나실제대상주장은실효성에대한의심이다."
    }
  ],
  "sdss_seen": false,
  "confidence": 0.9,
  "quota_status": "unavailable"
}
```
