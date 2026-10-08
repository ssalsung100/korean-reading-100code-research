

<!-- luna-raw:BGS-answer_check-20261002-r4-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G423",
  "blind_answer": 1,
  "official_answer": 1,
  "official_answer_transcription": "①",
  "official_answer_source": "자료/LEET_언어이해/원본/2011/2011_answer_2011_법학적성시험_언어이해_정답표.hwp",
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "logic_without_codes_fixed": "의를 행하면 생계가 타격받는다는 우려와 묵자의 체류를 꺼리는 태도는 다르다. 실제 체류 권유를 근거로 후자를 배제한다.",
  "limitations": [
    "봉인된 공식 전사 답과 대조. 원정답표 독립 시각 대조 미실시. 과거 노출 unknown 지위 유지."
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:BGS-independent_code-20261002-r4-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G423",
  "sdss_seen": false,
  "general_task": "인물 행동과 동기의 대응 판정",
  "decisive_relation": "의 실천에 대한 생계 우려를 방문자의 체류에 대한 경계로 옮기는 오류; 실제 체류 권유가 반대 방향의 근거",
  "primary": {
    "code": 78,
    "name": "행위설명",
    "scope": "정답①",
    "reason": "머물게 하려는 행동과 체류를 경계한다는 동기 설명이 일치하는지 검증한다."
  },
  "auxiliary": [
    {
      "code": 17,
      "scope": "정답①",
      "reason": "우려 대상이 의의 실천인지 체류인지 분리한다."
    },
    {
      "code": 36,
      "scope": "정답①",
      "reason": "점심과 하룻밤을 권하는 행동은 체류를 경계했다는 해석에 맞지 않는 구체적 근거이다. 보편명제의 형식적 반례라기보다 해석 반증의 국소 용법."
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "의에 관한 내용이 있으나 오답을 결정하는 것은 체류 동기의 부당한 귀속."
    }
  ],
  "competing_codes": [
    {
      "code": 46,
      "verdict": "보조 관점 가능, 주로는 기각",
      "refutation": "생계 우려의 원인 항목 이동을 지적할 수 있으나 자연적 발생 경로보다 인물 동기 귀속 검증을 하는 문항이다."
    },
    {
      "code": 55,
      "verdict": "주로는 기각",
      "refutation": "체류→입지 위협이라는 설명은 무근거지만 관찰된 상관에서 인과를 추정하는 별도 행동은 없다. 허위적 인과의 넓은 용법 여부는 유보."
    },
    {
      "code": 18,
      "verdict": "좁은 논리적 모순 판정으로는 기각",
      "refutation": "체류를 권하면서 내심 경계하는 복합 동기는 논리적으로 가능하다. 본문에는 그 내심의 근거가 없고 환대 서술만 있으므로 텍스트 해석의 부적합이지 p와 not-p의 필연적 모순은 아니다."
    }
  ],
  "countermodel": "겉으로 환대하면서 속으로 경계하는 다른 인물은 가능하다. 따라서 체류 권유만으로 경계가 논리적으로 불가능하다고 일반화하지 않고 이 원문의 동기 근거 부재와 대상 이동을 함께 기록한다.",
  "confidence": 0.96
}
```
