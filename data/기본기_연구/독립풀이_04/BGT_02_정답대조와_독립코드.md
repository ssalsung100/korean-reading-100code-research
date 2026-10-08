

<!-- luna-raw:BGT-answer_check-20261002-r4-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G423",
  "blind_answer": 2,
  "official_answer": 2,
  "official_answer_transcription": "②",
  "official_answer_source": "자료/LEET_언어이해/원본/2011/2011_answer_2011_법학적성시험_언어이해_정답표.hwp",
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "logic_without_codes_fixed": "신분과 무관한 실천 요구 및 자기·타인 모두의 이익이라는 두 내용이 보기 ㄴ과 대응한다.",
  "limitations": [
    "봉인된 공식 전사 답과 대조. 원정답표 독립 시각 대조 미실시. 과거 노출 unknown 지위 유지."
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:BGT-independent_code-20261002-r4-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G423",
  "sdss_seen": false,
  "general_task": "인물의 주장과 보기의 사상 대응",
  "decisive_relation": "천민/대인을 가리지 않는 의 실천 요구와 자기·타인에게 이로움이라는 평가 기준의 동시 보존",
  "primary": {
    "code": 79,
    "name": "규범",
    "scope": "정답②(ㄴ)",
    "reason": "누구나 따라야 한다는 당위를 원문의 신분을 넘는 의 실천 요구와 연결한다."
  },
  "auxiliary": [
    {
      "code": 15,
      "scope": "정답② 및 나무 까치 평가",
      "reason": "사람에게 이로운가를 훌륭함/좋음의 판단 기준으로 쓰는 대응을 유지한다."
    },
    {
      "code": 4,
      "scope": "정답② 및 천민/대인 대화",
      "reason": "의 실천의 적용 범위를 특정 신분에 제한하지 않는다."
    },
    {
      "code": 39,
      "scope": "문항 전체",
      "reason": "본문과 보기의 중심 주장을 같은 비교 축에서 맞춘다. 포괄 작업명이며 구체 관계는79·15."
    }
  ],
  "surface": [
    {
      "code": 69,
      "reason": "본문 구거 비유가 있으나 보기의 대응은 유사한 인과구조로 새 결론을 추론하는 유추가 아니다."
    },
    {
      "code": 88,
      "reason": "이익이 등장하지만 비용·편익 크기의 계산이나 저울질이 필요하지 않다."
    }
  ],
  "competing_codes": [
    {
      "code": 15,
      "verdict": "강한 보조·유일 주 우선 유보",
      "refutation": "나무 까치 대목만 보면15가 주가 될 수 있으나 정답ㄴ은 보편적 도덕 요구까지 묶는다.79와15의 결합을 보존한다."
    },
    {
      "code": 37,
      "verdict": "포괄 보조 후보",
      "refutation": "보기는 원리의 구체 사례라기보다 주장 자체의 다른 표현이므로 사례 충족요건 판정이라는 기술은 덜 직접적이다."
    },
    {
      "code": 100,
      "verdict": "본문 국소, 정답 주로는 기각",
      "refutation": "구거와 밥그릇의 비유를 해석할 수 있으나 ㄴ과의 결정적 대응은 명시된 보편성과 이로움이다."
    }
  ],
  "falsification_test": "보편적 의 요구만 남으면 상호 이익 조건을, 이로움만 남으면 신분 초월의 당위 범위를 충분히 설명하지 못한다. 다만 객관식 소거로 한 단서만으로도 답을 고를 가능성과 전체 의미 설명을 구분한다.",
  "confidence": 0.94
}
```
