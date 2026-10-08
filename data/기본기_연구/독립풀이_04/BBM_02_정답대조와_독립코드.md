

<!-- luna-raw:BBM-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G377",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "answer_source": "sealed/answer_sdss.jsonl official_answer; data/meet_questions.jsonl official-page-verified canonical transcript",
  "verification_limit": "이번 세션 원 정답표 독립 재확인 없음",
  "all_group_blind_records_before_any_group_answer_check": true,
  "minimal_logic_without_codes": "산업화 중 서비스 확대와 선진국 간 구조 차이는 단일 단계 모형 비판에 유리하다. 화이트칼라 증가는 인정된 사실이나 양쪽 공통 예상이므로 판별 증거가 아니다.",
  "original_blind_preserved": true,
  "sdss_seen": false
}
```


<!-- luna-raw:BBM-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G377",
  "primary": [
    {
      "code": 63,
      "reason": "사례가 단일 모형 비판에 유리한지 평가하며 공통 예상과 판별 증거를 구분"
    }
  ],
  "auxiliary": [
    {
      "code": 74,
      "reason": "탈산업 단일 단계 설명과 다양한 경로 설명의 예상을 비교;75 연구군과 국소 중첩"
    },
    {
      "code": 36,
      "reason": "ㄱ 서비스 확대를 탈산업 전용 징표로 보는 주장에 대한 반례 후보;ㄴ 동일 구조 가정의 반례 후보. 단일 지점 차이만으로 미래 수렴까지 반증하지 않음."
    }
  ],
  "surface": [
    {
      "code": 58,
      "reason": "ㄹ은 공통으로 인정한 자료이지만 공통 논거로 역할을 명시한 것은 아니어서 자동 공통전제 부여 불가"
    }
  ],
  "competitors_rejected": [
    {
      "code": 23,
      "reason": "두 입장의 공통 인정 사실을 찾기만 하면ㄹ을 오선택. 영향 방향 평가 필요."
    },
    {
      "code": 37,
      "reason": "사례라는 형식만으로 요건 일치 사례 찾기라 볼 수 없음. 사례의 주장 영향이 핵심."
    },
    {
      "code": 77,
      "reason": "단일 사례 일반화가 비판 배경이나 새 일반화를 수행하는 발문 아님."
    }
  ],
  "boundary_note": "주장의 부정 예측과 부딪히는 반례는36, 넓은 유불리 평가는63.ㄴ 현재 비중 차이는 이론 약화 자료이지 모든 수렴 가능성을 논리적으로 제거한 증명 아님.",
  "confidence": 0.93,
  "sdss_seen": false
}
```
