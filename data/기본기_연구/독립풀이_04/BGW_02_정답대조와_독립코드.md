

<!-- luna-raw:BGW-answer_check-20261002-r4-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G424",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2011/2011_answer_2011_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "주요화음의 구성음 집합과 마디 선율을 대응하여 근음과 첫 음을 분리.",
  "limitations": [
    "봉인 공식 전사 답 대조이며 원정답표 시각 대조는 미실시. 답 일치로 논거의 유보를 해소하지 않음."
  ],
  "source_restoration_before_answer": true
}
```


<!-- luna-raw:BGW-independent_code-20261002-r4-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G424",
  "sdss_seen": false,
  "general_task": "주어진 조건과 화음 정의를 악보에 적용",
  "decisive_relation": "화음의 근음은 화음 단위의 기준음이며 선율에서 시간상 첫 음과 동일하지 않다.",
  "primary": {
    "code": 17,
    "scope": "정답⑤",
    "reason": "화음의 근음과 마디의 첫 음이라는 서로 다른 역할을 혼동했는지 판정한다."
  },
  "auxiliary": [
    {
      "code": 16,
      "scope": "정답⑤ 및①~④",
      "reason": "3화음·7화음·으뜸/딸림/버금딸림 정의를 복원한다."
    },
    {
      "code": 37,
      "scope": "마디별 화음 대응",
      "reason": "각 마디 음들이 정의된 화음의 구성음에 맞는지 확인한다."
    },
    {
      "code": 12,
      "scope": "조건 적용",
      "reason": "도를 으뜸음으로 정한 조건에서 파/솔의 근음 역할을 정하고 한 마디 하나의 화음을 적용한다."
    }
  ],
  "surface": [
    {
      "code": 3,
      "reason": "첫 음은 시간 위치이지만 문항 전체의 시대 선후를 판정하는 것은 아니다."
    },
    {
      "code": 92,
      "reason": "3도/5도/7화음 수는 정의명·간격이며 계산이 정답의 핵심은 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 40,
      "verdict": "①보조 후보, 주로는 기각",
      "refutation": "화음 구성음과 선율의 일부 음을 구별하는 데 유용하나 정답⑤는 두 집합의 부분 여부보다 근음/첫음의 역할 차이이다."
    },
    {
      "code": 4,
      "verdict": "정답⑤ 보조 후보",
      "refutation": "각 마디라는 전칭을 반례 하나로 배제 가능하다. 다만 반례를 만드는 실제 판단은 근음과 첫 음 구분이다."
    },
    {
      "code": 36,
      "verdict": "국소 보조 후보",
      "refutation": "첫 마디 첫음 솔과 근음 도의 불일치만으로⑤를 반증한다.17과 경쟁 배타항이 아니라 오류 식별과 반증 방식의 층위 차이."
    }
  ],
  "concrete_counterexample": {
    "measure": 1,
    "first_note": "솔",
    "chord_root": "도",
    "impact": "각 마디 첫음=근음이라는 전칭을 반증"
  },
  "confidence": 0.97
}
```
