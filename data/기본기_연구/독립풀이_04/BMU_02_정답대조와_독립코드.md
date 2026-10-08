

<!-- luna-raw:BMU-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G476",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2021/2021_answer_2021_LEET_언어이해_정답표_배포용.hwp",
  "minimal_logic_without_codes": "b3에서b1으로 올려도 P의 왼쪽에 남아 다시 O로 내려가므로 덫을 벗어나는 지원이 아니다.②가 부적절하다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BMU-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G476",
  "minimal_logic_without_codes": "한 번의 지원 뒤에도 소득이 P 왼쪽에 있으면 다음 소득을 다시 입력하는 반복 과정에서 O로 돌아간다. b3→b1은 성장 영역 진입에 충분하지 않다.",
  "primary": [
    {
      "code": 45,
      "reason": "현재 소득→미래 소득의 함수를 반복 적용하여 지원 후의 장기 경로를 추적한다."
    }
  ],
  "auxiliary": [
    {
      "code": 57,
      "reason": "P 경계의 양쪽에서 O 또는 Q로 향하는 경로가 달라진다."
    },
    {
      "code": 10,
      "reason": "지속 성장 경로에 들어갈 만큼 경계를 넘는 조건을 단순한 소득 증가로 대체하지 않는다."
    },
    {
      "code": 74,
      "reason": "덫이 있는 S형과 덫이 없는 뒤집힌 L형이라는 다른 가설의 그림 해석을 구분한다."
    },
    {
      "code": 3,
      "reason": "당장의 소득 상승과 장기 수렴값을 별개 시점의 결과로 본다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "정확한 소득값이나 지원금액은 계산하지 않고 곡선·45도선의 상대 위치를 판독한다."
    }
  ],
  "competing_codes": [
    {
      "code": 49,
      "rejection": "단순 증감 방향 하나로 끝나지 않고 다음 시기의 출력을 다시 입력하는 경로를 따라야 한다."
    },
    {
      "code": 87,
      "rejection": "미분계수의 수치 계산은 필요 없다. 경계 양쪽의 반복 경로가 주어진다."
    },
    {
      "code": 88,
      "rejection": "지원의 사회적 비용편익 최적값을 찾는 것이 아니라 지원 수준이 어느 수렴 영역에 속하는지 판정한다."
    }
  ],
  "scope_limit": "경계의 정확 좌표·최소 지원금액·현실 국가의 성장률을 추정하지 않는다.",
  "confidence": 0.95,
  "sdss_seen": false
}
```
