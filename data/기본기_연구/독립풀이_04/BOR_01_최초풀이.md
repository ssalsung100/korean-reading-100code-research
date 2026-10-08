

<!-- luna-raw:BOR-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G493",
  "selected_answer": 1,
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
      "location": "정태상태 설명 마지막 문장",
      "evidence": "정태상태 자본량은 저축률·감가상각률·생산함수에 의해 결정된다."
    },
    {
      "location": "앞부분 정의·식",
      "evidence": "생산은 자본의 증가함수, 저축=투자, 자본 변화=투자-감가상각, 자본 증가의 생산 한계효과는 감소한다."
    }
  ],
  "minimal_logic_without_codes": "생산함수가 정태상태에 영향을 준다는 명시 문장을 부정한①이 틀리다.",
  "intermediate_reasoning": [
    "② 투자와감가상각의 차이가 자본 변화이므로 다르면 변화량이0이 아니다.",
    "③ 단순 모형의 생산 증가함수를 적용한다.",
    "④ 저축과투자가언제나같다는모형의 항등식에 따른다.",
    "⑤ 자본의한계생산 증가폭이감소한다는가정과같다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "현실경제의다른변수가능성을임의로추가하여본문이인구·기술을고정한증가함수라는조건을무시한다."
  },
  "source_limit": "공통그래프와[A]범위는후속문항을위해복원대기지만①결정근거와나머지정의문장은텍스트에있다."
}
```
