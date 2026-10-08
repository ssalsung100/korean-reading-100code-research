

<!-- luna-raw:BCA-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G382",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "answer_source": "sealed/answer_sdss.jsonl official_answer; data/meet_questions.jsonl 정본전사",
  "verification_limit": "원 정답표 이번 세션 독립 재확인 없음",
  "all_group_blind_records_before_any_group_answer_check": true,
  "minimal_logic_without_codes": "어린 시절 머스매 입적→작년 갓난애 입적→출생공포 속 거위 사건→현재 이야기 청취.서술 순서와 사건 순서를 분리.",
  "original_blind_preserved": true,
  "sdss_seen": false
}
```


<!-- luna-raw:BCA-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G382",
  "primary": [
    {
      "code": 3,
      "reason": "언급 순서와 다른 사건 발생 시점을 어린 시절/작년/회상/현재 단서로 배열"
    }
  ],
  "auxiliary": [
    {
      "code": 46,
      "reason": "갓난애 입적→출생 의심/공포→거위 사건의 동기적 경로가ㄱ<ㄷ의 추론 근거"
    }
  ],
  "surface": [
    {
      "code": 12,
      "reason": "대사가 모두 참이라는 발문은 풀이 전제이며 조건문의 역/대우 판정 자체 아님"
    }
  ],
  "competitors_rejected": [
    {
      "code": 9,
      "reason": "사건 순서는 우열이나 중요도 서열이 아님."
    },
    {
      "code": 80,
      "reason": "꿈을 둘러싼 인식이 소재이나 여기서는 대사 참을 가정하고 사건 순서를 복원."
    },
    {
      "code": 90,
      "reason": "다섯 배열 중 선택하지만 경우의 수 계산은 없음."
    }
  ],
  "boundary_note": "ㄱ<ㄷ는 명시 날짜보다 공포 형성의 이야기 연쇄에 의존.선후3과 인과46이 국소 결합하지만 시간 순서만으로 인과를 도출한 것은 아님.",
  "confidence": 0.91,
  "sdss_seen": false
}
```
