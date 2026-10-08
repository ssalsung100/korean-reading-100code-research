

<!-- luna-raw:ATY-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G313",
  "initial_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "official_answer_source": "prepared_backlog/sealed/answer_sdss.jsonl의 공식 페이지 검증 정본",
  "code_free_logic": "최초 blind에 고정한 세포별 작용 경로/용량과 작용 종류 구분/질환별 목적 구분을 유지한다.",
  "barrier": "group 전체 blind raw 3건 저장 후 공개"
}
```


<!-- luna-raw:ATY-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    44
  ],
  "auxiliary": [
    37,
    17,
    19
  ],
  "surface": [
    46,
    50
  ],
  "decisive_operation": "두 질환의 치료·예방 목적과 수술 전후 위험을 각각 대응시켜 같은 계열 약물이면 중복이라는 결론을 거부한다.",
  "code_evidence": {
    "44": "동맥경화 예방/관절염 진통의 목적에 다른 사용을 배정",
    "37": "진료 기록의 병력·수술 조건에 본문 적용",
    "17": "공통 COX 억제 범주와 동일 임상 역할을 혼동하지 않음",
    "19": "④ 회복되지 않는 지혈 작용을 정상 혈소판 보충으로 보완하는 오답 제거 경로"
  },
  "competitor_refutations": [
    {
      "code": 23,
      "reason": "효소 억제 공통점만으로 두 목적의 동시 충족이나 완전 대체는 보장되지 않는다."
    },
    {
      "code": 20,
      "reason": "복수 약물이 한 목적을 충분히 실현한다는 조건은 입증되지 않아 대체 가능으로 처리할 수 없다."
    },
    {
      "code": 19,
      "reason": "④의 보충은 국소 제거 근거이며 정답①의 목적 차이를 대체하지 않는다."
    },
    {
      "code": 63,
      "reason": "의사 조치 타당성 평가지만 논증 강화·약화 자료를 새로 제시하는 과제는 아니다."
    }
  ],
  "confidence": 0.93,
  "passage_group": "G313",
  "sdss_seen": false
}
```
