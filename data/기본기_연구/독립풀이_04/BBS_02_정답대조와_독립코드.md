

<!-- luna-raw:BBS-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G379",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "answer_source": "sealed/answer_sdss.jsonl official_answer; data/meet_questions.jsonl 정본전사",
  "verification_limit": "원 정답표 이번 세션 독립 재확인 없음",
  "all_group_blind_records_before_any_group_answer_check": true,
  "minimal_logic_without_codes": "삭망월 길이와 절기/중기의 황도 배당으로 무중월을 식별.월초 상대 위치 조건과 직접 운행 속도 분석은 그 국소 규칙에 제시되지 않음.평균 속도와 주기 관계 자체를 부정하지 않음.",
  "original_blind_preserved": true,
  "sdss_seen": false
}
```


<!-- luna-raw:BBS-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G379",
  "primary": [
    {
      "code": 45,
      "reason": "무중월 판별의 입력인 달의 월 길이와 중기 배당을 복원하고 월초 설정 입력과 구별"
    }
  ],
  "auxiliary": [
    {
      "code": 15,
      "reason": "중기가 없는 달이라는 윤달 배치 기준"
    },
    {
      "code": 17,
      "reason": "상위 달력 제작 일반과 국소 윤달 배치 단계 범위 구분"
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "수치가 있지만 새 계산을 하는 문제 아님"
    },
    {
      "code": 87,
      "reason": "운행 속도라는ㄴ을 제시했으나 변화율 판정 근거 없음"
    }
  ],
  "competitors_rejected": [
    {
      "code": 10,
      "reason": "고려 요소라는 발문을 모든 물리적 필요조건 열거로 읽으면 주기와 연결된 속도까지 무제한 확장.서술된 절차 입력의 범위가 우선."
    },
    {
      "code": 19,
      "reason": "윤달 자체는 주기 차이 보정이지만 어떤 달을 고르는지의 입력 판별이 직접 과제."
    },
    {
      "code": 43,
      "reason": "타변수 고정 비교가 아니라 절차에 쓰인 입력 식별."
    }
  ],
  "boundary_note": "ㄴ 평균 각속도는 공전 주기와 관련될 수 있으므로 속도는 전혀 무관하다는 일반화 금지.본문의 등분/평균기간 판별과 속도 분석을 분리한 국소 판정.",
  "confidence": 0.86,
  "sdss_seen": false
}
```
