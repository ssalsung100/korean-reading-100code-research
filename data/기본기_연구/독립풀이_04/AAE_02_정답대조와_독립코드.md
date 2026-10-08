

<!-- luna-raw:AAE-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G167",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "지역·시대를 바꾼 요청은 자기 생성 방향 편중 점검ⓒ이며 출처/사실/표현 편견 점검과 구별.",
  "official_answer_source": "sealed answer_sdss canonical 기계 연결; 해당 배포정답표 별도 직접검증 아님",
  "group_barrier": "AAC/AAD/AAE 전체blind raw 저장 후 answer만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AAE-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    17
  ],
  "auxiliary": [
    15,
    44
  ],
  "surface": [
    25,
    93,
    4
  ],
  "evidence": "행동별 점검 대상을 표현편견/출처/자기 요청 방향으로 분리하여 지역·시대 확장을ⓒ에 귀속.",
  "competing_codes": [
    {
      "code": 25,
      "assessment": "점검 유형에 행동을 분류한다는 의미에서17과 국소 중첩. 핵심은 주어진 구체 목적을 다른 점검 대상으로 옮기지 않는 것."
    },
    {
      "code": 15,
      "assessment": "무엇을 점검하는지의 기준을 유지하는 필수 보조. 신규 기준을 구성하거나 타당성을 검증하지 않음."
    },
    {
      "code": 93,
      "assessment": "출처 확인은④ 오답 배제에 해당하지만 정답③은 자기 요청 방향의 조절. 생성 자료 전달 경로 자체의 판정 아님."
    },
    {
      "code": 4,
      "assessment": "동양 안의 다양한 사례와 다양한 지역이라는 범위 차이는② 오독 반증에 유용하나 정답③의 목적 귀속을 대신하지 못함."
    }
  ],
  "counterfactual_test": "인터넷검색이라는 수단만으로출처/사실/편견검토를확정할수없다. 보기의 확인하기 위해라는 목적 서술이 귀속 근거이며 도구의 종류는 결정 기준이 아니다.",
  "confidence": 0.94,
  "passage_group": "G167",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
