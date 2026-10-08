

<!-- luna-raw:ATX-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G313",
  "initial_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "official_answer_source": "prepared_backlog/sealed/answer_sdss.jsonl의 공식 페이지 검증 정본",
  "code_free_logic": "최초 blind에 고정한 세포별 작용 경로/용량과 작용 종류 구분/질환별 목적 구분을 유지한다.",
  "barrier": "group 전체 blind raw 3건 저장 후 공개"
}
```


<!-- luna-raw:ATX-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    4,
    17
  ],
  "auxiliary": [
    1,
    52
  ],
  "surface": [
    46,
    24
  ],
  "decisive_operation": "④의 고용량에서 응고 억제만이라는 배타적 제한을 검증한다. 본문은 저용량 혈소판 활성 강도 차이를 설명하며 진통 소실을 말하지 않는다.",
  "code_evidence": {
    "4": "만이라는 다른 효과 전체 배제",
    "17": "용량·활성 정도의 차이를 작용 종류의 변경으로 교체",
    "52": "⑤ 응고 억제 물질 생성 억제→응고 촉진은 오답 제거 경로"
  },
  "competitor_refutations": [
    {
      "code": 52,
      "reason": "⑤를 제거하는 데 중요하지만 정답④의 무근거 효과 배제를 직접 설명하지 않는다. 주코드로 올리지 않는다."
    },
    {
      "code": 24,
      "reason": "고용량이 예외라는 규칙이 본문에 주어진 것이 아니라 선지가 임의 구성한다."
    },
    {
      "code": 12,
      "reason": "고용량→진통 없음의 조건 연결을 도출할 전제가 없다. 충분조건 연쇄 추론 문제로 환원하지 않는다."
    }
  ],
  "confidence": 0.91,
  "passage_group": "G313",
  "sdss_seen": false
}
```
