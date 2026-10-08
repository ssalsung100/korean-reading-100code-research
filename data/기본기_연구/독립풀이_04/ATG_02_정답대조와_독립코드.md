

<!-- luna-raw:ATG-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G307",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "비교 대상과 비유적 지칭을 구분하고 각 표현의 역사적 지시 대상을 유지한다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ATE",
    "ATF",
    "ATG"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ATG-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G307",
  "primary": [
    99
  ],
  "auxiliary": [
    46,
    39,
    100
  ],
  "surface": [
    3
  ],
  "decisive_operation": "시의 당신·그분·형제/동생을 본문의 인물에 대응하고 숙명의 의미를 최초 살해→후대 내전이라는 시적 원인 연결로 복원한다.",
  "competing_codes": [
    {
      "code": 46,
      "rebuttal": "정답② 직접 확인은 원죄→내전 인과 해석이라46도 공동 주 후보 가능.99는 다른 선지의 지칭 오류 제거를 대표한다."
    },
    {
      "code": 100,
      "rebuttal": "저주·숙명의 함축은 유효하지만①의 맹수 비교를 무조건 동일시로 읽으면 오독이다."
    },
    {
      "code": 3,
      "rebuttal": "작시 시점은 내전/재건 맥락을 돕지만 지칭과 의미 관계를 대신하지 않는다."
    }
  ],
  "boundary_note": "정답 직접 확인46과 지칭 오답 배제99의 경로를 분리한다. 시적 인과를 실제 역사 인과로 승인하지 않는다.",
  "confidence": 0.94,
  "sdss_seen": false
}
```
