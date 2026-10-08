

<!-- luna-raw:BBI-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G376",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "answer_source": "prepared_backlog/sealed/answer_sdss.jsonl의 official_answer; data/meet_questions.jsonl official-page-verified canonical transcript",
  "verification_limit": "원 정답표를 이번 세션에서 독립 재확인하지 않음",
  "all_group_blind_records_before_any_group_answer_check": true,
  "minimal_logic_without_codes": "실제 평균 밀도와 임계 밀도의 상대 관계가 모양·운명의 판단 근거. 기준값 변화만으로 대체 불가. ⑤의 지지 표현 강도 유보는 최초 기록대로 보존.",
  "original_blind_preserved": true,
  "sdss_seen": false,
  "incidental_exposure": "answer 필드 필터가 site_marked_answer도 표시함. SDSS 코드 태그는 미열람."
}
```


<!-- luna-raw:BBI-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G376",
  "primary": [
    {
      "code": 15,
      "name": "기준",
      "reason": "정답②는 판정 기준값과 실제 판정 대상의 비교를 기준값 자체 변화로 대체한다."
    }
  ],
  "auxiliary": [
    {
      "code": 86,
      "reason": "평균 밀도와 임계 밀도의 대소·같음 보존"
    },
    {
      "code": 12,
      "reason": "대소 조건별 팽창·수축 결과 연결"
    }
  ],
  "surface": [
    {
      "code": 5,
      "reason": "변화라는 말이 있으나 지속/변화 여부보다 비교항 누락이 결정적"
    }
  ],
  "competitors_rejected": [
    {
      "code": 45,
      "reason": "시뮬레이션 입력은③의 국소 설명. 정답②의 핵심은 구체적 함수 계산이 아닌 비교 기준의 완전성."
    },
    {
      "code": 87,
      "reason": "임계 밀도 변화라는 표현만 있으며 시간 기울기를 계산할 자료 없음."
    },
    {
      "code": 63,
      "reason": "⑤ 이론 지지 논점에는 적용 가능하나 정답②의 결정 연산 아님."
    }
  ],
  "boundary_note": "15와86은 이 사례에서 기준 비교라는 같은 행동을 다른 층위로 기술하므로 별도 필수 연산으로 이중 계수하지 않음. 기준값을 삭제하면 순수 양적 비교, 크기를 비수량 조건으로 바꾸면 기준 판정으로 재분할 가능.",
  "confidence": 0.86,
  "sdss_seen": false
}
```
