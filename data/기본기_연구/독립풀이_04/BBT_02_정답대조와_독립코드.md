

<!-- luna-raw:BBT-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G379",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "answer_source": "sealed/answer_sdss.jsonl official_answer; data/meet_questions.jsonl 정본전사",
  "verification_limit": "원 정답표 이번 세션 독립 재확인 없음",
  "all_group_blind_records_before_any_group_answer_check": true,
  "minimal_logic_without_codes": "군주가 관측과 계절 정립으로 천명을 백성 생활에 실천하는①이 핵심.④의 천문 징후와 통치 상태의 대응만으로는 역법 제정 기능이 빠짐.",
  "original_blind_preserved": true,
  "sdss_seen": false
}
```


<!-- luna-raw:BBT-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G379",
  "primary": [
    {
      "code": 37,
      "reason": "역법 제정으로 천명을 실천한다는 관념의 필수 구성 관계를 모두 보이는 사례① 선택"
    }
  ],
  "auxiliary": [
    {
      "code": 44,
      "reason": "천체 관측·계절 정립이라는 수단으로 천명 실천/백성 통치라는 목적을 구현"
    },
    {
      "code": 80,
      "reason": "하늘의 뜻을 읽는 관념은①④ 공유하지만④는 제정/실천 단계 부재"
    }
  ],
  "surface": [
    {
      "code": 100,
      "reason": "② 씨줄/날줄,⑤ 천지 형상은 비유·상징 표면으로 핵심 관념과 다름"
    }
  ],
  "competitors_rejected": [
    {
      "code": 69,
      "reason": "비슷한 사례를 선택하지만 본문의 주장을 다른 영역으로 옮겨 새 결론을 정당화하는 유추가 아니라 구성요건 부합 확인."
    },
    {
      "code": 49,
      "reason": "④의 천문 현상-통치 징후 대응만으로 역법 관념의 전체 구조 충족 불가."
    },
    {
      "code": 79,
      "reason": "통치 정당성과 천명이 소재지만 허용·금지·당위 조건을 판단하는 과제 아님."
    }
  ],
  "boundary_note": "37은 과제층위,44는 사례 내용의 실제 관계.유일 주 우선순위는 과제/내용 선택에 의존하므로 양자를 동일 연산으로 중복 계수하지 않음.",
  "confidence": 0.9,
  "sdss_seen": false
}
```
