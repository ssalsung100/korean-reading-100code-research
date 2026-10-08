

<!-- luna-raw:BKJ-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G455",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "3~4문단",
      "evidence": "효용은 기대되는 쾌락 총량에서 고통 총량을 뺀 값. 기술 발전으로 포식 방지 의무가 산출될 가능성."
    },
    {
      "location": "5문단",
      "evidence": "의무론은 결과가 아닌 행동 자체 성격을 평가하며, 의무를 지니려면 실행 능력을 가져야 한다."
    }
  ],
  "minimal_logic_without_codes": "ㄱ은 포식 제거의 순효용이 양으로 평가되면 의무가 나올 수 있다는 본문 논증에 맞고 ㄹ은 비결과주의 평가 기준에 맞는다. ㄴ의 반비례는 없고 ㄷ은 의무의 필요 요건인 능력을 충분조건으로 뒤집는다. 따라서 ㄱ·ㄹ인 ②.",
  "intermediate_reasoning": [
    "ㄱ은 보기와 본문이 설정한 포식 개입 대안의 쾌락·고통 비교에 한정한다. 모든 양의 효용 행위를 대안 비교 없이 무조건 수행한다는 일반 규칙으로 확대하지 않는다.",
    "ㄴ 기술 발전은 개입을 쉽게 만들어 오히려 포식 방지 의무가 산출될 가능성을 열 뿐 윤리적 대우 범위 감소·반비례 수식은 주지 않는다.",
    "ㄷ 의무→능력으로부터 능력→의무는 도출되지 않는다.",
    "ㄹ 도덕적 평가가 의무 수행 등 행위 자체 성질에 근거한다는 문장 재진술."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "ㄷ을 포함한다. 구출이 가능한 사실만으로 구출 의무가 필연적으로 생긴다고 바꾸어 필요·충분 방향을 혼동한다."
  },
  "source_limit": "BKK 표지 누락은 별도 hold. BKJ의 보기와 ㄱ~ㄹ은 온전하며 전체 group 답은 아직 비공개."
}
```
