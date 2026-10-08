

<!-- luna-raw:AAC-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G167",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "독자 예상 밖 정보도 가능하다는 범위를 예상 안으로만 한정한② 기각.",
  "official_answer_source": "sealed answer_sdss canonical 기계 연결; 해당 배포정답표 별도 직접검증 아님",
  "group_barrier": "AAC/AAD/AAE 전체blind raw 저장 후 answer만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AAC-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    2
  ],
  "auxiliary": [
    17
  ],
  "surface": [
    4,
    45
  ],
  "evidence": "예상 밖 정보가 생성될 수 있음과 예상 범위 안으로만 제한됨은 같은 사건의 가능성을 인정/배제하는 차이.",
  "competing_codes": [
    {
      "code": 4,
      "assessment": "생성 정보 전체를 예상 안으로 제한하는 범위 표현으로도 기술 가능하여2와 국소 중첩. 개인 예측 범위 밖 정보의 존재 가능성을 직접 대조하는2 작업 대표."
    },
    {
      "code": 17,
      "assessment": "독자의 예상 범위와 실제 생성 정보 범위를 유지하는 보조. 무엇의 가능성인지 대상 범위를 먼저 특정."
    },
    {
      "code": 45,
      "assessment": "생성 시스템의 입력/출력을 다루지만 알고리즘 대응을 재구성하지 않고 원문의 가능성을 보존하면 충분."
    }
  ],
  "counterfactual_test": "독자 요구에 맞는 정보를 제공할 수 있다고 해서 독자가 그 모든 정보를 사전에 예상했다는 말은 아니다. 관련성과 예측 가능성을 구분.",
  "confidence": 0.92,
  "passage_group": "G167",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
