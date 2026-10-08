

<!-- luna-raw:BBX-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G381",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "answer_source": "sealed/answer_sdss.jsonl official_answer; data/meet_questions.jsonl 정본전사",
  "verification_limit": "원 정답표 이번 세션 독립 재확인 없음",
  "all_group_blind_records_before_any_group_answer_check": true,
  "minimal_logic_without_codes": "(가)의 적응 중심을 생성 중심으로 바꾸고(나)의 생성·정체 논의를 소멸만으로 축소하면 입장 대비가 왜곡됨.기본 단위와 예외·강화약화 강도 구분.",
  "original_blind_preserved": true,
  "sdss_seen": false
}
```


<!-- luna-raw:BBX-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G381",
  "primary": [
    {
      "code": 75,
      "reason": "두 입장의 중심 문제·기본 선택 단위·변화 양상을 축별로 귀속하고 생성/소멸이라는 잘못된 대립을 배제"
    }
  ],
  "auxiliary": [
    {
      "code": 64,
      "reason": "(가)의 핵심 논의 대상은 적응이며 종 생성 전용 이론으로 축소 불가"
    },
    {
      "code": 24,
      "reason": "기본 선택단위와 상위선택 예외를 함께 보존"
    },
    {
      "code": 63,
      "reason": "⑤ 중간 화석의 상대적 지지/약화 역할"
    }
  ],
  "surface": [
    {
      "code": 26,
      "reason": "생성/소멸 이항대립은 정답②가 덧씌운 오류"
    }
  ],
  "competitors_rejected": [
    {
      "code": 74,
      "reason": "75와 같은 연구군으로 내용 중첩 가능.주 행동은 새 관측 판별보다 입장 내용 보존이므로 별도 본질 구별 아님."
    },
    {
      "code": 36,
      "reason": "⑤의 약화를 단일 화석에 의한 완전 반증으로 승격하지 않음."
    },
    {
      "code": 3,
      "reason": "연속/불연속은④ 국소 내용이며 정답②의 주제 왜곡 자체는 시간 순서 오류 아님."
    }
  ],
  "boundary_note": "63은⑤에 국소 적용,75/64는② 정답 결정.사이트 태그 범위를 문항 전체와 정답으로 분리할 필요.",
  "confidence": 0.93,
  "sdss_seen": false
}
```
