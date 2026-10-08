

<!-- luna-raw:BHG-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G428",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2012/2012_answer_2012_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "예선 후보를 고정한 뒤 본선의 기권 구간과 투표 집단을 비교한다. 후기 방향0/9에서는[0,2]보다[7,10]의 유권자가 많아 B2가 승리한다.",
  "limitations": [
    "봉인된 공식 정답 전사와 대조. 원정답표 시각 재대조 미실시. past_exposure unknown 및 strict 제외 유지."
  ]
}
```


<!-- luna-raw:BHG-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G428",
  "sdss_seen": false,
  "general_task": "이론별 예선·본선 결과 예측",
  "decisive_relation": "효용 규칙에 기권 조건을 결합하여 투표자 집합을 정한 후 분포의 대칭으로 총표를 비교",
  "primary": {
    "code": 45,
    "scope": "예선→본선 및 관용 경계 적용",
    "reason": "입력인 후보 위치·유권자 위치·이론·기권 조건에 따라 선택 결과가 바뀐다.예선 출력이 본선 입력이 된다."
  },
  "auxiliary": [
    {
      "code": 86,
      "scope": "⑤",
      "reason": "[0,2]와[7,10]의 인원은 대칭과 추가 양의 면적으로 순위 비교.구간 길이만으로 밀도 무시하지 않는다."
    },
    {
      "code": 12,
      "scope": "보기ㄹ/ㅁ",
      "reason": "두 후보가 동시에 허용 거리 밖이면 기권하고 동효용이면 기권한다."
    },
    {
      "code": 74,
      "scope": "문항 전체",
      "reason": "동일 선거 자료에 경쟁 이론을 적용한 예측 비교."
    },
    {
      "code": 3,
      "scope": "예선/본선",
      "reason": "본선 후보를 처음 네 후보 전체와 혼동하지 않는다."
    }
  ],
  "surface": [
    {
      "code": 78,
      "reason": "유권자 행위 설명이라는 주제만으로 실제 조건·면적 연산을 대체하지 못한다."
    }
  ],
  "competing_codes": [
    {
      "code": 92,
      "verdict": "보조 및 국소 중첩",
      "refutation": "좌표와 거리 계산은 필요하나⑤결정에는 정밀 득표 계산 없이 조건 분기와 대칭에 따른 대소 판단이면 충분하다."
    },
    {
      "code": 85,
      "verdict": "주 기각",
      "refutation": "관용 경계 도입으로 기권자가 달라지므로 총투표수를 고정하여 두 후보 비중의 경쟁으로 해결할 수 없다."
    },
    {
      "code": 43,
      "verdict": "주 기각",
      "refutation": "같은 분포에 모형을 적용하지만 실제 관측의 인과효과를 다른 변수로부터 식별하는 실험은 아니다."
    },
    {
      "code": 54,
      "verdict": "현실 인과 주 기각",
      "refutation": "모형 규칙 아래 결과 예측이지 이념 위치만으로 현실 선거가 충분히 결정된다는 일반 명제가 아니다."
    }
  ],
  "falsification_attempt": "초기 방향의 좌우 대칭이 후기에도 동률을 보장한다는 가설은 후보0/9의 허용 구간 비대칭으로 반증된다.반대로 후보0/10이라면 동일 관용 폭에서 대칭 투표 구간이 되어 동률 예측을 회복한다.",
  "unresolved": "후기 근접의 심리 가중치는 미명시.임의 수치 가중에 대한 전범위 정리로④를 확장하지 않는다.",
  "confidence": 0.94
}
```
