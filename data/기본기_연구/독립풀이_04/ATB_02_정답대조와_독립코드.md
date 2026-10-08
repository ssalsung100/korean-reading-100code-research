

<!-- luna-raw:ATB-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G306",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "strict_blind_eligible": false,
  "logic_without_codes": "주택 없이도 다른 점수 조합으로 기준을 충족한다. 직업 범주 두 행을 동시에 합산하지 않는다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ATB",
    "ATC",
    "ATD"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ATB-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G306",
  "primary": [
    20
  ],
  "auxiliary": [
    10,
    45,
    92
  ],
  "surface": [
    84
  ],
  "decisive_operation": "주택 점수 없이 다른 입력 조합으로3점 이상을 구성하여 주택 소유가 필수 아님을 확인한다.",
  "competing_codes": [
    {
      "code": 10,
      "rebuttal": "필요조건 부정과20의 대체 실현은 같은 논리의 요건/경로 관점이다."
    },
    {
      "code": 45,
      "rebuttal": "점수 입력→합산→분류의 함수가 배경이나 정답은 한 입력이 없어도 같은 출력을 만드는 조합이다."
    },
    {
      "code": 84,
      "rebuttal": "소득90%는 점수 부여 기준이며 분수 계산은 정답에 필요하지 않다."
    }
  ],
  "independence_limit": "기준문서의 동일 소재 함수/인과 예시를 사전 열람했으므로 무노출 코드 판정으로 계수하지 않는다. 현재 SDSS 태그는 미열람.",
  "confidence": 0.97,
  "sdss_seen": false
}
```
