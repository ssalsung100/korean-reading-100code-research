

<!-- luna-raw:BBZ-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G381",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "answer_source": "sealed/answer_sdss.jsonl official_answer; data/meet_questions.jsonl 정본전사",
  "verification_limit": "원 정답표 이번 세션 독립 재확인 없음",
  "all_group_blind_records_before_any_group_answer_check": true,
  "minimal_logic_without_codes": "집단 분포 범위가 멸종 저항을 높이는①.④ 정체는 같은 지문의 다른 주장이지㉡ 종 수준 선택 사례가 아님.개체군=종 전체라는 강한 동치는 유보.",
  "original_blind_preserved": true,
  "sdss_seen": false
}
```


<!-- luna-raw:BBZ-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G381",
  "primary": [
    {
      "code": 17,
      "reason": "특성의 보유 단위를 개체에서 집단/종 수준으로 올바르게 구별"
    }
  ],
  "auxiliary": [
    {
      "code": 46,
      "reason": "지리적 분포 범위→격변시 멸종 저항이라는 작용"
    },
    {
      "code": 37,
      "reason": "종 수준의 특성과 멸종/분화 유리함이라는 요건에 부합하는 사례 검사"
    },
    {
      "code": 64,
      "reason": "밑줄㉡의 논의 범위를(나)전체 정체 주장으로 넓히지 않음"
    }
  ],
  "surface": [
    {
      "code": 9,
      "reason": "상위 수준이라는 말은 우열 서열이 아니라 분류/선택 단위의 차이"
    }
  ],
  "competitors_rejected": [
    {
      "code": 41,
      "reason": "개체 성질을 전체로 부당하게 옮기는 결합 오류가 아니라 집단에만 성립하는 분포 특성을 확인."
    },
    {
      "code": 77,
      "reason": "여러 사례에서 새 일반 명제를 귀납하는 작업 아님."
    },
    {
      "code": 5,
      "reason": "④의 장기 정체는 원문 타당 내용이어도㉡ 사례가 아니므로 지속만으로 판별 불가."
    }
  ],
  "boundary_note": "①의 개체군이 종 전체와 반드시 같은 외연이라는 주장은 하지 않음.개별 개체를 넘는 분포와 멸종저항 축을 공유한다는 국소 적합성.",
  "confidence": 0.89,
  "sdss_seen": false
}
```
